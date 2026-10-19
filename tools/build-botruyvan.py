# -*- coding: utf-8 -*-
"""
build-botruyvan.py — Sinh bộ truy vấn GEO Paris theo MẪU CHUẨN 6 SHEET.

    python tools/build-botruyvan.py                 # sinh cả 10 bộ
    python tools/build-botruyvan.py --scope implant  # chỉ một bộ

Mẫu lấy từ `HCI-Knowledge/KN-BotruyvanGEO/*.xlsx` (bộ Kangnam v3) — giữ nguyên
tên sheet, thứ tự cột và cách đọc. Khác bộ gốc ở hai chỗ, đều có lý do:
  · Bảng màu đổi sang bộ nhận diện Nha khoa Paris (80% trắng/kem · 15% xanh · 5% đỏ).
  · CƠ HỘI GEO = 1 cho MỌI cụm, vì Paris chưa có mốc traffic AI nào để chấm 2–3.
    Sau tháng Setup đo xong mốc gốc thì phải chấm lại và chạy lại script này.

Nguồn dữ liệu:
  · `data/bo-truy-van/*.json`  — cấp CỤM (tầng · giai đoạn · % điểm · số bài · trang đích)
  · `data/truy-van/<key>.json` — cấp TRUY VẤN (17 dòng/cụm). Thiếu file này thì
    sheet 3 vẫn sinh đủ 255 dòng nhưng cột TRUY VẤN và KHỐI TRẢ LỜI để trống
    cho đội content điền — mọi cột suy ra được đã điền sẵn.
"""
import argparse
import glob
import json
import os
import sys
from collections import OrderedDict

import openpyxl
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_CUM = os.path.join(ROOT, "data", "bo-truy-van")
SRC_TV = os.path.join(ROOT, "data", "truy-van")
OUT_DIR = os.path.join(ROOT, "doc", "BotruyvanGEO-Paris")

TV_MOI_CUM = 17  # mỗi cụm 17 truy vấn — quy ước của mẫu chuẩn

# Tên sheet Excel giới hạn 31 ký tự. Sheet dài nhất là "3. <ten>- Bo truy van Master"
# = 23 + len(ten) → tên ngắn phải ≤ 8 ký tự.
TEN_NGAN = {
    "thuonghieu": "Brand", "implant": "Implant", "allon": "All-On",
    "niengmaccai": "Nieng", "invisalign": "Invisal", "rangsu": "Rang su",
    "veneer": "Veneer", "tongquat": "Tongquat", "nhachu": "Nha chu",
    "trenem": "Tre em",
}

# ── bảng màu Nha khoa Paris ──────────────────────────────────────────────
BLUE = "2A52BE"
BLUE_DEEP = "0C1D4D"
BLUE_LIGHT = "EAF0FC"
BLUE_MID = "D7E2FA"
RED = "ED2E38"
RED_WASH = "FDEAEB"
CREAM = "FBF8F3"
WHITE = "FFFFFF"
INK = "131A2E"

THIN = Side(style="thin", color=BLUE_MID)
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)

GIAI_DOAN = {
    "S1": "S1 · NHẬN BIẾT (Cold)",
    "S2": "S2 · TÌM HIỂU (Warm)",
    "S3": "S3 · CÂN NHẮC & NỖI SỢ (Warm→Hot)",
    "S4": "S4 · THỰC HIỆN (Hot)",
    "S5": "S5 · TRẢI NGHIỆM & HẬU ĐIỀU TRỊ (Existing)",
    "S6": "S6 · GẮN BÓ & MỞ RỘNG (LTV)",
}
TANG_TEN = {
    "A": "A · CORE 80/20",
    "B": "B · Đòn bẩy chuyển đổi",
    "C": "C · Uy tín & giữ chân",
    "D": "D · Cửa vào rộng",
}
# nhiệt độ & ưu tiên mặc định suy từ giai đoạn / tầng khi dữ liệu truy vấn chưa khai
NHIET_MD = {"S1": "Cold", "S2": "Warm", "S3": "Hot", "S4": "Hot",
            "S5": "Existing", "S6": "Existing"}
UUTIEN_MD = {"A": "P1", "B": "P2", "C": "P2", "D": "P3"}
DIEM_DT = {"Cao": 3, "TB": 2, "Thấp": 1}
DIEM_NHIET = {"Hot": 3, "Warm": 2, "Existing": 2, "Cold": 1}
DIEM_UT = {"P1": 3, "P2": 2, "P3": 1}
CO_HOI_GEO = 1  # Paris chưa có mốc traffic AI — xem docstring

