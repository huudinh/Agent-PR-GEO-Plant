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

Viết như đang nói chuyện với một người làm GEO có nghề. Không cần dùng mã nội bộ — Agent tự ánh xạ sang tầng, cụm, giai đoạn.

## 2.1 Toàn hệ thống

```
Tôi muốn làm kế hoạch GEO cho toàn bộ Nha khoa Paris trong 6 tháng, bắt đầu từ tháng 01/2027.
Xuất cho tôi file Excel gồm bảng KPI và bảng giao việc theo đúng mẫu.
```

## 2.2 Dồn lực một mảng dịch vụ

```
Quý này tôi muốn tập trung vào mảng trồng răng — cả Implant lẻ lẫn All-On toàn hàm —
trong 4 tháng từ tháng 11/2026. Làm các cụm quan trọng nhất trước,
phần xây uy tín giữ chân khách thì để sang quý sau.
```

## 2.3 Bốn dịch vụ doanh thu cao nhất

```
Quý tới chúng tôi muốn dồn lực vào 4 dịch vụ doanh thu cao nhất: Implant, All-On 4/6,
Invisalign và răng sứ toàn hàm. Làm kế hoạch 3 tháng từ 01/2027,
và nói rõ những gì phải cắt bỏ để đổi lấy việc dồn lực này.
```

## 2.4 Khi đội không kham nổi

```
Làm kế hoạch 3 tháng từ 01/2027 cho mảng nha khoa thẩm mỹ (răng sứ và Veneer).
Đội content của tôi chỉ viết được tối đa 20 bài mỗi tháng — hãy cắt phạm vi cho vừa sức,
và nói rõ phần nào phải để lại kỳ sau cùng lý do.
```

## 2.5 Chiếm một nỗi lo của khách

```
Khách của chúng tôi hay nghi ngờ chuyện vật liệu — trụ Implant, phôi sứ, khay niềng
có đúng hàng chính hãng không. Quý tới tôi muốn chiếm lĩnh đúng chủ đề này trên AI.
Làm kế hoạch 3 tháng, cắt ngang cả 10 dịch vụ, chỉ tập trung vật liệu và bằng chứng thương hiệu.
```

## 2.6 Chiếm khoảng trống đối thủ

```
Tôi thấy mảng nha khoa tổng quát và nha chu gần như không ai làm nội dung tử tế.
Làm kế hoạch 4 tháng từ 02/2027 cho hai mảng này,
và thuyết phục giúp tôi vì sao đáng đầu tư dù doanh thu hai mảng đó thấp.
```

## 2.7 Trang riêng cho 7 cơ sở

```
Tôi muốn làm trang riêng cho cả 7 cơ sở: Hà Nội, Hải Phòng, Quảng Ninh, Vinh,
Đà Nẵng, TP.HCM, Bình Dương. Làm kế hoạch 4 tháng từ 01/2027,
chỉ rõ thông tin nào bắt buộc phải lấy mới từ trang tìm phòng khám,
và mỗi trang phải tránh điều gì về pháp lý.
```

---

# 2B. Sản xuất BỘ TRUY VẤN (đầu ra B — §18)

Đây là đầu ra thứ hai của Agent, **khác hẳn** kế hoạch tháng. Bạn **nói chuyện bình thường**, không cần cú pháp — chỉ cần nêu tên dịch vụ bằng tiếng Việt thường ngày, Agent tự tra chỉ mục và tìm đúng bộ.

**Mặc định Agent trả về file Excel 6 tab.** Muốn JSON để chạy script thì nói thêm *"xuất JSON cho tôi chạy script"*.

## ⚠ Vì sao không có prompt nào ép Agent trả đủ 255 truy vấn một lượt

| | Số chữ |
|---|---|
| Một bộ đầy đủ 255 truy vấn (riêng cột truy vấn + brief) | **58.027 ký tự** |
| Một cụm 17 truy vấn | 3.868 ký tự — vừa đúng một lượt |

Không mô hình nào xuất 58.000 ký tự trong một lần trả lời. Đây **không phải lỗi prompt** — đổi câu chữ kiểu gì cũng không khác.

**Cách đúng: 1 cụm mỗi lượt, ~15 lượt là xong một bộ.** Agent phải báo khối lượng này **trước khi viết** (§18.0). Nếu nó im lặng trả file có sheet 3 gần trống rồi coi như xong thì là nó làm sai — nhắc lại §18.0.

