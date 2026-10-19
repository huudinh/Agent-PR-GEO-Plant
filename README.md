# 🦷 Agent-PR-GEO-Plant

> Version 1.0 · AI lập **kế hoạch GEO (Generative Engine Optimization)** theo tháng cho **Hệ thống Nha khoa Paris** (`nhakhoaparis.vn`) — đầu ra là file Excel **2 TAB: KPI + Công việc triển khai**.

Đóng vai **Growth Operating AI**: đọc 10 bộ truy vấn GEO → xác định đối tượng & rào cản theo 6 giai đoạn hành trình → xếp ưu tiên cụm theo 80/20 → quy ra khối lượng bài viết → rải theo tháng → gắn KPI đo được và người phụ trách.

Kế thừa kiến trúc 3 tầng của [`Agent-KN-GEO-Plant`](../Agent-KN-GEO-Plant), thay toàn bộ dữ liệu ngành thẩm mỹ bằng dữ liệu **nha khoa** và bộ nhận diện **Nha khoa Paris**.

---

## Nguyên tắc tối thượng

> **Nha khoa Paris không đi kể chuyện mình giỏi. Paris đi theo hành trình của khách, gỡ từng nỗi lo, rồi mới xuất hiện như giải pháp.**

| Cách cũ (brand-first) | Cách của Agent này (customer-journey-first) |
|---|---|
| "Nha khoa Paris là hệ thống nha khoa tiêu chuẩn Pháp đầu tiên…" | "Bọc răng sứ có phải mài hết men răng thật không?" |
| Nội dung xoay quanh **chúng tôi có gì** | Nội dung xoay quanh **khách đang sợ gì** |
| Đo bằng thứ hạng từ khoá | Đo bằng **AI có trích dẫn Nha khoa Paris không** |
| Né chủ đề mài răng, biến chứng, giá, tháo sứ làm lại | **Chiếm lĩnh** đúng những chủ đề đó — vì đó là nơi khách quyết định |

---

## Ba rào cản chốt — điểm khác biệt so với ngành thẩm mỹ

| Rào cản | Khách đang nghĩ gì | Bằng chứng Paris dùng để gỡ |
|---|---|---|
| **① SỢ** | Đau khi nhổ/khoan/cấy. **Mài mất răng thật** — men răng không mọc lại. Niềng thì lâu, đau, xấu suốt thời gian đeo. | Piezotome · RECIPROC BLUE · bác sĩ theo dõi từng giai đoạn · Invisalign trong suốt |
| **② NGỜ** | Trụ Implant / phôi sứ / khay niềng **có chính hãng không**? Bác sĩ có giỏi? Giá có ẩn? Hỏng ai bảo hành? | **Straumann** (top 1) · **Invisalign Black Diamond** · **Nacera** · **Ormco Diamond Star** · 100% BS ĐH Y có chứng chỉ hành nghề · GP Sở Y tế |
| **③ NGẠI** | Điều trị nhiều buổi, đi lại nhiều lần, chi phí lớn. | Lộ trình rõ số buổi · trả góp · 7 cơ sở · đặt lịch linh hoạt |

> ⚠ **Rào NGỜ ở nha khoa nặng hơn hẳn thẩm mỹ** — khách **không tự kiểm tra được vật liệu nằm trong miệng mình**. Đây là lý do cụm **C03 (vật liệu)** và **C14 (thực thể, kiểm chứng)** được đẩy lên **Tầng A** ở các bộ Implant · Invisalign · Răng sứ.
>
> Nghịch lý phải nhớ: **bằng chứng mạnh nhất của Paris (đối tác hãng) cũng là rào pháp lý dễ sai nhất (R7)** — chữ *"chính hãng"* chỉ dùng cho đúng 4 hãng trên.

---

## Trục 6 bước

```
① Chọn lĩnh vực  →  ② Đối tượng KH  →  ③ Giai đoạn hành trình (S1–S6)
        →  ④ Cụm truy vấn (từ khoá)  →  ⑤ Cụm nội dung (bài viết)  →  ⑥ GEO/SEO
```