RAO_OF = {
    "C01": "R0", "C02": "R0", "C03": "R7 · R2", "C04": "R13 · R2", "C05": "R0 · R6",
    "C06": "R1 · R9", "C07": "R12 · R9", "C08": "R3 · R4 · R6", "C09": "R13 · R1",
    "C10": "R0 · R13", "C11": "R6 · R1 · R5", "C12": "R0 · R4", "C13": "R13 · R8",
    "C14": "R3 · R4 · R7", "C15": "R0 · R12",
}
RAO_BANG = [
    ("R0", "Thấp — nội dung kiến thức",
     "Gắn CTA bán hàng dồn dập trong bài kiến thức",
     "Giữ giọng giáo dục; CTA mềm cuối bài; vẫn ghi ngày cập nhật + bác sĩ thẩm định",
     "Content lead"),
    ("R1", "Cam kết kết quả & mức độ đau",
     "“khỏi 100%”, “niềng không bao giờ đau”, “không biến chứng”, “răng sứ dùng vĩnh viễn”",
     "“tỷ lệ thành công cao khi đúng chỉ định và chăm sóc đúng*”; “độ bền theo khuyến cáo của hãng, có chế độ bảo hành”",
     "Pháp chế"),
    ("R2", "Danh mục kỹ thuật & phạm vi chuyên môn",
     "Đăng kỹ thuật không có trong danh mục đã phê duyệt của đúng cơ sở",
     "Chỉ nêu kỹ thuật có trong danh mục; tên thương mại soi chiếu được về tên chuyên môn",
     "Pháp chế + Chuyên môn"),
    ("R3", "Đúng pháp nhân & đúng cơ sở",
     "Gắn giấy phép cơ sở Hà Nội cho trang local tỉnh khác; dựng trang local cho tỉnh không có cơ sở",
     "Mỗi trang gắn đúng số giấy phép của chính cơ sở đó; ngoài phạm vi thì ghi rõ điều hướng",
     "Pháp chế"),
    ("R4", "Bác sĩ",
     "Dùng tên bác sĩ không có trong hồ sơ thương hiệu; gắn bác sĩ vào dịch vụ chưa xác minh",
     "Chỉ dùng 3 bác sĩ đã có hồ sơ; author box “Thẩm định chuyên môn: …”",
     "Chuyên môn + HR"),
    ("R5", "Hình ảnh khách hàng & before–after",
     "Dùng ảnh khách khi mới có thoả thuận miệng; tạo ảnh kết quả giả",
     "Văn bản đồng ý minh thị nêu rõ loại dữ liệu · mục đích · kênh · thời hạn · quyền rút lại",
     "CSKH + Pháp chế"),
    ("R6", "So sánh đối thủ",
     "Nêu tên hạ thấp cơ sở khác; ám chỉ “nơi khác làm hỏng”",
     "Bộ tiêu chí khách quan để khách tự đánh giá; tuyệt đối không phán xét nơi cũ",
     "Pháp chế"),
    ("R7", "“CHÍNH HÃNG” & vật tư ⚠ đặc thù nha khoa",
     "Gắn chữ “chính hãng” cho vật liệu ngoài 4 hãng có hồ sơ",
     "Chỉ dùng cho Straumann · Invisalign · Nacera · Ormco; phải có văn bản đối tác",
     "Kho vật tư + Pháp chế"),
    ("R8", "Khách nước ngoài & Việt kiều",
     "Đăng nội dung tiếp nhận khách nước ngoài khi thiếu điều kiện bắt buộc",
     "Đủ: kỹ thuật trong danh mục · phạm vi chuyên môn · năng lực ngôn ngữ · đồng ý song ngữ",
     "Pháp chế"),
    ("R9", "Giấy xác nhận nội dung quảng cáo",
     "Phát hành nội dung quảng cáo dịch vụ KCB chưa xin GXNNDQC",
     "Xin tại Sở Y tế trước chiến dịch; là đầu việc riêng của tháng Setup",
     "Pháp chế (Sở Y tế)"),
    ("R10", "KOL / người chuyển tải quảng cáo",
     "KOL nói về dịch vụ mà không công khai là quảng cáo",
     "Công khai #quảng_cáo, xác minh tính trung thực, ràng buộc trong hợp đồng",
     "Brand + Pháp chế"),
    ("R11", "Người nổi tiếng",
     "Nêu tên hoặc dùng hình người nổi tiếng; suy đoán họ đã làm răng",
     "Phân tích xu hướng chung, không cá nhân hoá",
     "Brand + Pháp chế"),
    ("R12", "GIÁ · ƯU ĐÃI · TRẢ GÓP = dữ liệu động ⚠ đặc thù Paris",
     "Đưa con số giá, % ưu đãi, lãi suất trả góp vào nội dung hoặc kế hoạch",
     "Lấy tại thời điểm chạy từ trang bảng giá; chỉ nêu dải min–max + ngày cập nhật",
     "Sale ops + Pháp chế"),
    ("R13", "Chẩn đoán & hứa thời gian ⚠ đặc thù nha khoa",
     "Chẩn đoán qua ảnh/mô tả; kê đơn; báo giá ca cụ thể; hứa thời gian điều trị cứng",
     "Tư vấn định hướng rồi mời thăm khám; nêu dải thời gian, nói rõ phụ thuộc từng ca",
     "Chuyên môn + Pháp chế"),
]

SAU_QUY_TAC = [
    "① BLUF — câu đầu tiên của mỗi mục PHẢI là câu trả lời đứng độc lập, hiểu được khi tách khỏi ngữ cảnh. AI trích theo ĐOẠN, không trích theo bài.",
    "② CÓ SỐ — nội dung có số liệu được hiển thị trong câu trả lời AI cao hơn 30–40%. “Hết ê buốt sau 3–7 ngày ở phần lớn ca” thắng “hết ê buốt khá nhanh”.",
    "③ PHỦ 8 GÓC HỎI cho mỗi chủ đề: định nghĩa · so sánh · hướng dẫn · trường hợp áp dụng · phản đối/rủi ro · thực thể liên quan · chi phí/chỉ số · địa phương.",
    "④ DÁM NÓI ĐIỀU BẤT LỢI — “mài răng là không hoàn nguyên”, “Invisalign không kéo nổi mọi ca”, “nha chu phải duy trì cả đời”. Nội dung cân bằng được AI trích nhiều hơn hẳn.",
    "⑤ GHI NGÀY CẬP NHẬT + TÊN BÁC SĨ THẨM ĐỊNH trên mọi bài y khoa (schema ProfilePage / IndividualPhysician). Chỉ dùng 3 bác sĩ đã có hồ sơ (R4).",
    "⑥ KHÔNG NHỒI TỪ KHOÁ — nhồi từ khoá cho kết quả THẤP HƠN mức nền trong AI search. Viết như đang trả lời một người thật đang lo.",
]


# ─────────────────────────── helper định dạng ────────────────────────────

def put(ws, r, c, v, *, bold=False, size=10, color=INK, fill=None,
        wrap=True, ha="left", va="top", border=True, italic=False):
    cl = ws.cell(r, c, v)
    cl.font = Font(name="Arial", sz=size, b=bold, i=italic, color=color)
    if fill:
        cl.fill = PatternFill("solid", fgColor=fill)
    cl.alignment = Alignment(horizontal=ha, vertical=va, wrap_text=wrap)
    if border:
        cl.border = BORDER
    return cl


def band(ws, r, c1, c2, text, fill, *, size=11, color=WHITE, h=None):
    ws.merge_cells(start_row=r, start_column=c1, end_row=r, end_column=c2)
    put(ws, r, c1, text, bold=True, size=size, color=color, fill=fill,
        ha="left", va="center")
    for c in range(c1 + 1, c2 + 1):
        put(ws, r, c, None, fill=fill)
    if h:
        ws.row_dimensions[r].height = h


