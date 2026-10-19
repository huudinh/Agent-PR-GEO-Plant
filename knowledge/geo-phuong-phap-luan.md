# PHƯƠNG PHÁP LUẬN GEO — NHA KHOA PARIS

Version: 1.0 · Đây là **xương sống tư duy** của Agent. Mọi kế hoạch GEO phải đi đúng trục này, không đảo bước, không bỏ bước.

---

# 0. TUYÊN NGÔN — VÌ SAO KHÔNG GIỚI THIỆU VỀ MÌNH

> **Nha khoa Paris không đi kể chuyện mình giỏi. Paris đi theo hành trình của khách, gỡ từng nỗi lo, rồi mới xuất hiện như giải pháp.**

| Cách cũ (brand-first) | Cách của bộ này (customer-journey-first) |
|---|---|
| "Nha khoa Paris là hệ thống nha khoa tiêu chuẩn Pháp đầu tiên…" | "Bọc răng sứ có phải mài hết men răng thật không?" |
| Nội dung xoay quanh **chúng tôi có gì** | Nội dung xoay quanh **khách đang sợ gì** |
| Đo bằng thứ hạng từ khoá | Đo bằng **AI có trích dẫn Nha khoa Paris không** |
| Viết bài theo danh mục dịch vụ | Viết bài theo **cụm truy vấn thật khách gõ vào AI** |
| Né chủ đề mài răng, biến chứng, giá, tháo sứ làm lại | **Chiếm lĩnh** đúng những chủ đề đó — vì đó là nơi khách quyết định |

**Hệ quả vận hành:** thứ tự ưu tiên nội dung KHÔNG theo doanh thu dịch vụ, mà theo **điểm ưu tiên của cụm truy vấn** — nơi nỗi sợ lớn nhất gặp cơ hội GEO lớn nhất. Vì vậy cụm "Tháo răng sứ làm lại" và "Mài răng, chết tuỷ" luôn đứng trên cụm "Các loại răng sứ"; cụm "Nha chu, răng lung lay" (giá trị doanh thu thấp) vẫn được ưu tiên vì đối thủ bỏ trống.

---

# 1. TRỤC 6 BƯỚC (BẮT BUỘC, KHÔNG ĐẢO THỨ TỰ)

```
① Chọn lĩnh vực  →  ② Đối tượng KH  →  ③ Giai đoạn hành trình (S1–S6)
        →  ④ Cụm truy vấn (từ khoá)  →  ⑤ Cụm nội dung (bài viết)  →  ⑥ GEO/SEO
```

| Bước | Làm gì | Nguồn dữ liệu | Đầu ra |
|---|---|---|---|
| ① **Chọn lĩnh vực** | Chốt phạm vi: thương hiệu tổng, Implant, Chỉnh nha, Thẩm mỹ, Tổng quát & Nha chu, Trẻ em | `geo-bo-truy-van-index.md` — 10 bộ | Danh sách bộ dịch vụ đưa vào kế hoạch |
| ② **Đối tượng KH** | Xác định nhóm khách của từng bộ (7–10 nhóm/bộ) và rào cản chốt của họ | `paris-brand-geo.md` §6 + chỉ mục bộ | Chân dung + rào cản chi phối |
| ③ **Giai đoạn** | Rải đối tượng lên 6 giai đoạn S1→S6, xác định giai đoạn quyết định | Bảng *Hành trình 6 giai đoạn* của từng bộ | Trọng số nỗ lực theo giai đoạn |
| ④ **Cụm truy vấn** | Lấy cụm C01–C15 + số truy vấn + điểm ưu tiên + tầng 80/20 | Bảng *Phân bổ 80/20* của từng bộ | Danh sách cụm xếp hạng |
| ⑤ **Cụm nội dung** | Quy cụm → số bài, dạng bài, trang đích, sóng, người phụ trách | Bảng *Bản đồ nội dung* — cột **Bài** | **Khối lượng sản xuất** (đơn vị: bài) |
| ⑥ **GEO/SEO** | Gắn KPI đo được: prompt đo GEO, top từ khoá, traffic AI, lead | `geo-kpi-framework.md` | 2 TAB Excel: KPI + Công việc triển khai |

**Quy tắc vàng:** không được nhảy từ ① sang ⑤. Mọi bài viết trong kế hoạch phải truy ngược được về **một cụm truy vấn**, cụm đó phải truy ngược được về **một giai đoạn**, giai đoạn đó phải truy ngược được về **một rào cản của một đối tượng thật**. Bài nào không truy ngược được → loại khỏi kế hoạch.

