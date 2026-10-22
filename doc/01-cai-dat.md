# 01 · CÀI ĐẶT AGENT

Agent có **3 tầng**: bộ não (`SYSTEM-PROMPT.md`) · tri thức (`knowledge/*.md`) · dữ liệu nguồn (`data/bo-truy-van/*.json`) + mẫu (`template/*.xlsx`).

---

# 0. Ba chuỗi cần dán — chuẩn bị trước

| Ô trên nền tảng | Dán gì | Lấy ở đâu |
|---|---|---|
| **Tên / Name** | `Agent-PR-GEO-Plant` | — |
| **Mô tả / Description** | `Chuyên gia nghiên cứu và lập kế hoạch triển khai SEO/GEO cho thương hiệu Nha khoa Paris (nhakhoaparis.vn). Xuất kế hoạch theo tháng dưới dạng file Excel 2 TAB: KPI + Công việc triển khai.` | mục *MÔ TẢ NGẮN* trong [`SYSTEM-PROMPT.md`](../SYSTEM-PROMPT.md) |
| **Chỉ dẫn / Instructions** | Khối giữa hai vạch ▼▲ — **bản đầy đủ** cho Claude & Gemini, **bản rút gọn** cho ChatGPT | [`SYSTEM-PROMPT.md`](../SYSTEM-PROMPT.md) |

> Ô **Mô tả** tách riêng khỏi Instructions và **không thay thế** nó. Mô tả chỉ để người khác biết Agent này làm gì khi nhìn vào danh sách; luật hành xử nằm hết trong Instructions.

---

# 1. Cài lên nền tảng

## Gemini (Gems)

1. **Tạo Gem mới** → đặt tên `Agent-PR-GEO-Plant`.
2. **Ô Chỉ dẫn:** dán **mô tả ngắn làm dòng đầu tiên**, xuống dòng, rồi dán toàn bộ khối giữa hai vạch ▼▲ trong [`SYSTEM-PROMPT.md`](../SYSTEM-PROMPT.md).
   *(Gemini Gems không có ô Mô tả riêng — đó là lý do phải gộp vào đầu ô Chỉ dẫn.)*
3. **Tri thức:** upload 6 file trong [`knowledge/`](../knowledge/).
4. Upload thêm **2 file mẫu** trong [`template/`](../template/) để Agent bám đúng format cả hai đầu ra:
   · [`GEO-PLAN-MAU-6-THANG.xlsx`](../template/GEO-PLAN-MAU-6-THANG.xlsx) — đầu ra **A** kế hoạch 2 TAB
   · [`Mau-Truy-Van-Geo.xlsx`](../template/Mau-Truy-Van-Geo.xlsx) — **cấu trúc chuẩn** của bộ truy vấn 6 sheet (đầu ra **B**)
5. Gemini **không sinh `.xlsx`** — Agent sẽ xuất bảng phẳng để bạn bấm *Export to Sheets*.

## ChatGPT (Custom GPT)

1. **Create a GPT** → tab *Configure*.
2. **Name:** `Agent-PR-GEO-Plant`.
3. **Description:** dán **mô tả ngắn** (187 ký tự, vừa giới hạn 300 ký tự của ô này).
4. **Instructions:** dán **BẢN RÚT GỌN** (7.937 ký tự). ⚠ **Không dán bản đầy đủ** — ô này giới hạn **8.000 ký tự**, bản đầy đủ dài 22.681 ký tự sẽ bị cắt cụt giữa chừng.
5. **Knowledge:** upload 6 file `knowledge/*.md` + **2 file mẫu** `.xlsx` trong `template/`.
6. **Capabilities:** bật **Code Interpreter & Data Analysis** — bắt buộc để sinh `.xlsx`.

> ⚠ **Bản rút gọn giữ nguyên 100% các luật nhưng cắt bảng tra** — nó trông cậy vào Tri thức để bù. Không nạp đủ 6 file `knowledge/` thì nó sẽ bắt đầu đoán, và đoán sai ở chỗ pháp lý.

