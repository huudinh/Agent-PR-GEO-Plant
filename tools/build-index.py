# -*- coding: utf-8 -*-
"""
build-index.py — Sinh knowledge/geo-bo-truy-van-index.md từ data/bo-truy-van/*.json.

    python tools/build-index.py

`data/bo-truy-van/*.json` là NGUỒN SỰ THẬT về khối lượng công việc. Sửa dữ liệu ở đó
rồi chạy lại script này; KHÔNG sửa tay file index trong knowledge/.

Script đồng thời tự soát ba bất biến của mỗi bộ và dừng nếu lệch:
  · đúng 15 cụm C01–C15
  · tổng % điểm của 15 cụm = 100
  · phân bổ tầng A/B/C/D = 5/5/3/2 cụm
"""
import glob
import json
import os
import sys
from collections import OrderedDict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "data", "bo-truy-van")
OUT = os.path.join(ROOT, "knowledge", "geo-bo-truy-van-index.md")

SONG_TEN = {1: "S1 (0–30n)", 2: "S2 (31–60n)", 3: "S3 (61–90n)", 4: "Nền (>90n)"}
TANG_CHUAN = {"A": 5, "B": 5, "C": 3, "D": 2}


def load():
    sets = []
    for path in sorted(glob.glob(os.path.join(SRC, "*.json"))):
        with open(path, encoding="utf-8") as fh:
            d = json.load(fh)
        d["_file"] = os.path.basename(path)
        sets.append(d)
    return sets


def validate(sets):
    loi = []
    for d in sets:
        cum = d["cum"]
        if len(cum) != 15:
            loi.append(f"{d['_file']}: {len(cum)} cụm (phải là 15)")
        pct = sum(c["pct"] for c in cum)
        if pct != 100:
            loi.append(f"{d['_file']}: tổng % điểm = {pct} (phải là 100)")
        dem = {}
        for c in cum:
            dem[c["tang"]] = dem.get(c["tang"], 0) + 1
        if dem != TANG_CHUAN:
            loi.append(f"{d['_file']}: phân bổ tầng {dem} (chuẩn {TANG_CHUAN})")
        ma = sorted(c["ma"] for c in cum)
        if ma != [f"C{i:02d}" for i in range(1, 16)]:
            loi.append(f"{d['_file']}: mã cụm không đủ C01–C15")
    return loi


def bang(headers, rows):
    out = ["| " + " | ".join(headers) + " |",
           "|" + "|".join(["---"] * len(headers)) + "|"]
    for r in rows:
        out.append("| " + " | ".join("" if v is None else str(v) for v in r) + " |")
    return "\n".join(out) + "\n"