def header_row(ws, r, labels, start=1):
    for i, h in enumerate(labels, start=start):
        put(ws, r, i, h, bold=True, size=9, color=WHITE, fill=BLUE,
            ha="center", va="center")
    ws.row_dimensions[r].height = 30


def widths(ws, spec):
    for c, w in spec.items():
        ws.column_dimensions[get_column_letter(c)].width = w


# ───────────────────────────── đọc nguồn ─────────────────────────────────

def load_bo(scope):
    out = []
    for path in sorted(glob.glob(os.path.join(SRC_CUM, "*.json"))):
        with open(path, encoding="utf-8") as fh:
            d = json.load(fh)
        if scope != ["all"] and d["key"] not in scope:
            continue
        d["_stem"] = os.path.splitext(os.path.basename(path))[0]
        tv_path = os.path.join(SRC_TV, d["key"] + ".json")
        d["_tv"] = None
        if os.path.exists(tv_path):
            with open(tv_path, encoding="utf-8") as fh:
                d["_tv"] = json.load(fh)
        out.append(d)
    return out


def rows_of(d):
    """Làm phẳng thành 255 dòng truy vấn, giữ đúng thứ tự: CORE trước, rồi theo hạng."""
    tv = d["_tv"] or {}
    gia_tri = (tv.get("gia_tri_dt") or "TB")
    kho = tv.get("truy_van", {})
    rows = []
    for cum in sorted(d["cum"], key=lambda c: c["hang"]):
        ma = cum["ma"]
        ds = kho.get(ma, [])
        for i in range(TV_MOI_CUM):
            q = ds[i] if i < len(ds) else {}
            nhiet = q.get("n") or NHIET_MD[cum["gd"]]
            ut = q.get("u") or UUTIEN_MD[cum["tang"]]
            dt = q.get("v") or gia_tri
            rows.append(dict(
                id=f"{ma}-{i+1:02d}", ma=ma, cum=cum, stt=i + 1,
                truy_van=q.get("q", ""), goc=q.get("g", ""),
                nhiet=nhiet, ut=ut, dt=dt,
                tu_khoa=q.get("k", ""), khoi=q.get("b", ""),
                trang=q.get("d") or cum["trang_dich"],
                rao=q.get("r") or RAO_OF.get(ma, "R0"),
                doi_tuong=q.get("t", "") or (tv.get("doi_tuong_md", {}) or {}).get(ma, "Chung"),
                diem=DIEM_DT.get(dt, 2) * DIEM_NHIET.get(nhiet, 2)
                     * DIEM_UT.get(ut, 2) * CO_HOI_GEO,
                core=i < cum["core"],
            ))
    # thứ tự triển khai của CORE: điểm cao trước, rồi theo hạng cụm
    k = 0
    for row in sorted([r for r in rows if r["core"]],
                      key=lambda r: (-r["diem"], r["cum"]["hang"], r["stt"])):
        k += 1
        row["thu_tu"] = k
    return rows


# ───────────────────────────── SHEET 1 ───────────────────────────────────

