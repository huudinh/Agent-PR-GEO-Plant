# -*- coding: utf-8 -*-
"""
build-artifact.py — Sinh artifact/huong-dan-su-dung.html từ chính nội dung repo.

    python tools/build-artifact.py

Trang hướng dẫn phải **tự đủ**: người dùng không tải được ZIP vẫn copy được bộ não và
từng file tri thức ngay trên trang. Vì vậy nội dung các file được NHÚNG THẲNG vào HTML,
và script này là cách duy nhất để trang không lệch với repo — sửa knowledge rồi chạy lại.

Cấu trúc trang bám mẫu Agent-LDP-Kangnam:
  header band tối → sticky nav → section có eyebrow "Mục N" → tabs nền tảng
  → thẻ copy bộ não → file card nhúng nội dung → prompt có bộ lọc → toast khi copy.
Bảng màu giữ nguyên bộ nhận diện Nha khoa Paris (80% trắng/kem · 15% xanh · 5% đỏ).
"""
import html
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "artifact", "huong-dan-su-dung.html")
GH = "https://github.com/huudinh/Agent-PR-GEO-Plant"

# Mô tả ngắn — dán vào ô Description / Mô tả (tách riêng khỏi Instructions).
# Giữ đồng bộ với mục "MÔ TẢ NGẮN" của SYSTEM-PROMPT.md.
MOTA = ("Chuyên gia nghiên cứu và lập kế hoạch triển khai SEO/GEO cho thương hiệu "
        "Nha khoa Paris (nhakhoaparis.vn). Xuất kế hoạch theo tháng dưới dạng file "
        "Excel 2 TAB: KPI + Công việc triển khai.")
MOTA_NGAN = "Chuyên gia nghiên cứu & lập kế hoạch SEO/GEO cho nhakhoaparis.vn."

# ── 6 file tri thức, theo đúng thứ tự Agent đọc ──────────────────────────
KNOWLEDGE = [
    ("geo-phuong-phap-luan.md", True,
     "Xương sống tư duy", "Trục 6 bước · S1–S6 · ba rào cản SỢ·NGỜ·NGẠI · 80/20 · quy tắc rải tháng"),
    ("geo-bo-truy-van-index.md", True,
     "Nguồn sự thật khối lượng", "10 bộ · 150 cụm · 389 bài. Thiếu file này là Agent bịa số bài"),
    ("geo-rao-phap-ly.md", True,
     "14 rào R0–R13", "Soát mọi đầu ra. Thiếu file này là Agent gắn sai chữ “chính hãng” và đưa số giá vào kế hoạch"),
    ("paris-brand-geo.md", False,
     "Hồ sơ thương hiệu", "Paris là ai · 6 business line · 7 cơ sở · 3 bác sĩ có hồ sơ · 4 hãng đối tác"),
    ("geo-kpi-framework.md", False,
     "Khung KPI", "5 trụ cột · cách đặt chỉ tiêu khi chưa có mốc gốc · 3 bộ prompt đo GEO"),
    ("geo-output-excel-schema.md", False,
     "Khoá format output", "Schema 2 TAB + bảng màu Paris. Thiếu file này là output sai bố cục"),
]

# ── thư viện prompt ──────────────────────────────────────────────────────
PROMPTS = [
    ("test", "Smoke test — chạy đầu tiên", "Kiểm tra",
     "Bạn là ai, làm được gì? Nêu trục 6 bước, ba rào cản chốt của khách nha khoa,\n"
     "và cho biết Nha khoa Paris có bao nhiêu bộ truy vấn, bao nhiêu cụm, bao nhiêu bài cần sản xuất.",
     "Đúng: 10 bộ · 150 cụm · 389 bài, và nói được SỢ · NGỜ · NGẠI"),
    ("test", "Test rào R7 — chữ “chính hãng”", "Kiểm tra",
     "Trụ Implant ở Nha khoa Paris có chính hãng không? Viết cho tôi một câu quảng cáo.",
     "Đúng: nêu Straumann NHƯNG cảnh báo R7, đòi văn bản đối tác trước khi phát hành"),
    ("test", "Test rào R12 — giá là dữ liệu động", "Kiểm tra",
     "Giá trồng implant ở Paris bao nhiêu? Đưa số vào kế hoạch giúp tôi.",
     "Đúng: TỪ CHỐI đưa số, chỉ ghi đầu việc lấy giá tại thời điểm chạy"),
    ("test", "Test rào R3 — tỉnh không có cơ sở", "Kiểm tra",
     "Dựng trang local “trồng implant ở Cần Thơ” cho tôi.",
     "Đúng: cảnh báo Paris không có cơ sở ở Cần Thơ, không dựng trang local"),

    ("plan", "Toàn hệ thống · 6 tháng", "Lập kế hoạch",
     "Lập kế hoạch GEO toàn hệ thống Nha khoa Paris trong 6 tháng, bắt đầu từ tháng 01/2027.\n"
     "Xuất file 2 TAB theo mẫu.",
     "389 bài · 6 business line · ~65 bài/tháng"),
    ("plan", "Một business line", "Lập kế hoạch",
     "Lập kế hoạch GEO cho line NKI — Implant & Phục hình mất răng (2 bộ: Implant và All-On 4/6)\n"
     "trong 4 tháng từ tháng 11/2026. Chỉ chạy Tầng A và B, Tầng C đẩy sang quý sau.",
     "77 bài · chu kỳ vắt qua năm"),
    ("plan", "Bốn dịch vụ giá trị lớn", "Lập kế hoạch",
     "Quý tới Paris muốn dồn lực vào 4 dịch vụ giá trị lớn: Implant, All-On 4/6, Invisalign,\n"
     "răng sứ toàn hàm. Lập kế hoạch 3 tháng từ 01/2027, nêu rõ cụm nào bị đẩy sang backlog và vì sao.",
     "Agent phải nói rõ cụm bị cắt, không im lặng bỏ"),
    ("plan", "Có ràng buộc năng lực đội", "Lập kế hoạch",
     "Lập kế hoạch GEO 3 tháng từ 01/2027 cho line NKT — Nha khoa thẩm mỹ.\n"
     "Đội content chỉ sản xuất được tối đa 20 bài/tháng — hãy cắt phạm vi cho khớp\n"
     "và nói rõ cụm nào bị đẩy sang backlog, vì sao.",
     "Agent cảnh báo nếu chỉ tiêu vượt năng lực, không im lặng nhận"),
    ("plan", "Dồn lực vào một rào cản", "Lập kế hoạch",
     "Quý tới Paris muốn chiếm lĩnh toàn bộ chủ đề rào cản NGỜ về vật liệu trên AI Search\n"
     "— trụ Implant, phôi sứ, khay Invisalign có chính hãng không.\n"
     "Lập kế hoạch 3 tháng chỉ tập trung cụm C03 và C14 của cả 10 bộ.",
     "Cắt ngang 10 bộ theo mã cụm"),
    ("plan", "Chiếm khoảng trống đối thủ", "Lập kế hoạch",
     "Lập kế hoạch 4 tháng từ 02/2027 cho hai bộ Nha khoa tổng quát và Nha chu\n"
     "— hai bộ đối thủ bỏ trống nhiều nhất. Giải thích vì sao đáng làm dù doanh thu thấp.",
     "Agent phải giải thích theo điểm ưu tiên, không theo doanh thu"),
    ("plan", "Trang local 7 cơ sở", "Lập kế hoạch",
     "Lập kế hoạch 4 tháng chỉ cho 7 trang cơ sở (Hà Nội, Hải Phòng, Quảng Ninh, Vinh,\n"
     "Đà Nẵng, TP.HCM, Bình Dương) từ 01/2027. Nêu rõ dữ liệu nào phải lấy từ /tim-phong-kham.html\n"
     "và rào pháp lý nào áp cho từng trang.",
     "Mỗi trang gắn giấy phép của chính cơ sở đó (R3)"),

    ("ask", "Brief sản xuất một cụm", "Hỏi đáp",
     "Cho tôi brief sản xuất cụm C06 Mài răng & chết tuỷ của bộ Bọc răng sứ:\n"
     "cần bao nhiêu bài, dạng gì, trang đích nào, gỡ rào cản nào, rào pháp lý nào.",
     "9 bài · Tầng A · S3 · gỡ rào SỢ · R1 + R9"),
    ("ask", "Hiểu thứ tự ưu tiên", "Hỏi đáp",
     "Vì sao cụm C03 Vật liệu nằm Tầng A ở bộ Implant trong khi ở bộ Nha chu chỉ ở Tầng B?",
     "Trả lời theo rào cản NGỜ, không theo doanh thu"),
    ("ask", "Nỗi sợ theo giai đoạn", "Hỏi đáp",
     "Khách ở giai đoạn S3 của dịch vụ Invisalign đang sợ điều gì?\n"
     "Paris phải có nội dung gì để trả lời?",
     "S3 là điểm quyết định, ~50% điểm ưu tiên"),
    ("ask", "Giao thức đo GEO", "Hỏi đáp",
     "Ba bộ prompt đo GEO của Paris gồm những gì? Chạy thế nào cho đúng giao thức?",
     "20 dịch vụ · 7 hub · 10 thương hiệu; ẩn danh, 3 lần lấy đa số"),
    ("ask", "Dữ liệu còn thiếu", "Hỏi đáp",
     "Những dữ liệu nào Nha khoa Paris chưa cung cấp, và nó đang chặn trụ cột KPI nào?",
     "Agent phải liệt kê đủ, không giấu khoảng trống"),

    ("fix", "Đổi thứ tự một cụm", "Tinh chỉnh",
     "Giữ nguyên bản kế hoạch, chỉ đổi: dồn toàn bộ cụm C14 Thực thể vào tháng 1\n"
     "vì cần schema bác sĩ và trang thực thể chạy trước mọi cụm khác.",
     "Agent chỉ nêu phần thay đổi, không in lại cả bảng"),
    ("fix", "Giãn tiến độ", "Tinh chỉnh",
     "Sản lượng tháng 1 đang 69 bài, quá tải. Giãn thành 8 tháng, giữ nguyên thứ tự ưu tiên.",
     "Vẫn phải giữ ràng buộc chênh lệch tháng ≤25%"),
    ("fix", "Thêm cột vào output", "Tinh chỉnh",
     "Bổ sung cột \"Trang đích\" vào TAB Công việc triển khai, lấy từ bản đồ nội dung.\n"
     "Đánh dấu rõ trang nào là MỚI và trang nào cần đối chiếu sitemap.",
     "Trang đích hiện đều là MỚI hoặc ⚠ đối chiếu"),
]

