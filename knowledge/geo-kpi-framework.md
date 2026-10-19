# KHUNG KPI GEO — 5 TRỤ CỘT & CÁCH ĐẶT CHỈ TIÊU · NHA KHOA PARIS

Version: 1.0 · Agent dùng file này để **đặt số** cho TAB KPI. Nguyên tắc xuyên suốt: **tính được thì đưa số, không tính được thì đề xuất mức tăng trưởng %, tuyệt đối không bịa số tuyệt đối.**

---

# 1. NĂM TRỤ CỘT & TRỌNG SỐ

| # | Trụ cột KPI | Bản chất đo | Trọng số mặc định | Nguồn số |
|---|---|---|---|---|
| 1 | **Hạ tầng Web & Hub** | Kiến trúc theo chuyên khoa · cổng Hub liên kết · schema · tải trang <2s | **0,10** | Team Tech/Dev |
| 2 | **Sản lượng Bài viết** | Số bài hoàn thành/tháng theo từng business line | **0,20** | ✅ Tính được từ `geo-bo-truy-van-index.md` |
| 3 | **SEO & GEO AI Search** | Top 3/5/10 Google + tỷ lệ được nhắc trên ChatGPT · Gemini · AI Overview | **0,40** | Rank tracker + 3 bộ prompt đo GEO |
| 4 | **Traffic** | Organic `google.com.vn` + **Traffic AI** (referral từ LLM) | **0,15** | GA4 |
| 5 | **Form Lead** | Số lead · sđt xác nhận có nhu cầu · KH đến phòng khám · doanh số | **0,15** | CRM |
| | **Tổng** | | **1,00** | |

Trọng số điều chỉnh được theo mục tiêu kỳ. Nếu người dùng đổi trọng số → giữ tổng = 1,00 và ghi chú lý do.

**Trọng số đánh giá theo tháng** (chu kỳ 4 tháng): Setup **20%** · Tăng tốc **25%** · Đột phá **30%** · Về đích **25%**. Chu kỳ khác số tháng → chia lại theo cùng logic: tháng đầu thấp nhất, tháng áp chót cao nhất.

> ⚠ **Paris chưa có mốc gốc cho trụ cột 3, 4, 5** (xem `paris-brand-geo.md` §8). Đây là trạng thái **cố ý ghi nhận**, không phải thiếu sót của kế hoạch. Agent phải nêu rõ trong phần Giả định mỗi lần trình spec.

---

# 2. TRỤ CỘT 2 — SẢN LƯỢNG BÀI VIẾT (trụ cột duy nhất được phép đưa số tuyệt đối tự tính)

## 2.1 Nguồn khối lượng

`knowledge/geo-bo-truy-van-index.md` → cột **Bài** của từng cụm. Tổng kho: **389 bài** trên **150 cụm** của **10 bộ dịch vụ**.

| Business line | Bộ dịch vụ | Bài |
|---|---|---|
| BRAND · Thương hiệu tổng | Thương hiệu Nha khoa Paris | 34 |
| NKI · Implant & Phục hình mất răng | Implant · All-On 4/6 | 77 |
| NKC · Chỉnh nha — Niềng răng | Mắc cài · Invisalign | 75 |
| NKT · Nha khoa thẩm mỹ | Răng sứ · Veneer | 81 |
| NKG · Nha khoa tổng quát & Nha chu | Tổng quát · Nha chu | 82 |
| NKF · Nha khoa trẻ em & Gia đình | Trẻ em & gói gia đình | 40 |
| **TỔNG** | **10 bộ** | **389** |

Cộng thêm **trang local 7 hub cơ sở** — rải ~1–2 trang/tháng, tính vào sản lượng.

## 2.2 Quy trình quy đổi khối lượng → chỉ tiêu tháng

```
Bước 1: Lọc phạm vi          → người dùng chọn bộ dịch vụ nào vào kế hoạch
Bước 2: Lọc tầng              → mặc định Tầng A + B trong chu kỳ; C chạy nền; D đẩy backlog
Bước 3: Cộng số bài theo cụm  → ra tổng khối lượng chu kỳ
Bước 4: Rải theo sóng → tháng → áp §6.1 của geo-phuong-phap-luan.md
Bước 5: Cân bằng               → chênh lệch tháng cao/thấp ≤25% (trừ tháng Setup)
Bước 6: Gộp theo business line → BRAND · NKI · NKC · NKT · NKG · NKF để lên dòng KPI
```

## 2.3 Hệ số quy đổi nhân lực

| Nhóm | Loại bài | Độ dài | Hệ số |
|---|---|---|---|
| A1 | Bài trụ / chuyên sâu / trang pillar | 2.000–2.750 từ | **1,5** |
| A2 | Bài thường / tình huống / FAQ dài | 1.400–1.750 từ | **1,0** |
| A3 | Trang local / FAQ ngắn / khối nhúng | <1.400 từ | **0,5** |