---

# 2. BƯỚC ③ — 6 GIAI ĐOẠN HÀNH TRÌNH (S1–S6)

Khung dùng chung cho cả 10 bộ. Mỗi giai đoạn có **một nỗi sợ khác nhau** — trả lời sai nỗi sợ thì mất khách dù tay nghề tốt.

| GĐ | Tên | Nhiệt | Khách đang nghĩ gì | Nội dung Paris phải có | Vai trò trong kế hoạch |
|---|---|---|---|---|---|
| **S1** | NHẬN BIẾT | Cold · ★ | "Răng hơi xấu / hơi ê nhưng chưa biết gọi là gì" | Nội dung **định danh vấn đề**, không bán hàng | Cửa vào rộng — traffic, không tính chuyển đổi |
| **S2** | TÌM HIỂU | Warm · ★★ | "Có bao nhiêu cách? Cái nào hợp với răng tôi?" | Bảng so sánh **trung thực, nêu cả nhược điểm** | Xây E-E-A-T, đổi cách AI phân loại Paris |
| **S3** | CÂN NHẮC & NỖI SỢ | Warm→Hot · ★★★ | "Có đau không? Có mài mất răng thật không? Vật liệu có chính hãng? Hết bao nhiêu? Hỏng thì ai chịu?" | **Rủi ro nói thật có số liệu · bảng giá công khai · cách tự kiểm tra giấy phép và vật liệu · case thật** | ⚠ **ĐIỂM QUYẾT ĐỊNH — chiếm ~50% điểm ưu tiên toàn bộ. Luôn ưu tiên tuyệt đối.** |
| **S4** | THỰC HIỆN | Hot · ★★ | "Mấy buổi? Nghỉ làm mấy ngày? Trả góp thế nào?" | Lộ trình từng bước **có mốc thời gian và số buổi** | Giảm huỷ lịch, tăng show-up rate |
| **S5** | TRẢI NGHIỆM & HẬU ĐIỀU TRỊ | Existing · ★★ | "Ê buốt thế này có bình thường không?" | Cẩm nang hậu điều trị **theo mốc ngày** | Không tạo lead mới nhưng **neo thực thể** trong AI + giảm biến chứng + tạo khách giới thiệu |
| **S6** | GẮN BÓ & MỞ RỘNG | LTV · ★ | "Răng tôi ổn rồi, giờ đến con và bố mẹ" | Cross-sell **gợi mở, mỗi bài một hướng** + gói gia đình | Tăng LTV — **mạnh hơn hẳn ngành thẩm mỹ**: một khách hài lòng thường kéo cả nhà |

**Phân bổ nỗ lực chuẩn theo giai đoạn** (dùng khi chưa có dữ liệu riêng): S3 ≈ 50% · S2 ≈ 25% · S1 ≈ 8% · S4 ≈ 7% · S5 ≈ 6% · S6 ≈ 4%.

## 2.1 BA RÀO CẢN CHỐT CỦA KHÁCH NHA KHOA — SỢ · NGỜ · NGẠI

Đây là điểm **khác biệt căn bản so với ngành thẩm mỹ** và là bộ lọc chính của Agent. Mọi bài phải gỡ được ít nhất một rào.

| Rào cản | Khách đang nghĩ gì | Bằng chứng Paris dùng để gỡ |
|---|---|---|
| **① SỢ** — sợ đau & sợ mất răng thật | Đau khi nhổ · khoan · cấy trụ. **Mài mất răng thật** khi bọc sứ, men răng không mọc lại. Niềng thì lâu, đau và xấu suốt thời gian đeo. | Nhổ răng siêu âm **Piezotome** · điều trị tuỷ **RECIPROC BLUE** · bác sĩ theo dõi từng giai đoạn · Invisalign trong suốt gỡ nỗi "xấu khi niềng" |
| **② NGỜ** — ngờ vật liệu & ngờ tay nghề | Trụ Implant / phôi sứ / khay niềng **có chính hãng không**? Bác sĩ có giỏi? Có giá ẩn phát sinh? Hỏng thì ai bảo hành? | **Đối tác Straumann (top 1) · Invisalign Black Diamond · Nacera · Ormco Diamond Star** · 100% BS tốt nghiệp ĐH Y có chứng chỉ hành nghề · giấy phép KCB · bảng giá công khai |
| **③ NGẠI** — ngại lộ trình dài & chi phí lớn | Điều trị nhiều buổi, đi lại nhiều lần, chi phí lớn, không biết khi nào xong. | Lộ trình rõ **số buổi và mốc thời gian** · **trả góp** · đặt lịch linh hoạt · hệ thống nhiều cơ sở |