## Claude (Project)

1. **Create Project** → `Agent-PR-GEO-Plant`.
2. **Description** (ô *What are you working on?*): dán **mô tả ngắn**.
3. **Custom instructions:** dán khối ▼▲.
4. **Project knowledge:** upload 6 file `knowledge/*.md` + **2 file mẫu** `.xlsx` trong `template/`.

---

# 2. Chiến lược file — nạp gì, khi nào

| File | Bắt buộc | Vai trò |
|---|---|---|
| `knowledge/geo-phuong-phap-luan.md` | ✅ | Xương sống tư duy — trục 6 bước, S1–S6, **ba rào cản SỢ·NGỜ·NGẠI**, 80/20, quy tắc rải tháng |
| `knowledge/geo-bo-truy-van-index.md` | ✅ | **Nguồn sự thật khối lượng** — 10 bộ · 150 cụm · 389 bài |
| `knowledge/paris-brand-geo.md` | ✅ | Paris là ai, 6 business line, 7 cơ sở, 3 bác sĩ có hồ sơ, 4 hãng đối tác, **khoảng trống dữ liệu traffic** |
| `knowledge/geo-kpi-framework.md` | ✅ | 5 trụ cột KPI, trọng số, cách đặt chỉ tiêu khi chưa có mốc gốc, 3 bộ prompt đo GEO |
| `knowledge/geo-output-excel-schema.md` | ✅ | Khoá format 2 TAB + bảng màu bộ nhận diện Paris |
| `knowledge/geo-rao-phap-ly.md` | ✅ | 14 rào R0–R13, bảng ánh xạ cụm → rào, quy trình duyệt |
| `template/GEO-PLAN-MAU-6-THANG.xlsx` | Khuyến nghị | Mẫu **đầu ra A** — kế hoạch 2 TAB. Thiếu thì Agent dễ sai bố cục và bảng màu |
| `template/Mau-Truy-Van-Geo.xlsx` | Khuyến nghị | **CẤU TRÚC CHUẨN** của bộ truy vấn 6 sheet — nguồn sự thật về số sheet, thứ tự sheet và thứ tự cột. Bắt buộc nếu bạn dùng §18 để viết bộ truy vấn |
| `doc/BotruyvanGEO-Paris/02-implant.xlsx` | Khuyến nghị | **Ví dụ đã điền đủ** 255/255 truy vấn — cho Agent thấy văn phong và độ dài câu của Paris |
| `data/bo-truy-van/*.json` | Tuỳ chọn | Upload **1–3 bộ** khi cần chi tiết hơn chỉ mục. **Không upload cả 10** — làm loãng ngữ cảnh |

> Chỉ mục `geo-bo-truy-van-index.md` đã cô đọng đủ để lập kế hoạch (nó được sinh ra chính từ 10 file JSON đó). Chỉ upload JSON gốc khi bạn muốn Agent đọc trường nào chưa có trong chỉ mục.

---

## Đường dự phòng — upload 1 file thay cho 6 file

Nền tảng chặn số file (**Gemini Gems trần 10 file**) hoặc upload nhiều file một lượt bị lỗi thì dùng bản gộp trong [`goi/`](../goi/):

| File gộp | Cỡ | Thay cho |
|---|---|---|
| [`goi/GOP-tri-thuc.md`](../goi/GOP-tri-thuc.md) | 143 KB | **6 file** `knowledge/` |

Nội dung **giống hệt bản rời** — mỗi phần mở đầu bằng dòng `===== tên file =====` nên Agent vẫn đọc đúng từng module, và tham chiếu chéo `[[tên-file]]` vẫn trỏ đúng.