def main():
    sets = load()
    if not sets:
        sys.exit(f"Không tìm thấy file nào trong {SRC}")
    loi = validate(sets)
    if loi:
        print("✖ Dữ liệu nguồn chưa hợp lệ:")
        for e in loi:
            print("  ·", e)
        sys.exit(1)

    tong_cum = sum(len(d["cum"]) for d in sets)
    tong_bai = sum(c["bai"] for d in sets for c in d["cum"])
    tong_tv = sum(d["quy_mo"]["truy_van"] for d in sets)

    L = []
    L.append("# GEO — CHỈ MỤC BỘ TRUY VẤN & BẢN ĐỒ NỘI DUNG · NHA KHOA PARIS\n")
    L.append("> Sinh tự động từ `data/bo-truy-van/*.json` bằng `tools/build-index.py`. "
             "**Không sửa tay file này** —\n"
             "> sửa file JSON nguồn rồi chạy lại script. Đây là **nguồn sự thật về khối lượng công việc**:\n"
             "> mỗi cụm cho biết cần bao nhiêu bài, thuộc giai đoạn nào của khách, sóng nào, trang đích nào.\n")
    L.append(f"**Tổng kho:** {len(sets)} bộ dịch vụ · {tong_cum} cụm chủ đề · **{tong_bai} bài viết** "
             f"cần sản xuất · {tong_tv:,} truy vấn đã phân loại.\n".replace(",", "."))

    L.append("**Quy ước đọc bảng:**\n")
    L.append(bang(["Ký hiệu", "Nghĩa"], [
        ["Tầng A", "CORE 80/20 — làm trong 90 ngày, **70% ngân sách nội dung**"],
        ["Tầng B", "Đòn bẩy chuyển đổi — bắt đầu khi A xong ~60%, **20%**"],
        ["Tầng C", "Uy tín & giữ chân — chạy nền, **10%**"],
        ["Tầng D", "Cửa vào rộng — **0% ngân sách mới**, chỉ viết pillar nền / tái sử dụng"],
        ["S1…S6", "Giai đoạn hành trình: Nhận biết · Tìm hiểu · Cân nhắc & nỗi sợ · "
                  "Thực hiện · Trải nghiệm & hậu điều trị · Gắn bó & mở rộng"],
        ["Sóng", "S1 0–30 ngày · S2 31–60 ngày · S3 61–90 ngày · Nền sau 90 ngày"],
        ["TV / CORE", "Số truy vấn của cụm / trong đó bao nhiêu truy vấn thuộc CORE 80/20"],
        ["Bài", "Số bài cần sản xuất cho cụm (`—` = tái sử dụng nội dung, không tính sản lượng mới)"],
        ["SỢ · NGỜ · NGẠI", "Ba rào cản chốt của khách nha khoa — mọi cụm phải gỡ được ít nhất một"],
        ["⚠ đối chiếu", "Trang đích CHƯA xác minh trên sitemap thật — phải soi chiếu trước khi giao việc"],
    ]))

    L.append("**Bảng tổng hợp khối lượng theo bộ:**\n")
    rows = []
    for i, d in enumerate(sets, 1):
        rows.append([i, d["ten"], d["line_ten"], f"`{d['_file']}`",
                     len(d["cum"]), f"**{sum(c['bai'] for c in d['cum'])}**"])
    rows.append(["", "**TỔNG**", "", "", f"**{tong_cum}**", f"**{tong_bai}**"])
    L.append(bang(["#", "Bộ dịch vụ", "Business line", "File nguồn", "Cụm", "Bài cần SX"], rows))

    # khối lượng theo business line — trục phân nhóm KPI sản lượng
    theo_line = OrderedDict()
    for d in sets:
        k = d["line_ten"]
        theo_line.setdefault(k, {"bo": [], "bai": 0, "cum": 0})
        theo_line[k]["bo"].append(d["ten"])
        theo_line[k]["bai"] += sum(c["bai"] for c in d["cum"])
        theo_line[k]["cum"] += len(d["cum"])
    L.append("**Khối lượng theo business line** — đây là trục phân nhóm dòng KPI sản lượng của file output:\n")
    L.append(bang(["Business line", "Bộ dịch vụ", "Cụm", "Bài"],
                  [[k, " · ".join(v["bo"]), v["cum"], f"**{v['bai']}**"]
                   for k, v in theo_line.items()]))

    L.append("---\n")

    for i, d in enumerate(sets, 1):
        bai_bo = sum(c["bai"] for c in d["cum"])
        q = d["quy_mo"]
        L.append(f"## {i}. {d['ten']}\n")
        L.append(f"`{d['_file']}` · {d['line_ten']} · **{bai_bo} bài cần sản xuất**\n")
        L.append(f"**Quy mô bộ:** {q['truy_van']} truy vấn · {q['cum']} cụm · {q['doi_tuong']} nhóm đối tượng "
                 f"· {q['core']} truy vấn CORE 80/20 ({round(q['core'] / q['truy_van'] * 100)}% bộ) "
                 f"chiếm {q['pct_diem_core']}% điểm ưu tiên\n")

        L.append("**Nỗi sợ quyết định (mọi nội dung phải gỡ được ít nhất một):**\n")
        for ns in d["noi_so"]:
            L.append(f"- {ns['ma']} {ns['ten']} → cụm xử lý **{ns['cum']}** "
                     f"({ns['tv']} truy vấn, {ns['core']} CORE)")
        L.append("")

        L.append("**Hành trình 6 giai đoạn:**\n")
        L.append(bang(["GĐ", "Ưu tiên", "Nỗi sợ chi phối", "Cụm", "TV", "CORE", "% điểm"],
                      [[h["gd"], h["uu_tien"], h["noi_so"], h["cum"], h["tv"], h["core"], f"{h['pct']}%"]
                       for h in d["hanh_trinh"]]))

        L.append("**Phân bổ 80/20:**\n")
        L.append(bang(["Tầng", "Cụm", "TV", "% điểm", "Phân bổ & danh sách cụm"],
                      [[t["tang"], t["cum"], t["tv"], f"{t['pct']}%", t["phan_bo"]] for t in d["tang"]]))

        L.append(f"**Bản đồ nội dung — {len(d['cum'])} cụm:**\n")
        L.append(bang(["Hạng", "Mã", "Cụm chủ đề", "Tầng", "GĐ", "TV", "CORE", "% điểm",
                       "Bài", "Sóng", "Trang đích"],
                      [[c["hang"], c["ma"], c["ten"], c["tang"], c["gd"], c["tv"],
                        c["core"] or "—", f"{c['pct']}%", c["bai"] or "—",
                        SONG_TEN[c["song"]], c["trang_dich"]] for c in d["cum"]]))
        L.append("---\n")

    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L))
    print(f"✔ {OUT}")
    print(f"  {len(sets)} bộ · {tong_cum} cụm · {tong_bai} bài · {tong_tv} truy vấn")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