> ⚠ **RÀO CẢN NGỜ Ở NGÀNH NHA KHOA NẶNG HƠN HẲN THẨM MỸ** — vì khách **không tự kiểm tra được vật liệu nằm trong miệng mình**. Đây là lý do toàn bộ các cụm C03 (vật liệu) và C14 (thực thể, kiểm chứng) được đẩy lên Tầng A ở các bộ Implant · Invisalign · Răng sứ, khác với phân bổ mặc định.
>
> Quan hệ đối tác hãng của Paris là **bằng chứng đối thủ khó sao chép nhất** → dùng sớm, dùng rõ, nhưng chỉ dùng chữ **"chính hãng"** cho đúng 4 hãng có hồ sơ (rào **R7**).

---

# 3. BƯỚC ④ — CỤM TRUY VẤN & CÔNG THỨC ƯU TIÊN

## 3.1 Vì sao không dùng bộ từ khoá SEO cũ

- Truy vấn vào AI dài gấp **~6 lần** truy vấn Google (≈23 từ so với 3–4 từ) — khách gõ nguyên một câu chuyện: *"răng tôi bọc sứ 3 năm trước giờ đen viền nướu và ê buốt, tháo ra làm lại có hại thêm không"*.
- AI "bung" (query fan-out) một câu hỏi thành **8–20 truy vấn con** rồi mới tổng hợp. Chỉ **32%** trích dẫn đến từ trang top 10 Google — **68%** đến từ trang ngoài top 10 nhưng khớp đúng một truy vấn con.
- **88%** thương hiệu KHÔNG được AI trích dẫn nếu chỉ tối ưu SEO truyền thống. Thương hiệu phủ được **>80% không gian chủ đề** giữ được **~85%** mức hiển thị trong AI.
- → Cuộc chơi không phải "lên top từ khoá", mà là **PHỦ KÍN KHÔNG GIAN CÂU HỎI** của một khách, từ lúc soi gương thấy răng xấu đến lúc tái khám năm thứ ba.

## 3.2 Công thức điểm ưu tiên (điểm tối đa 81)

```
ĐIỂM ƯU TIÊN = Giá trị DT × Nhiệt độ × Ưu tiên × Cơ hội GEO
               (Cao 3    (Hot 3     (P1 3     (1–3, lấy từ traffic AI
                TB  2     Warm 2     P2 2      thật của trang đích)
                Thấp 1)   Existing 2 P3 1)
                          Cold 1)
```

**Giá trị DT theo dịch vụ (Paris):** Cao = Implant · All-On 4/6 · Invisalign · răng sứ toàn hàm. TB = niềng mắc cài · bọc sứ lẻ · Veneer. Thấp = tổng quát · nha chu · trẻ em.

**Ngưỡng Cơ hội GEO** theo bằng chứng traffic AI của trang đích: ≥50 phiên → 3 · ≥5 phiên → 2 · còn lại (kể cả trang chưa có traffic) → 1.

> ⚠ **Paris CHƯA có mốc gốc traffic AI** (xem `paris-brand-geo.md` §8). Cho tới khi tháng Setup đo xong, mọi cụm lấy **Cơ hội GEO = 1** theo mặc định, trừ khi người dùng cung cấp số GA4 thật. **Agent KHÔNG được tự gán mức 2 hoặc 3 cho bất kỳ trang nào.**

**Nguyên tắc chống lệch:** giá trị doanh thu KHÔNG được một mình quyết định thứ tự. Nha chu và tổng quát có giá trị DT thấp nhưng **Ưu tiên P1** vì (a) đối thủ bỏ trống hoàn toàn, (b) đó là cửa vào rẻ nhất, (c) khách tổng quát hôm nay là khách Implant của 2 năm sau.

## 3.3 Bốn tầng 80/20 — quy tắc phân bổ ngân sách nội dung