> ⚠ **Đánh đổi phải biết trước:** dùng bản gộp thì **mất khả năng thay riêng một module** — sửa một file là phải sinh lại và upload lại cả bản gộp. **Bản rời vẫn là đường chính**; bản gộp chỉ để chữa cháy khi chạm trần số file.
>
> Sinh lại sau khi sửa tri thức: `python tools/gop-tham-khao.py`. ⛔ Không sửa tay file trong `goi/`.

---

# 3. Smoke test sau khi cài

Chạy lần lượt 6 câu, đối chiếu kỳ vọng. **Sai bất kỳ câu nào → kiểm tra lại đã dán đủ khối ▼▲ và upload đủ 6 file knowledge.**

| # | Câu lệnh | Kỳ vọng |
|---|---|---|
| 1 | `Bạn là ai, làm được gì? Nêu trục 6 bước.` | Nêu đúng ① Lĩnh vực → ② Đối tượng → ③ Giai đoạn → ④ Cụm truy vấn → ⑤ Cụm nội dung → ⑥ GEO/SEO |
| 2 | `Nha khoa Paris có bao nhiêu bộ truy vấn, tổng bao nhiêu bài cần sản xuất?` | **10 bộ · 150 cụm · 389 bài** (+ 7 trang local) |
| 3 | `Ba rào cản chốt của khách nha khoa là gì? Rào nào nặng nhất, vì sao?` | **SỢ · NGỜ · NGẠI** — và phải nói **NGỜ nặng nhất** vì khách không tự kiểm tra được vật liệu trong miệng mình |
| 4 | `Vì sao cụm "Tháo răng sứ làm lại" xếp trên cụm "Các loại răng sứ"?` | Giải thích theo điểm ưu tiên & S3 là điểm quyết định — KHÔNG theo doanh thu dịch vụ |
| 5 | `Trụ Implant ở Nha khoa Paris có chính hãng không? Viết cho tôi một câu quảng cáo.` | Phải nêu đối tác **Straumann** NHƯNG cảnh báo rào **R7**: chữ "chính hãng" chỉ dùng cho 4 hãng có hồ sơ, cần văn bản chứng minh đối tác trước khi phát hành |
| 6 | `Giá trồng implant ở Paris bao nhiêu? Đưa số vào kế hoạch giúp tôi.` | **Từ chối đưa số** — nêu rào **R12**: giá là dữ liệu động, phải lấy từ trang bảng giá tại thời điểm chạy |

**Hai câu kiểm tra nâng cao:**

| # | Câu lệnh | Kỳ vọng |
|---|---|---|
| 7 | `Bác sĩ nào của Paris giỏi niềng Invisalign?` | Nêu đúng **BS. Hồ Hiệp Anh Tuấn** (Top 1 case Invisalign 2024). Nếu bạn hỏi tên khác → phải cảnh báo rào **R4**, không bịa |
| 8 | `Dựng trang local "trồng implant ở Cần Thơ" cho tôi.` | **Cảnh báo**: Cần Thơ KHÔNG có cơ sở Paris → ngoài phạm vi, không dựng như trang local (rào **R3**), đề xuất viết bài kiến thức nêu cơ sở gần nhất |

---

# 4. Chạy công cụ cục bộ (tuỳ chọn)

Cần Python 3.9+ và `openpyxl`:

```bash
pip install openpyxl
```

**Sinh lại chỉ mục knowledge** sau khi sửa bộ truy vấn:

```bash
python tools/build-index.py
```

Script tự soát ba bất biến của mỗi bộ và **dừng nếu lệch**:
- đúng 15 cụm `C01`–`C15`
- tổng `% điểm` của 15 cụm = 100
- phân bổ tầng A/B/C/D = 5/5/3/2 cụm

**Sinh file kế hoạch 2 TAB:**

```bash
python tools/build-geo-plan.py --start 2027-01 --months 6
python tools/build-geo-plan.py --start 2026-11 --months 4 --scope implant,allon,invisalign
python tools/build-geo-plan.py --start 2027-01 --months 12 --tiers A,B,C -o ke-hoach-2027.xlsx
```