Mọi bài viết trong kế hoạch phải **truy ngược được** về một cụm truy vấn → một giai đoạn → một rào cản của một đối tượng thật. Bài nào không truy ngược được → loại khỏi kế hoạch.

**6 giai đoạn:** S1 Nhận biết · S2 Tìm hiểu · **S3 Cân nhắc & nỗi sợ ★★★ (điểm quyết định, ~50% điểm ưu tiên)** · S4 Thực hiện · S5 Trải nghiệm & hậu điều trị · S6 Gắn bó & mở rộng.

**S6 của nha khoa mạnh hơn hẳn thẩm mỹ** — một khách hài lòng thường kéo cả gia đình. Gói gia đình & nha khoa trẻ em là hướng LTV tự nhiên.

---

## Kho dữ liệu

**10 bộ dịch vụ · 150 cụm chủ đề · 389 bài viết cần sản xuất · 2.550 truy vấn đã phân loại**

| Business line | Bộ dịch vụ | Bài |
|---|---|---|
| **BRAND** · Thương hiệu tổng | Thương hiệu Nha khoa Paris | 34 |
| **NKI** · Implant & Phục hình mất răng | Trồng răng Implant · All-On 4/6 | 77 |
| **NKC** · Chỉnh nha — Niềng răng | Mắc cài (kim loại · sứ · pha lê · mặt trong) · Invisalign | 75 |
| **NKT** · Nha khoa thẩm mỹ | Bọc răng sứ & toàn hàm · Mặt dán Veneer | 81 |
| **NKG** · Nha khoa tổng quát & Nha chu | Nhổ răng · trám · tuỷ · cạo vôi · tẩy trắng · Nha chu & viêm nướu | 82 |
| **NKF** · Nha khoa trẻ em & Gia đình | Nha khoa trẻ em & gói Teeth Spa gia đình | 40 |
| | **TỔNG** | **389** |

Cộng thêm **7 trang local** cho 7 hub có cơ sở thật.

---

## Kiến trúc 3 tầng

- **Bộ não:** [`SYSTEM-PROMPT.md`](SYSTEM-PROMPT.md) — dán vào ô Chỉ dẫn/Instructions.
- **Tri thức:** [`knowledge/`](knowledge/) — 6 file `.md` upload vào Knowledge.
- **Dữ liệu nguồn:** [`data/bo-truy-van/`](data/bo-truy-van/) — 10 file JSON cấp **cụm** (15 cụm C01–C15 mỗi bộ) · [`data/truy-van/`](data/truy-van/) — JSON cấp **truy vấn** (17 dòng mỗi cụm).

Bộ não biết *cách làm*; knowledge cấp *dữ liệu + luật*; file JSON là *nguồn sự thật về khối lượng* — sửa JSON rồi chạy lại `tools/build-index.py`.

---

## Bộ truy vấn GEO — 10 bộ · 6 sheet mỗi bộ

[`doc/BotruyvanGEO-Paris/`](doc/BotruyvanGEO-Paris/) — sinh tự động bằng `tools/build-botruyvan.py`, theo **mẫu chuẩn 6 sheet** của bộ Kangnam (`HCI-Knowledge/KN-BotruyvanGEO/`):

| Sheet | Nội dung | Ai dùng |
|---|---|---|
| `1. Hướng dẫn` | Insight · phân bổ 80/20 · nhóm đối tượng · cách dùng 6 sheet · 6 quy tắc viết | Leader |
| `2. Hành vi KH` | 6 giai đoạn S1–S6: khách nghĩ gì · nỗi sợ · khát khao · trigger · Paris phải có gì | Content · Tư vấn |
| `3. Bộ truy vấn Master` | **255 truy vấn × 17 cột** + khối xếp hạng 15 cụm. Nguồn sự thật | SEO · Content |
| `4. Bản đồ nội dung` | Cụm → dạng bài → trang đích → sóng → phụ trách → trạng thái | Manager |
| `5. Prompt đo lường` | 20 prompt đo Share of Voice trong AI, có cột ChatGPT/Gemini/AI-ov | SEO lead |
| `6. Rào pháp lý` | R0–R13, **tự đếm** số truy vấn và CORE chịu từng rào | Pháp chế |