| Tầng | Tên | % ngân sách | Thời điểm | Đặc điểm |
|---|---|---|---|---|
| **A** | CORE 80/20 | **70%** | 90 ngày đầu | 5 cụm/bộ, ~33% truy vấn nhưng chiếm **~50–55% điểm ưu tiên**. Hầu hết nằm ở S3. |
| **B** | Đòn bẩy chuyển đổi | **20%** | Khi A xong ~60% | 5 cụm — phương pháp, chẩn đoán, quy trình, nhóm đặc thù |
| **C** | Uy tín & giữ chân | **10%** | Chạy nền | 3 cụm — y khoa E-E-A-T, hậu điều trị, cross-sell. Tái sử dụng qua Zalo OA/CSKH |
| **D** | Cửa vào rộng | **0% ngân sách mới** | Sau 90 ngày | 2 cụm — chỉ viết pillar nền, tái sử dụng nội dung sẵn có |

**Ngoại lệ bắt buộc:** cụm **C05 "khi nào KHÔNG nên làm"** ở các bộ Răng sứ · Implant · Niềng tuy nằm Tầng B nhưng là **khác biệt E-E-A-T lớn nhất của Paris**. Trang trụ cột của C05 phải ra **cùng đợt Tầng A**, không chờ sóng 2. Đây là nội dung đối thủ gần như không dám viết.

## 3.4 Bảy nhóm mở rộng ưu tiên cho nha khoa

> ⚠ **Đây là GIẢ THUYẾT ưu tiên dựa trên hành vi khách nha khoa, KHÔNG phải dữ liệu traffic đã quan sát của Paris.** Tháng Setup phải đo mốc gốc rồi xếp lại thứ tự theo bằng chứng thật. Agent phải nói rõ điều này khi trình kế hoạch.

| Mã | Nhóm mở rộng | Vì sao ưu tiên | Cách mở rộng |
|---|---|---|---|
| G1 | **Vật liệu & "chính hãng"** | Rào NGỜ nặng nhất ngành nha; khách không kiểm tra được vật liệu trong miệng | Mỗi hãng đối tác → 1 trang thực thể + cách khách tự kiểm chứng (mã trụ, phiếu bảo hành, tra cứu hãng). Chỉ 4 hãng có hồ sơ (**R7**) |
| G2 | **Thực thể thương hiệu & kiểm chứng** | AI được hỏi "nha khoa nào uy tín" trả lời bằng thực thể nó hiểu rõ nhất | Trang chủ + trang "Về Paris" + FAQPage schema cho từng câu kiểm chứng: giấy phép, pháp nhân, số cơ sở |
| G3 | **Bác sĩ** | Khách không đánh giá được tay nghề → tìm thứ kiểm chứng được: bằng cấp, hiệp hội, số ca | Chỉ 3 bác sĩ có hồ sơ xác minh → ProfilePage / `IndividualPhysician` + `sameAs` tới ESCD · ICOI · ITI (**R4**) |
| G4 | **Giá & chi phí bóc tách** | Giá mập mờ = tín hiệu bị lừa; AI trích bài **có con số** | Mỗi dịch vụ 1 trang giá: dải min–max, **bóc tách cấu phần** (trụ–abutment–mão / số khay / theo răng), trả góp, ngày cập nhật (**R12**) |
| G5 | **Chi nhánh × Dịch vụ × Tỉnh** | Mẫu "địa chỉ [dịch vụ] ở [tỉnh]" là ý định mạnh và rẻ nhất để chiếm | Ma trận 7 cơ sở × dịch vụ trọng điểm, chuẩn NAP, nêu đúng phạm vi chuyên môn từng cơ sở (**R3**) |
| G6 | **Hỏng & làm lại** | Khoảng trống lớn nhất: đối thủ né chủ đề tháo sứ, đào thải trụ, niềng thất bại | Phủ mốc hỏng + dấu hiệu + phương án làm lại cho cả 5 dịch vụ chính; **tuyệt đối không phán xét nơi khách từng làm** (**R6**) |
| G7 | **Hậu điều trị & gói gia đình** | Câu hậu điều trị được Perplexity/Claude trích mạnh; LTV nha khoa mạnh hơn thẩm mỹ | Phủ mốc hồi phục + dấu hiệu bất thường; mỗi dịch vụ gợi **MỘT** bước tiếp theo; lấp Nha khoa trẻ em & gói gia đình |

---

# 4. BƯỚC ⑤ — 6 QUY TẮC VIẾT ĐỂ ĐƯỢC AI TRÍCH DẪN

Bắt buộc với mọi bài trong kế hoạch. Khi Agent mô tả đầu việc nội dung, phải nhắc được các quy tắc này trong cột công việc chi tiết.

