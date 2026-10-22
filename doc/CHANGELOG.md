# CHANGELOG

## Bản gộp dự phòng cho file tri thức — 22/10/2026

Thêm 1 file gộp trong `goi/` và `tools/gop-tham-khao.py` để sinh lại:

- `goi/GOP-tri-thuc.md` — gộp **6 file** `knowledge/` (143 KB)

**Vì sao cần:** Gemini Gems chặn ở **10 file** tri thức, và upload hàng chục file một lượt rất hay lỗi. Gặp trần thì trước giờ không có đường nào ngoài bỏ bớt file — mà bỏ bớt file tri thức là bỏ bớt luật, và luật bị bỏ thường là luật pháp lý vì nó nằm ở file người ta tưởng không quan trọng.

**Không mất nội dung nào.** Mỗi phần trong bản gộp mở đầu bằng dòng `===== tên file =====`, nên Agent vẫn đọc đúng từng module và tham chiếu chéo `[[tên-file]]` vẫn trỏ đúng — chỉ đổi chỗ nằm, không đổi mã. Đã đối chiếu từng byte với bản rời.

**Đánh đổi, đã ghi vào `doc/01-cai-dat.md`:** dùng bản gộp thì **mất khả năng thay riêng một module** — sửa một file là phải sinh lại và upload lại cả bản gộp. **Bản rời vẫn là đường chính**; bản gộp chỉ để chữa cháy khi chạm trần.

⛔ Không sửa tay file trong `goi/`. Sửa ở thư mục nguồn rồi chạy `python tools/gop-tham-khao.py`.

---

## v1.0 — 19/10/2026

Bản đầu tiên của **Agent-PR-GEO-Plant**, kế thừa kiến trúc 3 tầng của [`Agent-KN-GEO-Plant`](../../Agent-KN-GEO-Plant).

### Những gì kế thừa từ Agent-KN-GEO-Plant

- Kiến trúc 3 tầng: bộ não `SYSTEM-PROMPT.md` · tri thức `knowledge/*.md` · dữ liệu nguồn.
- Trục 6 bước (Lĩnh vực → Đối tượng → Giai đoạn → Cụm truy vấn → Cụm nội dung → GEO/SEO).
- Khung 6 giai đoạn hành trình S1–S6 với S3 là điểm quyết định.
- Bốn tầng 80/20 (A 70% · B 20% · C 10% · D 0%) và cấu trúc 15 cụm C01–C15 mỗi bộ.
- Công thức điểm ưu tiên, 6 quy tắc viết để AI trích dẫn, hệ số quy đổi A1/A2/A3.
- 5 trụ cột KPI với trọng số 0,10 / 0,20 / 0,40 / 0,15 / 0,15 và 4 giai đoạn chu kỳ.
- Format output 2 TAB với ba cấp dòng tổng (chi tiết → `▶` business line → `★` tháng).
- Nguyên tắc "không bịa số" — thiếu mốc gốc thì ghi `⚠ Cần xác minh` + đề xuất % tăng trưởng.

### Những gì thay mới cho ngành nha khoa

**① Ba rào cản chốt SỢ · NGỜ · NGẠI thay cho 3 nỗi sợ ngành thẩm mỹ.**
Khác biệt căn bản: **rào NGỜ ở nha khoa nặng hơn hẳn thẩm mỹ** vì khách không tự kiểm tra được vật liệu nằm trong miệng mình. Hệ quả vận hành: cụm **C03 (vật liệu)** và **C14 (thực thể, kiểm chứng)** được đẩy lên **Tầng A** ở 3 bộ Implant · Invisalign · Răng sứ, khác với phân bổ mặc định.

**② Dữ liệu nguồn chuyển từ Excel sang JSON.**
Kangnam đọc 17 file `.xlsx` 6 sheet. Paris dùng **10 file JSON** trong `data/bo-truy-van/` — sửa trực tiếp được bằng editor, version-control được, và `build-index.py` tự soát ba bất biến (15 cụm C01–C15 · tổng % điểm = 100 · tầng A/B/C/D = 5/5/3/2) rồi **dừng nếu lệch**.