**Hai đường tắt:**
① Xin **JSON** thay vì Excel (gọn hơn mỗi lượt), rồi chạy `python tools/build-botruyvan.py --scope <key>` để tự ghép thành file 6 sheet.
② Chỉ làm **5 cụm Tầng A** — 85 truy vấn, ~5 lượt. Phần này chiếm ~50% điểm ưu tiên và là việc của 90 ngày đầu; 10 cụm còn lại để kỳ sau.

## 2B.1 Câu ngắn nhất — chỉ cần thế này

```
Tạo bộ truy vấn Geo cho dịch vụ trồng răng đầy đủ 6 tab
```

Agent tự tra chỉ mục, tìm đúng bộ Implant, rồi trả lời đại ý: *"255 truy vấn, cần ~15 lượt, mỗi lượt 1 cụm. Bắt đầu từ cụm hạng 1 nhé?"* — rồi mới viết.

Không cần viết hoa đúng, không cần nhắc tên file mẫu, không cần nói "Implant" — gõ *trồng răng* là đủ.

## 2B.1b Khi Agent trả sai bố cục — nhắc thẳng tên file chuẩn

```
Tôi muốn làm bộ truy vấn GEO cho dịch vụ trồng răng Implant,
giống hệt cấu trúc chuẩn Mau-Truy-Van-Geo.xlsx.
Trước khi viết, cho tôi biết bộ này bao nhiêu truy vấn, cần mấy lượt mới xong,
và nên bắt đầu từ cụm nào.
```

Dùng khi file nhận được thiếu sheet hoặc sai thứ tự cột — nghĩa là Agent chưa đọc `template/Mau-Truy-Van-Geo.xlsx` trong Tri thức.

## 2B.1c Viết cụm đầu tiên

```
Bắt đầu đi. Viết đủ 17 truy vấn của cụm hạng 1,
rồi xuất file Excel 6 tab với cụm đó đã đầy.
```

Sheet 1·2·4·5·6 đầy ngay từ lần xuất đầu. Sheet 3 đầy ở cụm vừa viết, cụm chưa viết để `[CẦN VIẾT]`.

## 2B.2 Hỏi nên bắt đầu từ đâu

```
Tôi muốn làm bộ truy vấn GEO cho dịch vụ bọc răng sứ.
Bộ này gồm những cụm chủ đề nào, và nên viết cụm nào trước thì có lợi nhất?
```

## 2B.3 Viết tiếp cụm kế tiếp

```
Viết tiếp giúp tôi cụm kế tiếp của bộ này, rồi xuất lại file Excel đã cập nhật.
```

## 2B.4 Dựng phần nền trước khi viết truy vấn

```
Tôi muốn bắt đầu bộ truy vấn cho dịch vụ niềng răng.
Trước mắt dựng giúp tôi phần chân dung khách hàng, hành vi 6 giai đoạn
và bản đồ nội dung — chưa cần viết truy vấn vội.
```

## 2B.5 Soát lại cụm vừa viết

```
Soát lại cụm bạn vừa viết giúp tôi: đã trộn câu dài và câu ngắn chưa,
phủ được mấy góc hỏi, có truy vấn nào trùng ý nhau không,
và có lọt số giá hay tên bác sĩ nào chưa xác minh không?
```

## Tên dịch vụ — gõ kiểu gì Agent cũng hiểu

| Bạn nói | Agent hiểu là bộ |
|---|---|
| `trồng răng` · `implant` · `cấy ghép` | Trồng răng Implant |
| `bọc sứ` · `răng sứ` · `mão sứ` | Bọc răng sứ |
| `niềng` · `mắc cài` · `chỉnh nha` | Niềng răng mắc cài |
| `niềng trong suốt` · `khay` · `invisalign` | Invisalign |
| `mặt dán` · `dán sứ` · `veneer` | Mặt dán sứ Veneer |
| `toàn hàm` · `mất hết răng` · `all-on` | All-On 4/6 |
| `nhổ răng` · `trám` · `tuỷ` · `tẩy trắng` | Nha khoa tổng quát |
| `răng lung lay` · `viêm nướu` · `nha chu` | Nha chu & viêm nướu |
| `trẻ em` · `trẻ nhỏ` · `gia đình` | Nha khoa trẻ em |
| `thương hiệu` · `brand` · `Paris` | Thương hiệu Nha khoa Paris |