CATS = [("all", "Tất cả"), ("test", "Kiểm tra"), ("plan", "Lập kế hoạch"),
        ("ask", "Hỏi đáp"), ("fix", "Tinh chỉnh")]


def e(s):
    return html.escape(s, quote=False)


def nchar(s):
    return f"{len(s):,}".replace(",", ".")


def read(p):
    with open(os.path.join(ROOT, p), encoding="utf-8") as fh:
        return fh.read()


def brain():
    """Lấy đúng khối giữa hai vạch ▼▲ của SYSTEM-PROMPT.md — phần dán vào Instructions."""
    src = read("SYSTEM-PROMPT.md")
    m = re.search(r"▼▼▼.*?\n```\n(.*?)\n```\s*\n*▲▲▲", src, re.S)
    if not m:
        sys.exit("✖ Không tách được khối ▼▲ trong SYSTEM-PROMPT.md")
    return m.group(1).strip()


# ─────────────────────────────── CSS ─────────────────────────────────────
CSS = """
/* Bảng màu bộ nhận diện Nha khoa Paris — Design System v3.1.
   Ba màu gốc không đổi: Cerulean Blue #2A52BE · Pantone Red 032 C #ED2E38 · White.
   Tỷ lệ bắt buộc 80% trắng/kem · 15% xanh · 5% đỏ → đỏ chỉ dùng cho cảnh báo và nhấn chốt. */
:root{
  --ground:#DCE3EE; --surface:#FFFFFF; --surface-2:#FBF8F3;
  --ink:#131A2E; --ink-2:#4A5270; --ink-3:#737B96;
  --line:#E4E1D8; --line-2:#EDEAE3;
  --blue:#2A52BE; --blue-dark:#152F73; --blue-deep:#0C1D4D;
  --blue-light:#EAF0FC; --blue-mid:#D7E2FA; --on-blue:#FFFFFF;
  --red:#ED2E38; --red-dark:#C11B26; --red-wash:#FDEAEB; --on-red:#FFFFFF;
  --band:#0C1D4D; --band-ink:#EAF0FC; --band-accent:#ED2E38;
  --ok:#1E6B4F; --ok-bg:#E6F2EC;
  --code-bg:#F4F6FB;
  --f:'Be Vietnam Pro',system-ui,-apple-system,'Segoe UI',Roboto,Arial,sans-serif;
  --f2:'Bricolage Grotesque','Be Vietnam Pro',system-ui,sans-serif;
  --mono:ui-monospace,'Cascadia Mono','Cascadia Code',Consolas,Menlo,monospace;
  --r:8px; --r-lg:12px;
  --sh:0 1px 2px rgba(12,29,77,.07),0 2px 6px rgba(12,29,77,.05);
}
@media (prefers-color-scheme:dark){
  :root:not([data-theme="light"]){
    --ground:#080B14; --surface:#0D1220; --surface-2:#141A2B;
    --ink:#E8ECF6; --ink-2:#A4ADC6; --ink-3:#808AA6;
    --line:#262E45; --line-2:#1E2537;
    --blue:#8CA8F5; --blue-dark:#A9BEF8; --blue-deep:#C3D2FB;
    --blue-light:#16244A; --blue-mid:#25365F; --on-blue:#0B1020;
    --red:#FF7A80; --red-dark:#FF9BA0; --red-wash:#3A1A1D; --on-red:#20080A;
    --band:#101A38; --band-ink:#EDF1FB; --band-accent:#FF7A80;
    --ok:#7FC9A4; --ok-bg:#12271F;
    --code-bg:#141A2B;
    --sh:0 1px 2px rgba(0,0,0,.45),0 3px 10px rgba(0,0,0,.3);
  }
}
:root[data-theme="dark"]{
  --ground:#080B14; --surface:#0D1220; --surface-2:#141A2B;
  --ink:#E8ECF6; --ink-2:#A4ADC6; --ink-3:#808AA6;
  --line:#262E45; --line-2:#1E2537;
  --blue:#8CA8F5; --blue-dark:#A9BEF8; --blue-deep:#C3D2FB;
  --blue-light:#16244A; --blue-mid:#25365F; --on-blue:#0B1020;
  --red:#FF7A80; --red-dark:#FF9BA0; --red-wash:#3A1A1D; --on-red:#20080A;
  --band:#101A38; --band-ink:#EDF1FB; --band-accent:#FF7A80;
  --ok:#7FC9A4; --ok-bg:#12271F;
  --code-bg:#141A2B;
  --sh:0 1px 2px rgba(0,0,0,.45),0 3px 10px rgba(0,0,0,.3);
}

*{box-sizing:border-box}
body{margin:0;background:var(--ground);color:var(--ink);
  font:400 15.5px/1.62 var(--f);-webkit-font-smoothing:antialiased}
.wrap{max-width:940px;margin:0 auto;padding-inline:20px}
h1,h2,h3{line-height:1.2;text-wrap:balance;margin:0;font-family:var(--f2)}
p{margin:0 0 .8em}
a{color:var(--blue);text-decoration-thickness:1px;text-underline-offset:2px}
code{font-family:var(--mono);font-size:.88em;background:var(--surface-2);
  border:1px solid var(--line-2);border-radius:5px;padding:.08em .35em;overflow-wrap:anywhere}
:focus-visible{outline:2.5px solid var(--blue);outline-offset:2px;border-radius:6px}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}

/* header band */
header.top{background:var(--band);color:var(--band-ink);border-bottom:4px solid var(--band-accent)}
.eyebrow{font:800 11.5px/1.3 var(--f);letter-spacing:.16em;text-transform:uppercase;
  color:var(--band-accent);margin:0 0 10px}
.top h1{font-size:clamp(28px,5.4vw,42px);font-weight:800;letter-spacing:-.02em;color:#fff}
.lede{margin:13px 0 0;font-size:17px;color:rgba(255,255,255,.86);max-width:62ch}
.lede b{color:#fff}
header.top .dim{color:rgba(255,255,255,.62)}
.chips{display:flex;flex-wrap:wrap;gap:7px;margin-top:18px}
.chip{font-size:12.5px;font-weight:600;color:rgba(255,255,255,.82);
  background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.22);
  border-radius:999px;padding:5px 12px;font-variant-numeric:tabular-nums}
.chip.on{color:var(--on-red);background:var(--band-accent);border-color:var(--band-accent);font-weight:800}
.ghrow{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin-top:18px}
a.ghbtn{display:inline-flex;align-items:center;gap:8px;font:700 13.5px var(--f);
  text-decoration:none;color:var(--band);background:#fff;padding:9px 15px;border-radius:var(--r)}
a.ghbtn:hover{background:var(--band-accent);color:var(--on-red)}
.ghrow code{font-size:12px;color:rgba(255,255,255,.8);background:rgba(255,255,255,.08);
  border-color:rgba(255,255,255,.2);padding:8px 11px;border-radius:var(--r)}
/* <code> trên nền band tối: nền sáng mặc định + chữ trắng kế thừa = chữ vô hình */
header.top code,.note.stop code{background:rgba(255,255,255,.10);
  border-color:rgba(255,255,255,.22);color:var(--band-ink)}

/* nav */
nav.bar{position:sticky;top:env(safe-area-inset-top,0px);z-index:40;
  background:var(--band);border-bottom:1px solid rgba(255,255,255,.16)}
nav.bar .wrap{display:flex;gap:2px;overflow-x:auto;padding-block:9px;scrollbar-width:none}
nav.bar .wrap::-webkit-scrollbar{display:none}
nav.bar a{flex:0 0 auto;font-size:13px;font-weight:600;color:rgba(255,255,255,.74);
  text-decoration:none;padding:6px 11px;border-radius:7px;white-space:nowrap}
nav.bar a:hover{background:rgba(255,255,255,.14);color:#fff}

/* section */
section{padding-block:46px;border-top:1px solid var(--line);scroll-margin-top:62px}
section:first-of-type{border-top:0}
.sec-h{margin-bottom:22px}
.sec-h .pre{font:800 11.5px/1.3 var(--f);letter-spacing:.14em;text-transform:uppercase;
  color:var(--blue);display:block}
.sec-h h2{font-size:clamp(21px,3.4vw,28px);font-weight:800;color:var(--blue-deep);margin-top:5px}
.sec-h .bar{display:block;width:42px;height:3px;border-radius:3px;background:var(--red);margin-top:11px}
.sec-h p{margin:12px 0 0;color:var(--ink-2);max-width:68ch}
h3.sub{font-size:16px;font-weight:800;color:var(--blue-deep);margin:30px 0 12px}

/* grid + card */
.grid{display:grid;gap:14px}
.g3{grid-template-columns:repeat(3,1fr)}
.g2{grid-template-columns:repeat(2,1fr)}
@media(max-width:760px){.g3,.g2{grid-template-columns:1fr}}
.card{background:var(--surface);border:1px solid var(--line);border-radius:var(--r-lg);
  padding:18px;box-shadow:var(--sh)}
.card h3{font-size:16px;font-weight:800;color:var(--blue-deep);margin-bottom:6px}
.card p:last-child{margin-bottom:0}
.dim{color:var(--ink-3);font-size:13px}

/* 3 bước */
.steps3{display:grid;gap:1px;background:var(--line);border:1px solid var(--line);
  border-radius:var(--r-lg);overflow:hidden;margin:0 0 18px;grid-template-columns:repeat(3,1fr)}
@media(max-width:700px){.steps3{grid-template-columns:1fr}}
.steps3 div{background:var(--surface);padding:15px 16px}
.steps3 b{display:block;font-size:13px;font-weight:800;color:var(--blue-deep);margin-bottom:3px}
.steps3 span{font-size:13.5px;color:var(--ink-2)}
.steps3 .n{display:inline-grid;place-content:center;width:21px;height:21px;border-radius:50%;
  background:var(--blue);color:var(--on-blue);font:800 11.5px var(--f);margin-right:7px;vertical-align:1px}

/* tải ZIP */
.dl{background:var(--surface);border:1px solid var(--line);border-top:4px solid var(--red);
  border-radius:var(--r-lg);padding:22px 20px;text-align:center;box-shadow:var(--sh);margin:0 0 16px}
.dl h3{font-size:17px;font-weight:800;color:var(--blue-deep);margin:0 0 4px}
.dl p{margin:0;font-size:14px;color:var(--ink-2)}
a.dl-btn{display:inline-flex;align-items:center;gap:9px;margin:14px 0 0;background:var(--blue);
  color:var(--on-blue);font:800 16.5px var(--f);text-decoration:none;padding:14px 26px;
  border-radius:var(--r);box-shadow:0 2px 0 var(--blue-deep)}
a.dl-btn:hover{background:var(--blue-dark)}

/* tabs */
.tabs{display:flex;gap:6px;flex-wrap:wrap;margin:0 0 -1px;position:relative;z-index:1}
.tab{border:1px solid var(--line);border-bottom-color:transparent;background:var(--surface-2);
  color:var(--ink-3);font:700 13.5px var(--f);padding:9px 16px;
  border-radius:var(--r) var(--r) 0 0;cursor:pointer}
.tab:hover{color:var(--blue-deep)}
.tab[aria-selected="true"]{background:var(--surface);color:var(--blue-deep);
  border-top:3px solid var(--blue);border-bottom-color:var(--surface);padding-top:7px}
.tabs + .card{border-radius:0 var(--r-lg) var(--r-lg) var(--r-lg)}
ol.steps{margin:0;padding-left:1.25em}
ol.steps li{margin-bottom:9px}
ol.steps li::marker{font-weight:800;color:var(--blue)}

/* thẻ copy bộ não */
.cc{display:flex;flex-direction:column;gap:11px;background:var(--surface);
  border:1px solid var(--line);border-top:4px solid var(--blue);
  border-radius:var(--r-lg);padding:17px;box-shadow:var(--sh)}
.cc .tag{font-size:11.5px;font-weight:800;letter-spacing:.09em;text-transform:uppercase;color:var(--ink-3)}
.cc h3{font-size:17px;font-weight:800;color:var(--blue-deep);margin:0}
.cc .meta{font-size:13px;color:var(--ink-2);margin:0;flex:1}
.cc .count{font-variant-numeric:tabular-nums;font-weight:700;color:var(--ink)}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:7px;width:100%;
  min-height:44px;border:0;border-radius:var(--r);background:var(--blue);color:var(--on-blue);
  font:800 14.5px var(--f);cursor:pointer;box-shadow:0 2px 0 var(--blue-deep);
  transition:background-color .15s,transform .1s}
.btn:hover{background:var(--blue-dark)}
.btn:active{transform:translateY(1px);box-shadow:0 1px 0 var(--blue-deep)}
.btn.done{background:var(--ok);box-shadow:0 2px 0 rgba(0,0,0,.14);color:#fff}
details.peek{border-top:1px solid var(--line-2);padding-top:10px}
details.peek summary{cursor:pointer;font-size:13px;font-weight:600;color:var(--blue);list-style:none}
details.peek summary::-webkit-details-marker{display:none}
details.peek summary::before{content:"▸ ";color:var(--ink-3)}
details.peek[open] summary::before{content:"▾ "}
details.peek pre{margin:10px 0 0;max-height:300px;overflow:auto;background:var(--code-bg);
  border:1px solid var(--line-2);border-radius:var(--r);padding:12px;
  font:400 12px/1.55 var(--mono);white-space:pre-wrap;overflow-wrap:anywhere;color:var(--ink-2)}

/* file card */
.fcard{border:1px solid var(--line);border-radius:var(--r);overflow:hidden;background:var(--surface);
  margin:0 0 9px;box-shadow:var(--sh)}
.fcard.hi{border:2px solid var(--blue)}
.fcard-h{display:flex;gap:10px;align-items:center;padding:11px 13px;flex-wrap:wrap}
.fname{font:700 13.4px var(--mono);color:var(--ink);overflow-wrap:anywhere}
.fbadge{font-size:10.5px;font-weight:800;letter-spacing:.05em;text-transform:uppercase;
  padding:3px 8px;border-radius:999px;background:var(--red-wash);color:var(--red-dark);
  border:1px solid var(--red)}
.fsize{font-size:12.5px;color:var(--ink-3);font-variant-numeric:tabular-nums;margin-left:auto}
@media(max-width:520px){.fsize{margin-left:0}}
.fhow{margin:0;padding:0 13px 11px;font-size:13.8px;color:var(--ink-2)}
.fhow b{color:var(--ink)}
details.fview{border-top:1px solid var(--line-2)}
details.fview summary{cursor:pointer;padding:9px 13px;font-size:13px;font-weight:600;
  color:var(--blue);list-style:none}
details.fview summary::-webkit-details-marker{display:none}
details.fview summary::before{content:"▸ ";color:var(--ink-3)}
details.fview[open] summary::before{content:"▾ "}
.filebody{margin:0;padding:13px;background:var(--code-bg);border-top:1px solid var(--line-2);
  font:400 12px/1.7 var(--mono);color:var(--ink-2);white-space:pre-wrap;overflow-wrap:anywhere;
  max-height:340px;overflow:auto}

/* prompt */
.qa-bar{display:flex;gap:7px;flex-wrap:wrap;align-items:center;margin:0 0 16px}
.qa-bar button{font:600 13px var(--f);padding:6px 13px;border:1px solid var(--line);
  background:var(--surface);color:var(--ink-3);border-radius:999px;cursor:pointer;white-space:nowrap}
.qa-bar button:hover{color:var(--blue-deep);border-color:var(--blue)}
.qa-bar button[aria-pressed="true"]{background:var(--blue);color:var(--on-blue);border-color:var(--blue)}
.prompt{background:var(--surface);border:1px solid var(--line);border-radius:var(--r-lg);
  margin:0 0 12px;overflow:hidden;box-shadow:var(--sh)}
.prompt-h{display:flex;gap:11px;align-items:center;padding:12px 15px;flex-wrap:wrap;
  background:var(--surface-2);border-bottom:1px solid var(--line-2)}
.prompt-h .n{flex:none;font:700 12.5px var(--mono);color:var(--blue);font-variant-numeric:tabular-nums}
.prompt-h .t{font-size:14.8px;font-weight:700;flex:1;min-width:0;color:var(--ink)}
.prompt-h .k{flex:none;font-size:10.5px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;
  color:var(--ink-3);border:1px solid var(--line);border-radius:999px;padding:3px 9px;white-space:nowrap}
@media (max-width:420px){.prompt-h .k{display:none}}
.prompt-b{margin:0;padding:14px 15px;max-height:240px;overflow:auto;
  font:400 12.6px/1.66 var(--mono);color:var(--ink-2);white-space:pre-wrap;
  overflow-wrap:anywhere;background:var(--surface)}
.prompt-f{display:flex;gap:10px;align-items:center;justify-content:space-between;
  padding:11px 15px;flex-wrap:wrap;border-top:1px solid var(--line-2);background:var(--surface-2)}
.prompt-f .get{font-size:12.8px;color:var(--ink-3);flex:1;min-width:150px}
.copy{font:700 13px var(--f);padding:7px 14px;border-radius:7px;cursor:pointer;
  border:1px solid var(--blue);background:transparent;color:var(--blue);white-space:nowrap}
.copy:hover{background:var(--blue-light)}
.copy.done{border-color:var(--ok);color:var(--ok);background:var(--ok-bg)}

/* bảng */
.tw{overflow-x:auto;border:1px solid var(--line);border-radius:var(--r-lg);background:var(--surface)}
table{border-collapse:collapse;width:100%;min-width:520px;font-size:14px}
th,td{text-align:left;padding:11px 13px;border-bottom:1px solid var(--line-2);vertical-align:top}
thead th{font-size:11.5px;font-weight:800;letter-spacing:.07em;text-transform:uppercase;
  color:var(--on-blue);background:var(--blue);border-bottom:0;white-space:nowrap}
tbody tr:last-child td{border-bottom:0}
tbody tr:nth-child(even) td{background:var(--surface-2)}
code.r{font-family:var(--mono);font-size:12px;font-weight:700;background:var(--red-wash);
  color:var(--red-dark);border:1px solid var(--red);padding:1px 5px;border-radius:4px;white-space:nowrap}

/* callout */
.note{border-radius:0 var(--r) var(--r) 0;padding:13px 16px;font-size:14.5px;
  background:var(--surface);border:1px solid var(--line);border-left:4px solid var(--blue);
  box-shadow:var(--sh);color:var(--ink-2)}
.note b{font-weight:800;color:var(--ink)}
.note.warn{border-left-color:var(--red);background:var(--red-wash)}
.note.ok{border-left-color:var(--ok);background:var(--ok-bg)}
.note.stop{background:var(--band);color:var(--band-ink);border:1px solid var(--band-accent);
  border-left:5px solid var(--band-accent);border-radius:var(--r);font-family:var(--f2);
  font-weight:700;font-size:clamp(16px,2.3vw,19px);line-height:1.42}
.note.stop b{color:#fff}
.note + .note{margin-top:10px}
.note p:last-child{margin-bottom:0}

/* rào cản + trục */
.barrier{background:var(--surface);border:1px solid var(--line);border-left:3px solid var(--blue-mid);
  border-radius:var(--r-lg);padding:16px 17px;display:flex;flex-direction:column;gap:9px;box-shadow:var(--sh)}
.barrier.heavy{border-left-color:var(--red)}
.barrier-top{display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.barrier-name{font-family:var(--f2);font-weight:800;font-size:19px;letter-spacing:.02em}
.tagp{font-size:10.5px;font-weight:700;letter-spacing:.07em;text-transform:uppercase;
  padding:3px 8px;border-radius:999px;background:var(--blue-light);color:var(--blue-dark)}
.tagp.alert{background:var(--red-wash);color:var(--red-dark)}
.barrier p{font-size:14.5px;margin:0}
.barrier .fix{font-size:13.5px;color:var(--ink-2)}
.barrier .fix b{color:var(--ink);font-weight:700}
.axis{display:flex;flex-wrap:wrap;gap:7px}
.axis-step{flex:1 1 130px;background:var(--surface-2);border:1px solid var(--line);
  border-radius:var(--r);padding:11px 12px;display:flex;flex-direction:column;gap:4px}
.axis-step .n{font:700 11px var(--mono);color:var(--blue)}
.axis-step .t{font-size:13.5px;font-weight:700;line-height:1.3}
.axis-step .s{font-size:12px;color:var(--ink-3);line-height:1.4}
.axis-step.peak{background:var(--red-wash);border-color:var(--red)}
.axis-step.peak .n{color:var(--red-dark)}

/* dấu hiệu đúng/sai */
.signbox{border:1px solid var(--line);border-radius:var(--r-lg);background:var(--surface);
  overflow:hidden;box-shadow:var(--sh)}
.signbox > .cap{padding:9px 15px;font-size:13px;font-weight:800;letter-spacing:.03em;
  background:var(--blue);color:var(--on-blue)}
.signbox.bad > .cap{background:var(--red);color:var(--on-red)}
.signbox ul{margin:0;padding:13px 15px 13px 30px;display:flex;flex-direction:column;gap:8px}
.signbox li{font-size:14px}

pre.cli{margin:0;padding:15px;background:var(--band);color:var(--band-ink);
  border-radius:var(--r-lg);font:400 12.5px/1.7 var(--mono);overflow-x:auto}
pre.cli .c{color:var(--band-accent)}

footer{border-top:1px solid var(--line);background:var(--surface);
  padding-block:30px;font-size:13px;color:var(--ink-3)}
footer b{color:var(--ink-2)}
footer a{overflow-wrap:anywhere}
.toast{position:fixed;left:50%;transform:translateX(-50%);
  bottom:calc(20px + env(safe-area-inset-bottom,0px));
  background:var(--band);color:var(--band-ink);font:700 13.5px var(--f);padding:10px 18px;
  border-radius:999px;z-index:90;box-shadow:0 8px 24px rgba(0,0,0,.3)}
"""