**Điểm quy đổi tháng** = Σ(số bài × hệ số). Dùng để kiểm tra năng lực đội: nếu điểm quy đổi/tháng vượt năng lực đã biết → **cảnh báo và đề xuất giãn tiến độ, không im lặng nhận chỉ tiêu không khả thi**.

## 2.4 Phân nhóm dòng KPI sản lượng

Mỗi business line một dòng tổng, bên dưới là dòng chi tiết từng bộ:

- **NKI · NKC · NKT** — ba line trọng điểm, **tháng nào cũng phải có mặt**.
- **NKG** — cửa vào rẻ nhất, đối thủ bỏ trống nhiều nhất → chạy đều mọi tháng, không dồn.
- **NKF** — đòn bẩy LTV mạnh nhất của Paris (một khách kéo cả nhà) → gắn CRM/Zalo OA từ sớm.
- **BRAND** — ra trước mọi line vì cụm C14 là khối bằng chứng nuôi tất cả cụm còn lại.
- **Trang local** — chỉ 7 hub có cơ sở thật; trang "dịch vụ × tỉnh không có cơ sở" đẩy backlog (**R3**).

---

# 3. TRỤ CỘT 3 — SEO & GEO AI SEARCH (trọng số cao nhất 0,40)

## 3.1 Hai nhánh đo song song

**Nhánh A — Google Search truyền thống:** đếm số từ khoá ở Top 3 / Top 5 / Top 10 cho từng business line.

**Nhánh B — GEO AI Search (nhánh chiến lược):** đếm số truy vấn mà Nha khoa Paris **được nhắc tên** trên **ChatGPT · Gemini · Google AI Overview**.

## 3.2 Giao thức đo GEO — bắt buộc

1. Chế độ **ẩn danh**: không đăng nhập, tắt cá nhân hoá, xoá lịch sử phiên.
2. Dán **nguyên văn** prompt từ bộ đo đã khoá.
3. Ghi `1` nếu Paris được nhắc tên, `0` nếu không. **Ghi thêm đối thủ được AI nhắc.**
4. **Chạy 3 lần, lấy đa số.**
5. Nhân bản sheet đo mỗi tháng; **khoá bộ đo từ tháng Setup** để so sánh được cả chu kỳ.

**Ba bộ prompt vận hành của Paris** (xây trong tháng Setup):

| Bộ | Số prompt | Nội dung | Ví dụ |
|---|---|---|---|
| Dịch vụ trọng điểm | **20** | Bám cụm Tầng A của 6 line | *"trồng răng implant có đau không"* · *"bọc răng sứ có phải mài răng thật"* · *"niềng invisalign giá bao nhiêu"* |
| Hub cơ sở | **7** | Một prompt / tỉnh thành có cơ sở | *"nha khoa trồng implant tốt ở Đà Nẵng"* |
| Kiểm chứng thương hiệu | **10** | Câu khách hỏi để kiểm chứng Paris | *"nha khoa Paris có uy tín không"* · *"nha khoa Paris có giấy phép gì"* · *"trụ implant ở nha khoa Paris có chính hãng không"* |

> ⚠ **Bản chất dữ liệu:** kết quả AI thay đổi theo phiên — chỉ ~27% truy vấn con lặp lại giữa các lần chạy. Vì vậy KPI GEO là **KPI xu hướng theo tháng**, không phải con số tuyệt đối một lần. Khi trình bày, luôn kèm mốc gốc (baseline) của tháng đầu.

## 3.3 Đặt chỉ tiêu

Cần **số hiện tại** làm mốc. Paris chưa có → cột "Hiện tại" ghi `⚠ Cần xác minh từ Nha khoa Paris`, cột chỉ tiêu ghi **% tăng trưởng** thay vì số tuyệt đối. **Tháng Setup của mọi chu kỳ là tháng lấy mốc gốc, không đặt chỉ tiêu tăng trưởng.**

---

# 4. TRỤ CỘT 4 — TRAFFIC

Hai dòng cho mỗi business line:

- **`google.com.vn`** — organic traffic truyền thống.
- **Traffic AI** — phiên đến từ ChatGPT · Gemini · Claude · Perplexity · Brave.

**Mốc nền:** `⚠ Cần xác minh từ Nha khoa Paris` — chưa có dữ liệu GA4 nào được cung cấp cho bộ này.

**Chỉ tiêu phụ:** Time-on-site > 2,5 phút.