**③ Kho dữ liệu mới: 10 bộ · 150 cụm · 389 bài · 2.550 truy vấn.**

| Business line | Bộ | Bài |
|---|---|---|
| BRAND · Thương hiệu tổng | Thương hiệu Nha khoa Paris | 34 |
| NKI · Implant & Phục hình | Implant · All-On 4/6 | 77 |
| NKC · Chỉnh nha | Niềng mắc cài · Invisalign | 75 |
| NKT · Nha khoa thẩm mỹ | Bọc răng sứ · Veneer | 81 |
| NKG · Tổng quát & Nha chu | Tổng quát · Nha chu | 82 |
| NKF · Trẻ em & Gia đình | Nha khoa trẻ em & gói gia đình | 40 |

**④ Rào pháp lý mở rộng từ 12 (R0–R11) lên 14 (R0–R13),** thêm hai rào đặc thù:
- **R7 · "CHÍNH HÃNG"** — rào dễ sai nhất của ngành nha khoa. Chỉ dùng cho Straumann · Invisalign · Nacera · Ormco. Nghịch lý: *bằng chứng mạnh nhất của Paris cũng là rào pháp lý dễ sai nhất.*
- **R12 · GIÁ · ƯU ĐÃI · TRẢ GÓP = DỮ LIỆU ĐỘNG** — tuyệt đối không đưa con số vào kế hoạch.
- **R13 · Chẩn đoán & hứa thời gian** — không chẩn đoán qua ảnh/mô tả, không báo giá ca cụ thể, không hứa thời gian điều trị cứng.
- Thêm **bảng ánh xạ cụm → rào** (§5) để Agent ghi mã rào tự động vào cột Công việc chi tiết.

**⑤ Trang local: 7 hub có cơ sở thật thay vì 8 hub + 19 tỉnh vệ tinh.**
Paris có cơ sở tại Hà Nội · Hải Phòng · Quảng Ninh · Vinh · Đà Nẵng · TP.HCM · Bình Dương. Script phủ hết 7 hub rồi **chuyển sang rà soát & tối ưu**, không sinh thêm trang tỉnh không có cơ sở — vì mỗi trang local phải gắn **giấy phép của chính cơ sở đó** (R3), và `2032/HNO-GPHĐ/CL1` chỉ là giấy phép của cơ sở Hà Nội.

**⑥ Bảng màu output chuyển sang bộ nhận diện Nha khoa Paris.**
Cerulean Blue `#2A52BE` · Pantone Red 032 C `#ED2E38` · White, theo tỷ lệ bắt buộc **80% trắng/kem · 15% xanh · 5% đỏ**. Đỏ **chỉ** dùng cho dòng `★ TỔNG SẢN LƯỢNG THÁNG` (một dòng mỗi tháng) và header panel sản lượng. Font Excel giữ **Arial** — không dùng font web Bricolage Grotesque / Be Vietnam Pro vì máy người nhận thường chưa cài.

**⑦ Quy tắc C05 ra cùng Tầng A.**
Cụm "khi nào KHÔNG nên làm" của 3 bộ Răng sứ · Implant · Niềng mắc cài được **nâng lên Sóng 1** dù nằm Tầng B. Đây là khác biệt E-E-A-T lớn nhất của Paris và là nội dung đối thủ gần như không dám viết. Script tự áp quy tắc này qua hằng số `C05_EARLY`.

**⑧ Ba bộ prompt đo GEO mới:** 20 prompt dịch vụ trọng điểm · 7 prompt hub cơ sở · 10 prompt kiểm chứng thương hiệu (thay cho 20 chính · 8 hub · 19 tỉnh của Kangnam).

**⑨ Micro-conversion riêng cho Paris:** 4 công cụ kiểm tra online (răng miệng · niềng · răng sứ · trồng răng) được đo như một bậc riêng trước form — vừa gỡ rào NGẠI vừa neo thực thể cho cụm C01.

### Thành phần bản 1.0