**Trạng thái nội dung:**

| Bộ | Truy vấn đã viết | Ghi chú |
|---|---|---|
| `02-implant.xlsx` | **255 / 255** ✅ | Bộ mẫu chuẩn — dùng làm khuôn khi viết 9 bộ còn lại |
| 9 bộ còn lại | 0 / 255 | Đủ 6 sheet; sheet 3 đã điền sẵn mọi cột suy ra được (cụm · giai đoạn · nhiệt độ · ưu tiên · tầng · điểm · rào · trang đích · đối tượng), chỉ trống cột **TRUY VẤN** và **KHỐI TRẢ LỜI** |

Viết thêm một bộ: tạo `data/truy-van/<key>.json` theo đúng cấu trúc của `implant.json` rồi chạy `python tools/build-botruyvan.py --scope <key>`.

> ⚠ **CƠ HỘI GEO = 1 cho mọi cụm** vì Paris chưa có mốc traffic AI. Sau tháng Setup đo xong mốc gốc thì phải chấm lại 1–3 và chạy lại script.

---

## Quick start (3 bước)

**Ba chuỗi cần dán:**

| Ô trên nền tảng | Dán gì |
|---|---|
| **Tên / Name** | `Agent-PR-GEO-Plant` |
| **Mô tả / Description** | *Chuyên gia nghiên cứu và lập kế hoạch triển khai SEO/GEO cho thương hiệu Nha khoa Paris (nhakhoaparis.vn). Xuất kế hoạch theo tháng dưới dạng file Excel 2 TAB: KPI + Công việc triển khai.* |
| **Chỉ dẫn / Instructions** | Khối giữa hai vạch ▼▲ trong [`SYSTEM-PROMPT.md`](SYSTEM-PROMPT.md) |

1. **Instructions:** dán toàn bộ khối giữa hai vạch ▼▲ trong [`SYSTEM-PROMPT.md`](SYSTEM-PROMPT.md).
2. **Knowledge:** upload 6 file `.md` trong [`knowledge/`](knowledge/).
3. **Template:** upload **2 file mẫu** trong [`template/`](template/) — [`GEO-PLAN-MAU-6-THANG.xlsx`](template/GEO-PLAN-MAU-6-THANG.xlsx) cho đầu ra A (kế hoạch 2 TAB) và [`BO-TRUY-VAN-MAU-6-SHEET.xlsx`](template/BO-TRUY-VAN-MAU-6-SHEET.xlsx) cho đầu ra B (bộ truy vấn 6 sheet).

→ Chi tiết từng nền tảng + smoke test: [doc/01-cai-dat.md](doc/01-cai-dat.md)

**Câu lệnh đầu tiên để test:**

```
Bạn là ai, làm được gì? Nêu trục 6 bước, ba rào cản chốt của khách nha khoa,
và cho biết Nha khoa Paris có bao nhiêu bài cần sản xuất.
```

**Câu lệnh lập kế hoạch:**

```
Lập kế hoạch GEO toàn hệ thống Nha khoa Paris trong 6 tháng, bắt đầu từ tháng 01/2027.
Xuất file 2 TAB theo mẫu.
```

→ Thư viện prompt mẫu đầy đủ: [doc/02-cau-lenh.md](doc/02-cau-lenh.md)
→ **Trang hướng dẫn tra cứu nhanh (bấm Copy từng prompt):** https://claude.ai/artifact/1P7KAhxMwAzoBEMi2TqsYo — mã nguồn tại [artifact/huong-dan-su-dung.html](artifact/huong-dan-su-dung.html)

---

## Đầu ra — 2 TAB