def sheet1(wb, d, rows):
    ws = wb.create_sheet(f"1. {d['ten_ngan']}- Huong dan")
    q = d["quy_mo"]
    bai = sum(c["bai"] for c in d["cum"])
    band(ws, 1, 1, 6, f"{d['ten'].upper()} — HƯỚNG DẪN & CHIẾN LƯỢC  |  "
                      f"Bộ truy vấn GEO · Nha khoa Paris", BLUE_DEEP, size=12, h=26)
    put(ws, 2, 1, "File theo MẪU CHUẨN 6 SHEET (nhân bản từ bộ Kangnam v3). "
                  "Sinh tự động bằng tools/build-botruyvan.py — sửa dữ liệu ở "
                  "data/bo-truy-van/ và data/truy-van/ rồi chạy lại, KHÔNG sửa tay file này.",
        size=9, italic=True)
    put(ws, 3, 1, "Tối ưu để ChatGPT · Gemini · Google AI Overview TRÍCH DẪN Nha khoa Paris "
                  "— không phải để lên top từ khoá Google.", size=9, italic=True)

    r = 5
    band(ws, r, 1, 6, "1 · INSIGHT CHIẾN LƯỢC — VÌ SAO BỘ NÀY KHÁC BỘ TỪ KHOÁ SEO", BLUE)
    for t in [
        "• Truy vấn vào AI dài gấp ~6 lần truy vấn Google (≈23 từ so với 3–4 từ) — khách gõ nguyên một câu chuyện.",
        "• AI “bung” (query fan-out) một câu hỏi thành 8–20 truy vấn con rồi mới tổng hợp. Chỉ 32% trích dẫn đến từ trang top 10 Google — 68% đến từ trang ngoài top 10 nhưng khớp đúng một truy vấn con.",
        "• 88% thương hiệu KHÔNG được AI trích dẫn nếu chỉ tối ưu SEO truyền thống. Thương hiệu phủ được >80% không gian chủ đề giữ được ~85% mức hiển thị trong AI.",
        "• Rào cản chốt của khách nha khoa là SỢ · NGỜ · NGẠI. NGỜ nặng hơn hẳn thẩm mỹ vì khách KHÔNG tự kiểm tra được vật liệu nằm trong miệng mình → cụm vật liệu (C03) và thực thể (C14) phải ra sớm.",
        "• ⚠ Paris CHƯA có mốc traffic AI nào → CƠ HỘI GEO của mọi cụm tạm lấy = 1. Sau tháng Setup đo xong mốc gốc phải chấm lại 1–3 và chạy lại script.",
    ]:
        r += 1
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=6)
        put(ws, r, 1, t, size=9.5)
        ws.row_dimensions[r].height = 28

    r += 2
    band(ws, r, 1, 6, "2 · KẾT LUẬN 80/20 — TẦNG ƯU TIÊN & PHÂN BỔ NGUỒN LỰC", BLUE)
    r += 1
    header_row(ws, r, ["Tầng", "Số cụm", "Số truy vấn", "% truy vấn",
                       "% điểm ưu tiên", "Phân bổ ngân sách nội dung & danh sách cụm"])
    tong_tv = q["truy_van"]
    for t in d["tang"]:
        r += 1
        put(ws, r, 1, TANG_TEN[t["tang"]], bold=True,
            fill=RED_WASH if t["tang"] == "A" else CREAM)
        put(ws, r, 2, t["cum"], ha="center")
        put(ws, r, 3, t["tv"], ha="center")
        put(ws, r, 4, round(t["tv"] / tong_tv, 4), ha="center")
        put(ws, r, 5, t["pct"] / 100, ha="center")
        put(ws, r, 6, t["phan_bo"], size=9)
        ws.row_dimensions[r].height = 46
    r += 1
    put(ws, r, 1, f"Riêng {q['core']} truy vấn CORE 80/20", bold=True, fill=RED_WASH)
    put(ws, r, 2, "—", ha="center")
    put(ws, r, 3, q["core"], ha="center")
    put(ws, r, 4, round(q["core"] / tong_tv, 4), ha="center")
    put(ws, r, 5, q["pct_diem_core"] / 100, ha="center")
    put(ws, r, 6, "Danh sách giao việc 90 ngày: lọc sheet 3 cột NHÓM 80/20 = CORE 80/20, "
                  "sắp theo cột THỨ TỰ TRIỂN KHAI.", size=9)

    r += 2
    band(ws, r, 1, 6, "3 · THEO NHÓM ĐỐI TƯỢNG (tự đếm từ cột ĐỐI TƯỢNG của sheet 3)", BLUE)
    r += 1
    header_row(ws, r, ["Nhóm đối tượng", "Số truy vấn", "CORE", "% truy vấn",
                       "Điểm", "Mô tả / lưu ý"])
    nhom = OrderedDict()
    for row in rows:
        k = row["doi_tuong"] or "Chung"
        nhom.setdefault(k, {"tv": 0, "core": 0, "diem": 0})
        nhom[k]["tv"] += 1
        nhom[k]["core"] += 1 if row["core"] else 0
        nhom[k]["diem"] += row["diem"]
    mota = ((d["_tv"] or {}).get("mo_ta_doi_tuong") or {})
    for k, v in sorted(nhom.items(), key=lambda x: -x[1]["diem"]):
        r += 1
        put(ws, r, 1, k, bold=True)
        put(ws, r, 2, v["tv"], ha="center")
        put(ws, r, 3, v["core"], ha="center")
        put(ws, r, 4, round(v["tv"] / tong_tv, 4), ha="center")
        put(ws, r, 5, v["diem"], ha="center")
        put(ws, r, 6, mota.get(k, ""), size=9)

    r += 2
    band(ws, r, 1, 6, "4 · CÁCH DÙNG 6 SHEET (Đối tượng → Hành trình → Truy vấn → "
                      "Nội dung → Đo lường → Pháp lý)", BLUE)
    r += 1
    header_row(ws, r, ["Sheet", "Dùng để", "Ai dùng", "", "", "Cách dùng nhanh"])
    for a, b, c, e in [
        ("1. Hướng dẫn", "Quyết định & phân bổ", "Leader",
         "Duyệt tầng ưu tiên + phân bổ ngân sách (mục 2) và trọng tâm nhóm đối tượng (mục 3)."),
        ("2. Hành vi KH", "Thấu hiểu đối tượng theo 6 giai đoạn", "Content · Tư vấn · Sale",
         "Đọc TRƯỚC khi viết. S3 ★★★ là điểm quyết định; mỗi giai đoạn một nỗi sợ khác nhau."),
        ("3. Bộ truy vấn Master", "Nguồn sự thật + khuyến nghị 80/20", "SEO · Content",
         "Lọc NHÓM 80/20 = CORE để giao việc 90 ngày; lọc ĐỐI TƯỢNG để làm theo chân dung."),
        ("4. Bản đồ nội dung", "Cụm → dạng bài → trang đích → sóng → phụ trách", "Manager",
         "Xếp theo hạng 80/20; cập nhật cột Trạng thái hằng tuần."),
        ("5. Prompt đo lường", "KPI Share of Voice trong AI", "SEO lead",
         "Chạy hằng tháng ẩn danh, 3 lần lấy đa số; nhân bản sheet mỗi tháng."),
        ("6. Rào pháp lý", "Soát trước khi đăng", "Pháp chế · Content",
         "Mỗi truy vấn có mã R0–R13; bảng tự đếm số truy vấn chịu từng rào."),
    ]:
        r += 1
        put(ws, r, 1, a, bold=True)
        put(ws, r, 2, b, size=9)
        put(ws, r, 3, c, size=9)
        put(ws, r, 6, e, size=9)

    r += 2
    band(ws, r, 1, 6, "5 · SÁU QUY TẮC VIẾT ĐỂ ĐƯỢC AI TRÍCH DẪN (bắt buộc với mọi bài)", BLUE)
    for t in SAU_QUY_TAC:
        r += 1
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=6)
        put(ws, r, 1, t, size=9.5)
        ws.row_dimensions[r].height = 28

    widths(ws, {1: 30, 2: 11, 3: 13, 4: 12, 5: 14, 6: 92})
    ws.freeze_panes = "A5"


# ───────────────────────────── SHEET 2 ───────────────────────────────────