**Bộ não** — `SYSTEM-PROMPT.md`, 17 mục. Trọng tâm §2 (không giới thiệu về mình), §5 (ba rào cản SỢ·NGỜ·NGẠI), §12 (R0–R13 với R7 & R12), §13 (schema 2 TAB + bảng màu Paris), §14 (self-review 14 điểm).

**Tri thức (6 file)**
- `geo-phuong-phap-luan.md` — trục 6 bước · S1–S6 · ba rào cản chốt · công thức điểm ưu tiên · 4 tầng 80/20 · 7 nhóm mở rộng ưu tiên cho nha khoa · 6 quy tắc viết · 8 nguyên tắc rải tháng.
- `geo-bo-truy-van-index.md` — **sinh tự động** từ 10 file JSON: 150 cụm · 389 bài · bản đồ cụm → tầng → giai đoạn → sóng → trang đích.
- `paris-brand-geo.md` — định vị · 6 business line · 7 cơ sở · 3 bác sĩ có hồ sơ · 4 hãng đối tác · tone of voice · **§8 khoảng trống dữ liệu traffic**.
- `geo-kpi-framework.md` — 5 trụ cột & trọng số · quy trình quy đổi khối lượng → chỉ tiêu tháng · 3 bộ prompt đo GEO · 17 mã KPI nền.
- `geo-output-excel-schema.md` — khoá format 2 TAB: bảng màu Paris, bố cục dòng/cột, 3 cấp dòng tổng, checklist trước khi xuất.
- `geo-rao-phap-ly.md` — 14 rào R0–R13 · ba rào chi phối khối lượng lớn nhất · bảng ánh xạ cụm → rào.

**Công cụ**
- `tools/build-index.py` — sinh lại chỉ mục knowledge từ JSON, có validate ba bất biến.
- `tools/build-geo-plan.py` — sinh file kế hoạch 2 TAB cho số tháng bất kỳ. Rải cụm riêng từng business line theo hạn ngạch, tách cụm lớn sang tháng kế, nâng C05 lên Sóng 1 ở 3 bộ, phủ 7 hub local rồi chuyển sang tối ưu. In ra ngay chênh lệch sản lượng tháng và kết luận ĐẠT/VƯỢT ràng buộc ≤25%.

**Mẫu**
- `template/GEO-PLAN-MAU-6-THANG.xlsx` — bản mẫu 6 tháng (395 đầu việc nội dung · 163 đầu việc KPI).
- `template/GEO-NKPARIS-T01-T06-2027.xlsx` — bản sinh theo quy ước tên file chuẩn.

**Tài liệu** — `doc/01-cai-dat.md` (8 câu smoke test) · `doc/02-cau-lenh.md` (14 prompt mẫu) · `doc/03-output-mau.md` (output mẫu có số thật) · `artifact/huong-dan-su-dung.html` (trang hướng dẫn + thư viện prompt).

---

## v1.1 — 19/10/2026 · Bộ truy vấn GEO theo mẫu chuẩn 6 sheet

Áp dụng **mẫu template** của bộ Kangnam (`HCI-Knowledge/KN-BotruyvanGEO/*.xlsx`) cho Paris.

**Công cụ mới** — `tools/build-botruyvan.py`: sinh 10 file `.xlsx` 6 sheet vào `doc/BotruyvanGEO-Paris/`, giữ nguyên tên sheet, thứ tự cột và cách đọc của bộ gốc. Sheet 1 · 2 · 4 · 6 và khối xếp hạng cụm của sheet 3 sinh tự động từ `data/bo-truy-van/*.json`; sheet 6 **tự đếm** số truy vấn và CORE chịu từng rào R0–R13.

**Tầng dữ liệu mới** — `data/truy-van/<key>.json`: cấp truy vấn (17 dòng mỗi cụm) gồm câu khách gõ vào AI, góc hỏi fan-out, nhiệt độ, ưu tiên, từ khoá, brief khối trả lời, rào pháp lý và nhóm đối tượng. Thiếu file này thì sheet 3 vẫn đủ 255 dòng với mọi cột suy ra được đã điền sẵn.