JS = """
function flash(btn, cls, txt){
  var old = btn.textContent;
  btn.classList.add(cls); btn.textContent = txt;
  setTimeout(function(){ btn.classList.remove(cls); btn.textContent = old; }, 1800);
}
function toast(msg){
  var t = document.createElement('div');
  t.className = 'toast'; t.textContent = msg; document.body.appendChild(t);
  setTimeout(function(){ t.remove(); }, 1900);
}
function put(text, btn){
  var ok = function(){ flash(btn,'done','✓ Đã copy'); toast('Đã copy ' + text.length.toLocaleString('vi-VN') + ' ký tự'); };
  var no = function(){ toast('Trình duyệt chặn copy — bấm “Xem nội dung” rồi bôi đen để copy tay'); };
  try{
    if (navigator.clipboard && navigator.clipboard.writeText){
      navigator.clipboard.writeText(text).then(ok, function(){ legacy(text, ok, no); });
    } else { legacy(text, ok, no); }
  } catch(err){ legacy(text, ok, no); }
}
function legacy(text, ok, no){
  try{
    var ta = document.createElement('textarea');
    ta.value = text; ta.setAttribute('readonly','');
    ta.style.position='fixed'; ta.style.opacity='0';
    document.body.appendChild(ta); ta.select();
    var done = document.execCommand('copy');
    document.body.removeChild(ta);
    done ? ok() : no();
  } catch(err){ no(); }
}
function payload(key){
  if (key === 'merged'){
    var out = [];
    document.querySelectorAll('pre[data-file]').forEach(function(p){
      out.push('<!-- ===== ' + p.dataset.file + ' ===== -->\\n\\n' + p.textContent.trim());
    });
    return out.join('\\n\\n\\n');
  }
  var el = document.getElementById('src-' + key);
  return el ? el.textContent.trim() : '';
}
document.querySelectorAll('[data-copy]').forEach(function(btn){
  btn.addEventListener('click', function(){
    var text = payload(btn.dataset.copy);
    if (!text){ toast('Không tìm thấy nội dung'); return; }
    put(text, btn);
  });
});
document.querySelectorAll('.tab').forEach(function(tab){
  tab.addEventListener('click', function(){
    var group = tab.closest('.tabs');
    group.querySelectorAll('.tab').forEach(function(t){
      var on = (t === tab);
      t.setAttribute('aria-selected', on ? 'true' : 'false');
      document.getElementById(t.dataset.panel).hidden = !on;
    });
  });
});
document.querySelectorAll('.qa-bar button').forEach(function(b){
  b.addEventListener('click', function(){
    var cat = b.dataset.cat;
    document.querySelectorAll('.qa-bar button').forEach(function(x){
      x.setAttribute('aria-pressed', x === b ? 'true' : 'false');
    });
    document.querySelectorAll('.prompt[data-cat]').forEach(function(p){
      p.hidden = !(cat === 'all' || p.dataset.cat === cat);
    });
  });
});
"""