def sheet2(wb, d, rows):
    ws = wb.create_sheet(f"2. {d['ten_ngan']}- Hanh vi KH")
    band(ws, 1, 1, 11, f"{d['ten'].upper()} — THẤU HIỂU HÀNH VI KHÁCH HÀNG · "
                       f"6 GIAI ĐOẠN HÀNH TRÌNH", BLUE_DEEP, size=12, h=26)
    put(ws, 2, 1, "Dùng để brief content, huấn luyện tư vấn viên và thiết kế kịch bản chốt. "
                  "Mỗi giai đoạn một NỖI SỢ khác nhau — trả lời sai nỗi sợ thì mất khách dù "
                  "tay nghề tốt.", size=9, italic=True)
    put(ws, 3, 1, "Cột SỐ TV · CORE · % ĐIỂM đếm từ sheet 3. S3 là điểm quyết định "
                  "(~50% điểm ưu tiên) — luôn xuất bản S3 trước S1.", size=9, italic=True)
    header_row(ws, 4, ["GIAI ĐOẠN", "ƯU TIÊN", "KHÁCH ĐANG NGHĨ GÌ", "NỖI SỢ CHI PHỐI",
                       "KHÁT KHAO THẬT", "TRIGGER CHUYỂN GIAI ĐOẠN",
                       "NHA KHOA PARIS PHẢI CÓ GÌ", "CỤM TRUY VẤN", "SỐ TV", "CORE", "% ĐIỂM"])
    ext = ((d["_tv"] or {}).get("hanh_vi") or {})
    r = 4
    for h in d["hanh_trinh"]:
        r += 1
        e = ext.get(h["gd"], {})
        fill = RED_WASH if h["gd"] == "S3" else (CREAM if r % 2 else None)
        put(ws, r, 1, GIAI_DOAN[h["gd"]], bold=True, fill=fill)
        put(ws, r, 2, h["uu_tien"], ha="center", fill=fill)
        put(ws, r, 3, e.get("nghi", ""), size=9, fill=fill)
        put(ws, r, 4, h["noi_so"], size=9, fill=fill)
        put(ws, r, 5, e.get("khat_khao", ""), size=9, fill=fill)
        put(ws, r, 6, e.get("trigger", ""), size=9, fill=fill)
        put(ws, r, 7, e.get("phai_co", ""), size=9, fill=fill)
        put(ws, r, 8, h["cum"], size=9, fill=fill)
        put(ws, r, 9, h["tv"], ha="center", fill=fill)
        put(ws, r, 10, h["core"], ha="center", fill=fill)
        put(ws, r, 11, h["pct"] / 100, ha="center", fill=fill)
        ws.row_dimensions[r].height = 92

    r += 2
    band(ws, r, 1, 11, "BA RÀO CẢN CHỐT CỦA KHÁCH NHA KHOA — mọi bài phải gỡ được ít nhất một",
         BLUE)
    r += 1
    header_row(ws, r, ["RÀO CẢN", "KHÁCH ĐANG NGHĨ GÌ", "", "BẰNG CHỨNG PARIS DÙNG ĐỂ GỠ"])
    for ten, nghi, gan in [
        ("① SỢ — đau & mất răng thật",
         "Đau khi nhổ, khoan, cấy trụ. Mài mất răng thật — men răng không mọc lại.",
         "Piezotome · RECIPROC BLUE · bác sĩ theo dõi từng giai đoạn · Invisalign trong suốt"),
        ("② NGỜ — vật liệu & tay nghề  ⚠ NẶNG NHẤT",
         "Trụ Implant / phôi sứ / khay niềng có CHÍNH HÃNG không? Bác sĩ có giỏi? Hỏng ai bảo hành?",
         "Straumann (top 1) · Invisalign Black Diamond · Nacera · Ormco Diamond Star · "
         "100% BS ĐH Y có chứng chỉ hành nghề · giấy phép Sở Y tế"),
        ("③ NGẠI — lộ trình & chi phí",
         "Điều trị nhiều buổi, đi lại nhiều lần, chi phí lớn, không biết khi nào xong.",
         "Lộ trình rõ số buổi và mốc thời gian · trả góp · 7 cơ sở · đặt lịch linh hoạt"),
    ]:
        r += 1
        f = RED_WASH if "NẶNG NHẤT" in ten else CREAM
        put(ws, r, 1, ten, bold=True, fill=f)
        ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=3)
        put(ws, r, 2, nghi, size=9, fill=f)
        put(ws, r, 3, None, fill=f)
        ws.merge_cells(start_row=r, start_column=4, end_row=r, end_column=11)
        put(ws, r, 4, gan, size=9, fill=f)
        for c in range(5, 12):
            put(ws, r, c, None, fill=f)
        ws.row_dimensions[r].height = 40

    widths(ws, {1: 34, 2: 10, 3: 46, 4: 46, 5: 40, 6: 40, 7: 50, 8: 22, 9: 8, 10: 8, 11: 10})
    ws.freeze_panes = "A5"


# ───────────────────────────── SHEET 3 ───────────────────────────────────

