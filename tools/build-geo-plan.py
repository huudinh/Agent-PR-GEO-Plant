# -*- coding: utf-8 -*-
"""
build-geo-plan.py — Sinh file kế hoạch GEO 2 TAB (KPI + Công việc triển khai)
cho Nha khoa Paris, từ 10 bộ truy vấn trong data/bo-truy-van/.

    python tools/build-geo-plan.py --start 2027-01 --months 6
    python tools/build-geo-plan.py --start 2026-11 --months 4 --scope implant,allon,invisalign
    python tools/build-geo-plan.py --start 2027-01 --months 12 --tiers A,B,C -o ke-hoach-2027.xlsx

Tham số:
  --start   YYYY-MM, tháng bắt đầu chu kỳ
  --months  số tháng (3 · 4 · 6 · 12 · bất kỳ)
  --scope   danh sách `key` của bộ dịch vụ, phẩy ngăn cách; mặc định `all` = cả 10 bộ
  --tiers   tầng đưa vào chu kỳ, mặc định `A,B,C` (D đẩy backlog sang kỳ sau)
  -o        đường dẫn file xuất

Thuật toán rải tháng bám §6 của knowledge/geo-phuong-phap-luan.md:
  · Xếp cụm theo đúng thứ tự ưu tiên — Sóng 1 (Tầng A/S3) trước, rồi Sóng 2, 3, Nền.
  · C05 "khi nào KHÔNG nên làm" của 3 bộ Răng sứ · Implant · Niềng mắc cài được
    NÂNG LÊN SÓNG 1 dù nằm Tầng B (§6.3 quy tắc 3) — đây là khác biệt E-E-A-T lớn nhất.
  · Rải RIÊNG từng business line theo hạn ngạch `tổng bài / số tháng` → mọi line trọng
    điểm có mặt ở mọi tháng (§6.3 quy tắc 4) và sản lượng tháng phẳng (quy tắc 5).
  · Cụm lớn hơn hạn ngạch một tháng được TÁCH sang tháng kế — cột Công việc chi tiết
    ghi rõ "x/y bài (làm tiếp ở tháng khác)".
  · Trang local chỉ dựng cho 7 hub có cơ sở thật; hết 7 hub thì chuyển sang đầu việc
    rà soát & tối ưu, KHÔNG sinh thêm trang tỉnh không có cơ sở (rào R3).
"""
import argparse
import calendar
import glob
import json
import os
import sys
from collections import defaultdict

import openpyxl
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "data", "bo-truy-van")

# ── bảng màu bộ nhận diện Nha khoa Paris ─────────────────────────────────
# Ba màu gốc không được đổi: Cerulean Blue #2A52BE · Pantone Red 032 C #ED2E38 · White.
# Tỷ lệ bắt buộc 80% trắng/kem · 15% xanh · 5% đỏ → đỏ CHỈ dùng cho dòng ★ tổng tháng.
BLUE = "2A52BE"        # --blue      header chính TAB 1
BLUE_DEEP = "0C1D4D"   # --blue-deep header điều hành TAB 2 + dải tháng
BLUE_LIGHT = "EAF0FC"  # --blue-light dòng ▶ TỔNG business line
BLUE_MID = "D7E2FA"    # --blue-mid  ô trụ cột + viền
RED = "ED2E38"         # --red       dòng ★ TỔNG SẢN LƯỢNG THÁNG (5% accent)
CREAM = "FBF8F3"       # --cream     dòng chi tiết
WHITE = "FFFFFF"
INK = "131A2E"         # --ink

THIN = Side(style="thin", color=BLUE_MID)
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)

LINE_ORDER = [
    "BRAND · Thương hiệu tổng",
    "NKI · Implant & Phục hình mất răng",
    "NKC · Chỉnh nha — Niềng răng",
    "NKT · Nha khoa thẩm mỹ",
    "NKG · Nha khoa tổng quát & Nha chu",
    "NKF · Nha khoa trẻ em & Gia đình",
]

# 7 hub có cơ sở thật. Trang "dịch vụ × tỉnh KHÔNG có cơ sở" nằm ngoài phạm vi (R3).
HUBS = ["Hà Nội", "Hải Phòng", "Quảng Ninh", "Vinh (Nghệ An)",
        "Đà Nẵng", "TP.HCM", "Bình Dương"]

PHASES = ["Setup", "Tăng tốc", "Đột phá", "Về đích"]
PHASE_WEIGHT = [0.20, 0.25, 0.30, 0.25]
UNVERIFIED = "⚠ Cần xác minh từ Nha khoa Paris"

# C05 phải ra cùng Tầng A ở 3 bộ này (geo-phuong-phap-luan.md §6.3 quy tắc 3)
C05_EARLY = {"rangsu", "implant", "niengmaccai"}