1. **BLUF** — câu đầu tiên của mỗi mục PHẢI là câu trả lời đứng độc lập, hiểu được khi tách khỏi ngữ cảnh. *AI trích theo đoạn, không trích theo bài.*
2. **CÓ SỐ** — nội dung có số liệu được hiển thị trong câu trả lời AI cao hơn **30–40%**. "Hết ê buốt sau 3–7 ngày ở phần lớn ca" thắng "hết ê buốt khá nhanh".
3. **PHỦ 8 GÓC HỎI** cho mỗi chủ đề: định nghĩa · so sánh · hướng dẫn · trường hợp áp dụng · phản đối/rủi ro · thực thể liên quan · chi phí/chỉ số · địa phương. *Đây chính là 8 hướng AI bung truy vấn.*
4. **DÁM NÓI ĐIỀU BẤT LỢI** — "mài răng là không hoàn nguyên", "Invisalign không kéo nổi mọi ca", "nha chu không chữa khỏi hẳn, phải duy trì". Nội dung cân bằng được AI đánh giá là nguồn khách quan và trích nhiều hơn hẳn nội dung một chiều.
5. **GHI NGÀY CẬP NHẬT + TÊN BÁC SĨ THẨM ĐỊNH** trên mọi bài y khoa (schema `ProfilePage` / `IndividualPhysician`). Chỉ dùng 3 bác sĩ đã có hồ sơ (**R4**).
6. **KHÔNG NHỒI TỪ KHOÁ** — nhồi từ khoá cho kết quả **thấp hơn mức nền** trong AI search. Viết như đang trả lời một người thật đang lo.

**Quy đổi khối lượng sản xuất** (dùng khi quy bài ra nhân lực):

| Nhóm | Mô tả | Độ dài | Hệ số quy đổi |
|---|---|---|---|
| A1 | Bài trụ / chuyên sâu / trang pillar | 2.000–2.750 từ | **1,5** |
| A2 | Bài thường / bài tình huống / FAQ dài | 1.400–1.750 từ | **1,0** |
| A3 | Trang local, FAQ ngắn, khối nội dung nhúng | <1.400 từ | **0,5** |

---

# 5. BƯỚC ⑥ — ĐO LƯỜNG GEO (KPI THAY THẾ THỨ HẠNG TỪ KHOÁ)

## 5.1 Share of Voice trong AI — KPI trung tâm

**Cách chạy:** chế độ **ẩn danh** (không đăng nhập, tắt cá nhân hoá), dán nguyên văn từng prompt vào **ChatGPT · Gemini · Google AI Overview**. Ghi `1` nếu Nha khoa Paris được nhắc tên, `0` nếu không. **Chạy 3 lần lấy đa số.** Nhân bản sheet đo mỗi tháng.

**Lưu ý bản chất:** kết quả AI thay đổi theo phiên (chỉ ~27% truy vấn con lặp lại giữa các lần) → **đo XU HƯỚNG theo tháng, không đo tuyệt đối một lần**.

**Ba bộ prompt vận hành của Paris** (xây trong tháng Setup, khoá lại để so sánh được cả chu kỳ):

- **20 prompt dịch vụ trọng điểm** — Implant · All-On · Invisalign · niềng mắc cài · bọc sứ · Veneer, bám cụm Tầng A.
- **7 prompt hub cơ sở** — một prompt cho mỗi tỉnh thành có cơ sở: *"nha khoa trồng implant tốt ở [tỉnh]"*.
- **10 prompt kiểm chứng thương hiệu** — *"nha khoa Paris có uy tín không"*, *"nha khoa Paris có giấy phép gì"*, *"trụ implant ở nha khoa Paris có chính hãng không"*.

Mỗi lần đo phải ghi thêm **đối thủ được AI nhắc** — đây là dữ liệu quý nhất để biết AI đang coi ai là nguồn.

## 5.2 Năm trụ cột KPI (khớp TAB KPI của file output)

| # | Trụ cột | Chỉ tiêu trọng tâm | Trọng số mặc định |
|---|---|---|---|
| 1 | Hạ tầng Web & Hub | Kiến trúc theo chuyên khoa · cổng Hub liên kết · tải trang <2s | 0,10 |
| 2 | Sản lượng Bài viết | Số bài hoàn thành/tháng theo từng business line | 0,20 |
| 3 | SEO & GEO AI Search | Top 3/5/10 Google · tỷ lệ được nhắc trên ChatGPT/Gemini/AI Overview | 0,40 |
| 4 | Traffic | Organic traffic google.com.vn + **Traffic AI** (referral từ LLM) | 0,15 |
| 5 | Form Lead | Số lead · sđt xác nhận có nhu cầu · KH đến phòng khám | 0,15 |