| TAB | Nội dung |
|---|---|
| **`BẢNG TỔNG QUAN KPI`** | 5 trụ cột (Hạ tầng 0,10 · Sản lượng 0,20 · SEO&GEO 0,40 · Traffic 0,15 · Lead 0,15) × từng business line × từng tháng. Số cột tháng co giãn theo chu kỳ. |
| **`CÔNG VIỆC TRIỂN KHAI`** | Bảng giao việc: `Mã KPI · Trụ cột · Hạng mục · Tháng · CHỈ TIÊU (số bài) · Trong đó CORE · Công việc chi tiết · Người phụ trách · Hạn chót · Hoàn thành`. Ba cấp dòng: chi tiết → `▶ TỔNG business line` → `★ TỔNG SẢN LƯỢNG THÁNG`. |

**Màu bám bộ nhận diện Paris:** Cerulean Blue `#2A52BE` · Pantone Red 032 C `#ED2E38` · White — tỷ lệ **80% trắng/kem · 15% xanh · 5% đỏ**. Đỏ **chỉ** dùng cho dòng `★ TỔNG SẢN LƯỢNG THÁNG`.

Xem output mẫu có số thật: [doc/03-output-mau.md](doc/03-output-mau.md)

---

## Công cụ

```bash
pip install openpyxl

python tools/build-index.py                                    # sinh lại chỉ mục knowledge từ JSON
python tools/build-geo-plan.py --start 2027-01 --months 6      # sinh file kế hoạch 2 TAB
python tools/build-geo-plan.py --start 2026-11 --months 4 --scope implant,allon,invisalign
python tools/build-geo-plan.py --start 2027-01 --months 12 --tiers A,B,C -o ke-hoach-2027.xlsx

python tools/build-botruyvan.py                 # sinh 10 bộ truy vấn .xlsx 6 sheet
python tools/build-botruyvan.py --scope implant # chỉ một bộ
python tools/build-artifact.py                  # sinh lại trang hướng dẫn HTML
```

`build-index.py` tự soát ba bất biến của mỗi bộ và **dừng nếu lệch**: đúng 15 cụm C01–C15 · tổng % điểm = 100 · phân bổ tầng A/B/C/D = 5/5/3/2.

---

## Tài liệu

