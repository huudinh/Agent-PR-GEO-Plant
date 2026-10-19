# 02 · CÂU LỆNH & PROMPT MẪU

---

# 1. Công thức ra lệnh

```
Lập kế hoạch GEO cho [PHẠM VI] trong [SỐ THÁNG] tháng, bắt đầu từ [THÁNG/NĂM].
[Ràng buộc nếu có: năng lực đội, tầng ưu tiên, line trọng điểm]
```

**Ba thông tin bắt buộc:** phạm vi · số tháng · tháng bắt đầu. Thiếu → Agent sẽ hỏi lại.

**Giá trị hợp lệ của phạm vi:**

| Cách gọi | Nghĩa |
|---|---|
| `toàn hệ thống` | Cả 10 bộ dịch vụ · 389 bài |
| Tên business line | `BRAND` · `NKI` Implant & Phục hình · `NKC` Chỉnh nha · `NKT` Thẩm mỹ · `NKG` Tổng quát & Nha chu · `NKF` Trẻ em & Gia đình |
| Tên bộ dịch vụ | Thương hiệu · Implant · All-On 4/6 · Niềng mắc cài · Invisalign · Bọc răng sứ · Veneer · Nha khoa tổng quát · Nha chu · Nha khoa trẻ em |
| Một cụm xuyên bộ | ví dụ `chỉ cụm C11 Hỏng & làm lại của cả 10 bộ` |

---

# 2. Prompt mẫu theo tình huống

## 2.1 Kế hoạch toàn hệ thống

```
Lập kế hoạch GEO toàn hệ thống Nha khoa Paris trong 6 tháng, bắt đầu từ tháng 01/2027.
Xuất file 2 TAB theo mẫu.
```

## 2.2 Kế hoạch một business line

```
Lập kế hoạch GEO cho line NKI — Implant & Phục hình mất răng (2 bộ: Implant và All-On 4/6)
trong 4 tháng từ tháng 11/2026. Chỉ chạy Tầng A và B, Tầng C đẩy sang quý sau.
```

## 2.3 Kế hoạch dịch vụ giá trị lớn

```
Quý tới Paris muốn dồn lực vào 4 dịch vụ giá trị lớn: Implant, All-On 4/6, Invisalign,
răng sứ toàn hàm. Lập kế hoạch 3 tháng từ 01/2027, nêu rõ cụm nào bị đẩy sang backlog.
```

## 2.4 Kế hoạch có ràng buộc năng lực

```
Lập kế hoạch GEO 3 tháng từ 01/2027 cho line NKT — Nha khoa thẩm mỹ.
Đội content chỉ sản xuất được tối đa 20 bài/tháng — hãy cắt phạm vi cho khớp
và nói rõ cụm nào bị đẩy sang backlog, vì sao.
```

## 2.5 Kế hoạch ưu tiên một rào cản

```
Quý tới Paris muốn chiếm lĩnh toàn bộ chủ đề rào cản NGỜ về vật liệu trên AI Search
— trụ Implant, phôi sứ, khay Invisalign có chính hãng không.
Lập kế hoạch 3 tháng chỉ tập trung cụm C03 và C14 của cả 10 bộ.
```

## 2.6 Kế hoạch chiếm khoảng trống đối thủ

```
Lập kế hoạch 4 tháng từ 02/2027 cho hai bộ Nha khoa tổng quát và Nha chu
— hai bộ đối thủ bỏ trống nhiều nhất. Giải thích vì sao đáng làm dù doanh thu thấp.
```

## 2.7 Kế hoạch thương hiệu tổng (GEO Entity)

```
Lập kế hoạch 3 tháng chỉ cho bộ Thương hiệu tổng (01-thuonghieu),
mục tiêu để AI trả lời đúng "Nha khoa Paris là ai, có mấy cơ sở, có giấy phép gì,
vật liệu có chính hãng không".
```

## 2.8 Kế hoạch LTV / gói gia đình

```
Lập kế hoạch 4 tháng cho line NKF — Nha khoa trẻ em & Gia đình, từ 03/2027.
Mục tiêu: biến một khách hài lòng thành cả gia đình. Nêu rõ đầu việc nào gắn CRM/Zalo OA.
```

