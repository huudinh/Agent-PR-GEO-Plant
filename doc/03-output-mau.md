# 03 · OUTPUT MẪU

File tham chiếu thật: [`template/GEO-PLAN-MAU-6-THANG.xlsx`](../template/GEO-PLAN-MAU-6-THANG.xlsx)
— sinh bằng `python tools/build-geo-plan.py --start 2027-01 --months 6`.

Quy mô bản mẫu: **10 bộ dịch vụ · 132 lát cụm · 388 bài nội dung + 7 trang local = 395 · 6 tháng · 6 business line · 163 đầu việc KPI.**

---

# 1. Agent trả lời trong chat trước khi xuất file

```
Phạm vi: 10 bộ dịch vụ · Tầng A+B+C · 6 tháng từ 01/2027

PHÂN TÍCH
Tổng khối lượng: 389 bài trên 150 cụm (388 bài ở Tầng A+B+C, 1 bài Tầng D đẩy backlog).
Tầng A chiếm 5 cụm/bộ nhưng ~50–55% điểm ưu tiên, hầu hết nằm ở giai đoạn S3 — điểm khách
quyết định. Rào cản chi phối ở S3 của ngành nha là NGỜ (vật liệu & tay nghề), nặng hơn hẳn
ngành thẩm mỹ, nên cụm C03 Vật liệu và C14 Thực thể được đẩy lên Tầng A ở 3 bộ Implant,
Invisalign, Răng sứ. Vì vậy 3 tháng đầu dồn toàn bộ Tầng A.

KẾT LUẬN
Rải được 61–69 bài/tháng, chênh lệch tháng cao/thấp 12% — đạt ràng buộc ≤25%.
Tầng A hết ở giữa tháng 4; từ tháng 5 CORE về 0 — đúng thiết kế 80/20.
C05 "khi nào KHÔNG nên làm" của 3 bộ Răng sứ · Implant · Niềng đã được nâng lên Sóng 1
để ra cùng Tầng A, vì đó là khác biệt E-E-A-T lớn nhất và đối thủ gần như không viết.

ĐỀ XUẤT
· T1 Setup: khoá 3 bộ prompt đo GEO lấy mốc gốc · tách kênh traffic AI trong GA4 ·
  đối chiếu sitemap chốt trang đích · xin GXNNDQC (R9) · thu văn bản đối tác 4 hãng (R7) ·
  lấy bảng giá & điều kiện trả góp hiện hành (R12)
· T2–T3 Tăng tốc: chạy hết Tầng A — C06 Mài răng/đau · C11 Hỏng & làm lại · C03 Vật liệu ·
  C07 Chi phí bóc tách · C14 Thực thể
· T4–T5 Đột phá: mở Tầng B, phủ hết 7 trang local hub, đẩy schema bác sĩ & LocalBusiness,
  xếp lại Cơ hội GEO theo traffic thật đo được
· T6 Về đích: Tầng C chạy nền, hoàn thiện gói gia đình, tổng kết đo GEO, chốt backlog

GIẢ ĐỊNH & DỮ LIỆU CÒN THIẾU
· Năng lực đội đủ cho ~65 bài/tháng — cần xác nhận
· ⚠ Paris CHƯA cung cấp bất kỳ số GA4, thứ hạng từ khoá hay số lead nào
  → trụ cột KPI 3, 4, 5 chỉ đặt được % tăng trưởng; cột "Hiện tại" để ⚠ Cần xác minh
  → Cơ hội GEO của mọi cụm lấy mặc định = 1; thứ tự ưu tiên hiện dựa trên rào cản khách,
    chưa hiệu chỉnh bằng traffic thật
· ⚠ Địa chỉ + SĐT + số giấy phép từng cơ sở: phải lấy tại /tim-phong-kham.html khi chạy (R3)
· ⚠ Chưa có bác sĩ gán được cho 2 bộ Nha chu và Nha khoa trẻ em → cụm C14 của 2 bộ này
  bị chặn bởi R4

Xác nhận để tôi xuất file 2 TAB? (ok/sửa)
```

> **Đây là phần quan trọng nhất của output.** Agent phải nêu khoảng trống dữ liệu **trước** khi xuất file, không để người dùng tự phát hiện sau.

---

# 2. TAB 1 — `BẢNG TỔNG QUAN KPI`

Trích thật từ file mẫu:

| TRỤ CỘT KPI | HẠNG MỤC | Số lượng | Hiện tại | T01 | T02 | T03 | T04 | T05 | T06 | TRỌNG SỐ |
|---|---|---|---|---|---|---|---|---|---|---|
| 1. Hạ tầng Web & Hub | Kiến trúc hệ thống & UI/UX các chuyên khoa | | ⚠ Cần xác minh | | | | | | | **0,10** |
| | Phân line chuyên khoa & Cổng Hub liên kết | | ⚠ Cần xác minh | | | | | | | |
| 2. Sản lượng Bài viết | BRAND · Thương hiệu tổng | 34 | — | 6 | 6 | 6 | 6 | 5 | 5 | **0,20** |
| | NKI · Implant & Phục hình mất răng | 77 | — | 13 | 13 | 13 | 13 | 13 | 12 | |
| | NKC · Chỉnh nha — Niềng răng | 75 | — | 13 | 13 | 13 | 12 | 12 | 12 | |
| | NKT · Nha khoa thẩm mỹ | 81 | — | 14 | 14 | 14 | 13 | 13 | 13 | |
| | NKG · Nha khoa tổng quát & Nha chu | 82 | — | 14 | 14 | 14 | 14 | 13 | 13 | |
| | NKF · Nha khoa trẻ em & Gia đình | 39 | — | 7 | 7 | 7 | 6 | 6 | 6 | |
| | Trang local — 7 hub cơ sở | 7 | — | 2 | 2 | 2 | 1 | 0 | 0 | |
| 3. SEO & GEO AI Search | NKI · Implant… · *Top 3* | | ⚠ Cần xác minh | | | | | | | **0,40** |
| | NKI · Implant… · *ChatGPT* | | ⚠ Cần xác minh | | | | | | | |
| 4. Traffic | NKI · Implant… · *google.com.vn* | | ⚠ Cần xác minh | | | | | | | **0,15** |
| | NKI · Implant… · *Traffic AI* | | ⚠ Cần xác minh | | | | | | | |
| 5. Form Lead & Chuyển đổi | NKI · Implant & Phục hình mất răng | | ⚠ Cần xác minh | | | | | | | **0,15** |
| | *Công cụ kiểm tra răng online (micro-conversion)* | | ⚠ Cần xác minh | | | | | | | |

Hai dòng cuối:

| | | T01 | T02 | T03 | T04 | T05 | T06 | Tổng |
|---|---|---|---|---|---|---|---|---|
| **TRỌNG SỐ ĐÁNH GIÁ THÁNG** | Tỷ trọng hoàn thành theo tháng | 0,129 | 0,161 | 0,161 | 0,194 | 0,194 | 0,161 | **1,00** |
| **TỔNG TRỌNG SỐ DANH MỤC** | Giai đoạn | Setup | Tăng tốc | Tăng tốc | Đột phá | Đột phá | Về đích | **1,00** |

> **Đọc đúng bảng:** chỉ trụ cột 2 có số tuyệt đối, vì số đó **tính được** từ bản đồ nội dung.
> Ba trụ cột còn lại để `⚠ Cần xác minh từ Nha khoa Paris` cho tới khi có mốc gốc thật — **đây là cố ý, không phải thiếu sót**. Paris hiện chưa cung cấp số GA4 nào.
>
> Dòng `Trang local` giảm về 0 từ T05 là **đúng thiết kế**: đã phủ đủ 7 hub có cơ sở thật, tháng sau chuyển sang rà soát & tối ưu chứ không sinh thêm trang tỉnh không có cơ sở (rào **R3**).

---

# 3. TAB 2 — `CÔNG VIỆC TRIỂN KHAI`

```
════  THÁNG 1/2027  ·  giai đoạn SETUP  ·  hạn chót 31/01/2027  ════
```

| Mã KPI | Trụ cột | Hạng mục | Tháng | CHỈ TIÊU | CORE | Người phụ trách |
|---|---|---|---|---|---|---|
| KPI-01 | 1. Hạ tầng Web & Hub | Kiến trúc hệ thống & UI/UX các chuyên khoa | Tháng 1 | | | Team Tech/Dev |
| KPI-03 | 2. Tuyến nội dung theo hành trình | Quy chuẩn loại bài + checklist R1 & R7 | Tháng 1 | | | Team Content |
| KPI-06.2 | 3. Sản lượng — NKI · Implant & Phục hình | Trồng răng Implant | Tháng 1 | 9 | 9 | Team Content |
| **KPI-06** | 3. Sản lượng — NKI · Implant & Phục hình | **▶ TỔNG NKI · IMPLANT & PHỤC HÌNH MẤT RĂNG** | Tháng 1 | **13** | **13** | Lead Content |
| KPI-11 | 3. Sản lượng — Trang local | Hub cơ sở: Hà Nội · Hải Phòng | Tháng 1 | 2 | 2 | Team Content/SEO |
| **KPI-TỔNG** | 3. Sản lượng Bài viết | **★ TỔNG SẢN LƯỢNG THÁNG (toàn hệ thống)** | Tháng 1 | **69** | **69** | Lead Content/SEO |
| KPI-14 | 4. SEO & GEO AI Search | Đo GEO — 3 bộ prompt (20 dịch vụ · 7 hub · 10 thương hiệu) | Tháng 1 | | | Team SEO/GEO |
| KPI-17 | 0. Pháp lý | GXNNDQC (R9) · văn bản đối tác 4 hãng (R7) · bảng giá hiện hành (R12) | Tháng 1 | | | Pháp chế |

## Cột `Công việc chi tiết` — đây là nơi phương pháp luận thành hành động

Nội dung **thật** của ô `KPI-08.1` tháng 1 (bộ Bọc răng sứ):