**Cách đặt chỉ tiêu Traffic AI khi chưa có mốc:**
1. Tháng Setup: **tách kênh traffic AI trong GA4** (ChatGPT · Gemini · Claude · Perplexity · Brave) và **ghi mốc gốc** — đây chính là chỉ tiêu của tháng Setup, không phải tăng trưởng.
2. Từ tháng 2: đặt chỉ tiêu theo **% tăng so với tháng trước**, dựa trên tốc độ tăng của chính Paris, **không lấy benchmark của thương hiệu khác**.
3. Dòng có mốc gốc = 0 → đặt chỉ tiêu **bậc thang nhỏ** và ghi rõ là **chỉ tiêu thăm dò**.

---

# 5. TRỤ CỘT 5 — FORM LEAD & CHUYỂN ĐỔI

Chuỗi đo: **Form lead → sđt xác nhận (có nhu cầu) → KH đến phòng khám → doanh số.**

Mỗi business line một dòng. Paris có thêm một bậc trước form: **công cụ kiểm tra răng miệng / niềng / răng sứ / trồng răng online** — đây là **micro-conversion** nên đo riêng, vì nó vừa là bước gỡ rào NGẠI vừa là điểm neo thực thể tốt cho cụm C01.

Ba mức sau form lead thường **chưa có số** → ghi `⚠ Cần xác minh từ Nha khoa Paris` và đề xuất tỷ lệ chuyển đổi mục tiêu thay vì số tuyệt đối.

---

# 6. BỐN GIAI ĐOẠN CỦA MỘT CHU KỲ

| Giai đoạn | Trọng số tháng | Việc đặc trưng |
|---|---|---|
| **Setup** | 20% | **Khoá 3 bộ prompt đo GEO lấy mốc gốc** · audit từ khoá · thiết lập GA4 + heatmap + tách kênh traffic AI · ban hành khung loại bài + **checklist 4 hãng (R7)** + checklist từ cấm (R1) · thiết lập tag theo line & hành trình · **đối chiếu sitemap thật để chốt trang đích** · **xin GXNNDQC (R9)** · lấy bảng giá & điều kiện trả góp hiện hành (R12) |
| **Tăng tốc** | 25% | Chạy hết Tầng A · C05 ra cùng Tầng A · thiết kế UI/UX các chuyên khoa · liên kết Hub ↔ landing · gắn thẻ 100% bài mới |
| **Đột phá** | 30% | Mở Tầng B · dựng trang local 7 hub · đẩy schema thực thể (`Dentist`, `LocalBusiness`) & bác sĩ (`IndividualPhysician`) · tối ưu bài đã đăng theo kết quả đo GEO · **xếp lại Cơ hội GEO của từng cụm theo traffic thật** |
| **Về đích** | 25% | Tầng C chạy nền · hoàn thiện cross-sell & gói gia đình · tổng kết đo GEO · chốt backlog kỳ sau |

---

# 7. DANH SÁCH ĐẦU VIỆC NỀN (luôn có trong mọi kế hoạch, không phụ thuộc bộ dịch vụ)

| Mã | Trụ cột | Hạng mục | Xuất hiện ở |
|---|---|---|---|
| KPI-01 | Hạ tầng | Kiến trúc hệ thống & UI/UX các chuyên khoa | Mọi tháng |
| KPI-02 | Hạ tầng | Phân line chuyên khoa & cổng Hub liên kết | Mọi tháng |
| KPI-03 | Tuyến nội dung | Quy chuẩn loại bài + checklist R1 & R7 | Setup, rồi duy trì |
| KPI-04 | Tuyến nội dung | Gắn thẻ tagging theo hành trình KH (S1–S6) | Setup, rồi 100% bài mới |
| KPI-05…10 | Sản lượng | Theo từng business line (BRAND · NKI · NKC · NKT · NKG · NKF) | Mọi tháng |
| KPI-11 | Sản lượng | Trang local 7 hub cơ sở | Mọi tháng |
| KPI-12 | Sản lượng | Quy trình biên tập & duyệt 2 lớp (BS + Pháp chế) | Mọi tháng |
| KPI-13 | SEO & GEO | Top từ khoá Google Search | Mọi tháng |
| KPI-14 | SEO & GEO | Đo GEO — 3 bộ prompt (20 dịch vụ · 7 hub · 10 thương hiệu) | Mọi tháng |
| KPI-15 | Traffic | Traffic & Time-on-site | Mọi tháng |
| KPI-16 | Chuyển đổi | Tỷ lệ chuyển đổi Lead + micro-conversion công cụ online | Mọi tháng |
| KPI-17 | Pháp lý | GXNNDQC (**R9**) · văn bản đối tác 4 hãng (**R7**) · bảng giá hiện hành (**R12**) | **Setup bắt buộc**, rồi duy trì |

Agent được phép thêm mã KPI-18+ khi phạm vi mở rộng, nhưng **không được bỏ** 17 mã nền này.