# Rào pháp lý theo cụm — geo-rao-phap-ly.md §5
RAO_OF = {
    "C01": "R0", "C02": "R0", "C03": "R7 · R2", "C04": "R13 · R2", "C05": "R0 · R6",
    "C06": "R1 · R9", "C07": "R12 · R9", "C08": "R3 · R4 · R6", "C09": "R13 · R1",
    "C10": "R0 · R13", "C11": "R6 · R1 · R5", "C12": "R0 · R4", "C13": "R13 · R8",
    "C14": "R3 · R4 · R7", "C15": "R0 · R12",
}

# Rào cản chốt mà cụm đang gỡ — geo-phuong-phap-luan.md §2.1
RAOCAN_OF = {
    "C01": "SỢ", "C02": "SỢ", "C03": "NGỜ", "C04": "NGỜ", "C05": "NGỜ",
    "C06": "SỢ", "C07": "NGẠI", "C08": "NGỜ", "C09": "NGẠI", "C10": "SỢ",
    "C11": "NGỜ", "C12": "NGỜ", "C13": "NGẠI", "C14": "NGỜ", "C15": "NGẠI",
}


# ─────────────────────────────── đọc nguồn ───────────────────────────────

def load_clusters(scope):
    """Trả về list cụm (đã làm phẳng) của các bộ trong phạm vi."""
    out = []
    for path in sorted(glob.glob(os.path.join(SRC, "*.json"))):
        with open(path, encoding="utf-8") as fh:
            d = json.load(fh)
        if scope != ["all"] and d["key"] not in scope:
            continue
        for c in d["cum"]:
            if c["bai"] <= 0:
                continue
            song = c["song"]
            if c["ma"] == "C05" and d["key"] in C05_EARLY:
                song = 1  # §6.3 quy tắc 3
            out.append(dict(
                key=d["key"], svc=d["ten"], line=d["line_ten"],
                code=c["ma"], name=c["ten"], tier=c["tang"], stage=c["gd"],
                tv=c["tv"], tv_core=c["core"],
                # "Trong đó CORE" của kế hoạch đếm theo SỐ BÀI thuộc Tầng A,
                # không phải số truy vấn CORE của cụm.
                core=c["bai"] if c["tang"] == "A" else 0,
                art=c["bai"], wave=song, url=c["trang_dich"], rank=c["hang"],
            ))
    return out


# ──────────────────────────── rải cụm vào tháng ───────────────────────────

def month_labels(start, n):
    y, m = int(start[:4]), int(start[5:7])
    out = []
    for _ in range(n):
        last = calendar.monthrange(y, m)[1]
        out.append(dict(y=y, m=m, label=f"Tháng {m}",
                        header=f"THÁNG {m:02d}/{y}",
                        deadline=f"{last:02d}/{m:02d}/{y}",
                        banner=f"THÁNG {m}/{y}"))
        m += 1
        if m > 12:
            m, y = 1, y + 1
    return out