## 2.9 Kế hoạch trang local

```
Lập kế hoạch 4 tháng chỉ cho 7 trang cơ sở (Hà Nội, Hải Phòng, Quảng Ninh, Vinh,
Đà Nẵng, TP.HCM, Bình Dương) từ 01/2027. Nêu rõ dữ liệu nào phải lấy từ /tim-phong-kham.html
và rào pháp lý nào áp cho từng trang.
```

---

# 2B. Prompt sản xuất BỘ TRUY VẤN (đầu ra B — §18)

Đây là đầu ra thứ hai của Agent, **khác hẳn** kế hoạch tháng. Agent chỉ làm khi bạn yêu cầu rõ.

> Mỗi bộ cố định **15 cụm C01–C15 × 17 truy vấn = 255**. Agent mặc định làm **1 cụm/lượt** và báo còn cụm nào chưa làm. Đầu ra là **JSON** dán thẳng vào `data/truy-van/<key>.json`, rồi chạy `python tools/build-botruyvan.py --scope <key>`.

## 2B.1 Viết một cụm

```
Viết bộ truy vấn GEO cho cụm C06 của bộ Bọc răng sứ — đủ 17 truy vấn.
Xuất JSON đúng schema §18 để tôi dán vào data/truy-van/rangsu.json.
```

## 2B.2 Viết trọn Tầng A của một bộ

```
Viết bộ truy vấn GEO cho toàn bộ 5 cụm Tầng A của bộ Niềng răng mắc cài
(85 truy vấn). Xuất JSON theo schema §18, làm lần lượt từng cụm.
```

## 2B.3 Khởi tạo metadata cho bộ mới

```
Tôi muốn viết bộ truy vấn cho bộ Nha chu. Lấy data/truy-van/implant.json làm khuôn:
sinh trước phần metadata (doi_tuong_md, mo_ta_doi_tuong, hanh_vi, khuyen_nghi, ban_do)
cho bộ Nha chu, chưa cần viết truy vấn.
```

## 2B.4 Soát lại bộ đã viết

```
Soát cụm C06 bộ Implant theo self-review §18: có trộn câu dài/ngắn chưa,
phủ mấy góc hỏi, brief đã có số dạng dải và điều bất lợi chưa,
có truy vấn nào trùng ý không, có lọt số giá hay tên bác sĩ lạ không.
```

**Thứ tự đề xuất khi viết 9 bộ còn lại:** `rangsu` (47 bài, khoảng trống AI lớn nhất) → `niengmaccai` → `thuonghieu` (cụm C14 nuôi 9 bộ kia) → `invisalign` → `tongquat` → `allon` → `nhachu` → `veneer` → `trenem`.

---

# 3. Prompt hỏi đáp (không lập kế hoạch)

| Mục đích | Prompt |
|---|---|
| Hiểu ưu tiên | `Vì sao cụm C03 Vật liệu lại nằm Tầng A ở bộ Implant trong khi ở bộ Nha chu chỉ ở Tầng B?` |
| Brief một cụm | `Cho tôi brief sản xuất cụm C06 Mài răng & chết tuỷ của bộ Bọc răng sứ: cần bao nhiêu bài, dạng gì, trang đích nào, gỡ rào cản nào, rào pháp lý nào.` |
| Đối tượng khách | `Khách ở giai đoạn S3 của dịch vụ Invisalign đang sợ điều gì? Paris phải có nội dung gì để trả lời?` |
| Rào cản | `Ba rào cản chốt của khách nha khoa là gì? Rào nào nặng nhất và vì sao nặng hơn ngành thẩm mỹ?` |
| Đo lường | `Ba bộ prompt đo GEO của Paris gồm những gì? Chạy thế nào cho đúng giao thức?` |
| Pháp lý | `Rào R7 "chính hãng" áp cho những cụm nào? Phải có gì trong tay trước khi phát hành?` |
| Pháp lý | `Rào R12 nói gì về giá? Vì sao không được đưa số giá vào kế hoạch?` |
| Thương hiệu | `Paris có mấy cơ sở, ở đâu? Hub nào nằm trong phạm vi chu kỳ và vì sao tỉnh khác thì không?` |
| Bác sĩ | `Paris có mấy bác sĩ đã có hồ sơ xác minh? Gắn ai vào dịch vụ nào?` |
| Khoảng trống | `Bộ dịch vụ nào của Paris đang có khoảng trống AI lớn nhất? Vì sao nên lấp trước?` |
| Dữ liệu thiếu | `Những dữ liệu nào Paris chưa cung cấp và nó chặn trụ cột KPI nào?` |