def sheet3(wb, d, rows):
    ws = wb.create_sheet(f"3. {d['ten_ngan']}- Bo truy van Master")
    q = d["quy_mo"]
    band(ws, 1, 1, 17, f"{d['ten'].upper()} — BỘ TRUY VẤN MASTER  |  "
                       f"ChatGPT · Gemini · Google AI Overview", BLUE_DEEP, size=12, h=24)
    band(ws, 1, 19, 29, "KHUYẾN NGHỊ CỤM ƯU TIÊN THEO NGUYÊN TẮC 80/20", BLUE_DEEP, size=11)
    put(ws, 2, 1, f"{q['truy_van']} truy vấn · {q['cum']} cụm · {q['doi_tuong']} nhóm đối tượng "
                  f"· {q['core']} truy vấn CORE 80/20 ({round(q['core']/q['truy_van']*100)}% bộ) "
                  f"chiếm {q['pct_diem_core']}% điểm ưu tiên · CORE xếp theo thứ tự triển khai 90 ngày",
        size=9, italic=True)
    put(ws, 2, 19, "Xếp hạng cụm theo điểm ưu tiên. Tầng A = làm trước trong 90 ngày với 70% "
                   "ngân sách nội dung; B mở khi A xong ~60%.", size=9, italic=True)
    put(ws, 3, 1, "ĐIỂM ƯU TIÊN = Giá trị DT (Cao 3 · TB 2 · Thấp 1) × Nhiệt độ (Hot 3 · Warm 2 · "
                  "Existing 2 · Cold 1) × Ưu tiên (P1 3 · P2 2 · P3 1) × CƠ HỘI GEO. "
                  "⚠ Paris chưa có mốc traffic AI → CƠ HỘI GEO = 1 cho mọi cụm; chấm lại sau tháng Setup.",
        size=9, italic=True, color="C11B26")

    header_row(ws, 4, ["ID", "CỤM CHỦ ĐỀ", "GIAI ĐOẠN", "TRUY VẤN KHÁCH GÕ VÀO AI",
                       "GÓC HỎI (fan-out)", "NHIỆT ĐỘ", "ƯU TIÊN", "GIÁ TRỊ DT", "NHÓM 80/20",
                       "TẦNG ƯU TIÊN", "THỨ TỰ TRIỂN KHAI (CORE)", "ĐIỂM ƯU TIÊN",
                       "TỪ KHOÁ ƯU TIÊN", "KHỐI TRẢ LỜI CẦN CÓ (brief giao content)",
                       "TRANG ĐÍCH PARIS", "RÀO PHÁP LÝ", "ĐỐI TƯỢNG"])
    header_row(ws, 4, ["HẠNG", "MÃ", "CỤM", "TẦNG", "CƠ HỘI GEO (1–3)", "SỐ TV", "CORE",
                       "ĐIỂM CỤM", "% ĐIỂM (chỉ mục)", "% LŨY KẾ", "KHUYẾN NGHỊ HÀNH ĐỘNG"],
               start=19)

    # CORE lên trước, trong CORE theo thứ tự triển khai; phần còn lại theo hạng cụm
    core_rows = sorted([r for r in rows if r["core"]], key=lambda r: r["thu_tu"])
    rest = [r for r in rows if not r["core"]]
    r = 4
    for row in core_rows + rest:
        r += 1
        f = RED_WASH if row["core"] else (CREAM if row["cum"]["tang"] == "A" else None)
        put(ws, r, 1, row["id"], size=9, ha="center", fill=f, bold=row["core"])
        put(ws, r, 2, f"{row['ma']} · {row['cum']['ten']}", size=9, fill=f)
        put(ws, r, 3, GIAI_DOAN[row["cum"]["gd"]], size=9, fill=f)
        put(ws, r, 4, row["truy_van"] or "[CẦN VIẾT]", size=10, fill=f,
            italic=not row["truy_van"], color=INK if row["truy_van"] else "9AA3BD")
        put(ws, r, 5, row["goc"], size=9, ha="center", fill=f)
        put(ws, r, 6, row["nhiet"], size=9, ha="center", fill=f)
        put(ws, r, 7, row["ut"], size=9, ha="center", fill=f)
        put(ws, r, 8, row["dt"], size=9, ha="center", fill=f)
        put(ws, r, 9, "CORE 80/20" if row["core"] else "—", size=9, ha="center",
            fill=f, bold=row["core"])
        put(ws, r, 10, TANG_TEN[row["cum"]["tang"]], size=9, fill=f)
        put(ws, r, 11, row.get("thu_tu", ""), size=9, ha="center", fill=f)
        put(ws, r, 12, row["diem"], size=9, ha="center", fill=f, bold=True)
        put(ws, r, 13, row["tu_khoa"], size=9, fill=f)
        put(ws, r, 14, row["khoi"] or "[CẦN VIẾT brief: BLUF + số liệu + điều bất lợi]",
            size=9, fill=f, italic=not row["khoi"],
            color=INK if row["khoi"] else "9AA3BD")
        put(ws, r, 15, row["trang"], size=9, fill=f)
        put(ws, r, 16, row["rao"], size=9, fill=f)
        put(ws, r, 17, row["doi_tuong"], size=9, fill=f)
        ws.row_dimensions[r].height = 58

    # khối xếp hạng cụm
    diem_cum = {}
    for row in rows:
        diem_cum[row["ma"]] = diem_cum.get(row["ma"], 0) + row["diem"]
    luy = 0
    rr = 4
    khuyen = ((d["_tv"] or {}).get("khuyen_nghi") or {})
    for cum in sorted(d["cum"], key=lambda c: c["hang"]):
        rr += 1
        luy += cum["pct"]
        f = RED_WASH if cum["tang"] == "A" else (CREAM if rr % 2 else None)
        put(ws, rr, 19, cum["hang"], ha="center", fill=f, bold=True)
        put(ws, rr, 20, cum["ma"], ha="center", fill=f, bold=True)
        put(ws, rr, 21, f"{cum['ma']} · {cum['ten']}", size=9, fill=f)
        put(ws, rr, 22, TANG_TEN[cum["tang"]], size=9, fill=f)
        put(ws, rr, 23, CO_HOI_GEO, ha="center", fill=f)
        put(ws, rr, 24, cum["tv"], ha="center", fill=f)
        put(ws, rr, 25, cum["core"], ha="center", fill=f)
        put(ws, rr, 26, diem_cum.get(cum["ma"], 0), ha="center", fill=f)
        put(ws, rr, 27, cum["pct"] / 100, ha="center", fill=f)
        put(ws, rr, 28, round(luy / 100, 4), ha="center", fill=f)
        put(ws, rr, 29, khuyen.get(cum["ma"], ""), size=9, fill=f)
        ws.row_dimensions[rr].height = max(ws.row_dimensions[rr].height or 0, 46)

    widths(ws, {1: 10, 2: 40, 3: 30, 4: 62, 5: 14, 6: 11, 7: 9, 8: 11, 9: 13, 10: 22,
                11: 13, 12: 11, 13: 26, 14: 74, 15: 44, 16: 34, 17: 24, 18: 3,
                19: 8, 20: 8, 21: 40, 22: 22, 23: 12, 24: 8, 25: 8, 26: 11, 27: 14,
                28: 11, 29: 70})
    ws.freeze_panes = "E5"
    ws.auto_filter.ref = f"A4:Q{4 + len(rows)}"


# ───────────────────────────── SHEET 4 ───────────────────────────────────