> Sản xuất theo bản đồ nội dung: **C06 Mài răng, chết tuỷ & biến chứng không hồi phục** (Tầng A · S3 · **gỡ rào SỢ** · 9 bài → MỚI: `/kien-thuc/rang-su/boc-rang-su-co-hai-khong/`). Áp 6 quy tắc trích dẫn AI (BLUF · có số · phủ 8 góc hỏi · nói cả điều bất lợi · ngày cập nhật + BS thẩm định · không nhồi từ khoá). **Soát rào: R1 · R9.** Duyệt 2 lớp BS + Pháp chế.

Nội dung **thật** của ô `KPI-11` tháng 1 (trang local):

> Dựng 2 trang local chuẩn NAP cho **Hà Nội · Hải Phòng** — **LẤY địa chỉ, SĐT và SỐ GIẤY PHÉP CỦA CHÍNH CƠ SỞ ĐÓ tại `/tim-phong-kham.html` ngay tại thời điểm chạy**; nêu đúng phạm vi chuyên môn, kỹ thuật ngoài phạm vi thì ghi rõ điều hướng về cơ sở thực hiện; gắn schema LocalBusiness/Dentist (**R3 · R2**)

Nội dung **thật** của ô `KPI-17` tháng Setup:

> **BA ĐẦU VIỆC CHẶN TIẾN ĐỘ, phải xong trong tháng Setup:** ① Lập danh mục nội dung quảng cáo dịch vụ KCB cần GXNNDQC, nộp Sở Y tế trước chiến dịch — R9 chạm phần lớn cụm Tầng A. ② Thu thập văn bản chứng minh quan hệ đối tác Straumann · Invisalign · Nacera · Ormco để dùng chữ "chính hãng" an toàn (**R7**). ③ Lấy bảng giá min–max + điều kiện & lãi suất trả góp hiện hành từ trang bảng giá; **KHÔNG đưa con số vào kế hoạch**, chỉ chốt quy trình cập nhật (**R12**).

Mỗi ô trả lời được bốn câu: **làm gì · cho cụm nào (mã + tầng + giai đoạn) · gỡ rào cản nào (SỢ/NGỜ/NGẠI) · rào pháp lý nào.**

## Panel phụ bên phải (cột L–M)

| | |
|---|---|
| **TỔNG SẢN LƯỢNG THEO THÁNG** *(nền đỏ `#ED2E38`)* | |
| Tháng 1 … Tháng 6 | 69 · 69 · 69 · 65 · 62 · 61 |
| TỔNG CHU KỲ | **395** |
| **THỐNG KÊ TIẾN ĐỘ** *(nền xanh đậm `#0C1D4D`)* | |
| Tổng số đầu việc KPI | 163 |
| Đã hoàn thành / Chưa hoàn thành / Tiến độ | 0 / 163 / 0% |

---

# 4. Năm dấu hiệu output ĐÚNG

1. **CORE giảm dần theo tháng** — T1 `69/69` → T3 `69/68` → T4 `65/33` → T5 `62/0` → T6 `61/0`. Tầng A dồn đầu chu kỳ đúng luật 80/20. Nếu CORE rải đều mọi tháng → sai.
2. **Mọi business line có mặt mọi tháng** — không dồn một line vào một tháng (§9 quy tắc 4).
3. **Mọi ô `Công việc chi tiết` có mã cụm + rào cản + mã rào pháp lý** — không có ô nào chỉ ghi "viết bài SEO".
4. **Màu đỏ `#ED2E38` chỉ xuất hiện 6 lần** (một dòng `★` mỗi tháng) + 1 header panel — đúng tỷ lệ 5% của bộ nhận diện Paris.
5. **Tháng Setup có đủ KPI-17 với cả ba việc R9 · R7 · R12**, và KPI-14 ghi rõ "ĐÂY LÀ MỐC GỐC, không đặt chỉ tiêu tăng trưởng".

# 5. Sáu dấu hiệu output SAI

1. Cột `Hiện tại` của trụ cột 3/4/5 có **số tuyệt đối** mà Paris chưa cung cấp → **bịa số**.
2. **Bất kỳ con số giá, % ưu đãi hay lãi suất trả góp nào xuất hiện trong file** → vi phạm **R12**.
3. Chữ **"chính hãng"** gắn cho vật liệu ngoài Straumann · Invisalign · Nacera · Ormco → vi phạm **R7**.
4. Tháng Setup thiếu đầu việc xin GXNNDQC hoặc thiếu việc khoá bộ đo GEO → mất mốc gốc và tắc pháp lý giữa chu kỳ.
5. Có tên bác sĩ ngoài 3 người có hồ sơ, hoặc gắn bác sĩ vào bộ Nha chu / Trẻ em → vi phạm **R4**.
6. Có trang local cho tỉnh **không có cơ sở** (Cần Thơ, Thanh Hoá, Bình Định…), hoặc gắn giấy phép `2032/HNO-GPHĐ/CL1` cho trang tỉnh khác → vi phạm **R3**.