---

# 4. Prompt tinh chỉnh sau khi có bản nháp

```
Giữ nguyên bản kế hoạch, chỉ đổi: dồn toàn bộ cụm C14 Thực thể vào tháng 1
vì cần schema bác sĩ và trang thực thể chạy trước mọi cụm khác.
```

```
Sản lượng tháng 1 đang 69 bài, quá tải. Giãn thành 8 tháng, giữ nguyên thứ tự ưu tiên.
```

```
Bổ sung cột "Trang đích" vào TAB Công việc triển khai, lấy từ bản đồ nội dung.
Đánh dấu rõ trang nào là MỚI và trang nào cần đối chiếu sitemap.
```

```
Tách riêng một dòng KPI cho micro-conversion của 4 công cụ kiểm tra online
(răng miệng, niềng, răng sứ, trồng răng).
```

> Agent chỉ nêu phần thay đổi, không in lại toàn bộ bảng trừ khi bạn yêu cầu.

---

# 5. Những gì Agent sẽ TỪ CHỐI hoặc CẢNH BÁO

| Yêu cầu | Phản hồi của Agent |
|---|---|
| "Đặt KPI traffic AI tháng 1 là 3.000 phiên" | Cảnh báo **không có mốc gốc nào** → đề xuất % tăng trưởng, ghi `⚠ Cần xác minh từ Nha khoa Paris` |
| "Giá implant 18 triệu, điền vào kế hoạch" | Từ chối — rào **R12**: giá là dữ liệu động, chỉ ghi đầu việc lấy dải giá tại thời điểm chạy |
| "Viết 'phôi sứ Zirconia chính hãng'" | Cảnh báo rào **R7** — Zirconia không nằm trong 4 hãng có hồ sơ; chỉ Straumann · Invisalign · Nacera · Ormco |
| "Ghi bác sĩ X phụ trách line Nha chu" | Kiểm tra danh sách; không có trong 3 hồ sơ → cảnh báo rào **R4** |
| "Thêm 'niềng không đau' vào tiêu đề bài" | Từ chối — rào **R1**; đề xuất "giảm cảm giác khó chịu nhờ công nghệ, bác sĩ theo dõi từng giai đoạn" |
| "So sánh Paris với [đối thủ] trong bài" | Từ chối nêu tên hạ thấp; đề xuất bộ tiêu chí khách quan (rào **R6**) |
| "Viết bài: khách này bọc sứ ở chỗ khác bị hỏng" | Cảnh báo rào **R6** — tuyệt đối không phán xét nơi cũ; viết theo hướng phương án xử lý |
| "Dựng trang local cho Cần Thơ, Thanh Hoá" | Cảnh báo ngoài phạm vi — Paris không có cơ sở ở đó; dựng trang local là chạm rào **R3** |
| "Gắn giấy phép 2032/HNO-GPHĐ/CL1 cho trang Đà Nẵng" | Từ chối — rào **R3**; mỗi cơ sở có giấy phép riêng do Sở Y tế tỉnh đó cấp |
| "Dự đoán răng của khách qua ảnh họ gửi" | Từ chối — rào **R13**: không chẩn đoán, không kê đơn, không báo giá ca cụ thể |
| "Hứa niềng xong trong 12 tháng" | Từ chối — rào **R13**; nêu **dải** thời gian, nói rõ phụ thuộc từng ca |
| "Bỏ qua bước đo GEO cho nhanh" | Cảnh báo mất mốc gốc → không đánh giá được tăng trưởng cả chu kỳ, và Paris hiện **chưa có số nào** nên bỏ bước này là mất trắng |
| "Làm Tầng B trước, Tầng A để sau" | Cảnh báo vi phạm 80/20; nêu đánh đổi rồi mới làm theo nếu bạn khẳng định lại |