def sheet4(wb, d, rows):
    ws = wb.create_sheet(f"4. {d['ten_ngan']}- Ban do noi dung")
    bai = sum(c["bai"] for c in d["cum"])
    band(ws, 1, 1, 16, f"{d['ten'].upper()} — BẢN ĐỒ SẢN XUẤT NỘI DUNG · 15 CỤM → "
                       f"DẠNG BÀI → TRANG ĐÍCH → SÓNG → PHỤ TRÁCH", BLUE_DEEP, size=12, h=24)
    put(ws, 2, 1, "Xếp theo hạng 80/20 của sheet 3. Sóng 1 (0–30 ngày) = Tầng A; "
                  "Sóng 2 (31–60) = Tầng B; Sóng 3 (61–90) = Tầng C; Nền (>90) = Tầng D. "
                  "⚠ C05 “khi nào KHÔNG nên làm” của bộ Răng sứ · Implant · Niềng phải ra "
                  "CÙNG đợt Tầng A.", size=9, italic=True)
    put(ws, 3, 1, "Cột Tầng · Số TV · CORE · % điểm lấy từ sheet 3. "
                  "Cột Trạng thái và Ghi chú để Manager cập nhật hằng tuần.", size=9, italic=True)
    put(ws, 2, 10, bai, bold=True, ha="center")
    put(ws, 2, 11, "bài viết", size=9)
    put(ws, 3, 10, len(d["cum"]), bold=True, ha="center")
    put(ws, 3, 11, "cụm", size=9)
    header_row(ws, 4, ["HẠNG", "MÃ", "TÊN CỤM", "TẦNG", "GIAI ĐOẠN", "SỐ TV", "CORE",
                       "% ĐIỂM", "VAI TRÒ TRONG PHỄU", "SỐ BÀI",
                       "DẠNG NỘI DUNG CẦN SẢN XUẤT", "TRANG ĐÍCH CHÍNH", "SÓNG TRIỂN KHAI",
                       "PHỤ TRÁCH", "TRẠNG THÁI", "GHI CHÚ / VƯỚNG"])
    ext = ((d["_tv"] or {}).get("ban_do") or {})
    song_ten = {1: "Sóng 1 · 0–30 ngày", 2: "Sóng 2 · 31–60 ngày",
                3: "Sóng 3 · 61–90 ngày", 4: "Nền · sau 90 ngày"}
    r = 4
    for cum in sorted(d["cum"], key=lambda c: c["hang"]):
        r += 1
        e = ext.get(cum["ma"], {})
        f = RED_WASH if cum["tang"] == "A" else (CREAM if r % 2 else None)
        put(ws, r, 1, cum["hang"], ha="center", fill=f, bold=True)
        put(ws, r, 2, cum["ma"], ha="center", fill=f, bold=True)
        put(ws, r, 3, cum["ten"], size=9, fill=f)
        put(ws, r, 4, TANG_TEN[cum["tang"]], size=9, fill=f)
        put(ws, r, 5, GIAI_DOAN[cum["gd"]], size=9, fill=f)
        put(ws, r, 6, cum["tv"], ha="center", fill=f)
        put(ws, r, 7, cum["core"] or "—", ha="center", fill=f)
        put(ws, r, 8, cum["pct"] / 100, ha="center", fill=f)
        put(ws, r, 9, e.get("vai_tro", ""), size=9, fill=f)
        put(ws, r, 10, cum["bai"] or "—", ha="center", fill=f, bold=True)
        put(ws, r, 11, e.get("dang_bai", ""), size=9, fill=f)
        put(ws, r, 12, cum["trang_dich"], size=9, fill=f)
        put(ws, r, 13, song_ten[cum["song"]], size=9, fill=f)
        put(ws, r, 14, e.get("phu_trach", "Team Content + BS thẩm định"), size=9, fill=f)
        put(ws, r, 15, "Chưa làm", size=9, ha="center", fill="FFF8E7")
        put(ws, r, 16, "", fill="FFF8E7")
        ws.row_dimensions[r].height = 52
    widths(ws, {1: 8, 2: 8, 3: 44, 4: 22, 5: 30, 6: 8, 7: 8, 8: 10, 9: 34, 10: 9,
                11: 70, 12: 46, 13: 20, 14: 26, 15: 13, 16: 30})
    ws.freeze_panes = "C5"


# ───────────────────────────── SHEET 5 ───────────────────────────────────

def sheet5(wb, d, rows):
    ws = wb.create_sheet(f"5. {d['ten_ngan']}- Prompt do luong")
    band(ws, 1, 1, 10, f"{d['ten'].upper()} — BỘ PROMPT ĐO LƯỜNG GEO · "
                       f"SHARE OF VOICE TRONG AI", BLUE_DEEP, size=12, h=24)
    put(ws, 2, 1, "Cách chạy: CHẾ ĐỘ ẨN DANH (không đăng nhập, tắt cá nhân hoá, xoá lịch sử "
                  "phiên), dán NGUYÊN VĂN từng prompt vào ChatGPT · Gemini · Google AI Overview. "
                  "Ghi 1 nếu Nha khoa Paris được nhắc tên, 0 nếu không. CHẠY 3 LẦN LẤY ĐA SỐ.",
        size=9, italic=True)
    put(ws, 3, 1, "Kết quả AI thay đổi theo phiên → đo XU HƯỚNG theo tháng, không đo tuyệt đối "
                  "một lần. Nhân bản sheet này mỗi tháng. Cột cuối ghi đối thủ được AI nhắc — "
                  "đây là dữ liệu quý nhất.", size=9, italic=True)
    put(ws, 4, 1, "Tháng đo:", bold=True)
    put(ws, 4, 3, "⚠ Chưa đo — tháng Setup là tháng lấy mốc gốc", fill="FFF8E7", size=9)
    header_row(ws, 5, ["#", "PROMPT KIỂM TRA (dán nguyên văn)", "CỤM ĐO", "MÃ CỤM", "TẦNG",
                       "ChatGPT", "Gemini", "AI Overview", "SỐ NỀN TẢNG NHẮC",
                       "ĐỐI THỦ ĐƯỢC AI NHẮC (ghi chú)"])

    ds = ((d["_tv"] or {}).get("prompt_do") or [])
    if not ds:  # chưa khai → tự chọn truy vấn ngắn nhất của từng cụm Tầng A
        for cum in sorted([c for c in d["cum"] if c["tang"] == "A"], key=lambda c: c["hang"]):
            cands = [r for r in rows if r["ma"] == cum["ma"] and r["truy_van"]]
            cands.sort(key=lambda r: len(r["truy_van"]))
            for r_ in cands[:4]:
                ds.append({"p": r_["truy_van"], "ma": cum["ma"]})
    r = 5
    for i, p in enumerate(ds, 1):
        r += 1
        cum = next((c for c in d["cum"] if c["ma"] == p["ma"]), None)
        f = CREAM if i % 2 else None
        put(ws, r, 1, i, ha="center", fill=f)
        put(ws, r, 2, p["p"], size=10, fill=f)
        put(ws, r, 3, (cum["ten"] if cum else ""), size=9, fill=f)
        put(ws, r, 4, p["ma"], ha="center", fill=f)
        put(ws, r, 5, TANG_TEN[cum["tang"]] if cum else "", size=9, fill=f)
        for c in (6, 7, 8):
            put(ws, r, c, None, fill="FFF8E7", ha="center")
        put(ws, r, 9, None, ha="center", fill=f)
        put(ws, r, 10, None, fill="FFF8E7")
        ws.row_dimensions[r].height = 34
    widths(ws, {1: 6, 2: 76, 3: 36, 4: 10, 5: 22, 6: 11, 7: 11, 8: 13, 9: 15, 10: 40})
    ws.freeze_panes = "B6"