**Trọng số đánh giá theo tháng** trong một chu kỳ 4 tháng: Setup 20% · Tăng tốc 25% · Đột phá 30% · Về đích 25%.

---

# 6. QUY TẮC LẬP KẾ HOẠCH THEO THÁNG

Khi người dùng nói "lập kế hoạch GEO cho N tháng, từ tháng X", Agent áp dụng:

## 6.1 Ánh xạ sóng → tháng

| Số tháng | Ánh xạ |
|---|---|
| 3 tháng | T1 = Sóng 1 (Tầng A) · T2 = Sóng 2 (Tầng B) · T3 = Sóng 3 (Tầng C) |
| 4 tháng | T1 Setup + Sóng 1 · T2 Sóng 1 (tiếp) + Sóng 2 · T3 Sóng 2 + Sóng 3 · T4 Sóng 3 + Nền |
| 6 tháng | Sóng 1 trải T1–T2 · Sóng 2 trải T3–T4 · Sóng 3 T5 · Nền T6 |
| 12 tháng | Quý 1 Sóng 1 · Quý 2 Sóng 2 · Quý 3 Sóng 3 · Quý 4 Nền + nhân bản trang cơ sở/tỉnh |

## 6.2 Bốn giai đoạn của một chu kỳ (đặt tên cho từng tháng)

**Setup → Tăng tốc → Đột phá → Về đích.** Tháng Setup luôn gồm: **khoá 3 bộ prompt đo GEO lấy mốc gốc**, audit từ khoá, thiết lập GA4 + heatmap + tách kênh traffic AI, ban hành khung loại bài + checklist từ cấm, gắn thẻ tagging theo hành trình, **đối chiếu sitemap thật để chốt trang đích**, và **xin giấy xác nhận nội dung quảng cáo (R9)**.

## 6.3 Tám nguyên tắc phân bổ sản lượng

1. **Tầng A trước** — không mở Tầng B khi Tầng A chưa xong ~60%.
2. **S3 trước S1** — luôn xuất bản cụm nỗi sợ / vật liệu / giá / chọn cơ sở trước cụm nhận biết.
3. **C05 ra cùng Tầng A** — cụm "khi nào KHÔNG nên làm" không được đẩy sang sóng 2 ở 3 bộ Răng sứ · Implant · Niềng.
4. **Tháng nào cũng chạy đủ các line trọng điểm** — Implant · Chỉnh nha · Thẩm mỹ phải có mặt mọi tháng, không dồn một line vào một tháng.
5. **Sản lượng phẳng** — chênh lệch giữa tháng cao nhất và thấp nhất ≤25%, trừ tháng Setup được phép thấp hơn.
6. **Trang cơ sở** chỉ làm **7 hub có cơ sở thật** (Hà Nội · Hải Phòng · Quảng Ninh · Vinh – Nghệ An · Đà Nẵng · TP.HCM · Bình Dương), rải đều ~1–2 trang/tháng. Trang "dịch vụ × tỉnh không có cơ sở" **KHÔNG nằm trong phạm vi chu kỳ** — đẩy backlog.
7. **Mỗi đầu việc nội dung phải có người phụ trách và hạn chót cuối tháng** — không để trống.
8. **Cộng thời gian duyệt 2 lớp (BS + Pháp chế)** vào hạn chót; không đặt hạn sản xuất trùng ngày phát hành.

## 6.4 Quy tắc số liệu

- Chỉ tiêu sản lượng: **tính được** từ `geo-bo-truy-van-index.md` → được phép đưa số cụ thể.
- Chỉ tiêu SEO/GEO/Traffic/Lead: **phải có số hiện tại làm mốc**. Paris chưa cung cấp → ghi `⚠ Cần xác minh từ Nha khoa Paris` ở cột "Hiện tại", đề xuất **mức tăng trưởng tương đối** (%), **KHÔNG bịa số tuyệt đối**.
- **Giá · ưu đãi · điều kiện trả góp là DỮ LIỆU ĐỘNG** (rào **R12**): không đưa số vào kế hoạch, chỉ ghi đầu việc "lấy giá tại thời điểm chạy từ trang bảng giá".
- Mọi con số, case, giấy phép, danh sách bác sĩ phải xác minh trước khi chạy.