**Bộ `implant` hoàn chỉnh 255/255 truy vấn** làm khuôn cho 9 bộ còn lại — 64 CORE, 8 nhóm đối tượng, mỗi truy vấn có brief BLUF + số liệu + điều bất lợi phải nói thẳng.

**Hai điểm khác bộ gốc Kangnam, đều có lý do:**
- Bảng màu chuyển sang bộ nhận diện Nha khoa Paris (80% trắng/kem · 15% xanh · 5% đỏ).
- **CƠ HỘI GEO = 1 cho MỌI cụm** vì Paris chưa có mốc traffic AI nào để chấm 2–3. Kangnam chấm được 1–3 nhờ có GA4 thật. Hệ quả: cột `ĐIỂM CỤM` (cộng bottom-up từ truy vấn) và cột `% ĐIỂM (chỉ mục)` lệch nhau — đã ghi chú ngay trên sheet 3 và phải hợp nhất sau tháng Setup.

**Giới hạn tên sheet Excel 31 ký tự** → mỗi bộ có tên ngắn ≤8 ký tự trong `TEN_NGAN`; script dừng nếu vượt.

---

## ⚠ Khoảng trống dữ liệu lớn nhất của bản 1.0

Khác với Kangnam (có GA4 thật: 2.131 phiên AI, 17 landing page phân loại), **Paris chưa cung cấp bất kỳ số liệu nào**. Agent được thiết kế để **nói rõ điều này** thay vì lấp bảng bằng số bịa.

| Hạng mục | Ảnh hưởng |
|---|---|
| Traffic AI & organic hiện tại (GA4) | Trụ cột KPI 4 chỉ đặt được % tăng trưởng |
| Thứ hạng từ khoá Top 3/5/10 | Trụ cột KPI 3 không có mốc gốc |
| Số lead / sđt xác nhận / KH đến phòng khám | Trụ cột KPI 5 không có mốc gốc |
| Landing page nào đang hút traffic AI | **Cơ hội GEO của mọi cụm = 1** → thứ tự ưu tiên hiện dựa trên rào cản khách, chưa hiệu chỉnh bằng traffic thật. Đây là điểm cần sửa ngay sau tháng Setup đầu tiên |
| Địa chỉ + SĐT + số giấy phép từng cơ sở | 6/7 trang local bị chặn bởi rào **R3** |
| Danh sách bác sĩ nha chu & nha khoa trẻ em | Cụm C14 của 2 bộ `nhachu`, `trenem` bị chặn bởi rào **R4** |
| Văn bản chứng minh đối tác 4 hãng | Chữ "chính hãng" bị chặn bởi rào **R7** |
| Năng lực sản xuất thực tế của đội content (bài/tháng) | Chưa kiểm chứng được chỉ tiêu ~65 bài/tháng |

---

## Việc còn treo cho bản 1.1

| Hạng mục | Vì sao cần |
|---|---|
| Đối chiếu **sitemap thật** của `nhakhoaparis.vn` | Mọi `trang_dich` trong JSON hiện là `MỚI:` (tạo mới) hoặc `⚠ đối chiếu` (chưa xác minh). Chỉ 2 URL đã biết chắc: `/hoan-my-bang-gia-dich-vu-nha-khoa.html` và `/tim-phong-kham.html` |
| Nạp số GA4 + thứ hạng từ khoá thật | Để xếp lại **Cơ hội GEO** của 150 cụm và hiệu chỉnh thứ tự ưu tiên |
| Viết truy vấn chi tiết cho 9 bộ còn lại | Bộ `implant` đã đủ 255/255 truy vấn làm mẫu. 9 bộ còn lại mới có khung sheet 3 — cần điền cột TRUY VẤN và KHỐI TRẢ LỜI (2.295 dòng) |
| Bổ sung bộ dịch vụ còn thiếu | Cầu răng sứ · răng toàn sứ riêng · đính đá · cắt lợi trùm — hiện gom trong `rangsu` và `tongquat` |
| Danh sách bác sĩ đầy đủ theo cơ sở | Mở khoá cụm C14 cho 2 bộ còn bị chặn và cho phép gán bác sĩ theo từng hub local |