def assign(clusters, n):
    """Rải cụm vào tháng theo hạn ngạch khối lượng của từng business line.

    Xếp cụm theo thứ tự ưu tiên (Sóng 1 → Nền, trong sóng: Tầng A → D, rồi hạng),
    sau đó đổ tuần tự vào từng tháng cho tới khi tháng đó đầy hạn ngạch
    `tổng bài của line / số tháng`.

    Cách này giữ nguyên luật "S3/Tầng A ra trước", đồng thời bảo đảm mọi line
    trọng điểm có mặt mọi tháng và sản lượng tháng phẳng — thay vì để một sóng
    khối lượng nhỏ chiếm trọn một tháng.
    """
    load = [0] * n
    by_line = defaultdict(list)
    for c in clusters:
        by_line[c["line"]].append(c)

    slices = []
    for line_clusters in by_line.values():
        line_clusters.sort(key=lambda c: (c["wave"], c["tier"], c["rank"], -c["art"]))
        total = sum(c["art"] for c in line_clusters)
        target = [total // n + (1 if i < total % n else 0) for i in range(n)]
        m, filled = 0, 0
        for c in line_clusters:
            remain, core_left = c["art"], c["core"]
            while remain > 0:
                if m < n - 1 and filled >= target[m]:
                    m, filled = m + 1, 0
                room = remain if m == n - 1 else max(1, target[m] - filled)
                take = min(remain, room)
                core_take = min(core_left, round(c["core"] * take / c["art"]))
                slices.append({**c, "month": m, "art": take, "core": core_take,
                               "art_total": c["art"], "split": take != c["art"]})
                remain -= take
                core_left -= core_take
                filled += take
                load[m] += take

    slices.sort(key=lambda s: (s["month"], s["line"], s["tier"], s["rank"]))
    return slices, load


def phase_of(i, n):
    """Tên giai đoạn + trọng số của tháng thứ i.

    Setup luôn gọn trong tháng đầu (khoá bộ đo, audit, GA4, GXNNDQC, bảng giá);
    các tháng còn lại chia đều cho Tăng tốc → Đột phá → Về đích.
    """
    if i == 0 or n == 1:
        return PHASES[0], PHASE_WEIGHT[0]
    seg = 1 + min(2, (i - 1) * 3 // (n - 1))
    return PHASES[seg], PHASE_WEIGHT[seg]


def hub_plan(n):
    """Trang local theo tháng: 2 hub/tháng cho tới khi phủ hết 7 hub, rồi chuyển
    sang rà soát & tối ưu. KHÔNG sinh trang tỉnh không có cơ sở (R3)."""
    plan, idx = [], 0
    for _ in range(n):
        if idx >= len(HUBS):
            plan.append([])
            continue
        batch = HUBS[idx:idx + 2]
        idx += len(batch)
        plan.append(batch)
    return plan


# ─────────────────────────────── style helper ─────────────────────────────

def put(ws, r, c, v, *, bold=False, size=10, color=INK, fill=None,
        wrap=True, ha="left", va="center", border=True):
    cl = ws.cell(r, c, v)
    cl.font = Font(name="Arial", sz=size, b=bold, color=color)
    if fill:
        cl.fill = PatternFill("solid", fgColor=fill)
    cl.alignment = Alignment(horizontal=ha, vertical=va, wrap_text=wrap)
    if border:
        cl.border = BORDER
    return cl


def band(ws, r, c1, c2, text, fill, *, size=11, color=WHITE):
    ws.merge_cells(start_row=r, start_column=c1, end_row=r, end_column=c2)
    put(ws, r, c1, text, bold=True, size=size, color=color, fill=fill, ha="center")
    for c in range(c1 + 1, c2 + 1):
        put(ws, r, c, None, fill=fill)


# ─────────────────────────────── TAB 1 — KPI ──────────────────────────────

def build_kpi(wb, months, by_line_month, lines, total_by_month):
    ws = wb.create_sheet("BẢNG TỔNG QUAN KPI")
    n = len(months)
    C_PILLAR, C_SUB, C_ITEM, C_QTY, C_LEVEL, C_NOW = 1, 2, 3, 4, 5, 6
    C_M0 = 7
    C_TARGET = C_M0 + n
    C_W_ROW = C_TARGET + 1
    C_W_PILLAR = C_TARGET + 2
    last = C_W_PILLAR

    band(ws, 2, 1, last,
         f"BẢNG TỔNG QUAN KPI & KẾ HOẠCH DỰ ÁN GEO/SEO NHA KHOA PARIS "
         f"({months[0]['header']} – {months[-1]['header']})", BLUE, size=12)

    banners = [
        (C_PILLAR, C_ITEM, "TỔNG BÀI VIẾT MỤC TIÊU",
         f"{sum(total_by_month)} bài · {n} tháng · rải theo sóng 80/20"),
        (C_QTY, C_NOW, "HẠ TẦNG WEB & CỔNG HUB",
         "Kiến trúc chuyên khoa + cổng Hub, schema thực thể, tải trang < 2s"),
        (C_M0, C_M0 + n - 1, "GEO / SEO AI SEARCH",
         "Paris được AI trích dẫn ở cụm nỗi sợ · vật liệu · giá · chọn cơ sở"),
        (C_TARGET, last, "TRAFFIC & LEAD CHUYỂN ĐỔI",
         "Tách kênh Traffic AI, Time-on-site > 2,5 phút, đồng bộ Lead"),
    ]
    for c1, c2, title, desc in banners:
        c2 = max(c1, min(c2, last))
        band(ws, 3, c1, c2, title, BLUE, size=10)
        band(ws, 4, c1, c2, desc, BLUE_LIGHT, size=9, color=INK)

    hdr = ["TRỤ CỘT KPI", "", "HẠNG MỤC / CHỈ TIÊU TRỌNG TÂM", "Số lượng", "", "Hiện tại"]
    hdr += [m["header"] for m in months]
    hdr += ["ĐÍCH ĐẾN CHU KỲ (TARGET)", "TRỌNG SỐ", "TRỌNG SỐ"]
    for i, h in enumerate(hdr, start=1):
        put(ws, 6, i, h, bold=True, size=9, color=WHITE, fill=BLUE, ha="center")

    r = 7

    def pillar_block(name, weight, rows):
        nonlocal r
        start = r
        for sub, item, qty, level, now, per_month, target, w_row in rows:
            put(ws, r, C_SUB, sub, size=9)
            put(ws, r, C_ITEM, item, size=10)
            put(ws, r, C_QTY, qty, ha="center")
            put(ws, r, C_LEVEL, level, ha="center", size=9)
            put(ws, r, C_NOW, now, ha="center", size=9)
            for i in range(n):
                put(ws, r, C_M0 + i, per_month[i] if per_month else None, ha="center")
            put(ws, r, C_TARGET, target, size=9)
            put(ws, r, C_W_ROW, w_row, ha="center", size=9)
            put(ws, r, C_W_PILLAR, None)
            r += 1
        ws.merge_cells(start_row=start, start_column=C_PILLAR, end_row=r - 1, end_column=C_PILLAR)
        put(ws, start, C_PILLAR, name, bold=True, size=11, fill=BLUE_MID, ha="center")
        ws.merge_cells(start_row=start, start_column=C_W_PILLAR, end_row=r - 1, end_column=C_W_PILLAR)
        put(ws, start, C_W_PILLAR, weight, bold=True, ha="center")

    # 1 · Hạ tầng
    pillar_block("1. Hạ tầng Web & Hub", 0.10, [
        ("", "Kiến trúc hệ thống & UI/UX các chuyên khoa", None, "", UNVERIFIED, None,
         "Hoàn thiện cổng Hub theo chuyên khoa; schema Dentist/LocalBusiness; tải trang < 2s", 0.05),
        ("", "Phân line chuyên khoa & Cổng Hub liên kết", None, "", UNVERIFIED, None,
         "Hub trung tâm liên kết đủ landing từng chuyên khoa + 7 trang cơ sở", 0.05),
    ])

    # 2 · Sản lượng
    rows = []
    for ln in lines:
        per = [by_line_month[ln][i] for i in range(n)]
        rows.append(("", ln, sum(per), "", "—", per,
                     f"Sản xuất theo bản đồ nội dung — tổng {sum(per)} bài trong chu kỳ",
                     round(0.20 / max(1, len(lines)), 3)))
    hubs = hub_plan(n)
    hub_per = [len(h) for h in hubs]
    rows.append(("", "Trang local — 7 hub cơ sở", sum(hub_per), "", "—", hub_per,
                 "Hà Nội · Hải Phòng · Quảng Ninh · Vinh · Đà Nẵng · TP.HCM · Bình Dương. "
                 "Tỉnh KHÔNG có cơ sở nằm ngoài phạm vi chu kỳ (R3)", "—"))
    pillar_block("2. Sản lượng Bài viết", 0.20, rows)

    # 3 · SEO & GEO — trọng số ghi MỘT LẦN cho mỗi nhóm phụ, không lặp theo line
    rows, first = [], True
    for ln in lines:
        for lv in ("Top 3", "Top 5", "Top 10"):
            rows.append(("Top từ khoá Google Search", ln, None, lv, UNVERIFIED, None,
                         "Top 1–3 từ khoá Brand & Top 5 dịch vụ giá trị lớn",
                         0.20 if first else ""))
            first = False
    first = True
    for ln in lines:
        for lv in ("ChatGPT", "Gemini", "AI-ov"):
            rows.append(("Tối ưu GEO AI Search", ln, None, lv, UNVERIFIED, None,
                         "Paris được AI trích dẫn — đo ẩn danh, 3 lần lấy đa số, "
                         "theo xu hướng tháng, ghi cả đối thủ được AI nhắc",
                         0.20 if first else ""))
            first = False
    pillar_block("3. SEO & GEO AI Search", 0.40, rows)

    # 4 · Traffic
    rows = []
    for i, ln in enumerate(lines):
        rows.append(("google.com.vn", ln, None, "", UNVERIFIED, None,
                     "Tăng trưởng Organic Traffic, Time-on-site > 2,5 phút",
                     0.10 if i == 0 else ""))
    for i, ln in enumerate(lines):
        rows.append(("Traffic AI", ln, None, "", UNVERIFIED, None,
                     "Phiên từ ChatGPT · Gemini · Claude · Perplexity · Brave",
                     0.05 if i == 0 else ""))
    pillar_block("4. Traffic", 0.15, rows)

    # 5 · Lead
    rows = [("", ln, None, "", UNVERIFIED, None, "Tỷ lệ chuyển đổi đạt mục tiêu kỳ", "—")
            for ln in lines]
    rows += [("Chuỗi sau form", x, None, "", UNVERIFIED, None, note, "—") for x, note in (
        ("Công cụ kiểm tra răng online (micro-conversion)",
         "Đo riêng — bước gỡ rào NGẠI trước form"),
        ("sđt xác nhận (có nhu cầu)", "Đo xuyên suốt form → sđt → đến phòng khám → doanh số"),
        ("KH đến phòng khám", "Đo xuyên suốt form → sđt → đến phòng khám → doanh số"),
        ("Doanh số", "Đo xuyên suốt form → sđt → đến phòng khám → doanh số"),
    )]
    pillar_block("5. Form Lead & Chuyển đổi", 0.15, rows)

    # hai dòng trọng số
    r += 1
    put(ws, r, C_PILLAR, "TRỌNG SỐ ĐÁNH GIÁ THÁNG", bold=True, size=10, color=WHITE, fill=BLUE)
    put(ws, r, C_ITEM, "Tỷ trọng mức độ hoàn thành theo từng tháng", size=9)
    weights = [phase_of(i, n)[1] for i in range(n)]
    scale = sum(weights)
    for i in range(n):
        put(ws, r, C_M0 + i, round(weights[i] / scale, 3), ha="center")
    put(ws, r, C_TARGET, "Tổng phân bổ", bold=True, ha="center")
    put(ws, r, C_W_ROW, 1.0, bold=True, ha="center")
    r += 1
    put(ws, r, C_PILLAR, "TỔNG TRỌNG SỐ DANH MỤC", bold=True, size=10, color=WHITE, fill=BLUE)
    put(ws, r, C_ITEM, "Tổng trọng số đánh giá 5 trụ cột KPI của chu kỳ", size=9)
    for i in range(n):
        put(ws, r, C_M0 + i, phase_of(i, n)[0], ha="center", size=9)
    put(ws, r, C_TARGET, "Tổng phân bổ", bold=True, ha="center")
    put(ws, r, C_W_PILLAR, 1.0, bold=True, ha="center")

    widths = {C_PILLAR: 23, C_SUB: 22, C_ITEM: 44, C_QTY: 10, C_LEVEL: 10, C_NOW: 26,
              C_TARGET: 44, C_W_ROW: 10, C_W_PILLAR: 10}
    for c in range(C_M0, C_M0 + n):
        widths[c] = 12
    for c, wd in widths.items():
        ws.column_dimensions[get_column_letter(c)].width = wd
    ws.row_dimensions[2].height = 26
    ws.freeze_panes = "D7"
    return ws


# ──────────────────────── TAB 2 — CÔNG VIỆC TRIỂN KHAI ────────────────────

def detail_text(cl_list):
    parts = []
    raos, raocans = [], []
    for c in sorted(cl_list, key=lambda x: (x["tier"], x["rank"])):
        qty = (f"{c['art']}/{c['art_total']} bài (làm tiếp ở tháng khác)"
               if c.get("split") else f"{c['art']} bài")
        parts.append(f"{c['code']} {c['name'].replace('⭐', '').strip()} "
                     f"(Tầng {c['tier']} · {c['stage']} · gỡ rào {RAOCAN_OF.get(c['code'], '—')} "
                     f"· {qty} → {c['url'] or 'trang đích cần chốt'})")
        for x in RAO_OF.get(c["code"], "").split(" · "):
            if x and x not in raos:
                raos.append(x)
        if RAOCAN_OF.get(c["code"]) not in raocans:
            raocans.append(RAOCAN_OF.get(c["code"]))
    return ("Sản xuất theo bản đồ nội dung: " + "; ".join(parts) +
            ". Áp 6 quy tắc trích dẫn AI (BLUF · có số · phủ 8 góc hỏi · nói cả điều bất lợi · "
            "ngày cập nhật + BS thẩm định · không nhồi từ khoá). "
            f"Soát rào: {' · '.join(raos)}. Duyệt 2 lớp BS + Pháp chế.")


def build_tasks(wb, months, assigned, lines):
    ws = wb.create_sheet("CÔNG VIỆC TRIỂN KHAI")
    n = len(months)
    # Mã KPI ổn định giữa các tháng: 01–04 nền, mỗi line một mã, rồi tới các mã vận hành.
    line_code = {ln: f"KPI-{5 + i:02d}" for i, ln in enumerate(lines)}
    nxt = 5 + len(lines)
    C_LOCAL, C_QC, C_SEO, C_GEO, C_TRAFFIC, C_LEAD, C_LEGAL = (
        f"KPI-{nxt + k:02d}" for k in range(7))
    heads = ["Mã KPI", "Trụ cột KPI", "Hạng mục", "Tháng", "CHỈ TIÊU (số bài)",
             "Trong đó CORE", "Công việc chi tiết", "Người phụ trách", "Hạn chót", "Hoàn thành"]
    for i, h in enumerate(heads, start=1):
        put(ws, 1, i, h, bold=True, size=10, color=WHITE, fill=BLUE_DEEP, ha="center")

    by_month = defaultdict(list)
    for c in assigned:
        by_month[c["month"]].append(c)
    hubs = hub_plan(n)

    r = 2
    month_totals = []
    task_rows = 0

    for i, mo in enumerate(months):
        phase, _ = phase_of(i, n)
        band(ws, r, 1, 10,
             f"════  {mo['banner']}  ·  giai đoạn {phase.upper()}  ·  hạn chót {mo['deadline']}  ════",
             BLUE_DEEP, size=11)
        r += 1

        def task(code, pillar, item, qty, core, detail, owner,
                 fill=None, bold=False, color=INK):
            nonlocal r, task_rows
            put(ws, r, 1, code, size=9, ha="center", fill=fill, bold=bold, color=color)
            put(ws, r, 2, pillar, size=9, fill=fill, bold=bold, color=color)
            put(ws, r, 3, item, size=10, fill=fill, bold=bold, color=color)
            put(ws, r, 4, mo["label"], size=9, ha="center", fill=fill, bold=bold, color=color)
            put(ws, r, 5, qty, ha="center", fill=fill, bold=bold, color=color)
            put(ws, r, 6, core, ha="center", fill=fill, bold=bold, color=color)
            put(ws, r, 7, detail, size=9, fill=fill, color=color)
            put(ws, r, 8, owner, size=9, ha="center", fill=fill, color=color)
            put(ws, r, 9, mo["deadline"], size=9, ha="center", fill=fill, color=color)
            put(ws, r, 10, False, ha="center", fill=fill, color=color)
            r += 1
            task_rows += 1

        setup = (i == 0)
        task("KPI-01", "1. Hạ tầng Web & Hub", "Kiến trúc hệ thống & UI/UX các chuyên khoa",
             None, None,
             "Quy hoạch kiến trúc theo 6 chuyên khoa, chốt sơ đồ URL, "
             "ĐỐI CHIẾU SITEMAP THẬT để xác nhận trang đích nào đã có / phải tạo mới" if setup
             else "Thiết kế & bàn giao UI/UX từng chuyên khoa theo tiến độ", "Team Tech/Dev")
        task("KPI-02", "1. Hạ tầng Web & Hub", "Phân line chuyên khoa & Cổng Hub liên kết",
             None, None,
             "Quy hoạch Hub: Implant · Chỉnh nha · Thẩm mỹ · Tổng quát & Nha chu · Trẻ em; "
             "chốt quy tắc liên kết Hub ↔ landing ↔ 7 trang cơ sở" if setup
             else "Liên kết Hub ↔ landing, đẩy schema Dentist/LocalBusiness, kiểm tra tải trang < 2s",
             "Team Tech/Dev")
        task("KPI-03", "2. Tuyến nội dung theo hành trình", "Quy chuẩn loại bài + checklist R1 & R7",
             None, None,
             "Ban hành khung loại bài + CHECKLIST TỪ CẤM (R1) + CHECKLIST 4 HÃNG được dùng chữ "
             "'chính hãng' — Straumann · Invisalign · Nacera · Ormco (R7) cho toàn đội content" if setup
             else "Triển khai bài tình huống & hỏi đáp chuyên sâu theo khung đã ban hành; "
                  "rà soát ngẫu nhiên 10% bài đã đăng theo checklist R1 & R7", "Team Content")
        task("KPI-04", "2. Tuyến nội dung theo hành trình",
             "Gắn thẻ tagging theo hành trình KH (S1–S6)", None, None,
             "Thiết lập cấu trúc tag theo chuyên khoa × giai đoạn S1–S6 × rào cản SỢ/NGỜ/NGẠI" if setup
             else "Gắn thẻ 100% bài mới theo chuyên khoa × giai đoạn S1–S6 × rào cản", "Team Content")

        month_total = month_core = 0
        for ln in lines:
            cls = [c for c in by_month[i] if c["line"] == ln]
            if not cls:
                continue
            svc_groups = defaultdict(list)
            for c in cls:
                svc_groups[c["svc"]].append(c)
            si = 0
            l_total = l_core = 0
            for svc in sorted(svc_groups):
                si += 1
                g = svc_groups[svc]
                art = sum(x["art"] for x in g)
                core = sum(x["core"] for x in g if x["tier"] == "A")
                l_total += art
                l_core += core
                task(f"{line_code[ln]}.{si}", f"3. Sản lượng — {ln}", svc, art, core,
                     detail_text(g), "Team Content", fill=CREAM)
            task(line_code[ln], f"3. Sản lượng — {ln}", f"▶ TỔNG {ln.upper()}", l_total, l_core,
                 f"Tổng sản lượng {ln} trong tháng — cộng từ các dòng chi tiết phía trên",
                 "Lead Content", fill=BLUE_LIGHT, bold=True)
            month_total += l_total
            month_core += l_core

        batch = hubs[i]
        if batch:
            task(C_LOCAL, "3. Sản lượng — Trang local", f"Hub cơ sở: {' · '.join(batch)}",
                 len(batch), len(batch),
                 f"Dựng {len(batch)} trang local chuẩn NAP cho {' · '.join(batch)} — "
                 f"LẤY địa chỉ, SĐT và SỐ GIẤY PHÉP CỦA CHÍNH CƠ SỞ ĐÓ tại /tim-phong-kham.html "
                 f"ngay tại thời điểm chạy; nêu đúng phạm vi chuyên môn, kỹ thuật ngoài phạm vi "
                 f"thì ghi rõ điều hướng về cơ sở thực hiện; gắn schema LocalBusiness/Dentist (R3 · R2)",
                 "Team Content/SEO", fill=CREAM)
            month_total += len(batch)
            month_core += len(batch)
        else:
            task(C_LOCAL, "3. Sản lượng — Trang local", "Rà soát & tối ưu 7 trang cơ sở đã dựng",
                 None, None,
                 "Đã phủ đủ 7 hub có cơ sở thật — tháng này KHÔNG dựng thêm trang tỉnh. "
                 "Rà lại NAP, số giấy phép, phạm vi chuyên môn; cập nhật nếu /tim-phong-kham.html "
                 "đổi dữ liệu. Trang 'dịch vụ × tỉnh không có cơ sở' đẩy backlog (R3)",
                 "Team Content/SEO", fill=CREAM)

        task("KPI-TỔNG", "3. Sản lượng Bài viết", "★ TỔNG SẢN LƯỢNG THÁNG (toàn hệ thống)",
             month_total, month_core,
             "Con số lãnh đạo đọc: tổng đầu việc nội dung hoàn thành trong tháng",
             "Lead Content/SEO", fill=RED, bold=True, color=WHITE)
        month_totals.append(month_total)

        task(C_QC, "3. Sản lượng — Kiểm duyệt",
             "Quy trình biên tập & duyệt 2 lớp (BS + Pháp chế)", None, None,
             "Thống nhất ma trận ai viết / ai thẩm định; soát R1 (cam kết & mức độ đau) · "
             "R4 (chỉ 3 bác sĩ có hồ sơ) · R5 (ảnh & before-after) · R6 (không phán xét nơi cũ) · "
             "R7 (chữ 'chính hãng') · R13 (không chẩn đoán, không hứa thời gian cứng) trước khi phát hành",
             "BS + Pháp chế")
        task(C_SEO, "4. SEO & GEO AI Search", "Top từ khoá Google Search", None, None,
             "Audit từ khoá & nghiên cứu bộ từ khoá 6 chuyên khoa, chốt bộ theo dõi, lấy mốc gốc" if setup
             else "Theo dõi Top 3/5/10, tối ưu bài đã đăng theo khoảng cách thứ hạng", "Team SEO")
        task(C_GEO, "4. SEO & GEO AI Search",
             "Đo GEO — 3 bộ prompt (20 dịch vụ · 7 hub · 10 thương hiệu)", None, None,
             "XÂY và KHOÁ 3 bộ prompt; chạy ẩn danh trên ChatGPT · Gemini · AI Overview, "
             "3 lần lấy đa số, ghi 1/0 + ghi đối thủ được AI nhắc — ĐÂY LÀ MỐC GỐC, "
             "không đặt chỉ tiêu tăng trưởng cho tháng này" if setup
             else "Chạy lại bộ đo đã khoá, ghi 1/0 theo nền tảng, so xu hướng với tháng trước, "
                  "ghi chú đối thủ được AI nhắc; xếp lại Cơ hội GEO của từng cụm theo traffic thật",
             "Team SEO/GEO")
        task(C_TRAFFIC, "5. Traffic & Chuyển đổi", "Traffic & Time-on-site", None, None,
             "Thiết lập GA4 + heatmap, TÁCH KÊNH Traffic AI (ChatGPT · Gemini · Claude · "
             "Perplexity · Brave), đo mốc gốc — Paris hiện chưa có số nào" if setup
             else "Theo dõi Organic + Traffic AI theo từng nguồn LLM, Time-on-site > 2,5 phút",
             "Team Data/SEO")
        task(C_LEAD, "5. Traffic & Chuyển đổi",
             "Tỷ lệ chuyển đổi Lead + micro-conversion công cụ online", None, None,
             "Gắn form tư vấn, dựng funnel lead, GẮN ĐO 4 công cụ kiểm tra online "
             "(răng miệng · niềng · răng sứ · trồng răng) làm micro-conversion trước form" if setup
             else "Đo form → sđt xác nhận → đến phòng khám; tối ưu CTA theo trang có traffic AI cao; "
                  "đo tỷ lệ dùng công cụ online → form", "Team MKT/Lead")
        if setup:
            task(C_LEGAL, "0. Pháp lý",
                 "GXNNDQC (R9) · văn bản đối tác 4 hãng (R7) · bảng giá hiện hành (R12)",
                 None, None,
                 "BA ĐẦU VIỆC CHẶN TIẾN ĐỘ, phải xong trong tháng Setup: "
                 "① Lập danh mục nội dung quảng cáo dịch vụ KCB cần GXNNDQC, nộp Sở Y tế trước "
                 "chiến dịch — R9 chạm phần lớn cụm Tầng A. "
                 "② Thu thập văn bản chứng minh quan hệ đối tác Straumann · Invisalign · Nacera · "
                 "Ormco để dùng chữ 'chính hãng' an toàn (R7). "
                 "③ Lấy bảng giá min–max + điều kiện & lãi suất trả góp hiện hành từ trang bảng giá; "
                 "KHÔNG đưa con số vào kế hoạch, chỉ chốt quy trình cập nhật (R12)", "Pháp chế")
        r += 1

    # panel phải
    band(ws, 1, 12, 13, "TỔNG SẢN LƯỢNG THEO THÁNG", RED)
    pr = 2
    for i, mo in enumerate(months):
        put(ws, pr, 12, mo["label"], size=9)
        put(ws, pr, 13, month_totals[i], ha="center")
        pr += 1
    put(ws, pr, 12, "TỔNG CHU KỲ", bold=True, size=9, fill=BLUE_LIGHT)
    put(ws, pr, 13, sum(month_totals), bold=True, ha="center", fill=BLUE_LIGHT)
    pr += 2
    band(ws, pr, 12, 13, "THỐNG KÊ TIẾN ĐỘ", BLUE_DEEP)
    pr += 1
    for label, val in (("Tổng số đầu việc KPI", task_rows), ("Đã hoàn thành", 0),
                       ("Chưa hoàn thành", task_rows), ("Tiến độ chung", 0)):
        put(ws, pr, 12, label, size=9)
        put(ws, pr, 13, val, ha="center")
        pr += 1
    pr += 1
    ws.merge_cells(start_row=pr, start_column=12, end_row=pr + 4, end_column=13)
    put(ws, pr, 12,
        "Dòng nền đỏ ★ là con số tổng của tháng — đọc trực tiếp ở cột CHỈ TIÊU. "
        "Dòng nền xanh ▶ là tổng của từng business line. Các dòng nền kem là chi tiết từng bộ dịch vụ.",
        size=9, fill=BLUE_LIGHT)

    for c, wd in {1: 11, 2: 32, 3: 44, 4: 10, 5: 14, 6: 13, 7: 80, 8: 18, 9: 12, 10: 12,
                  11: 3, 12: 28, 13: 12}.items():
        ws.column_dimensions[get_column_letter(c)].width = wd
    ws.freeze_panes = "A2"
    return ws


# ─────────────────────────────────── main ─────────────────────────────────

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", required=True, help="YYYY-MM")
    ap.add_argument("--months", type=int, required=True)
    ap.add_argument("--scope", default="all", help="danh sách key bộ, phẩy ngăn cách; hoặc 'all'")
    ap.add_argument("--tiers", default="A,B,C", help="tầng đưa vào chu kỳ")
    ap.add_argument("-o", "--out", default=None)
    a = ap.parse_args()

    scope = [s.strip() for s in a.scope.split(",")]
    tiers = {t.strip().upper() for t in a.tiers.split(",")}

    clusters = [c for c in load_clusters(scope) if c["tier"] in tiers]
    if not clusters:
        sys.exit("Không có cụm nào khớp phạm vi/tầng đã chọn.")

    months = month_labels(a.start, a.months)
    assigned, load = assign(clusters, a.months)

    lines = [ln for ln in LINE_ORDER if any(c["line"] == ln for c in assigned)]
    by_line_month = {ln: [0] * a.months for ln in lines}
    for c in assigned:
        by_line_month[c["line"]][c["month"]] += c["art"]
    hubs = hub_plan(a.months)
    total_by_month = [sum(by_line_month[ln][i] for ln in lines) + len(hubs[i])
                      for i in range(a.months)]

    wb = openpyxl.Workbook()
    wb.remove(wb.active)
    build_kpi(wb, months, by_line_month, lines, total_by_month)
    build_tasks(wb, months, assigned, lines)

    out = a.out or os.path.join(
        ROOT, "template",
        f"GEO-NKPARIS-T{months[0]['m']:02d}-T{months[-1]['m']:02d}-{months[-1]['y']}.xlsx")
    wb.save(out)
    lo, hi = min(total_by_month), max(total_by_month)
    print(f"✔ {out}")
    print(f"  {len(assigned)} lát cụm · {sum(c['art'] for c in assigned)} bài nội dung "
          f"· {sum(len(h) for h in hubs)} trang local · {a.months} tháng · {len(lines)} business line")
    print("  Tổng sản lượng theo tháng: " + " · ".join(
        f"{m['label']}={total_by_month[i]}" for i, m in enumerate(months)))
    print(f"  Chênh lệch tháng cao/thấp: {round((hi - lo) / hi * 100)}% "
          f"({'ĐẠT' if (hi - lo) / hi <= 0.25 else 'VƯỢT'} ràng buộc ≤25%)")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