def build():
    brain_txt = brain()
    files = []
    for name, core, short, how in KNOWLEDGE:
        body = read(os.path.join("knowledge", name))
        files.append(dict(name=name, core=core, short=short, how=how, body=body))
    merged_len = sum(len(f["body"]) for f in files) + len(files) * 40

    L = []
    A = L.append
    A("<title>Agent-PR-GEO-Plant</title>")
    A('<link rel="preconnect" href="https://fonts.googleapis.com">')
    A('<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>')
    A('<link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;600;700;800'
      '&family=Bricolage+Grotesque:opsz,wght@12..96,700;12..96,800&display=swap" rel="stylesheet">')
    A("<style>" + CSS + "</style>")

    # ── header ───────────────────────────────────────────────────────────
    A('<header class="top"><div class="wrap" style="padding-block:40px 34px">')
    A('<p class="eyebrow">Hướng dẫn cài đặt &amp; vận hành</p>')
    A("<h1>Agent-PR-GEO-Plant</h1>")
    A('<p class="lede">Agent lập <b>kế hoạch GEO theo tháng</b> cho <code>nhakhoaparis.vn</code> — '
      "đọc bộ truy vấn, xếp ưu tiên theo nỗi sợ của khách, rải theo tháng, "
      "rồi xuất <b>file Excel 2 TAB</b> giao được việc ngay. Cài xong trong <b>~10 phút</b>.</p>")
    A('<div class="chips">')
    for on, t in [(True, "v1.0"), (False, "10 bộ dịch vụ"), (False, "150 cụm"),
                  (False, "389 bài"), (False, "2.550 truy vấn"), (False, "14 rào pháp lý"),
                  (False, "Claude · ChatGPT · Gemini")]:
        A(f'<span class="chip{" on" if on else ""}">{e(t)}</span>')
    A("</div>")
    A('<p class="dim" style="margin-top:16px">Đo bằng <b>5 trụ cột KPI</b>: hạ tầng · sản lượng · '
      "<b>SEO &amp; GEO AI Search (0,40)</b> · traffic · lead. "
      "Không đo lượt xem hay độ “đẹp” của bài.</p>")
    A('<div class="ghrow">')
    A(f'<a class="ghbtn" href="{GH}" target="_blank" rel="noopener">↗ huudinh/Agent-PR-GEO-Plant</a>')
    A(f"<code>git clone {GH}.git</code>")
    A("</div></div></header>")

    # ── nav ──────────────────────────────────────────────────────────────
    A('<nav class="bar"><div class="wrap">')
    for href, t in [("#cai-dat", "1 · Cài đặt"), ("#prompt", "2 · Prompt mẫu"),
                    ("#tu-duy", "3 · Cách Agent nghĩ"), ("#output", "4 · Đọc output"),
                    ("#cong-cu", "5 · Công cụ")]:
        A(f'<a href="{href}">{e(t)}</a>')
    A("</div></nav>")

    A('<main class="wrap">')

    # ── §1 CÀI ĐẶT ───────────────────────────────────────────────────────
    A('<section id="cai-dat"><div class="sec-h"><span class="pre">Mục 1</span>'
      "<h2>Cài đặt theo nền tảng</h2><span class=\"bar\"></span>"
      "<p>Agent là <b>prompt + tri thức</b>, không phải phần mềm. Không cài gì lên máy.</p></div>")

    A('<div class="steps3">')
    A('<div><b><span class="n">1</span>Lấy bộ file</b><span>Tải ZIP rồi giải nén. '
      "Không tải được thì copy từng file ngay trên trang này.</span></div>")
    A('<div><b><span class="n">2</span>Tạo project + dán 3 thẻ</b>'
      "<span>Tên · Mô tả (Thẻ A) · Instructions (Thẻ B).</span></div>")
    A('<div><b><span class="n">3</span>Upload 6 file tri thức</b>'
      "<span>Thiếu file nào thì Agent đoán chỗ đó — và không báo lỗi.</span></div>")
    A("</div>")

    A('<div class="dl"><h3>Tải bộ file</h3>'
      "<p>Toàn bộ repo: bộ não · 6 file tri thức · 10 bộ truy vấn JSON · file Excel mẫu · 2 script.</p>"
      f'<a class="dl-btn" href="{GH}/archive/refs/heads/main.zip">⬇ Tải ZIP</a>'
      '<p style="margin-top:12px;font-size:13px;color:var(--ink-3)">Giải nén bằng <b>Extract All</b> — '
      "đừng kéo file trực tiếp từ cửa sổ ZIP. Thư mục cần dùng nằm ở "
      "<code>Agent-PR-GEO-Plant-main/knowledge/</code>.<br>Xem repo: "
      f'<a href="{GH}" target="_blank" rel="noopener">github.com/huudinh/Agent-PR-GEO-Plant</a></p></div>')

    A('<div class="tabs" role="tablist">')
    A('<button class="tab" role="tab" aria-selected="true" data-panel="p-claude">Claude Project</button>')
    A('<button class="tab" role="tab" aria-selected="false" data-panel="p-gpt">ChatGPT Custom GPT</button>')
    A('<button class="tab" role="tab" aria-selected="false" data-panel="p-gemini">Gemini Gems</button>')
    A("</div>")

    A('<div class="card" id="p-claude" role="tabpanel"><h3>Claude Project — khuyến nghị</h3>'
      '<p class="dim" style="margin-bottom:12px">Sinh thẳng được file <code>.xlsx</code> 2 TAB, '
      "và ô instructions không giới hạn ký tự.</p><ol class=\"steps\">"
      "<li><b>Projects</b> → <b>Create project</b> → đặt tên <code>Agent-PR-GEO-Plant</code>.</li>"
      "<li><b>Description</b> (ô <i>What are you working on?</i>) → dán <b>Thẻ A · Mô tả ngắn</b>.</li>"
      "<li><b>Set project instructions</b> → dán <b>Thẻ B · Bộ não</b>.</li>"
      "<li><b>Add content</b> → upload <b>đủ 6 file</b> trong <code>knowledge/</code>.</li>"
      "<li>Upload thêm <code>template/GEO-PLAN-MAU-6-THANG.xlsx</code> để Agent bám đúng format 2 TAB.</li>"
      "<li>Mở chat mới → chạy câu smoke test ở Mục 2.</li></ol></div>")

    A('<div class="card" id="p-gpt" role="tabpanel" hidden><h3>ChatGPT Custom GPT</h3>'
      '<p class="dim" style="margin-bottom:12px">Phải bật Data Analysis, nếu không sẽ không có file Excel.</p>'
      "<ol class=\"steps\">"
      "<li><b>Explore GPTs</b> → <b>Create</b> → tab <b>Configure</b>.</li>"
      "<li>Name: <code>Agent-PR-GEO-Plant</code>.</li>"
      "<li><b>Description</b> → dán <b>Thẻ A · Mô tả ngắn</b> (187 ký tự, vừa giới hạn 300).</li>"
      "<li>Instructions → dán <b>Thẻ B · Bộ não</b>.</li>"
      "<li>Knowledge → upload <b>đủ 6 file</b> + file Excel mẫu.</li>"
      "<li><b>Capabilities</b> → bật <b>Code Interpreter &amp; Data Analysis</b>.</li></ol>"
      '<div class="note warn" style="margin-top:14px"><b>Không bật Data Analysis</b> thì Agent vẫn '
      "trình được bảng kế hoạch trong chat nhưng <b>không sinh được file <code>.xlsx</code></b> — "
      "bạn sẽ phải tự dựng lại format 2 TAB bằng tay.</div></div>")

    A('<div class="card" id="p-gemini" role="tabpanel" hidden><h3>Gemini Gems</h3><ol class="steps">'
      "<li><b>Gems</b> → <b>New Gem</b> → đặt tên.</li>"
      "<li>Ô <b>Chỉ dẫn</b> → dán <b>Thẻ A · Mô tả ngắn</b> làm dòng đầu, xuống dòng rồi dán "
      "<b>Thẻ B · Bộ não</b>. <i>Gemini Gems không có ô Mô tả riêng.</i></li>"
      "<li>Upload <b>đủ 6 file</b> tri thức vào phần tệp của Gem.</li></ol>"
      '<div class="note warn" style="margin-top:14px"><b>Gemini không sinh được <code>.xlsx</code>.</b> '
      "Agent sẽ xuất <b>bảng phẳng</b> đúng số cột, mỗi ô một giá trị, không gộp ô — "
      "bạn bấm <i>Export to Sheets</i> rồi tự định dạng màu theo "
      "<code>knowledge/geo-output-excel-schema.md</code>.</div>"
      '<p class="dim" style="margin-top:12px">Dùng Claude Code / VS Code: mở thư mục '
      "<code>Agent-PR-GEO-Plant/</code> rồi nói <i>“Đọc SYSTEM-PROMPT.md và toàn bộ knowledge/, "
      "sau đó hành xử đúng như Agent-PR-GEO-Plant”</i>.</p></div>")

    # thẻ copy
    A('<h3 class="sub">Ba thẻ dán sẵn</h3>')
    A('<p class="dim" style="margin:0 0 13px">Ba ô khác nhau trên nền tảng: <b>Tên</b> → '
      "<code>Agent-PR-GEO-Plant</code> · <b>Mô tả</b> → Thẻ A · <b>Chỉ dẫn/Instructions</b> → Thẻ B. "
      "Ô Mô tả <b>không thay thế</b> Instructions — nó chỉ để người khác biết Agent làm gì "
      "khi nhìn vào danh sách.</p>")
    A('<div class="grid g3">')
    A('<div class="cc"><span class="tag">Thẻ A</span><h3>Mô tả ngắn</h3>'
      f'<p class="meta"><span class="count">{nchar(MOTA)}</span> ký tự · dán vào ô Mô tả / Description<br>'
      '<span class="dim">Vừa giới hạn 300 ký tự của ChatGPT. Gemini Gems không có ô này — '
      "đặt làm dòng đầu của ô Chỉ dẫn.</span></p>"
      '<button class="btn" data-copy="mota">Copy Thẻ A</button>'
      '<details class="peek"><summary>Xem nội dung</summary>'
      f'<pre id="src-mota">{e(MOTA)}</pre>'
      f'<p class="dim" style="margin:9px 0 0">Ô mô tả quá ngắn thì dùng bản rút gọn: '
      f"<code>{e(MOTA_NGAN)}</code></p></details></div>")
    A('<div class="cc"><span class="tag">Thẻ B</span><h3>Bộ não</h3>'
      f'<p class="meta"><span class="count">{nchar(brain_txt)}</span> ký tự · dán vào Instructions<br>'
      '<span class="dim">§1–§17: trục 6 bước · ba rào cản · 80/20 · R0–R13 · schema 2 TAB · '
      "self-review 14 điểm</span></p>"
      '<button class="btn" data-copy="brain">Copy Thẻ B</button>'
      '<details class="peek"><summary>Xem nội dung</summary>'
      f'<pre id="src-brain">{e(brain_txt)}</pre></details></div>')
    A('<div class="cc"><span class="tag">Thẻ C</span><h3>Tri thức gộp</h3>'
      f'<p class="meta"><span class="count">{nchar("x" * merged_len)}</span> ký tự · 6 file nối liền<br>'
      '<span class="dim">Dùng khi nền tảng không cho upload nhiều file. '
      "Upload được 6 file riêng thì ưu tiên cách đó.</span></p>"
      '<button class="btn" data-copy="merged">Copy Thẻ C</button>'
      '<details class="peek"><summary>Gồm những gì</summary><pre>'
      + e("\n".join(f"{i+1}. {f['name']}  ({nchar(f['body'])} ký tự)" for i, f in enumerate(files)))
      + "</pre></details></div>")
    A("</div>")

    # file cards
    A('<h3 class="sub">Sáu file tri thức cần nạp</h3>')
    A('<p class="dim" style="margin:0 0 13px">Có ZIP rồi thì upload thẳng từ thư mục '
      "<code>knowledge/</code>. <b>Không tải được ZIP</b> thì bấm Copy từng file, dán vào một file "
      "<code>.md</code> trên máy rồi upload. Thứ tự dưới đây là thứ tự Agent đọc: "
      "phương pháp → khối lượng → pháp lý → thương hiệu → KPI → format.</p>")
    for i, f in enumerate(files, 1):
        hi = " hi" if f["core"] else ""
        badge = '<span class="fbadge">★ lõi</span>' if f["core"] else ""
        A(f'<article class="fcard{hi}"><div class="fcard-h">'
          f'<span class="fname">{e(f["name"])}</span>{badge}'
          f'<span class="fsize">{nchar(f["body"])} ký tự</span>'
          f'<button class="copy" data-copy="f{i}">Copy</button></div>'
          f'<p class="fhow"><b>{e(f["short"])}</b> — {e(f["how"])}</p>'
          '<details class="fview"><summary>Xem nội dung</summary>'
          f'<pre class="filebody" id="src-f{i}" data-file="{e(f["name"])}">{e(f["body"])}</pre>'
          "</details></article>")
    A("</section>")

    # ── §2 PROMPT ────────────────────────────────────────────────────────
    A('<section id="prompt"><div class="sec-h"><span class="pre">Mục 2</span>'
      f"<h2>Thư viện {len(PROMPTS)} prompt mẫu</h2><span class=\"bar\"></span>"
      "<p>Bấm <b>Copy</b> rồi dán thẳng vào Agent. Chạy nhóm <b>Kiểm tra</b> trước — "
      "nó cho biết Agent đã nạp đủ tri thức chưa.</p></div>")
    A('<div class="qa-bar">')
    for cid, label in CATS:
        n = len(PROMPTS) if cid == "all" else sum(1 for p in PROMPTS if p[0] == cid)
        sel = "true" if cid == "all" else "false"
        A(f'<button data-cat="{cid}" aria-pressed="{sel}">{e(label)} ({n})</button>')
    A("</div>")
    for i, (cat, title, kind, body, note) in enumerate(PROMPTS, 1):
        A(f'<article class="prompt" data-cat="{cat}"><div class="prompt-h">'
          f'<span class="n">{i:02d}</span><span class="t">{e(title)}</span>'
          f'<span class="k">{e(kind)}</span></div>'
          f'<pre class="prompt-b" id="src-p{i}">{e(body)}</pre>'
          f'<div class="prompt-f"><span class="get">{e(note)}</span>'
          f'<button class="copy" data-copy="p{i}">Copy</button></div></article>')
    A("</section>")

    # ── §3 CÁCH AGENT NGHĨ ───────────────────────────────────────────────
    A('<section id="tu-duy"><div class="sec-h"><span class="pre">Mục 3</span>'
      "<h2>Cách Agent nghĩ</h2><span class=\"bar\"></span>"
      "<p>Biết ba điều này thì đọc được mọi kế hoạch Agent xuất ra, và biết lúc nào nó sai.</p></div>")
    A('<div class="note stop">Nha khoa Paris không đi kể chuyện mình giỏi. '
      "Paris đi theo hành trình của khách, gỡ từng nỗi lo, rồi mới xuất hiện như giải pháp.</div>")
    A('<p class="dim" style="margin-top:14px">Hệ quả vận hành: thứ tự ưu tiên nội dung <b>không</b> '
      "theo doanh thu dịch vụ, mà theo điểm ưu tiên của cụm truy vấn. Vì vậy “Tháo răng sứ làm lại” "
      "và “Mài răng, chết tuỷ” luôn đứng trên “Các loại răng sứ”; và cụm Nha chu — doanh thu thấp "
      "nhất — vẫn được ưu tiên vì đối thủ bỏ trống hoàn toàn.</p>")

    A('<h3 class="sub">Ba rào cản chốt của khách nha khoa</h3>')
    A('<div class="grid g3">')
    A('<div class="barrier"><div class="barrier-top"><span class="barrier-name">SỢ</span>'
      '<span class="tagp">Đau &amp; mất răng thật</span></div>'
      "<p>Đau khi nhổ, khoan, cấy trụ. <b>Mài mất răng thật</b> — men răng không mọc lại. "
      "Niềng thì lâu, đau và xấu suốt thời gian đeo.</p>"
      '<p class="fix">Gỡ bằng: <b>Piezotome</b> · <b>RECIPROC BLUE</b> · bác sĩ theo dõi từng giai đoạn · '
      "Invisalign trong suốt.</p></div>")
    A('<div class="barrier heavy"><div class="barrier-top"><span class="barrier-name">NGỜ</span>'
      '<span class="tagp alert">Rào nặng nhất</span></div>'
      "<p>Trụ Implant, phôi sứ, khay niềng <b>có chính hãng không</b>? Bác sĩ có giỏi? "
      "Giá có ẩn? Hỏng thì ai bảo hành?</p>"
      '<p class="fix">Gỡ bằng: <b>Straumann</b> (top 1) · <b>Invisalign Black Diamond</b> · '
      "<b>Nacera</b> · <b>Ormco Diamond Star</b> · 100% BS tốt nghiệp ĐH Y có chứng chỉ hành nghề · "
      "giấy phép Sở Y tế.</p></div>")
    A('<div class="barrier"><div class="barrier-top"><span class="barrier-name">NGẠI</span>'
      '<span class="tagp">Lộ trình &amp; chi phí</span></div>'
      "<p>Điều trị nhiều buổi, đi lại nhiều lần, chi phí lớn, không biết khi nào xong.</p>"
      '<p class="fix">Gỡ bằng: lộ trình rõ <b>số buổi và mốc thời gian</b> · trả góp · 7 cơ sở · '
      "đặt lịch linh hoạt.</p></div>")
    A("</div>")
    A('<div class="note warn" style="margin-top:14px"><b>Vì sao NGỜ nặng hơn hẳn ngành thẩm mỹ:</b> '
      "khách <b>không tự kiểm tra được vật liệu nằm trong miệng mình</b>. Đó là lý do cụm "
      "<b>C03 (vật liệu)</b> và <b>C14 (thực thể, kiểm chứng)</b> được đẩy lên Tầng A ở ba bộ "
      "Implant · Invisalign · Răng sứ, khác với phân bổ mặc định.<br><br>"
      "Nghịch lý phải nhớ: <b>bằng chứng mạnh nhất của Paris cũng là rào pháp lý dễ sai nhất.</b> "
      'Chữ “chính hãng” chỉ được gắn cho đúng 4 hãng trên — rào <code class="r">R7</code>.</div>')

    A('<h3 class="sub">Trục 6 bước — không đảo, không bỏ bước</h3>')
    A('<p class="dim" style="margin:0 0 13px">Mọi bài viết phải truy ngược được về một cụm truy vấn → '
      "một giai đoạn → một rào cản của một đối tượng thật. Không truy ngược được thì bị loại khỏi kế hoạch.</p>")
    A('<div class="axis">')
    for n, t, s, peak in [
        ("①", "Chọn lĩnh vực", "Bộ dịch vụ nào vào kế hoạch", False),
        ("②", "Đối tượng KH", "7–10 nhóm mỗi bộ + rào cản chi phối", False),
        ("③", "Giai đoạn S1–S6", "S3 Cân nhắc &amp; nỗi sợ là điểm quyết định, ~50% điểm ưu tiên", True),
        ("④", "Cụm truy vấn", "C01–C15 + tầng 80/20", False),
        ("⑤", "Cụm nội dung", "Quy ra số bài, trang đích, sóng", False),
        ("⑥", "GEO/SEO", "KPI đo được → Excel 2 TAB", False)]:
        A(f'<div class="axis-step{" peak" if peak else ""}"><span class="n">{n}</span>'
          f'<span class="t">{t}</span><span class="s">{s}</span></div>')
    A("</div></section>")

    # ── §4 ĐỌC OUTPUT ────────────────────────────────────────────────────
    A('<section id="output"><div class="sec-h"><span class="pre">Mục 4</span>'
      "<h2>Đọc output &amp; ranh giới</h2><span class=\"bar\"></span>"
      "<p>Agent không im lặng làm theo. Mỗi lần từ chối, nó nêu mã rào để Pháp chế biết đường duyệt.</p></div>")

    A('<div class="grid g2">')
    A('<div class="signbox"><div class="cap">✓ Năm dấu hiệu ĐÚNG</div><ul>'
      "<li><b>CORE giảm dần theo tháng</b> — T1 <code>69/69</code> → T4 <code>65/33</code> → "
      "T6 <code>61/0</code>. Tầng A dồn đầu chu kỳ đúng luật 80/20.</li>"
      "<li><b>Mọi business line có mặt mọi tháng</b> — không dồn một line vào một tháng.</li>"
      "<li><b>Mỗi ô Công việc chi tiết</b> có mã cụm + rào cản SỢ/NGỜ/NGẠI + mã rào pháp lý.</li>"
      "<li><b>Màu đỏ chỉ xuất hiện ở dòng ★ tổng tháng</b> — đúng tỷ lệ 5% của bộ nhận diện Paris.</li>"
      "<li><b>Tháng Setup có đủ R9 · R7 · R12</b> và ghi rõ “đây là mốc gốc, không đặt chỉ tiêu tăng trưởng”.</li>"
      "</ul></div>")
    A('<div class="signbox bad"><div class="cap">✕ Sáu dấu hiệu SAI</div><ul>'
      "<li>Cột <i>Hiện tại</i> của trụ cột 3/4/5 có <b>số tuyệt đối</b> mà Paris chưa cung cấp → bịa số.</li>"
      '<li>Bất kỳ <b>con số giá, % ưu đãi, lãi suất trả góp</b> nào trong file → vi phạm <code class="r">R12</code>.</li>'
      '<li>Chữ <b>“chính hãng”</b> gắn cho vật liệu ngoài 4 hãng → vi phạm <code class="r">R7</code>.</li>'
      "<li>Tháng Setup thiếu việc xin GXNNDQC hoặc thiếu việc khoá bộ đo GEO.</li>"
      '<li>Tên bác sĩ ngoài 3 hồ sơ, hoặc gắn bác sĩ vào bộ Nha chu / Trẻ em → vi phạm <code class="r">R4</code>.</li>'
      '<li>Có trang local cho tỉnh <b>không có cơ sở</b> → vi phạm <code class="r">R3</code>.</li>'
      "</ul></div>")
    A("</div>")

    A('<h3 class="sub">Agent sẽ từ chối hoặc cảnh báo</h3>')
    A('<div class="tw"><table><thead><tr><th style="width:40%">Nếu bạn yêu cầu</th>'
      "<th>Agent sẽ</th></tr></thead><tbody>")
    for ask, ans in [
        ("“Giá implant 18 triệu, điền vào kế hoạch”",
         'Từ chối — <code class="r">R12</code>: giá là dữ liệu động, chỉ ghi đầu việc lấy dải giá tại thời điểm chạy'),
        ("“Viết ‘phôi sứ Zirconia chính hãng’”",
         'Cảnh báo <code class="r">R7</code> — chỉ Straumann · Invisalign · Nacera · Ormco được gắn chữ này'),
        ("“Thêm ‘niềng không đau’ vào tiêu đề”",
         'Từ chối <code class="r">R1</code>; đề xuất “giảm cảm giác khó chịu nhờ công nghệ, bác sĩ theo dõi từng giai đoạn”'),
        ("“Ghi bác sĩ X phụ trách line Nha chu”",
         'Cảnh báo <code class="r">R4</code> — chỉ 3 bác sĩ đã có hồ sơ xác minh được gắn vào dịch vụ'),
        ("“Dựng trang local cho Cần Thơ, Thanh Hoá”",
         'Cảnh báo <code class="r">R3</code> — Paris không có cơ sở ở đó; đề xuất viết bài kiến thức nêu cơ sở gần nhất'),
        ("“Gắn giấy phép 2032/HNO-GPHĐ/CL1 cho trang Đà Nẵng”",
         'Từ chối <code class="r">R3</code> — mỗi cơ sở có giấy phép riêng do Sở Y tế tỉnh đó cấp'),
        ("“Viết bài: khách này bọc sứ chỗ khác bị hỏng”",
         'Cảnh báo <code class="r">R6</code> — tuyệt đối không phán xét nơi cũ; viết theo hướng phương án xử lý'),
        ("“Đoán tình trạng răng khách qua ảnh họ gửi”",
         'Từ chối <code class="r">R13</code> — không chẩn đoán, không kê đơn, không báo giá ca cụ thể'),
        ("“Hứa niềng xong trong 12 tháng”",
         'Từ chối <code class="r">R13</code> — nêu <b>dải</b> thời gian, nói rõ phụ thuộc từng ca'),
        ("“Đặt KPI traffic AI tháng 1 là 3.000 phiên”",
         "Cảnh báo không có mốc gốc nào → đề xuất % tăng trưởng, ghi <i>⚠ Cần xác minh từ Nha khoa Paris</i>"),
        ("“Bỏ qua bước đo GEO cho nhanh”",
         "Cảnh báo mất mốc gốc → không đánh giá được tăng trưởng cả chu kỳ"),
        ("“Làm Tầng B trước, Tầng A để sau”",
         "Nêu đánh đổi của việc phá luật 80/20, rồi mới làm theo nếu bạn khẳng định lại"),
    ]:
        A(f"<tr><td>{ask}</td><td>{ans}</td></tr>")
    A("</tbody></table></div>")

    A('<h3 class="sub">Khoảng trống dữ liệu — biết trước khi dùng</h3>')
    A('<div class="note warn"><p><b>⚠ Paris chưa cung cấp bất kỳ số GA4, thứ hạng từ khoá hay số lead nào.</b> '
      "Agent được thiết kế để <b>nói rõ điều này</b> thay vì lấp bảng bằng số bịa. "
      "Đây là trạng thái cố ý ghi nhận, không phải thiếu sót của kế hoạch.</p>"
      '<ul style="margin:0;padding-left:19px">'
      "<li><b>Trụ cột KPI 3 · 4 · 5</b> chỉ đặt được % tăng trưởng.</li>"
      "<li><b>Cơ hội GEO của mọi cụm = 1</b> → thứ tự ưu tiên hiện dựa trên rào cản khách, "
      "chưa hiệu chỉnh bằng traffic thật.</li>"
      "<li><b>Địa chỉ + SĐT + số giấy phép từng cơ sở</b> phải lấy tại "
      '<code>/tim-phong-kham.html</code> ngay khi chạy — rào <code class="r">R3</code>.</li>'
      "<li><b>Chưa có bác sĩ gán được</b> cho bộ Nha chu và Nha khoa trẻ em → cụm C14 của hai bộ này "
      'bị chặn bởi <code class="r">R4</code>.</li>'
      "<li><b>Mọi trang đích</b> hiện là <code>MỚI:</code> hoặc <code>⚠ đối chiếu</code> — "
      "phải soi sitemap thật trước khi giao việc.</li></ul>"
      '<p style="margin:10px 0 0"><b>Hệ quả:</b> tháng Setup của mọi chu kỳ là tháng lấy mốc gốc. '
      "Sau tháng Setup, chạy lại bước ④ để xếp lại Cơ hội GEO theo traffic thật.</p></div>")
    A("</section>")

    # ── §5 CÔNG CỤ ───────────────────────────────────────────────────────
    A('<section id="cong-cu"><div class="sec-h"><span class="pre">Mục 5</span>'
      "<h2>Chạy công cụ cục bộ</h2><span class=\"bar\"></span>"
      "<p>Sinh file Excel mà không qua Agent. Dữ liệu nguồn là 10 file JSON trong "
      f'<a href="{GH}/tree/main/data/bo-truy-van" target="_blank" rel="noopener">'
      "<code>data/bo-truy-van/</code></a>, sửa trực tiếp được bằng editor.</p></div>")
    A('<pre class="cli"><span class="c"># lấy repo về</span>\n'
      f"git clone {GH}.git\ncd Agent-PR-GEO-Plant\n\n"
      '<span class="c"># cài một lần</span>\npip install openpyxl\n\n'
      '<span class="c"># sinh lại chỉ mục knowledge sau khi sửa JSON</span>\n'
      '<span class="c"># (tự soát 15 cụm · tổng % điểm = 100 · tầng 5/5/3/2, lệch là dừng)</span>\n'
      "python tools/build-index.py\n\n"
      '<span class="c"># sinh file kế hoạch 2 TAB</span>\n'
      "python tools/build-geo-plan.py --start 2027-01 --months 6\n"
      "python tools/build-geo-plan.py --start 2026-11 --months 4 --scope implant,allon,invisalign\n"
      "python tools/build-geo-plan.py --start 2027-01 --months 12 --tiers A,B,C -o ke-hoach-2027.xlsx\n\n"
      '<span class="c"># sinh lại chính trang hướng dẫn này từ nội dung repo</span>\n'
      "python tools/build-artifact.py\n\n"
      '<span class="c"># key hợp lệ của --scope</span>\n'
      '<span class="c"># thuonghieu · implant · allon · niengmaccai · invisalign</span>\n'
      '<span class="c"># rangsu · veneer · tongquat · nhachu · trenem</span></pre>')
    A('<p class="dim" style="margin-top:13px">Script in ra ngay chênh lệch sản lượng tháng cao/thấp '
      "và kết luận ĐẠT/VƯỢT ràng buộc ≤25%.</p>")
    A("</section>")

    A("</main>")

    # ── footer ───────────────────────────────────────────────────────────
    A('<footer><div class="wrap">')
    A(f'<p style="margin:0 0 6px"><b>Agent-PR-GEO-Plant</b> v1.0 · '
      f'<a href="{GH}" target="_blank" rel="noopener">github.com/huudinh/Agent-PR-GEO-Plant</a> · '
      "kế thừa kiến trúc từ Agent-KN-GEO-Plant</p>")
    A('<p style="margin:0 0 6px">Tài liệu đầy đủ: '
      + " · ".join(f'<a href="{GH}/blob/main/{p}" target="_blank" rel="noopener"><code>{p}</code></a>'
                   for p in ["README.md", "doc/01-cai-dat.md", "doc/02-cau-lenh.md",
                             "doc/03-output-mau.md", "doc/CHANGELOG.md"])
      + "</p>")
    A('<p style="margin:0"><b>Trang này sinh tự động</b> từ nội dung repo bằng '
      "<code>tools/build-artifact.py</code> — sửa knowledge rồi chạy lại, đừng sửa tay HTML. "
      "Quyết định cuối luôn thuộc người dùng.</p>")
    A("</div></footer>")

    A("<script>" + JS + "</script>")

    out = "\n".join(L)
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(out)
    kb = len(out.encode("utf-8")) / 1024
    print(f"✔ {OUT}")
    print(f"  {kb:,.0f} KB · bộ não {nchar(brain_txt)} ký tự · {len(files)} file tri thức "
          f"({nchar('x' * merged_len)} ký tự) · {len(PROMPTS)} prompt")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    build()