# ───────────────────────────── SHEET 6 ───────────────────────────────────

def sheet6(wb, d, rows):
    ws = wb.create_sheet(f"6. {d['ten_ngan']}- Rao phap ly")
    band(ws, 1, 1, 9, f"{d['ten'].upper()} — RÀO PHÁP LÝ · SOÁT TRƯỚC KHI ĐĂNG BẤT KỲ "
                      f"NỘI DUNG NÀO TRONG BỘ NÀY", BLUE_DEEP, size=12, h=24)
    put(ws, 2, 1, "NGUYÊN TẮC NỀN: KHÔNG CHẮC → DỪNG → HỎI PHÁP CHẾ → RỒI MỚI ĐĂNG. "
                  "Tài liệu nội bộ, không thay thế ý kiến Pháp chế.", size=9, italic=True)
    put(ws, 3, 1, "Mỗi truy vấn ở sheet 3 (cột RÀO PHÁP LÝ) bắt đầu bằng mã R0–R13 → "
                  "cột SỐ TV và CORE dưới đây tự đếm từ đó.", size=9, italic=True)
    header_row(ws, 4, ["MÃ", "RÀO", "KHÔNG ĐƯỢC LÀM", "THAY BẰNG", "ÁP DỤNG CHO CỤM",
                       "SỐ TV", "CORE", "NGƯỜI DUYỆT", "ĐÃ PHỔ BIẾN CHO TEAM"])
    r = 4
    for ma, ten, khong, thay, duyet in RAO_BANG:
        r += 1
        hit = [x for x in rows if ma in [t.strip() for t in x["rao"].replace("·", " ").split()]]
        cums = sorted({x["ma"] for x in hit})
        nong = ma in ("R7", "R12", "R9", "R1")
        f = RED_WASH if nong else (CREAM if r % 2 else None)
        put(ws, r, 1, ma, bold=True, ha="center", fill=f)
        put(ws, r, 2, ten, size=9, bold=nong, fill=f)
        put(ws, r, 3, khong, size=9, fill=f)
        put(ws, r, 4, thay, size=9, fill=f)
        put(ws, r, 5, " ".join(cums) or "—", size=9, fill=f)
        put(ws, r, 6, len(hit), ha="center", fill=f)
        put(ws, r, 7, sum(1 for x in hit if x["core"]), ha="center", fill=f)
        put(ws, r, 8, duyet, size=9, fill=f)
        put(ws, r, 9, "Chưa", size=9, ha="center", fill="FFF8E7")
        ws.row_dimensions[r].height = 46
    r += 2
    band(ws, r, 1, 9, "QUY TRÌNH BẮT BUỘC", BLUE)
    r += 1
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=9)
    put(ws, r, 1, "Content/Chi nhánh soạn → tự kiểm checklist R0–R13 → BS thẩm định chuyên môn "
                  "→ Pháp chế duyệt nội dung, hình ảnh và chữ “chính hãng” → (nếu là quảng cáo "
                  "dịch vụ KCB) xin GXNNDQC tại Sở Y tế → phát hành → lưu hồ sơ.  "
                  "⚠ Mọi đầu việc phải CỘNG thời gian duyệt 2 lớp vào hạn chót.", size=10)
    ws.row_dimensions[r].height = 42
    widths(ws, {1: 7, 2: 36, 3: 54, 4: 60, 5: 34, 6: 8, 7: 8, 8: 22, 9: 16})
    ws.freeze_panes = "A5"


# ─────────────────────────────── main ────────────────────────────────────

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scope", default="all", help="key bộ, phẩy ngăn cách; hoặc 'all'")
    a = ap.parse_args()
    scope = [s.strip() for s in a.scope.split(",")]

    os.makedirs(OUT_DIR, exist_ok=True)
    bos = load_bo(scope)
    if not bos:
        sys.exit("Không có bộ nào khớp --scope.")

    for d in bos:
        d["ten_ngan"] = TEN_NGAN.get(d["key"], d["key"][:8].capitalize())
        if len(d["ten_ngan"]) > 8:
            sys.exit(f"✖ TEN_NGAN['{d['key']}'] dài {len(d['ten_ngan'])} ký tự — "
                     f"tên sheet sẽ vượt 31 ký tự của Excel. Rút còn ≤8.")
        rows = rows_of(d)
        wb = openpyxl.Workbook()
        wb.remove(wb.active)
        sheet1(wb, d, rows)
        sheet2(wb, d, rows)
        sheet3(wb, d, rows)
        sheet4(wb, d, rows)
        sheet5(wb, d, rows)
        sheet6(wb, d, rows)
        out = os.path.join(OUT_DIR, f"{d['_stem']}.xlsx")
        wb.save(out)
        da = sum(1 for r in rows if r["truy_van"])
        print(f"✔ {os.path.basename(out):26} {len(rows)} truy vấn · "
              f"{da} đã viết · {len(rows)-da} chờ viết · "
              f"{sum(1 for r in rows if r['core'])} CORE")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