Tên không khớp bộ nào → Agent liệt kê 10 bộ cho bạn chọn, **không đoán bừa**.

## Lệnh tắt cho người quen việc

Không bắt buộc, chỉ để gõ nhanh: `tiếp` · `<số>` (chọn cụm theo hạng) · `soát` · `đổi bộ răng sứ`.

## Nếu bạn tự chạy script

Xin JSON thay vì Excel, dán vào `data/truy-van/<key>.json` rồi chạy:

```bash
python tools/build-botruyvan.py --scope implant
```

**Thứ tự đề xuất viết 9 bộ còn lại:** `răng sứ` (47 bài, khoảng trống AI lớn nhất) → `niềng` → `thương hiệu` (cụm C14 nuôi 9 bộ kia) → `invisalign` → `tổng quát` → `all-on` → `nha chu` → `veneer` → `trẻ em`.

---

# 3. Prompt hỏi đáp (không lập kế hoạch)

## 3.1 Brief giao việc cho đội content

```
Tôi sắp giao cho đội content viết về chuyện mài răng và chết tuỷ khi bọc sứ.
Cho tôi brief đầy đủ: cần bao nhiêu bài, dạng bài gì, đăng ở trang nào,
gỡ được nỗi lo nào của khách, và phải tránh gì về pháp lý.
```

## 3.2 Hiểu thứ tự ưu tiên

```
Vì sao chủ đề vật liệu lại được ưu tiên cao nhất ở Implant,
trong khi ở Nha chu thì xếp sau? Giải thích giúp tôi logic đằng sau.
```

## 3.3 Khách sắp quyết định thì sợ gì

```
Khách đang cân nhắc niềng Invisalign, gần quyết định rồi nhưng vẫn chần chừ.
Lúc đó họ sợ điều gì nhất, và Paris phải có sẵn nội dung gì để trả lời?
```

## 3.4 Đo xem AI có nhắc Paris không

```
Tôi muốn đo xem AI có nhắc tới Nha khoa Paris không.
Cần chuẩn bị những bộ câu hỏi nào, và chạy thế nào cho ra số liệu tin được?
```

## 3.5 Còn thiếu dữ liệu gì

```
Hiện còn thiếu những dữ liệu nào từ phía Nha khoa Paris,
và mỗi thứ thiếu đó đang làm kẹt phần nào của kế hoạch?
```

## 3.6 Các câu hỏi nhanh khác

| Mục đích | Hỏi thế nào |
|---|---|
| Rào cản khách | `Ba rào cản lớn nhất của khách nha khoa là gì, và cái nào nặng nhất?` |
| Chữ "chính hãng" | `Khi nào tôi được phép dùng chữ "chính hãng", và cần có gì trong tay trước đã?` |
| Giá | `Vì sao không được đưa số giá vào kế hoạch hay vào bài viết?` |
| Cơ sở | `Paris có mấy cơ sở, ở đâu? Tỉnh không có cơ sở thì làm nội dung kiểu gì?` |
| Bác sĩ | `Tôi được nhắc tên bác sĩ nào trong bài, và gắn ai vào dịch vụ nào?` |
| Khoảng trống | `Mảng nào của Paris đang bị đối thủ bỏ trống nhiều nhất trên AI?` |

---

# 4. Prompt tinh chỉnh sau khi có bản nháp

## 4.1 Đổi thứ tự một phần việc

```
Giữ nguyên bản kế hoạch, chỉ đổi một chỗ: dồn hết phần làm trang thương hiệu
và hồ sơ bác sĩ vào tháng 1 — những trang đó phải có trước
thì các bài còn lại mới dẫn về được.
```

## 4.2 Giãn tiến độ cho vừa sức

```
Tháng 1 mà 69 bài thì đội tôi không kham nổi.
Giãn ra thành 8 tháng giúp tôi, nhưng giữ nguyên thứ tự ưu tiên như cũ.
```

## 4.3 Thêm cột vào bảng giao việc

```
Thêm cho tôi một cột ghi rõ mỗi đầu việc sẽ đăng lên trang nào,
và đánh dấu trang nào phải tạo mới, trang nào cần kiểm tra lại xem website đã có chưa.
```

## 4.4 Tách riêng một chỉ số

```
Tách riêng một dòng KPI để theo dõi 4 công cụ kiểm tra răng online
(răng miệng, niềng, răng sứ, trồng răng) — tôi muốn biết bao nhiêu người
dùng công cụ rồi mới điền form.
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