| File | Nội dung |
|---|---|
| [SYSTEM-PROMPT.md](SYSTEM-PROMPT.md) | Bộ não Agent — 17 mục, dán vào Instructions |
| [knowledge/geo-phuong-phap-luan.md](knowledge/geo-phuong-phap-luan.md) | Trục 6 bước · S1–S6 · ba rào cản SỢ·NGỜ·NGẠI · 80/20 · 7 nhóm mở rộng · quy tắc rải tháng |
| [knowledge/geo-bo-truy-van-index.md](knowledge/geo-bo-truy-van-index.md) | Chỉ mục 10 bộ · 150 cụm · 389 bài *(sinh tự động)* |
| [knowledge/paris-brand-geo.md](knowledge/paris-brand-geo.md) | Paris là ai · 6 business line · 7 cơ sở · 3 bác sĩ có hồ sơ · 4 hãng đối tác · khoảng trống dữ liệu traffic |
| [knowledge/geo-kpi-framework.md](knowledge/geo-kpi-framework.md) | 5 trụ cột KPI · cách đặt chỉ tiêu khi chưa có mốc gốc · 3 bộ prompt đo GEO · 17 mã KPI nền |
| [knowledge/geo-output-excel-schema.md](knowledge/geo-output-excel-schema.md) | Khoá format 2 TAB + bảng màu Paris |
| [knowledge/geo-rao-phap-ly.md](knowledge/geo-rao-phap-ly.md) | 14 rào R0–R13 · bảng ánh xạ cụm → rào |
| [doc/01-cai-dat.md](doc/01-cai-dat.md) | Cài Gemini/ChatGPT/Claude · chiến lược file · smoke test · xử lý sự cố |
| [doc/02-cau-lenh.md](doc/02-cau-lenh.md) | Công thức ra lệnh · 14 prompt mẫu · điều Agent sẽ từ chối |
| [doc/03-output-mau.md](doc/03-output-mau.md) | Output mẫu có số thật · dấu hiệu đúng/sai |
| [doc/CHANGELOG.md](doc/CHANGELOG.md) | Lịch sử cập nhật · việc còn treo |
| [artifact/huong-dan-su-dung.html](artifact/huong-dan-su-dung.html) | Mã nguồn trang hướng dẫn + thư viện 18 prompt mẫu. GitHub không render HTML — xem bản đã publish tại [claude.ai/artifact/1P7KAhxMwAzoBEMi2TqsYo](https://claude.ai/artifact/1P7KAhxMwAzoBEMi2TqsYo), hoặc tải file về mở bằng trình duyệt |

---

## Cấu trúc repo

```
SYSTEM-PROMPT.md       Bộ não Agent
knowledge/             6 file tri thức (.md) — upload vào Knowledge
data/bo-truy-van/      10 bộ truy vấn cấp CỤM (.json) — NGUỒN SỰ THẬT về khối lượng
data/truy-van/         Truy vấn chi tiết từng dòng (.json) — hiện có bộ implant
doc/BotruyvanGEO-Paris/ 10 bộ truy vấn .xlsx 6 sheet (sinh tự động)
doc/                   Hướng dẫn cài đặt · câu lệnh · output mẫu · changelog
template/              2 file mẫu Excel (sinh từ script): kế hoạch 2 TAB + bộ truy vấn 6 sheet
tools/                 build-index.py · build-geo-plan.py · build-botruyvan.py · build-artifact.py
artifact/              Trang HTML hướng dẫn sử dụng + prompt mẫu
```

---

## Khoảng trống dữ liệu — phải biết trước khi dùng

> ⚠ **Nha khoa Paris CHƯA cung cấp bất kỳ số GA4, thứ hạng từ khoá hay số lead nào.** Agent được thiết kế để **nói rõ điều này** thay vì lấp bảng bằng số bịa.

| Hạng mục | Ảnh hưởng |
|---|---|
| Traffic AI & organic hiện tại | Trụ cột KPI 4 chỉ đặt được % tăng trưởng |
| Thứ hạng từ khoá Top 3/5/10 | Trụ cột KPI 3 không có mốc gốc |
| Số lead / sđt xác nhận / KH đến phòng khám | Trụ cột KPI 5 không có mốc gốc |
| Landing page nào đang hút traffic AI | **Cơ hội GEO của mọi cụm = 1** → thứ tự ưu tiên hiện dựa trên rào cản khách, chưa hiệu chỉnh bằng traffic thật |
| Địa chỉ + SĐT + số giấy phép từng cơ sở | Trang local bị chặn bởi rào **R3** cho tới khi lấy từ `/tim-phong-kham.html` |
| Danh sách bác sĩ nha chu & nha khoa trẻ em | Cụm C14 của 2 bộ `nhachu`, `trenem` bị chặn bởi rào **R4** |
| Văn bản chứng minh đối tác 4 hãng | Chữ "chính hãng" bị chặn bởi rào **R7** |

**Hệ quả:** tháng Setup của mọi chu kỳ là **tháng lấy mốc gốc**, không đặt chỉ tiêu tăng trưởng. Sau tháng Setup, chạy lại bước ④ để xếp lại Cơ hội GEO theo traffic thật.

---

## Ranh giới — Agent sẽ cảnh báo, không im lặng làm theo

Không cam kết tuyệt đối/100%/vĩnh viễn/trọn đời/không đau (**R1**) · không hạ thấp đối thủ, không phán xét nơi khách từng làm (**R6**) · không gắn bác sĩ ngoài 3 người có hồ sơ (**R4**) · không gắn số giấy phép Hà Nội cho trang local tỉnh khác (**R3**) · không dùng ảnh/case khách chưa có văn bản đồng ý (**R5**) · **không gắn chữ "chính hãng" cho vật liệu ngoài 4 hãng** (**R7**) · **không đưa con số giá / % ưu đãi / lãi suất vào kế hoạch** (**R12**) · không chẩn đoán qua ảnh, không báo giá ca cụ thể, không hứa thời gian điều trị cứng (**R13**) · **không bịa số liệu** — thiếu mốc gốc thì ghi `⚠ Cần xác minh từ Nha khoa Paris` và đề xuất % tăng trưởng.

*Quyết định cuối luôn thuộc người dùng.*
"# Agent-PR-GEO-Plant" 