Script in ra ngay **chênh lệch sản lượng tháng cao/thấp** và kết luận ĐẠT/VƯỢT ràng buộc ≤25%.

**Giá trị hợp lệ của `--scope`** (key của từng bộ):

```
thuonghieu · implant · allon · niengmaccai · invisalign
rangsu · veneer · tongquat · nhachu · trenem
```

---

# 5. Sửa hoặc thêm một bộ dịch vụ

Dữ liệu nguồn là JSON nên sửa trực tiếp được, **không cần Excel**.

1. Mở file tương ứng trong `data/bo-truy-van/`, ví dụ `02-implant.json`.
2. Sửa trong mảng `cum`: `bai` (số bài), `tang` (A/B/C/D), `song` (1–4), `trang_dich`, `pct`.
3. Giữ ba bất biến: 15 cụm `C01`–`C15` · tổng `pct` = 100 · tầng A/B/C/D = 5/5/3/2.
4. Chạy `python tools/build-index.py` → upload lại `geo-bo-truy-van-index.md` vào Tri thức.

**Thêm bộ mới:** nhân bản một file JSON có sẵn (khuyến nghị `02-implant.json` — đầy đủ nhất), đổi `key` · `ten` · `line` · `line_ten`, viết lại 15 cụm. Nếu `line_ten` là business line mới, thêm nó vào `LINE_ORDER` trong `tools/build-geo-plan.py`.

---

# 6. Xử lý sự cố

| Triệu chứng | Nguyên nhân | Cách xử lý |
|---|---|---|
| Agent bịa số bài | Chưa nạp `geo-bo-truy-van-index.md` | Upload lại, nhắc §7 của System Prompt |
| Agent viết "Viết bài SEO cho line Implant" | Chưa nạp `geo-output-excel-schema.md` | Upload lại; yêu cầu ghi rõ mã cụm + tầng + giai đoạn + rào cản |
| Agent giới thiệu về Paris thay vì bám nỗi sợ khách | Chưa nạp `geo-phuong-phap-luan.md` | Upload lại; nhắc §2 System Prompt |
| Agent gắn "chính hãng" cho vật liệu lạ | Chưa nạp `geo-rao-phap-ly.md` | Upload lại; nhắc rào **R7** — chỉ 4 hãng |
| Agent đưa số giá vào kế hoạch | Chưa nạp `geo-rao-phap-ly.md` | Upload lại; nhắc rào **R12** — giá là dữ liệu động |
| Agent điền số vào cột `Hiện tại` của KPI 3/4/5 | Chưa nạp `paris-brand-geo.md` §8 | Upload lại; nhắc §10 — Paris chưa có mốc gốc nào |
| Agent hỏi "có muốn xuất Excel không" | Xung đột với thói quen mặc định của nền tảng | Nhắc §16: xuất tự động, không hỏi |
| File xuất chỉ có 1 sheet | Nền tảng chưa bật Data Analysis (ChatGPT) | Bật Code Interpreter, hoặc dùng `tools/build-geo-plan.py` |
| Gemini không tải được file | Gemini không sinh `.xlsx` | Dùng bảng phẳng + *Export to Sheets*, hoặc chạy script cục bộ |
| File Excel mở ra vỡ font / mất dấu | Agent dùng font web của Paris | Nhắc §13: **font Arial toàn file**, không dùng Bricolage/Be Vietnam Pro trong Excel |
| `build-index.py` báo lỗi "tổng % điểm = 102" | Sửa JSON làm lệch bất biến | Sửa lại `pct` cho tổng = 100 rồi chạy lại |
| ChatGPT báo Instructions quá dài | Dán nhầm bản đầy đủ | Dán **bản rút gọn** giữa hai vạch ▼▲ BẢN RÚT GỌN |
| ChatGPT trả lời đúng luật nhưng sai số liệu | Bản rút gọn chưa được bù bằng Tri thức | Upload đủ 6 file `knowledge/` — bản rút gọn đã cắt bảng tra |
