# GEO — CHỈ MỤC BỘ TRUY VẤN & BẢN ĐỒ NỘI DUNG · NHA KHOA PARIS

> Sinh tự động từ `data/bo-truy-van/*.json` bằng `tools/build-index.py`. **Không sửa tay file này** —
> sửa file JSON nguồn rồi chạy lại script. Đây là **nguồn sự thật về khối lượng công việc**:
> mỗi cụm cho biết cần bao nhiêu bài, thuộc giai đoạn nào của khách, sóng nào, trang đích nào.

**Tổng kho:** 10 bộ dịch vụ · 150 cụm chủ đề · **389 bài viết** cần sản xuất · 2.550 truy vấn đã phân loại.

**Quy ước đọc bảng:**

| Ký hiệu | Nghĩa |
|---|---|
| Tầng A | CORE 80/20 — làm trong 90 ngày, **70% ngân sách nội dung** |
| Tầng B | Đòn bẩy chuyển đổi — bắt đầu khi A xong ~60%, **20%** |
| Tầng C | Uy tín & giữ chân — chạy nền, **10%** |
| Tầng D | Cửa vào rộng — **0% ngân sách mới**, chỉ viết pillar nền / tái sử dụng |
| S1…S6 | Giai đoạn hành trình: Nhận biết · Tìm hiểu · Cân nhắc & nỗi sợ · Thực hiện · Trải nghiệm & hậu điều trị · Gắn bó & mở rộng |
| Sóng | S1 0–30 ngày · S2 31–60 ngày · S3 61–90 ngày · Nền sau 90 ngày |
| TV / CORE | Số truy vấn của cụm / trong đó bao nhiêu truy vấn thuộc CORE 80/20 |
| Bài | Số bài cần sản xuất cho cụm (`—` = tái sử dụng nội dung, không tính sản lượng mới) |
| SỢ · NGỜ · NGẠI | Ba rào cản chốt của khách nha khoa — mọi cụm phải gỡ được ít nhất một |
| ⚠ đối chiếu | Trang đích CHƯA xác minh trên sitemap thật — phải soi chiếu trước khi giao việc |

**Bảng tổng hợp khối lượng theo bộ:**

| # | Bộ dịch vụ | Business line | File nguồn | Cụm | Bài cần SX |
|---|---|---|---|---|---|
| 1 | Thương hiệu Nha khoa Paris (brand tổng) | BRAND · Thương hiệu tổng | `01-thuonghieu.json` | 15 | **34** |
| 2 | Trồng răng Implant | NKI · Implant & Phục hình mất răng | `02-implant.json` | 15 | **42** |
| 3 | All-On 4/6 & phục hình toàn hàm | NKI · Implant & Phục hình mất răng | `03-allon.json` | 15 | **35** |
| 4 | Niềng răng mắc cài (kim loại · sứ · pha lê · mặt trong) | NKC · Chỉnh nha — Niềng răng | `04-niengmaccai.json` | 15 | **40** |
| 5 | Invisalign — niềng răng trong suốt | NKC · Chỉnh nha — Niềng răng | `05-invisalign.json` | 15 | **35** |
| 6 | Bọc răng sứ & răng sứ toàn hàm | NKT · Nha khoa thẩm mỹ | `06-rangsu.json` | 15 | **47** |
| 7 | Mặt dán sứ Veneer | NKT · Nha khoa thẩm mỹ | `07-veneer.json` | 15 | **34** |
| 8 | Nha khoa tổng quát (nhổ răng · trám · tuỷ · cạo vôi · tẩy trắng) | NKG · Nha khoa tổng quát & Nha chu | `08-tongquat.json` | 15 | **45** |
| 9 | Nha chu, viêm nướu & tụt lợi | NKG · Nha khoa tổng quát & Nha chu | `09-nhachu.json` | 15 | **37** |
| 10 | Nha khoa trẻ em & gói gia đình | NKF · Nha khoa trẻ em & Gia đình | `10-trenem.json` | 15 | **40** |
|  | **TỔNG** |  |  | **150** | **389** |

**Khối lượng theo business line** — đây là trục phân nhóm dòng KPI sản lượng của file output:

| Business line | Bộ dịch vụ | Cụm | Bài |
|---|---|---|---|
| BRAND · Thương hiệu tổng | Thương hiệu Nha khoa Paris (brand tổng) | 15 | **34** |
| NKI · Implant & Phục hình mất răng | Trồng răng Implant · All-On 4/6 & phục hình toàn hàm | 30 | **77** |
| NKC · Chỉnh nha — Niềng răng | Niềng răng mắc cài (kim loại · sứ · pha lê · mặt trong) · Invisalign — niềng răng trong suốt | 30 | **75** |
| NKT · Nha khoa thẩm mỹ | Bọc răng sứ & răng sứ toàn hàm · Mặt dán sứ Veneer | 30 | **81** |
| NKG · Nha khoa tổng quát & Nha chu | Nha khoa tổng quát (nhổ răng · trám · tuỷ · cạo vôi · tẩy trắng) · Nha chu, viêm nướu & tụt lợi | 30 | **82** |
| NKF · Nha khoa trẻ em & Gia đình | Nha khoa trẻ em & gói gia đình | 15 | **40** |

---

## 1. Thương hiệu Nha khoa Paris (brand tổng)

`01-thuonghieu.json` · BRAND · Thương hiệu tổng · **34 bài cần sản xuất**

**Quy mô bộ:** 255 truy vấn · 15 cụm · 10 nhóm đối tượng · 60 truy vấn CORE 80/20 (24% bộ) chiếm 52% điểm ưu tiên

**Nỗi sợ quyết định (mọi nội dung phải gỡ được ít nhất một):**

- ① NGỜ — SỢ CHỌN NHẦM CHUỖI LỚN MÀ MỖI CƠ SỞ MỘT CHẤT LƯỢNG → cụm xử lý **C08 + C14 + C06** (51 truy vấn, 36 CORE)
- ② NGỜ — SỢ REVIEW TRÊN MẠNG LÀ GIẢ, KHÔNG BIẾT TIN AI → cụm xử lý **C06 + C11 + C12** (51 truy vấn, 13 CORE)
- ③ NGẠI — SỢ BỊ ĐỘI GIÁ GIỮA LỘ TRÌNH, SỢ TRẢ GÓP CÓ BẪY → cụm xử lý **C07 + C04 + C09** (51 truy vấn, 11 CORE)

**Hành trình 6 giai đoạn:**

| GĐ | Ưu tiên | Nỗi sợ chi phối | Cụm | TV | CORE | % điểm |
|---|---|---|---|---|---|---|
| S1 | ★ Nền | Sợ không biết gì rồi bị dẫn dắt. Không phân biệt được phòng khám có giấy phép KCB và cơ sở làm răng trôi nổi. | C01 · C02 · C13 | 51 | 0 | 7% |
| S2 | ★★ | Sợ chuỗi lớn nhưng mỗi cơ sở một tay nghề. Sợ đến nơi lại không làm được dịch vụ mình cần, phải đi cơ sở khác. | C03 · C04 · C05 · C12 | 68 | 0 | 24% |
| S3 | ★★★ Quyết định | NGỜ LÀ NỖI SỢ LỚN NHẤT: bác sĩ trên quảng cáo có phải người trực tiếp làm? Vật liệu có chính hãng? Giá công khai có phải giá cuối? Bảo hành ai chịu khi cơ sở đổi chủ? | C06 · C07 · C08 · C11 · C14 | 85 | 60 | 52% |
| S4 | ★★ | Sợ xin nghỉ làm rồi đến nơi phải chờ, phải quay lại lần nữa mới được bác sĩ khám. | C09 | 17 | 0 | 8% |
| S5 | ★★ | Sợ làm xong ở cơ sở này, chuyển tỉnh thì cơ sở khác không nhận tái khám, không nhận bảo hành. | C10 | 17 | 0 | 6% |
| S6 | ★ Nền | Sợ bị bán chồng dịch vụ không cần thiết cho cả nhà. | C15 | 17 | 0 | 3% |

**Phân bổ 80/20:**

| Tầng | Cụm | TV | % điểm | Phân bổ & danh sách cụm |
|---|---|---|---|---|
| A | 5 | 85 | 52% | 70% — C14 Thực thể thương hiệu & kiểm chứng · C08 Chọn cơ sở & bác sĩ · C07 Chi phí minh bạch & trả góp · C06 Khủng hoảng niềm tin & review thật-giả · C11 Bảo hành, khiếu nại & làm lại. Làm trong 90 ngày. C14 phải ra TRƯỚC MỌI CỤM KHÁC vì nó là khối bằng chứng nuôi cả C06, C07, C08. |
| B | 5 | 85 | 31% | 20% — C12 Giấy phép, phạm vi chuyên môn & phân tuyến · C04 Khám – chẩn đoán – kế hoạch điều trị · C05 Bảo tồn: khi nào KHÔNG nên làm · C09 Đặt lịch, tiếp nhận & số buổi · C13 Nhóm khách đặc thù (khách tỉnh · Việt kiều · gia đình). Mở khi Tầng A xong ~60%; riêng C12 nên làm sớm vì là bằng chứng gốc của C08 và C14. |
| C | 3 | 51 | 14% | 10% — C10 Hậu điều trị đa cơ sở & chuyển tỉnh · C03 Hệ sinh thái dịch vụ & taxonomy · C15 Cross-sell gia đình. Chạy nền, tái sử dụng nội dung CSKH và Zalo OA. |
| D | 2 | 34 | 3% | 0% ngân sách mới — C01 Nhận biết loại hình cơ sở nha khoa · C02 Quan niệm & mẹo dân gian về răng. Chỉ viết pillar nền một lần, dùng lại khối tiêu chí cho C08 và C12. |

**Bản đồ nội dung — 15 cụm:**

| Hạng | Mã | Cụm chủ đề | Tầng | GĐ | TV | CORE | % điểm | Bài | Sóng | Trang đích |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | C14 | Thực thể thương hiệu & kiểm chứng (GEO Entity) ⭐⭐⭐ | A | S3 | 17 | 14 | 13% | 5 | S1 (0–30n) | Trang chủ + MỚI: /ve-nha-khoa-paris.html |
| 2 | C08 | Chọn cơ sở & bác sĩ — tự kiểm tra thế nào ⭐⭐⭐ | A | S3 | 17 | 13 | 12% | 4 | S1 (0–30n) | ⚠ đối chiếu: /tim-phong-kham.html + MỚI: /doi-ngu-bac-si.html |
| 3 | C07 | Chi phí minh bạch, bảng giá & trả góp ⭐⭐⭐ | A | S3 | 17 | 12 | 11% | 3 | S1 (0–30n) | ⚠ đối chiếu: /hoan-my-bang-gia-dich-vu-nha-khoa.html |
| 4 | C06 | Khủng hoảng niềm tin: review thật – giả, nha khoa bị tố ⭐⭐⭐ | A | S3 | 17 | 11 | 10% | 5 | S1 (0–30n) | MỚI: /kien-thuc/chon-nha-khoa/doc-review-nha-khoa/ |
| 5 | C11 | Bảo hành, khiếu nại & làm lại khi không hài lòng ⭐⭐ | A | S3 | 17 | 10 | 6% | 4 | S1 (0–30n) | MỚI: /chinh-sach-bao-hanh.html |
| 6 | C12 | Giấy phép KCB, phạm vi chuyên môn & phân tuyến cơ sở | B | S2 | 17 | — | 9% | 3 | S2 (31–60n) | MỚI: /kien-thuc/chon-nha-khoa/giay-phep-phong-kham-nha-khoa/ |
| 7 | C04 | Khám – chẩn đoán – kế hoạch điều trị & báo giá trước | B | S2 | 17 | — | 8% | 3 | S2 (31–60n) | MỚI: /kien-thuc/quy-trinh/kham-va-ke-hoach-dieu-tri/ |
| 8 | C05 | Bảo tồn: khi nào KHÔNG nên can thiệp ⭐⭐⭐ | B | S2 | 17 | — | 7% | 3 | S2 (31–60n) | MỚI: /kien-thuc/bao-ton/khi-nao-khong-nen-lam-rang/ |
| 9 | C09 | Đặt lịch, tiếp nhận & số buổi điều trị | B | S4 | 17 | — | 4% | 2 | S2 (31–60n) | MỚI: /dat-lich-hen.html |
| 10 | C13 | Nhóm khách đặc thù: khách tỉnh · Việt kiều · gia đình | B | S1 | 17 | — | 3% | 2 | S2 (31–60n) | MỚI: /kien-thuc/chon-nha-khoa/khach-tinh-xa-lam-rang/ |
| 11 | C10 | Hậu điều trị đa cơ sở & chuyển tỉnh ⭐ | C | S5 | 17 | — | 6% | — | S3 (61–90n) | MỚI: /kien-thuc/cham-soc/tai-kham-chuyen-co-so/ |
| 12 | C03 | Hệ sinh thái dịch vụ & taxonomy chuyên khoa | C | S2 | 17 | — | 5% | — | S3 (61–90n) | ⚠ đối chiếu: trang danh mục dịch vụ |
| 13 | C15 | Cross-sell gia đình & gói Teeth Spa (LTV) | C | S6 | 17 | — | 3% | — | S3 (61–90n) | MỚI: /goi-gia-dinh.html |
| 14 | C01 | Nhận biết loại hình cơ sở nha khoa (phòng khám · chuỗi · bệnh viện) | D | S1 | 17 | — | 2% | — | Nền (>90n) | MỚI: /kien-thuc/chon-nha-khoa/phan-biet-co-so-nha-khoa/ |
| 15 | C02 | Quan niệm & mẹo dân gian về răng (đặc thù VN) | D | S1 | 17 | — | 1% | — | Nền (>90n) | MỚI: /kien-thuc/meo-dan-gian-ve-rang/ |

---

## 2. Trồng răng Implant

`02-implant.json` · NKI · Implant & Phục hình mất răng · **42 bài cần sản xuất**

**Quy mô bộ:** 255 truy vấn · 15 cụm · 9 nhóm đối tượng · 64 truy vấn CORE 80/20 (25% bộ) chiếm 54% điểm ưu tiên

**Nỗi sợ quyết định (mọi nội dung phải gỡ được ít nhất một):**

- ① NGỜ — SỢ TRỤ IMPLANT BỊ TRÁO, KHÔNG CHÍNH HÃNG, VÀI NĂM ĐÀO THẢI MÀ KHÔNG CÒN AI BẢO HÀNH → cụm xử lý **C03 + C11 + C14** (51 truy vấn, 37 CORE)
- ② SỢ — SỢ ĐAU, SỢ KHOAN VÀO XƯƠNG, SỢ BIẾN CHỨNG VIÊM – TIÊU XƯƠNG – TỔN THƯƠNG DÂY THẦN KINH → cụm xử lý **C06 + C04 + C09** (51 truy vấn, 14 CORE)
- ③ NGẠI — SỢ CHI PHÍ LỚN BỊ ĐỘI THÊM: GHÉP XƯƠNG, NÂNG XOANG, ABUTMENT, MÃO TÍNH RIÊNG → cụm xử lý **C07 + C08 + C05** (51 truy vấn, 26 CORE)

**Hành trình 6 giai đoạn:**

| GĐ | Ưu tiên | Nỗi sợ chi phối | Cụm | TV | CORE | % điểm |
|---|---|---|---|---|---|---|
| S1 | ★ Nền | Mất răng lâu năm: sợ già đi, sợ mặt hóp lệch, sợ nhai kém rồi đau dạ dày. Chưa biết tiêu xương là gì và nó không tự dừng lại. | C01 · C02 · C13 | 51 | 0 | 6% |
| S2 | ★★ | Sợ bị tư vấn cấy nhiều trụ hơn cần. Không biết cầu răng hay tháo lắp có hợp với mình hơn không, và không ai nói thật điều đó. | C03 · C04 · C05 · C12 | 68 | 20 | 25% |
| S3 | ★★★ Quyết định | SỢ ĐẶT MỘT KHOẢN LỚN VÀO MỘT VẬT MÌNH KHÔNG KIỂM TRA ĐƯỢC. Trụ có đúng hãng không? Ai cầm tay khoan? Hỏng thì ai chịu? Giá công khai có phải giá cuối? | C06 · C07 · C08 · C11 · C14 | 85 | 44 | 54% |
| S4 | ★★ | Sợ đau khi cấy và sợ phải chờ 3–6 tháng tích hợp xương mà trong thời gian đó không có răng để ăn, để nói. | C09 | 17 | 0 | 7% |
| S5 | ★★ | Sợ mình là ca đào thải. Sợ bỏ tái khám rồi vài năm sau viêm quanh trụ mà không biết. | C10 | 17 | 0 | 5% |
| S6 | ★ Nền | Sợ làm từng phần mãi mà không giải quyết gốc, rồi tốn thêm một lần nữa. | C15 | 17 | 0 | 3% |

**Phân bổ 80/20:**

| Tầng | Cụm | TV | % điểm | Phân bổ & danh sách cụm |
|---|---|---|---|---|
| A | 5 | 85 | 54% | 70% — C11 Đào thải trụ & làm lại · C06 Đau, rủi ro & biến chứng · C03 Trụ Implant & vật liệu chính hãng · C07 Chi phí bóc tách trụ–abutment–mão · C14 Thực thể & kiểm chứng đối tác Straumann. ĐÂY LÀ BỘ CÓ LỢI THẾ GEO LỚN NHẤT CỦA PARIS: quan hệ đối tác top 1 Straumann là bằng chứng đối thủ khó sao chép. C03 được đẩy lên Tầng A (khác mặc định) vì rào cản NGỜ về vật liệu nặng hơn mọi rào khác ở bộ này. |
| B | 5 | 85 | 29% | 20% — C08 Chọn cơ sở & bác sĩ implant · C05 Bảo tồn: khi nào KHÔNG nên cấy implant · C04 Chẩn đoán CT Conebeam · ghép xương · nâng xoang · C09 Quy trình, số buổi & thời gian tích hợp · C13 Nhóm bệnh lý nền (tiểu đường · loãng xương · cao tuổi). C05 tuy Tầng B nhưng là khác biệt E-E-A-T lớn nhất — trang trụ cột của C05 phải ra cùng đợt Tầng A. |
| C | 3 | 51 | 14% | 10% — C10 Chăm sóc & tái khám sau implant · C12 Y khoa: tiêu xương · khớp cắn · nha chu · C15 Cross-sell toàn hàm. Chạy nền. Nội dung hậu điều trị được Perplexity/Claude trích mạnh nên rẻ mà hiệu quả. |
| D | 2 | 34 | 3% | 0% ngân sách mới — C01 Nhận biết hệ quả mất răng · C02 Quan niệm & mẹo dân gian khi mất răng. Chỉ viết pillar nền. |

**Bản đồ nội dung — 15 cụm:**

| Hạng | Mã | Cụm chủ đề | Tầng | GĐ | TV | CORE | % điểm | Bài | Sóng | Trang đích |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | C11 | Đào thải trụ, Implant hỏng & làm lại ⭐⭐⭐ | A | S3 | 17 | 14 | 13% | 8 | S1 (0–30n) | MỚI: /kien-thuc/implant/implant-bi-dao-thai-lam-lai/ |
| 2 | C06 | Đau, rủi ro & biến chứng cấy ghép ⭐⭐⭐ | A | S3 | 17 | 14 | 11% | 8 | S1 (0–30n) | MỚI: /kien-thuc/implant/bien-chung-trong-rang-implant/ |
| 3 | C03 | Trụ Implant & vật liệu — loại nào, có chính hãng không ⭐⭐⭐ | A | S2 | 17 | 13 | 11% | 6 | S1 (0–30n) | MỚI: /kien-thuc/implant/cac-loai-tru-implant/ |
| 4 | C07 | Chi phí: bóc tách trụ – abutment – mão & trả góp ⭐⭐⭐ | A | S3 | 17 | 12 | 11% | 4 | S1 (0–30n) | ⚠ đối chiếu: /hoan-my-bang-gia-dich-vu-nha-khoa.html + MỚI: /bang-gia/implant/ |
| 5 | C14 | Thực thể & kiểm chứng: đối tác Straumann · bác sĩ · giấy phép ⭐⭐ | A | S3 | 17 | 11 | 6% | 2 | S1 (0–30n) | MỚI: /chuyen-khoa/implant/ |
| 6 | C08 | Chọn cơ sở & bác sĩ implant — tiêu chí kiểm chứng được ⭐⭐ | B | S3 | 17 | — | 9% | 3 | S2 (31–60n) | MỚI: /kien-thuc/implant/chon-nha-khoa-trong-implant/ |
| 7 | C05 | Bảo tồn: khi nào KHÔNG nên cấy implant (cầu răng · tháo lắp) ⭐⭐⭐ | B | S2 | 17 | — | 8% | 4 | S2 (31–60n) | MỚI: /kien-thuc/implant/khi-nao-khong-nen-cay-implant/ |
| 8 | C04 | Chẩn đoán: CT Conebeam · ghép xương · nâng xoang | B | S2 | 17 | — | 7% | 3 | S2 (31–60n) | MỚI: /kien-thuc/implant/ghep-xuong-nang-xoang/ |
| 9 | C09 | Quy trình, số buổi & thời gian tích hợp xương | B | S4 | 17 | — | 4% | 2 | S2 (31–60n) | MỚI: /kien-thuc/implant/quy-trinh-cay-implant/ |
| 10 | C13 | Nhóm bệnh lý nền: tiểu đường · loãng xương · cao tuổi | B | S1 | 17 | — | 3% | 2 | S2 (31–60n) | MỚI: /kien-thuc/implant/implant-cho-nguoi-benh-nen/ |
| 11 | C10 | Chăm sóc, vệ sinh & tái khám sau implant ⭐ | C | S5 | 17 | — | 6% | — | S3 (61–90n) | MỚI: /kien-thuc/cham-soc/cham-soc-sau-cay-implant/ |
| 12 | C12 | Y khoa & chức năng: tiêu xương · khớp cắn · nha chu (E-E-A-T) | C | S2 | 17 | — | 5% | — | S3 (61–90n) | ⚠ đối chiếu: trang hỏi đáp |
| 13 | C15 | Cross-sell: từ 1 trụ → toàn hàm · All-On (LTV) | C | S6 | 17 | — | 3% | — | S3 (61–90n) | MỚI: /chuyen-khoa/all-on-4-6/ |
| 14 | C01 | Nhận biết hệ quả mất răng: tiêu xương · lệch mặt · nhai kém | D | S1 | 17 | — | 2% | — | Nền (>90n) | MỚI: /kien-thuc/implant/mat-rang-lau-nam-hau-qua/ |
| 15 | C02 | Quan niệm & mẹo dân gian khi mất răng | D | S1 | 17 | — | 1% | — | Nền (>90n) | MỚI: /kien-thuc/implant/quan-niem-ve-mat-rang/ |

---

## 3. All-On 4/6 & phục hình toàn hàm

`03-allon.json` · NKI · Implant & Phục hình mất răng · **35 bài cần sản xuất**

**Quy mô bộ:** 255 truy vấn · 15 cụm · 7 nhóm đối tượng · 58 truy vấn CORE 80/20 (23% bộ) chiếm 52% điểm ưu tiên

**Nỗi sợ quyết định (mọi nội dung phải gỡ được ít nhất một):**

- ① NGẠI — SỢ BỎ RA MỘT KHOẢN RẤT LỚN MÀ KHÔNG BIẾT ĐÃ ĐÚNG CHỈ ĐỊNH CHƯA → cụm xử lý **C07 + C05 + C04** (51 truy vấn, 24 CORE)
- ② NGỜ — SỢ 4 TRỤ KHÔNG ĐỦ GÁNH CẢ HÀM, VÀI NĂM SỤP CẢ KHUNG → cụm xử lý **C06 + C11 + C03** (51 truy vấn, 34 CORE)
- ③ SỢ — NGƯỜI CAO TUỔI SỢ KHÔNG CHỊU ĐƯỢC CA ĐẠI PHẪU, SỢ GÂY MÊ → cụm xử lý **C13 + C09 + C12** (51 truy vấn, 0 CORE)

**Hành trình 6 giai đoạn:**

| GĐ | Ưu tiên | Nỗi sợ chi phối | Cụm | TV | CORE | % điểm |
|---|---|---|---|---|---|---|
| S1 | ★ Nền | Mất răng gần hết hoặc đang dùng hàm giả tháo lắp: sợ hàm rơi khi nói, sợ không ăn được, sợ con cháu thấy mình già. | C01 · C02 · C13 | 51 | 0 | 7% |
| S2 | ★★ | Không phân biệt được All-On 4, All-On 6 và cấy từng trụ rời. Sợ bị chọn phương án đắt hơn mức cần. | C03 · C04 · C05 · C12 | 68 | 24 | 26% |
| S3 | ★★★ Quyết định | ĐÂY LÀ CA CHI PHÍ LỚN NHẤT CỦA NGÀNH NHA. Khách hỏi: 4 trụ có đủ chịu lực? Khung răng dùng được bao lâu? Hỏng một trụ thì tháo cả hàm? Ai bảo hành và bảo hành bao nhiêu năm? | C06 · C07 · C08 · C11 · C14 | 85 | 34 | 52% |
| S4 | ★★ | Sợ ca mổ dài, sợ gây mê ở tuổi cao, sợ sau mổ sưng không dám gặp ai. | C09 | 17 | 0 | 7% |
| S5 | ★★ | Sợ không biết vệ sinh dưới khung răng, sợ viêm mà phát hiện muộn. | C10 | 17 | 0 | 5% |
| S6 | ★ Nền | Sợ hàm trên làm rồi hàm dưới lại phải làm tiếp, tốn thêm một lần nữa. | C15 | 17 | 0 | 3% |

**Phân bổ 80/20:**

| Tầng | Cụm | TV | % điểm | Phân bổ & danh sách cụm |
|---|---|---|---|---|
| A | 5 | 85 | 52% | 70% — C07 Chi phí toàn hàm & trả góp · C06 Rủi ro, chịu lực & biến chứng · C11 Hỏng trụ, sụp khung & làm lại · C03 Loại trụ, khung & vật liệu chính hãng · C14 Thực thể & kiểm chứng. Ca giá trị lớn nhất → nội dung phải minh bạch chi phí sớm nhất, vì NGẠI là rào cản số một ở bộ này. |
| B | 5 | 85 | 30% | 20% — C05 Khi nào KHÔNG nên làm toàn hàm · C04 Chẩn đoán & lượng xương còn lại · C08 Chọn cơ sở đủ năng lực đại phẫu · C09 Quy trình & hồi phục · C13 Người cao tuổi & bệnh lý nền. C13 ở bộ này quan trọng hơn mọi bộ khác vì khách chủ lực là người trên 55 tuổi. |
| C | 3 | 51 | 15% | 10% — C10 Vệ sinh & tái khám dưới khung răng · C12 Y khoa: khớp cắn, lực nhai, tiêu xương · C15 Cross-sell hàm còn lại. Chạy nền. |
| D | 2 | 34 | 3% | 0% ngân sách mới — C01 Nhận biết mất răng toàn hàm · C02 Hàm giả tháo lắp truyền thống. Chỉ pillar nền. |

**Bản đồ nội dung — 15 cụm:**

| Hạng | Mã | Cụm chủ đề | Tầng | GĐ | TV | CORE | % điểm | Bài | Sóng | Trang đích |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | C07 | Chi phí toàn hàm & trả góp — bóc tách từng cấu phần ⭐⭐⭐ | A | S3 | 17 | 13 | 13% | 4 | S1 (0–30n) | ⚠ đối chiếu: /hoan-my-bang-gia-dich-vu-nha-khoa.html + MỚI: /bang-gia/all-on-4-6/ |
| 2 | C06 | Rủi ro, chịu lực & biến chứng All-On ⭐⭐⭐ | A | S3 | 17 | 12 | 12% | 6 | S1 (0–30n) | MỚI: /kien-thuc/all-on/rui-ro-all-on-4-6/ |
| 3 | C11 | Hỏng trụ, sụp khung & phương án làm lại ⭐⭐⭐ | A | S3 | 17 | 11 | 10% | 5 | S1 (0–30n) | MỚI: /kien-thuc/all-on/all-on-bi-hong-lam-lai/ |
| 4 | C03 | All-On 4 hay All-On 6 · loại trụ · khung & vật liệu ⭐⭐⭐ | A | S2 | 17 | 12 | 11% | 5 | S1 (0–30n) | MỚI: /kien-thuc/all-on/all-on-4-khac-all-on-6/ |
| 5 | C14 | Thực thể & kiểm chứng: đối tác hãng · bác sĩ · năng lực đại phẫu ⭐⭐ | A | S3 | 17 | 10 | 6% | 2 | S1 (0–30n) | MỚI: /chuyen-khoa/all-on-4-6/ |
| 6 | C05 | Khi nào KHÔNG nên làm toàn hàm ⭐⭐⭐ | B | S2 | 17 | — | 9% | 3 | S2 (31–60n) | MỚI: /kien-thuc/all-on/khi-nao-khong-nen-lam-toan-ham/ |
| 7 | C04 | Chẩn đoán: lượng xương còn lại · CT Conebeam · thiết kế khớp cắn | B | S2 | 17 | — | 7% | 2 | S2 (31–60n) | MỚI: /kien-thuc/all-on/danh-gia-xuong-truoc-all-on/ |
| 8 | C08 | Chọn cơ sở đủ năng lực đại phẫu & bác sĩ implant toàn hàm ⭐⭐ | B | S3 | 17 | — | 6% | 2 | S2 (31–60n) | MỚI: /kien-thuc/all-on/chon-noi-lam-all-on/ |
| 9 | C09 | Quy trình, gây mê, số buổi & thời gian hồi phục | B | S4 | 17 | — | 5% | 2 | S2 (31–60n) | MỚI: /kien-thuc/all-on/quy-trinh-all-on-4-6/ |
| 10 | C13 | Người cao tuổi & bệnh lý nền — ai làm được, ai không ⭐⭐ | B | S1 | 17 | — | 3% | 3 | S2 (31–60n) | MỚI: /kien-thuc/all-on/all-on-cho-nguoi-cao-tuoi/ |
| 11 | C10 | Vệ sinh dưới khung răng & tái khám định kỳ ⭐ | C | S5 | 17 | — | 7% | 1 | S3 (61–90n) | MỚI: /kien-thuc/cham-soc/ve-sinh-rang-all-on/ |
| 12 | C12 | Y khoa: lực nhai, khớp cắn & tiêu xương sau toàn hàm (E-E-A-T) | C | S2 | 17 | — | 5% | — | S3 (61–90n) | ⚠ đối chiếu: trang hỏi đáp |
| 13 | C15 | Cross-sell hàm còn lại & duy trì dài hạn (LTV) | C | S6 | 17 | — | 3% | — | S3 (61–90n) | MỚI: /chuyen-khoa/implant/ |
| 14 | C01 | Nhận biết mất răng toàn hàm & hệ quả toàn thân | D | S1 | 17 | — | 2% | — | Nền (>90n) | MỚI: /kien-thuc/all-on/mat-rang-toan-ham/ |
| 15 | C02 | Hàm giả tháo lắp truyền thống — vì sao khách muốn đổi | D | S1 | 17 | — | 1% | — | Nền (>90n) | MỚI: /kien-thuc/all-on/ham-gia-thao-lap/ |

---

## 4. Niềng răng mắc cài (kim loại · sứ · pha lê · mặt trong)

`04-niengmaccai.json` · NKC · Chỉnh nha — Niềng răng · **40 bài cần sản xuất**

**Quy mô bộ:** 255 truy vấn · 15 cụm · 9 nhóm đối tượng · 62 truy vấn CORE 80/20 (24% bộ) chiếm 53% điểm ưu tiên

**Nỗi sợ quyết định (mọi nội dung phải gỡ được ít nhất một):**

- ① SỢ — SỢ XẤU SUỐT 2 NĂM ĐEO MẮC CÀI, SỢ ĐỒNG NGHIỆP VÀ KHÁCH HÀNG NHÌN → cụm xử lý **C03 + C06 + C13** (51 truy vấn, 25 CORE)
- ② NGỜ — SỢ BÁC SĨ NON TAY LÀM LỆCH KHỚP CẮN, TỤT LỢI, CHẾT TUỶ, PHẢI NIỀNG LẠI → cụm xử lý **C06 + C11 + C08** (51 truy vấn, 37 CORE)
- ③ NGẠI — SỢ KÉO DÀI VÔ THỜI HẠN VÀ CHI PHÍ PHÁT SINH MỖI LẦN SIẾT → cụm xử lý **C07 + C09 + C04** (51 truy vấn, 12 CORE)

**Hành trình 6 giai đoạn:**

| GĐ | Ưu tiên | Nỗi sợ chi phối | Cụm | TV | CORE | % điểm |
|---|---|---|---|---|---|---|
| S1 | ★ Nền | Sợ bị chê răng khấp khểnh, hô, thưa. Chưa biết răng lệch còn ảnh hưởng ăn nhai và phát âm. | C01 · C02 · C13 | 51 | 0 | 7% |
| S2 | ★★ | Sợ chọn sai loại mắc cài: kim loại rẻ nhưng lộ, sứ đẹp nhưng dễ bung, mặt trong đắt và khó vệ sinh. Không ai nói thật nhược điểm từng loại. | C03 · C04 · C05 · C12 | 68 | 13 | 25% |
| S3 | ★★★ Quyết định | SỢ GIAO 2 NĂM CUỘC ĐỜI CHO NGƯỜI MÌNH KHÔNG BIẾT TAY NGHỀ. Khách hỏi: niềng có đau không, có phải nhổ răng không, có tụt lợi không, bác sĩ có theo đến hết lộ trình không, nếu nửa đường bác sĩ nghỉ thì sao. | C06 · C07 · C08 · C11 · C14 | 85 | 49 | 53% |
| S4 | ★★ | Sợ phải đi siết mỗi tháng — khách tỉnh sợ tốn kém đi lại suốt 2 năm. | C09 | 17 | 0 | 7% |
| S5 | ★★ | Sợ tháo niềng rồi răng chạy lại, mất cả công sức và tiền. Sợ quên đeo hàm duy trì. | C10 | 17 | 0 | 5% |
| S6 | ★ Nền | Niềng xong lại thấy răng xỉn màu hoặc cười hở nướu — sợ làm tiếp thì lại tốn. | C15 | 17 | 0 | 3% |

**Phân bổ 80/20:**

| Tầng | Cụm | TV | % điểm | Phân bổ & danh sách cụm |
|---|---|---|---|---|
| A | 5 | 85 | 53% | 70% — C06 Đau, nhổ răng, tụt lợi & biến chứng · C11 Niềng thất bại, răng chạy lại & niềng lần hai · C07 Chi phí theo loại mắc cài & trả góp · C08 Chọn bác sĩ chỉnh nha theo hết lộ trình · C14 Thực thể & kiểm chứng (Ormco Diamond Star). Làm trong 90 ngày. Đây là bộ mà nỗi sợ 'ai theo tôi suốt 2 năm' chi phối toàn bộ quyết định — C08 phải trả lời thẳng câu đó. |
| B | 5 | 85 | 29% | 20% — C03 So sánh 4 loại mắc cài, nêu cả nhược điểm · C09 Lộ trình, số lần siết & khách tỉnh · C04 Chẩn đoán: X-quang, khớp cắn, phân loại hô-thụt · C05 Khi nào KHÔNG cần niềng · C13 Niềng cho người trưởng thành & tuổi vàng của trẻ. C03 là cụm xây E-E-A-T mạnh nhất vì đối thủ chỉ viết ưu điểm. |
| C | 3 | 51 | 15% | 10% — C10 Hàm duy trì & tái khám sau tháo niềng · C12 Y khoa: khớp cắn, tuỷ, nha chu trong chỉnh nha · C15 Cross-sell tẩy trắng & cắt lợi sau niềng. Chạy nền, tái sử dụng cho CSKH. |
| D | 2 | 34 | 3% | 0% ngân sách mới — C01 Nhận biết răng lệch · C02 Mẹo dân gian & niềng tại nhà (CẢNH BÁO: cụm này traffic rất lớn quanh 'niềng răng tại nhà' nhưng là nội dung nguy hiểm — Paris viết để CẢNH BÁO, không hướng dẫn). |

**Bản đồ nội dung — 15 cụm:**

| Hạng | Mã | Cụm chủ đề | Tầng | GĐ | TV | CORE | % điểm | Bài | Sóng | Trang đích |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | C06 | Đau, nhổ răng, tụt lợi & biến chứng khi niềng ⭐⭐⭐ | A | S3 | 17 | 14 | 13% | 8 | S1 (0–30n) | MỚI: /kien-thuc/nieng-rang/nieng-rang-co-dau-khong/ |
| 2 | C11 | Niềng thất bại, răng chạy lại & niềng lần hai ⭐⭐⭐ | A | S3 | 17 | 13 | 12% | 7 | S1 (0–30n) | MỚI: /kien-thuc/nieng-rang/nieng-that-bai-nieng-lai/ |
| 3 | C07 | Chi phí theo loại mắc cài & trả góp ⭐⭐⭐ | A | S3 | 17 | 12 | 11% | 3 | S1 (0–30n) | ⚠ đối chiếu: /hoan-my-bang-gia-dich-vu-nha-khoa.html + MỚI: /bang-gia/nieng-rang/ |
| 4 | C08 | Chọn bác sĩ chỉnh nha — ai theo tôi suốt lộ trình ⭐⭐⭐ | A | S3 | 17 | 12 | 11% | 4 | S1 (0–30n) | MỚI: /kien-thuc/nieng-rang/chon-bac-si-chinh-nha/ |
| 5 | C14 | Thực thể & kiểm chứng: Ormco Diamond Star · bác sĩ · giấy phép ⭐⭐ | A | S3 | 17 | 11 | 6% | 2 | S1 (0–30n) | MỚI: /chuyen-khoa/chinh-nha/ |
| 6 | C03 | So sánh 4 loại mắc cài — nêu cả nhược điểm ⭐⭐⭐ | B | S2 | 17 | — | 9% | 5 | S2 (31–60n) | MỚI: /kien-thuc/nieng-rang/cac-loai-mac-cai/ |
| 7 | C09 | Lộ trình, số lần siết & giải pháp cho khách tỉnh ⭐⭐ | B | S4 | 17 | — | 7% | 3 | S2 (31–60n) | MỚI: /kien-thuc/nieng-rang/nieng-rang-bao-lau/ |
| 8 | C04 | Chẩn đoán: X-quang, khớp cắn & phân loại hô – thụt – thưa | B | S2 | 17 | — | 6% | 2 | S2 (31–60n) | MỚI: /kien-thuc/nieng-rang/phan-loai-khop-can/ |
| 9 | C05 | Khi nào KHÔNG cần niềng — phương án nhẹ hơn ⭐⭐⭐ | B | S2 | 17 | — | 4% | 2 | S2 (31–60n) | MỚI: /kien-thuc/bao-ton/khi-nao-khong-can-nieng/ |
| 10 | C13 | Niềng cho người trưởng thành & tuổi vàng của trẻ | B | S1 | 17 | — | 3% | 3 | S2 (31–60n) | MỚI: /kien-thuc/nieng-rang/nieng-rang-nguoi-truong-thanh/ |
| 11 | C10 | Hàm duy trì & tái khám sau tháo niềng ⭐⭐ | C | S5 | 17 | — | 7% | 1 | S3 (61–90n) | MỚI: /kien-thuc/cham-soc/ham-duy-tri-sau-nieng/ |
| 12 | C12 | Y khoa: khớp cắn, tuỷ & nha chu trong chỉnh nha (E-E-A-T) | C | S2 | 17 | — | 5% | — | S3 (61–90n) | ⚠ đối chiếu: trang hỏi đáp |
| 13 | C15 | Cross-sell sau niềng: tẩy trắng · cắt lợi · dán sứ (LTV) | C | S6 | 17 | — | 3% | — | S3 (61–90n) | MỚI: /chuyen-khoa/nha-khoa-tham-my/ |
| 14 | C01 | Nhận biết răng lệch, hô, thưa & ảnh hưởng chức năng | D | S1 | 17 | — | 2% | — | Nền (>90n) | MỚI: /kien-thuc/nieng-rang/tu-danh-gia-rang-lech/ |
| 15 | C02 | Mẹo dân gian & 'niềng tại nhà' — viết để CẢNH BÁO | D | S1 | 17 | — | 1% | — | Nền (>90n) | MỚI: /kien-thuc/nieng-rang/canh-bao-nieng-tai-nha/ |

---

## 5. Invisalign — niềng răng trong suốt

`05-invisalign.json` · NKC · Chỉnh nha — Niềng răng · **35 bài cần sản xuất**

**Quy mô bộ:** 255 truy vấn · 15 cụm · 8 nhóm đối tượng · 60 truy vấn CORE 80/20 (24% bộ) chiếm 53% điểm ưu tiên

**Nỗi sợ quyết định (mọi nội dung phải gỡ được ít nhất một):**

- ① NGỜ — SỢ MUA ĐẮT MÀ KHAY KHÔNG PHẢI INVISALIGN CHÍNH HÃNG, CHỈ LÀ KHAY NỘI ĐỊA ĐỔI TÊN → cụm xử lý **C03 + C14 + C07** (51 truy vấn, 38 CORE)
- ② NGỜ — SỢ TRẢ GIÁ CAO NHẤT MÀ KẾT QUẢ KHÔNG BẰNG MẮC CÀI, CA NẶNG KHÔNG KÉO NỔI → cụm xử lý **C05 + C06 + C11** (51 truy vấn, 22 CORE)
- ③ NGẠI — SỢ KHÔNG ĐỦ KỶ LUẬT ĐEO 20–22 GIỜ/NGÀY RỒI LỘ TRÌNH KÉO DÀI VÔ HẠN → cụm xử lý **C09 + C10 + C04** (51 truy vấn, 0 CORE)

**Hành trình 6 giai đoạn:**

| GĐ | Ưu tiên | Nỗi sợ chi phối | Cụm | TV | CORE | % điểm |
|---|---|---|---|---|---|---|
| S1 | ★ Nền | Người đi làm, người có nghề phải giao tiếp: muốn chỉnh răng nhưng không muốn ai biết mình đang niềng. | C01 · C02 · C13 | 51 | 0 | 7% |
| S2 | ★★ | Không phân biệt được Invisalign chính hãng với khay trong suốt nói chung. Sợ bị bán 'niềng trong suốt' giá Invisalign. | C03 · C04 · C05 · C12 | 68 | 26 | 26% |
| S3 | ★★★ Quyết định | NGỜ VỀ VẬT LIỆU LÀ RÀO CAO NHẤT: khay có đúng Invisalign không, kiểm tra thế nào, phòng khám có phải đối tác được hãng công nhận không. Kèm nỗi sợ trả giá cao nhất mà ca nặng không kéo nổi. | C06 · C07 · C08 · C11 · C14 | 85 | 34 | 53% |
| S4 | ★★ | Sợ không đủ kỷ luật tự đeo, sợ quên khay khi đi ăn ngoài, sợ lộ trình bị kéo dài vì lỗi của mình. | C09 | 17 | 0 | 6% |
| S5 | ★★ | Sợ khay vàng, có mùi; sợ tháo xong răng chạy lại. | C10 | 17 | 0 | 5% |
| S6 | ★ Nền | Niềng xong muốn trắng răng nhưng sợ dán sứ lại phải mài. | C15 | 17 | 0 | 3% |

**Phân bổ 80/20:**

| Tầng | Cụm | TV | % điểm | Phân bổ & danh sách cụm |
|---|---|---|---|---|
| A | 5 | 85 | 53% | 70% — C03 Invisalign chính hãng & cách tự kiểm chứng · C14 Thực thể: Paris hạng Black Diamond · C07 Chi phí theo số khay & trả góp · C06 Hiệu quả thật, giới hạn & rủi ro · C11 Không đạt kết quả & phương án chuyển mắc cài. C03 và C14 ĐƯỢC ĐẨY LÊN TẦNG A (khác mặc định) vì hạng Invisalign Black Diamond là bằng chứng mạnh nhất Paris có và là thứ đối thủ không sao chép được. |
| B | 5 | 85 | 29% | 20% — C05 Khi nào mắc cài hợp hơn Invisalign · C08 Chọn bác sĩ có kinh nghiệm Invisalign · C09 Số khay, thời gian & kỷ luật đeo · C04 Chẩn đoán & mô phỏng ClinCheck 3D · C13 Nhóm nghề đặc thù & người trưởng thành. C05 là cụm dám nói điều bất lợi — AI trích mạnh nhất. |
| C | 3 | 51 | 15% | 10% — C10 Vệ sinh khay & hàm duy trì · C12 Y khoa: lực chỉnh, khớp cắn, attachment · C15 Cross-sell thẩm mỹ sau niềng. Chạy nền. |
| D | 2 | 34 | 3% | 0% ngân sách mới — C01 Nhận biết nhu cầu chỉnh nha vô hình · C02 Khay trong suốt mua online — viết để CẢNH BÁO. |

**Bản đồ nội dung — 15 cụm:**

| Hạng | Mã | Cụm chủ đề | Tầng | GĐ | TV | CORE | % điểm | Bài | Sóng | Trang đích |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | C03 | Invisalign chính hãng & cách tự kiểm chứng khay ⭐⭐⭐ | A | S2 | 17 | 14 | 13% | 6 | S1 (0–30n) | MỚI: /kien-thuc/invisalign/invisalign-chinh-hang/ |
| 2 | C14 | Thực thể: Paris hạng Invisalign Black Diamond — ý nghĩa & kiểm chứng ⭐⭐⭐ | A | S3 | 17 | 13 | 12% | 4 | S1 (0–30n) | MỚI: /chuyen-khoa/invisalign/ |
| 3 | C07 | Chi phí theo số khay, mức ca & trả góp ⭐⭐⭐ | A | S3 | 17 | 12 | 11% | 4 | S1 (0–30n) | ⚠ đối chiếu: /hoan-my-bang-gia-dich-vu-nha-khoa.html + MỚI: /bang-gia/invisalign/ |
| 4 | C06 | Hiệu quả thật, giới hạn & rủi ro của niềng trong suốt ⭐⭐⭐ | A | S3 | 17 | 11 | 11% | 5 | S1 (0–30n) | MỚI: /kien-thuc/invisalign/invisalign-co-hieu-qua-khong/ |
| 5 | C11 | Không đạt kết quả & phương án chuyển sang mắc cài ⭐⭐ | A | S3 | 17 | 10 | 6% | 4 | S1 (0–30n) | MỚI: /kien-thuc/invisalign/invisalign-khong-hieu-qua/ |
| 6 | C05 | Khi nào mắc cài hợp hơn Invisalign ⭐⭐⭐ | B | S2 | 17 | — | 9% | 3 | S2 (31–60n) | MỚI: /kien-thuc/bao-ton/invisalign-hay-mac-cai/ |
| 7 | C08 | Chọn bác sĩ có kinh nghiệm Invisalign & số ca đã làm ⭐⭐ | B | S3 | 17 | — | 7% | 2 | S2 (31–60n) | MỚI: /kien-thuc/invisalign/chon-bac-si-invisalign/ |
| 8 | C09 | Số khay, thời gian & kỷ luật đeo 20–22 giờ | B | S4 | 17 | — | 6% | 2 | S2 (31–60n) | MỚI: /kien-thuc/invisalign/invisalign-bao-lau/ |
| 9 | C04 | Chẩn đoán & mô phỏng ClinCheck 3D trước khi quyết | B | S2 | 17 | — | 4% | 2 | S2 (31–60n) | MỚI: /kien-thuc/invisalign/mo-phong-clincheck/ |
| 10 | C13 | Nhóm nghề đặc thù: MC · giáo viên · sale · người trưởng thành | B | S1 | 17 | — | 3% | 2 | S2 (31–60n) | MỚI: /kien-thuc/invisalign/invisalign-cho-nguoi-di-lam/ |
| 11 | C10 | Vệ sinh khay, mùi, khay vàng & hàm duy trì ⭐ | C | S5 | 17 | — | 7% | 1 | S3 (61–90n) | MỚI: /kien-thuc/cham-soc/ve-sinh-khay-invisalign/ |
| 12 | C12 | Y khoa: lực chỉnh, attachment & khớp cắn (E-E-A-T) | C | S2 | 17 | — | 5% | — | S3 (61–90n) | ⚠ đối chiếu: trang hỏi đáp |
| 13 | C15 | Cross-sell sau niềng: tẩy trắng WhiteMax · Veneer (LTV) | C | S6 | 17 | — | 3% | — | S3 (61–90n) | MỚI: /chuyen-khoa/nha-khoa-tham-my/ |
| 14 | C01 | Nhận biết nhu cầu chỉnh nha mà không ai thấy | D | S1 | 17 | — | 2% | — | Nền (>90n) | MỚI: /kien-thuc/invisalign/nieng-vo-hinh-la-gi/ |
| 15 | C02 | Khay trong suốt mua online — viết để CẢNH BÁO | D | S1 | 17 | — | 1% | — | Nền (>90n) | MỚI: /kien-thuc/invisalign/canh-bao-khay-online/ |

---

## 6. Bọc răng sứ & răng sứ toàn hàm

`06-rangsu.json` · NKT · Nha khoa thẩm mỹ · **47 bài cần sản xuất**

**Quy mô bộ:** 255 truy vấn · 15 cụm · 9 nhóm đối tượng · 64 truy vấn CORE 80/20 (25% bộ) chiếm 55% điểm ưu tiên

**Nỗi sợ quyết định (mọi nội dung phải gỡ được ít nhất một):**

- ① SỢ — SỢ MÀI MẤT RĂNG THẬT RỒI KHÔNG HỒI PHỤC ĐƯỢC: CHẾT TUỶ, ĐAU DAI DẲNG, MẤT RĂNG → cụm xử lý **C06 + C05 + C12** (51 truy vấn, 27 CORE)
- ② NGỜ — SỢ PHÔI SỨ KHÔNG RÕ HÃNG: VÀI NĂM ĐEN VIỀN, NỨT, HỞ MÀ NƠI LÀM KHÔNG CÒN BẢO HÀNH → cụm xử lý **C03 + C11 + C14** (51 truy vấn, 37 CORE)
- ③ NGỜ — SỢ BỊ TƯ VẤN BỌC CẢ HÀM KHI LẼ RA CHỈ CẦN TẨY TRẮNG HOẶC NIỀNG → cụm xử lý **C05 + C04 + C07** (51 truy vấn, 12 CORE)

**Hành trình 6 giai đoạn:**

| GĐ | Ưu tiên | Nỗi sợ chi phối | Cụm | TV | CORE | % điểm |
|---|---|---|---|---|---|---|
| S1 | ★ Nền | Sợ bị chê răng xỉn, răng sâu đen; muốn nụ cười đẹp nhanh cho dịp cưới, phỏng vấn. | C01 · C02 · C13 | 51 | 0 | 6% |
| S2 | ★★ | SỢ BỊ TƯ VẤN LÀM NHIỀU HƠN CẦN. Không biết răng mình nên bọc, nên dán Veneer, nên niềng hay chỉ cần tẩy trắng. Không phân biệt được sứ toàn sứ với sứ kim loại. | C03 · C04 · C05 · C12 | 68 | 26 | 26% |
| S3 | ★★★ Quyết định | ĐÂY LÀ NỖI SỢ NẶNG NHẤT TOÀN NGÀNH NHA: MÀI RỒI KHÔNG HOÀN NGUYÊN. Khách hỏi: mài bao nhiêu men, có phải lấy tuỷ không, bao lâu thì hỏng, phôi có chính hãng không, hỏng thì tháo ra răng thật còn gì. | C06 · C07 · C08 · C11 · C14 | 85 | 38 | 55% |
| S4 | ★★ | Sợ đau khi mài, sợ phải đi nhiều buổi, sợ răng tạm xấu trong lúc chờ. | C09 | 17 | 0 | 6% |
| S5 | ★★ | Sợ ê buốt kéo dài sau bọc, sợ viền nướu đen, sợ ăn uống phải kiêng mãi. | C10 | 17 | 0 | 5% |
| S6 | ★ Nền | Làm từng phần mãi không giải quyết được gốc; sợ tốn thêm một lần nữa. | C15 | 17 | 0 | 2% |

**Phân bổ 80/20:**

| Tầng | Cụm | TV | % điểm | Phân bổ & danh sách cụm |
|---|---|---|---|---|
| A | 5 | 85 | 55% | 70% — C06 Mài răng, chết tuỷ & biến chứng không hồi phục · C11 Răng sứ hỏng, tháo ra & làm lại · C03 Phôi sứ & vật liệu: Nacera và cách kiểm chứng · C07 Chi phí theo răng, theo loại sứ & trả góp · C14 Thực thể & kiểm chứng. ĐÂY LÀ BỘ CÓ KHOẢNG TRỐNG AI LỚN NHẤT: đối thủ gần như không dám viết thẳng về mài răng và tháo sứ làm lại. Chiếm lĩnh ở đây là chiếm đúng nơi khách quyết định. |
| B | 5 | 85 | 28% | 20% — C05 Khi nào KHÔNG nên bọc răng sứ · C04 Chẩn đoán & kế hoạch điều trị trước khi mài · C08 Chọn cơ sở & bác sĩ · C09 Quy trình, số buổi & răng tạm · C13 Nhóm đặc thù: răng nhiễm màu kháng sinh, răng đã lấy tuỷ, cô dâu. C05 tuy Tầng B nhưng là KHÁC BIỆT E-E-A-T LỚN NHẤT của Paris — trang trụ cột C05 phải ra cùng đợt Tầng A, không chờ sóng 2. |
| C | 3 | 51 | 14% | 10% — C10 Ê buốt, viền nướu & chăm sóc sau bọc · C12 Y khoa: tuỷ, nha chu, khớp cắn · C15 Cross-sell nụ cười → hài hoà gương mặt. Chạy nền, tái sử dụng Zalo OA/CSKH. |
| D | 2 | 34 | 3% | 0% ngân sách mới — C01 Nhận biết vấn đề thẩm mỹ răng · C02 Mẹo làm trắng răng tại nhà (traffic rất lớn — chỉ viết pillar nền và dẫn về C05). |

**Bản đồ nội dung — 15 cụm:**

| Hạng | Mã | Cụm chủ đề | Tầng | GĐ | TV | CORE | % điểm | Bài | Sóng | Trang đích |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | C06 | Mài răng, chết tuỷ & biến chứng không hồi phục ⭐⭐⭐ | A | S3 | 17 | 14 | 13% | 9 | S1 (0–30n) | MỚI: /kien-thuc/rang-su/boc-rang-su-co-hai-khong/ |
| 2 | C11 | Răng sứ hỏng, tháo ra & làm lại ⭐⭐⭐ | A | S3 | 17 | 13 | 12% | 8 | S1 (0–30n) | MỚI: /kien-thuc/rang-su/thao-rang-su-lam-lai/ |
| 3 | C03 | Phôi sứ & vật liệu: Nacera, toàn sứ vs sứ kim loại ⭐⭐⭐ | A | S2 | 17 | 13 | 12% | 6 | S1 (0–30n) | MỚI: /kien-thuc/rang-su/cac-loai-rang-su/ |
| 4 | C07 | Chi phí theo răng, theo loại sứ & trả góp ⭐⭐⭐ | A | S3 | 17 | 12 | 12% | 4 | S1 (0–30n) | ⚠ đối chiếu: /hoan-my-bang-gia-dich-vu-nha-khoa.html + MỚI: /bang-gia/rang-su/ |
| 5 | C14 | Thực thể & kiểm chứng: đối tác Nacera · bác sĩ · giấy phép ⭐⭐ | A | S3 | 17 | 12 | 6% | 2 | S1 (0–30n) | MỚI: /chuyen-khoa/nha-khoa-tham-my/ |
| 6 | C05 | Khi nào KHÔNG nên bọc răng sứ ⭐⭐⭐ | B | S2 | 17 | — | 9% | 5 | S2 (31–60n) | MỚI: /kien-thuc/bao-ton/khi-nao-khong-nen-boc-rang-su/ |
| 7 | C04 | Chẩn đoán & kế hoạch điều trị trước khi mài | B | S2 | 17 | — | 7% | 3 | S2 (31–60n) | MỚI: /kien-thuc/quy-trinh/ke-hoach-truoc-khi-boc-su/ |
| 8 | C08 | Chọn cơ sở & bác sĩ — labo tại chỗ hay gửi ngoài ⭐⭐ | B | S3 | 17 | — | 6% | 3 | S2 (31–60n) | MỚI: /kien-thuc/rang-su/chon-nha-khoa-boc-su/ |
| 9 | C09 | Quy trình, số buổi & răng tạm trong lúc chờ | B | S4 | 17 | — | 4% | 2 | S2 (31–60n) | MỚI: /kien-thuc/rang-su/quy-trinh-boc-rang-su/ |
| 10 | C13 | Nhóm đặc thù: nhiễm màu kháng sinh · răng đã lấy tuỷ · cô dâu | B | S1 | 17 | — | 3% | 3 | S2 (31–60n) | MỚI: /kien-thuc/rang-su/rang-nhiem-mau-khang-sinh/ |
| 11 | C10 | Ê buốt, viền nướu đen & chăm sóc sau bọc ⭐⭐ | C | S5 | 17 | — | 7% | 2 | S3 (61–90n) | MỚI: /kien-thuc/cham-soc/cham-soc-rang-su/ |
| 12 | C12 | Y khoa: tuỷ, nha chu & khớp cắn (E-E-A-T) | C | S2 | 17 | — | 5% | — | S3 (61–90n) | ⚠ đối chiếu: trang hỏi đáp |
| 13 | C15 | Cross-sell: nụ cười → hài hoà gương mặt (LTV) | C | S6 | 17 | — | 2% | — | S3 (61–90n) | MỚI: /goi-gia-dinh.html |
| 14 | C01 | Nhận biết vấn đề thẩm mỹ răng & tự đánh giá | D | S1 | 17 | — | 1% | — | Nền (>90n) | MỚI: /kien-thuc/rang-su/tu-danh-gia-rang-cua-ban/ |
| 15 | C02 | Mẹo làm trắng răng tại nhà (đặc thù VN) | D | S1 | 17 | — | 1% | — | Nền (>90n) | MỚI: /kien-thuc/rang-su/meo-lam-trang-rang-tai-nha/ |

---

## 7. Mặt dán sứ Veneer

`07-veneer.json` · NKT · Nha khoa thẩm mỹ · **34 bài cần sản xuất**

**Quy mô bộ:** 255 truy vấn · 15 cụm · 7 nhóm đối tượng · 58 truy vấn CORE 80/20 (23% bộ) chiếm 52% điểm ưu tiên

**Nỗi sợ quyết định (mọi nội dung phải gỡ được ít nhất một):**

- ① SỢ — SỢ VẪN PHẢI MÀI MEN DÙ ĐƯỢC QUẢNG CÁO LÀ 'KHÔNG MÀI', VÀ MEN KHÔNG MỌC LẠI → cụm xử lý **C06 + C05 + C03** (51 truy vấn, 27 CORE)
- ② NGỜ — SỢ DÁN XONG BỊ BONG, HỞ VIỀN, NỨT KHI ĂN ĐỒ CỨNG MÀ KHÔNG AI BẢO HÀNH → cụm xử lý **C11 + C14 + C10** (51 truy vấn, 23 CORE)
- ③ NGẠI — SỢ TRẢ GIÁ CAO HƠN BỌC SỨ MÀ KHÔNG BIẾT CÓ ĐÚNG CHỈ ĐỊNH CHO RĂNG MÌNH → cụm xử lý **C07 + C04 + C08** (51 truy vấn, 20 CORE)

**Hành trình 6 giai đoạn:**

| GĐ | Ưu tiên | Nỗi sợ chi phối | Cụm | TV | CORE | % điểm |
|---|---|---|---|---|---|---|
| S1 | ★ Nền | Muốn nụ cười đẹp tự nhiên, thấy Veneer trên mạng xã hội nhưng chưa hiểu khác bọc sứ ở đâu. | C01 · C02 · C13 | 51 | 0 | 7% |
| S2 | ★★ | Sợ được bán Veneer trong khi răng mình cần niềng, hoặc ngược lại bị bọc sứ trong khi Veneer đủ. Không phân biệt được Veneer sứ, composite và 'dán sứ siêu mỏng'. | C03 · C04 · C05 · C12 | 68 | 27 | 26% |
| S3 | ★★★ Quyết định | 'KHÔNG MÀI RĂNG' LÀ CÂU QUẢNG CÁO KHÁCH NGỜ NHẤT. Khách hỏi: thật sự có mài không, mài bao nhiêu, bong thì dán lại được không, dùng được bao lâu, giá cao hơn bọc sứ để được gì. | C06 · C07 · C08 · C11 · C14 | 85 | 31 | 52% |
| S4 | ★★ | Sợ thử răng xong không giống mô phỏng, sợ không được xem trước khi dán cố định. | C09 | 17 | 0 | 7% |
| S5 | ★★ | Sợ bong mặt dán khi ăn, sợ đổi màu chỗ keo dán, sợ phải kiêng vĩnh viễn. | C10 | 17 | 0 | 5% |
| S6 | ★ Nền | Dán mấy răng trước rồi thấy răng sau không đều màu, sợ làm tiếp lại tốn. | C15 | 17 | 0 | 3% |

**Phân bổ 80/20:**

| Tầng | Cụm | TV | % điểm | Phân bổ & danh sách cụm |
|---|---|---|---|---|
| A | 5 | 85 | 52% | 70% — C06 'Không mài răng' thật hay không & rủi ro men răng · C11 Bong, nứt, hở viền & dán lại · C05 Veneer hay bọc sứ hay niềng: khi nào KHÔNG nên Veneer · C07 Chi phí theo răng & so với bọc sứ · C14 Thực thể & kiểm chứng. C05 ĐƯỢC ĐẨY LÊN TẦNG A ở bộ này vì chỉ định sai là nguyên nhân số một của ca Veneer thất bại. |
| B | 5 | 85 | 30% | 20% — C03 Loại mặt dán & vật liệu · C04 Chẩn đoán, thiết kế nụ cười & mô phỏng · C08 Chọn bác sĩ & labo · C09 Quy trình, thử răng & số buổi · C13 Nhóm đặc thù: răng thưa nhẹ, răng nhiễm màu, người làm nghề hình ảnh. |
| C | 3 | 51 | 15% | 10% — C10 Chăm sóc & những gì phải kiêng · C12 Y khoa: men răng, khớp cắn & lực ăn nhai · C15 Cross-sell tẩy trắng răng còn lại. Chạy nền. |
| D | 2 | 34 | 3% | 0% ngân sách mới — C01 Nhận biết nhu cầu thiết kế nụ cười · C02 Xu hướng răng đẹp trên mạng xã hội. Chỉ pillar nền. |

**Bản đồ nội dung — 15 cụm:**

| Hạng | Mã | Cụm chủ đề | Tầng | GĐ | TV | CORE | % điểm | Bài | Sóng | Trang đích |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | C06 | 'Không mài răng' thật hay không & rủi ro mất men ⭐⭐⭐ | A | S3 | 17 | 14 | 13% | 6 | S1 (0–30n) | MỚI: /kien-thuc/veneer/dan-veneer-co-phai-mai-rang/ |
| 2 | C11 | Bong, nứt, hở viền & dán lại ⭐⭐⭐ | A | S3 | 17 | 12 | 11% | 5 | S1 (0–30n) | MỚI: /kien-thuc/veneer/veneer-bi-bong-lam-lai/ |
| 3 | C05 | Veneer hay bọc sứ hay niềng — khi nào KHÔNG nên Veneer ⭐⭐⭐ | A | S2 | 17 | 13 | 11% | 5 | S1 (0–30n) | MỚI: /kien-thuc/bao-ton/khi-nao-khong-nen-dan-veneer/ |
| 4 | C07 | Chi phí theo răng & so sánh với bọc răng sứ ⭐⭐⭐ | A | S3 | 17 | 11 | 11% | 3 | S1 (0–30n) | ⚠ đối chiếu: /hoan-my-bang-gia-dich-vu-nha-khoa.html + MỚI: /bang-gia/veneer/ |
| 5 | C14 | Thực thể & kiểm chứng: bác sĩ thẩm mỹ · ESCD · labo ⭐⭐ | A | S3 | 17 | 8 | 6% | 2 | S1 (0–30n) | MỚI: /chuyen-khoa/nha-khoa-tham-my/ |
| 6 | C03 | Loại mặt dán & vật liệu: sứ · composite · siêu mỏng | B | S2 | 17 | — | 9% | 4 | S2 (31–60n) | MỚI: /kien-thuc/veneer/cac-loai-mat-dan-su/ |
| 7 | C04 | Chẩn đoán, thiết kế nụ cười & mô phỏng trước khi làm | B | S2 | 17 | — | 7% | 2 | S2 (31–60n) | MỚI: /kien-thuc/veneer/thiet-ke-nu-cuoi/ |
| 8 | C08 | Chọn bác sĩ & labo — tay nghề quyết định kết quả ⭐⭐ | B | S3 | 17 | — | 6% | 2 | S2 (31–60n) | MỚI: /kien-thuc/veneer/chon-bac-si-dan-veneer/ |
| 9 | C09 | Quy trình, thử răng & số buổi | B | S4 | 17 | — | 5% | 2 | S2 (31–60n) | MỚI: /kien-thuc/veneer/quy-trinh-dan-veneer/ |
| 10 | C13 | Nhóm đặc thù: răng thưa nhẹ · nhiễm màu · nghề hình ảnh | B | S1 | 17 | — | 3% | 2 | S2 (31–60n) | MỚI: /kien-thuc/veneer/veneer-cho-rang-thua/ |
| 11 | C10 | Chăm sóc & những gì phải kiêng sau dán ⭐ | C | S5 | 17 | — | 7% | 1 | S3 (61–90n) | MỚI: /kien-thuc/cham-soc/cham-soc-mat-dan-su/ |
| 12 | C12 | Y khoa: men răng, khớp cắn & lực ăn nhai (E-E-A-T) | C | S2 | 17 | — | 5% | — | S3 (61–90n) | ⚠ đối chiếu: trang hỏi đáp |
| 13 | C15 | Cross-sell: tẩy trắng các răng còn lại (LTV) | C | S6 | 17 | — | 3% | — | S3 (61–90n) | MỚI: /chuyen-khoa/nha-khoa-tham-my/ |
| 14 | C01 | Nhận biết nhu cầu thiết kế nụ cười | D | S1 | 17 | — | 2% | — | Nền (>90n) | MỚI: /kien-thuc/veneer/nu-cuoi-hai-hoa-la-gi/ |
| 15 | C02 | Xu hướng răng đẹp trên mạng xã hội | D | S1 | 17 | — | 1% | — | Nền (>90n) | MỚI: /kien-thuc/veneer/xu-huong-rang-dep/ |

---

## 8. Nha khoa tổng quát (nhổ răng · trám · tuỷ · cạo vôi · tẩy trắng)

`08-tongquat.json` · NKG · Nha khoa tổng quát & Nha chu · **45 bài cần sản xuất**

**Quy mô bộ:** 255 truy vấn · 15 cụm · 10 nhóm đối tượng · 60 truy vấn CORE 80/20 (24% bộ) chiếm 51% điểm ưu tiên

**Nỗi sợ quyết định (mọi nội dung phải gỡ được ít nhất một):**

- ① SỢ — SỢ ĐAU KHI NHỔ VÀ KHOAN: SỢ TIẾNG MÁY, SỢ TÊ KHÔNG ĂN THUỐC, SỢ CHẢY MÁU → cụm xử lý **C06 + C09 + C03** (51 truy vấn, 26 CORE)
- ② NGỜ — SỢ BỊ CHỈ ĐỊNH ĐIỀU TRỊ TUỶ HOẶC NHỔ RĂNG KHI RĂNG CÒN GIỮ ĐƯỢC → cụm xử lý **C05 + C04 + C12** (51 truy vấn, 13 CORE)
- ③ NGẠI — DỊCH VỤ NHỎ NÊN KHÔNG AI BÁO GIÁ RÕ, SỢ ĐẾN NƠI MỚI BIẾT PHẢI LÀM THÊM → cụm xử lý **C07 + C08 + C11** (51 truy vấn, 29 CORE)

**Hành trình 6 giai đoạn:**

| GĐ | Ưu tiên | Nỗi sợ chi phối | Cụm | TV | CORE | % điểm |
|---|---|---|---|---|---|---|
| S1 | ★ Nền | Đau răng, ê buốt, hôi miệng mà không ai nói. Sợ răng sâu rồi mất luôn. Chưa biết phải khám hay chịu đựng tiếp. | C01 · C02 · C13 | 51 | 0 | 8% |
| S2 | ★★ | SỢ BỊ TƯ VẤN LÀM NHIỀU HƠN CẦN — nhổ khi còn giữ được, lấy tuỷ khi chỉ cần trám. Không biết răng khôn của mình có thật sự cần nhổ. | C03 · C04 · C05 · C12 | 68 | 18 | 25% |
| S3 | ★★★ Quyết định | Ở dịch vụ tổng quát, nỗi sợ ĐAU và nỗi NGẠI chi phí mập mờ mạnh hơn nỗi sợ hỏng. Khách hỏi: nhổ răng khôn có đau không, mất bao lâu, giá bao nhiêu, lấy tuỷ xong răng có yếu không, chỗ nào tê tốt. | C06 · C07 · C08 · C11 · C14 | 85 | 42 | 51% |
| S4 | ★★ | Sợ phải nghỉ làm, sợ sưng mặt không gặp được khách; muốn làm xong trong một buổi. | C09 | 17 | 0 | 8% |
| S5 | ★★ | Sợ chảy máu kéo dài sau nhổ, sợ ổ răng nhiễm trùng mà không biết dấu hiệu. | C10 | 17 | 0 | 6% |
| S6 | ★ Nền | Mất răng rồi mới biết phải trồng lại; sợ tốn thêm một lần nữa. | C15 | 17 | 0 | 2% |

**Phân bổ 80/20:**

| Tầng | Cụm | TV | % điểm | Phân bổ & danh sách cụm |
|---|---|---|---|---|
| A | 5 | 85 | 51% | 70% — C06 Đau, tê & biến chứng khi nhổ / lấy tuỷ · C07 Chi phí từng dịch vụ nhỏ, công khai theo răng · C09 Số buổi & phục hồi sau nhổ · C08 Chọn cơ sở gần & bác sĩ · C14 Thực thể: Piezotome · RECIPROC BLUE · WhiteMax. C09 ĐƯỢC ĐẨY LÊN TẦNG A ở bộ này vì khách tổng quát quyết định theo 'mất bao lâu, có nghỉ làm không' nhiều hơn theo tay nghề. Đây cũng là CỬA VÀO RẺ NHẤT của hệ thống — khách tổng quát là nguồn khách Implant và niềng của 2 năm sau. |
| B | 5 | 85 | 31% | 20% — C05 Khi nào KHÔNG cần nhổ / không cần lấy tuỷ · C03 Phương pháp: Piezotome, RECIPROC BLUE, trám thẩm mỹ, WhiteMax · C04 Chẩn đoán & X-quang răng khôn · C11 Làm lại: trám bong, tuỷ tái nhiễm · C13 Nhóm đặc thù: phụ nữ mang thai, người sợ nha sĩ, người cao tuổi. |
| C | 3 | 51 | 15% | 10% — C10 Chăm sóc sau nhổ & dấu hiệu bất thường · C12 Y khoa: tuỷ, nha chu, răng khôn lệch (E-E-A-T) · C15 Cross-sell: mất răng → Implant. Chạy nền. Nội dung hậu điều trị được Perplexity/Claude trích mạnh. |
| D | 2 | 34 | 3% | 0% ngân sách mới — C01 Nhận biết đau răng, ê buốt, hôi miệng · C02 Mẹo dân gian chữa đau răng (traffic rất lớn — viết pillar nền có cảnh báo). |

**Bản đồ nội dung — 15 cụm:**

| Hạng | Mã | Cụm chủ đề | Tầng | GĐ | TV | CORE | % điểm | Bài | Sóng | Trang đích |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | C06 | Đau, tê & biến chứng khi nhổ răng / lấy tuỷ ⭐⭐⭐ | A | S3 | 17 | 14 | 12% | 8 | S1 (0–30n) | MỚI: /kien-thuc/tong-quat/nho-rang-khon-co-dau-khong/ |
| 2 | C07 | Chi phí từng dịch vụ nhỏ — công khai theo răng ⭐⭐⭐ | A | S3 | 17 | 13 | 12% | 5 | S1 (0–30n) | ⚠ đối chiếu: /hoan-my-bang-gia-dich-vu-nha-khoa.html |
| 3 | C09 | Số buổi, thời gian & phục hồi sau nhổ ⭐⭐⭐ | A | S4 | 17 | 12 | 11% | 5 | S1 (0–30n) | MỚI: /kien-thuc/tong-quat/nho-rang-bao-lau-khoi/ |
| 4 | C08 | Chọn cơ sở gần & bác sĩ cho ca tổng quát ⭐⭐ | A | S3 | 17 | 11 | 10% | 3 | S1 (0–30n) | ⚠ đối chiếu: /tim-phong-kham.html |
| 5 | C14 | Thực thể & công nghệ: Piezotome · RECIPROC BLUE · WhiteMax ⭐⭐ | A | S3 | 17 | 10 | 6% | 3 | S1 (0–30n) | MỚI: /chuyen-khoa/nha-khoa-tong-quat/ |
| 6 | C05 | Khi nào KHÔNG cần nhổ, KHÔNG cần lấy tuỷ ⭐⭐⭐ | B | S2 | 17 | — | 9% | 4 | S2 (31–60n) | MỚI: /kien-thuc/bao-ton/khi-nao-khong-can-nho-rang/ |
| 7 | C03 | Phương pháp & công nghệ: siêu âm · tuỷ · trám · tẩy trắng | B | S2 | 17 | — | 8% | 5 | S2 (31–60n) | MỚI: /kien-thuc/tong-quat/cong-nghe-nho-rang-sieu-am/ |
| 8 | C04 | Chẩn đoán & X-quang răng khôn — có cần nhổ không | B | S2 | 17 | — | 6% | 3 | S2 (31–60n) | MỚI: /kien-thuc/tong-quat/rang-khon-co-can-nho/ |
| 9 | C11 | Làm lại: trám bong, tuỷ tái nhiễm, tẩy trắng không ăn ⭐⭐ | B | S3 | 17 | — | 5% | 3 | S2 (31–60n) | MỚI: /kien-thuc/tong-quat/tram-rang-bi-bong/ |
| 10 | C13 | Nhóm đặc thù: mang thai · người sợ nha sĩ · người cao tuổi | B | S1 | 17 | — | 3% | 3 | S2 (31–60n) | MỚI: /kien-thuc/tong-quat/nho-rang-khi-mang-thai/ |
| 11 | C10 | Chăm sóc sau nhổ & dấu hiệu bất thường ⭐⭐ | C | S5 | 17 | — | 8% | 2 | S3 (61–90n) | MỚI: /kien-thuc/cham-soc/cham-soc-sau-nho-rang/ |
| 12 | C12 | Y khoa: tuỷ, nha chu & răng khôn lệch (E-E-A-T) | C | S2 | 17 | — | 5% | 1 | S3 (61–90n) | ⚠ đối chiếu: trang hỏi đáp |
| 13 | C15 | Cross-sell: mất răng → Implant · răng lệch → niềng (LTV) | C | S6 | 17 | — | 2% | — | S3 (61–90n) | MỚI: /chuyen-khoa/implant/ |
| 14 | C01 | Nhận biết đau răng, ê buốt & hôi miệng | D | S1 | 17 | — | 2% | — | Nền (>90n) | MỚI: /kien-thuc/tong-quat/tu-danh-gia-rang-mieng/ |
| 15 | C02 | Mẹo dân gian chữa đau răng — viết pillar có cảnh báo | D | S1 | 17 | — | 1% | — | Nền (>90n) | MỚI: /kien-thuc/tong-quat/meo-chua-dau-rang/ |

---

## 9. Nha chu, viêm nướu & tụt lợi

`09-nhachu.json` · NKG · Nha khoa tổng quát & Nha chu · **37 bài cần sản xuất**

**Quy mô bộ:** 255 truy vấn · 15 cụm · 8 nhóm đối tượng · 56 truy vấn CORE 80/20 (22% bộ) chiếm 50% điểm ưu tiên

**Nỗi sợ quyết định (mọi nội dung phải gỡ được ít nhất một):**

- ① SỢ — SỢ RĂNG LUNG LAY RỒI RỤNG HẾT MÀ KHÔNG CÓ CÁCH NÀO GIỮ LẠI → cụm xử lý **C06 + C11 + C12** (51 truy vấn, 24 CORE)
- ② NGỜ — SỢ CẠO VÔI LÀM MÒN RĂNG, SỢ ĐIỀU TRỊ NHA CHU CHỈ LÀ CÁCH MOI THÊM TIỀN → cụm xử lý **C05 + C03 + C07** (51 truy vấn, 20 CORE)
- ③ NGẠI — ĐIỀU TRỊ NHIỀU ĐỢT, PHẢI DUY TRÌ CẢ ĐỜI, KHÔNG BIẾT KHI NÀO XONG → cụm xử lý **C09 + C10 + C04** (51 truy vấn, 12 CORE)

**Hành trình 6 giai đoạn:**

| GĐ | Ưu tiên | Nỗi sợ chi phối | Cụm | TV | CORE | % điểm |
|---|---|---|---|---|---|---|
| S1 | ★ Nền | Chảy máu khi đánh răng, hôi miệng, nướu sưng — tưởng là chuyện nhỏ, không biết đó là nha chu đang tiến triển. | C01 · C02 · C13 | 51 | 0 | 9% |
| S2 | ★★ | Không biết cạo vôi có đủ hay phải điều trị nha chu sâu. Sợ cạo vôi làm răng mòn, ê buốt, thưa ra. | C03 · C04 · C05 · C12 | 68 | 20 | 25% |
| S3 | ★★★ Quyết định | SỢ MẤT RĂNG THẬT KHÔNG PHANH ĐƯỢC. Khách hỏi: răng lung lay còn giữ được không, nha chu có chữa khỏi không, điều trị bao nhiêu tiền, có phải làm cả đời không, tụt lợi có mọc lại được không. | C06 · C07 · C08 · C11 · C14 | 85 | 36 | 50% |
| S4 | ★★ | Sợ đau khi lấy cao dưới nướu, sợ phải phẫu thuật nướu, sợ phải đi nhiều đợt. | C09 | 17 | 0 | 7% |
| S5 | ★★ | Sợ tái phát sau điều trị; không biết duy trì thế nào cho đúng ở nhà. | C10 | 17 | 0 | 7% |
| S6 | ★ Nền | Nha chu ổn rồi nhưng đã mất mấy răng — sợ trồng lại thì nền nướu không đủ tốt. | C15 | 17 | 0 | 2% |

**Phân bổ 80/20:**

| Tầng | Cụm | TV | % điểm | Phân bổ & danh sách cụm |
|---|---|---|---|---|
| A | 5 | 85 | 50% | 70% — C06 Răng lung lay, tụt lợi & nguy cơ mất răng · C11 Nha chu tái phát & điều trị lại · C05 Cạo vôi có đủ hay cần điều trị nha chu sâu · C07 Chi phí theo đợt & theo vùng · C14 Thực thể & kiểm chứng. ĐÂY LÀ BỘ ĐỐI THỦ BỎ TRỐNG NHIỀU NHẤT: nha chu không phải dịch vụ giá trị lớn nên hầu như không ai làm nội dung tử tế. Phủ ở đây vừa rẻ vừa xây E-E-A-T y khoa cho cả hệ thống. |
| B | 5 | 85 | 30% | 20% — C03 Phương pháp: cạo vôi · lấy cao dưới nướu · phẫu thuật nướu · ghép nướu · C04 Chẩn đoán: đo túi nha chu, X-quang tiêu xương · C09 Số đợt & quy trình · C08 Chọn cơ sở & bác sĩ nha chu · C13 Nhóm đặc thù: tiểu đường, mang thai, người hút thuốc. |
| C | 3 | 51 | 17% | 10% — C10 Duy trì tại nhà & tái khám định kỳ · C12 Y khoa: liên hệ nha chu – tim mạch – tiểu đường (E-E-A-T mạnh nhất hệ thống) · C15 Cross-sell phục hình sau nha chu. Chạy nền nhưng C12 đáng đầu tư vì là nội dung y khoa AI trích nhiều. |
| D | 2 | 34 | 3% | 0% ngân sách mới — C01 Nhận biết chảy máu nướu & hôi miệng · C02 Mẹo dân gian trị viêm nướu. Chỉ pillar nền. |

**Bản đồ nội dung — 15 cụm:**

| Hạng | Mã | Cụm chủ đề | Tầng | GĐ | TV | CORE | % điểm | Bài | Sóng | Trang đích |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | C06 | Răng lung lay, tụt lợi & nguy cơ mất răng ⭐⭐⭐ | A | S3 | 17 | 13 | 12% | 6 | S1 (0–30n) | MỚI: /kien-thuc/nha-chu/rang-lung-lay-co-giu-duoc-khong/ |
| 2 | C11 | Nha chu tái phát & điều trị lại ⭐⭐⭐ | A | S3 | 17 | 11 | 11% | 4 | S1 (0–30n) | MỚI: /kien-thuc/nha-chu/nha-chu-tai-phat/ |
| 3 | C05 | Cạo vôi có đủ hay cần điều trị nha chu sâu ⭐⭐⭐ | A | S2 | 17 | 12 | 11% | 5 | S1 (0–30n) | MỚI: /kien-thuc/bao-ton/cao-voi-hay-dieu-tri-nha-chu/ |
| 4 | C07 | Chi phí điều trị nha chu theo đợt & theo vùng ⭐⭐ | A | S3 | 17 | 11 | 10% | 3 | S1 (0–30n) | ⚠ đối chiếu: /hoan-my-bang-gia-dich-vu-nha-khoa.html |
| 5 | C14 | Thực thể & kiểm chứng: bác sĩ nha chu · giấy phép ⭐ | A | S3 | 17 | 9 | 6% | 2 | S1 (0–30n) | MỚI: /chuyen-khoa/nha-chu/ |
| 6 | C03 | Phương pháp: cạo vôi · lấy cao dưới nướu · phẫu thuật · ghép nướu | B | S2 | 17 | — | 9% | 4 | S2 (31–60n) | MỚI: /kien-thuc/nha-chu/cac-phuong-phap-dieu-tri-nha-chu/ |
| 7 | C04 | Chẩn đoán: đo túi nha chu & X-quang tiêu xương | B | S2 | 17 | — | 7% | 2 | S2 (31–60n) | MỚI: /kien-thuc/nha-chu/do-tui-nha-chu/ |
| 8 | C09 | Số đợt điều trị & quy trình từng đợt | B | S4 | 17 | — | 7% | 2 | S2 (31–60n) | MỚI: /kien-thuc/nha-chu/quy-trinh-dieu-tri-nha-chu/ |
| 9 | C08 | Chọn cơ sở & bác sĩ chuyên nha chu ⭐ | B | S3 | 17 | — | 4% | 2 | S2 (31–60n) | ⚠ đối chiếu: /tim-phong-kham.html |
| 10 | C13 | Nhóm đặc thù: tiểu đường · mang thai · người hút thuốc | B | S1 | 17 | — | 3% | 2 | S2 (31–60n) | MỚI: /kien-thuc/nha-chu/nha-chu-o-nguoi-tieu-duong/ |
| 11 | C12 | Y khoa: nha chu – tim mạch – tiểu đường (E-E-A-T) ⭐⭐ | C | S2 | 17 | — | 8% | 3 | S3 (61–90n) | MỚI: /kien-thuc/nha-chu/nha-chu-va-benh-toan-than/ |
| 12 | C10 | Duy trì tại nhà & tái khám định kỳ ⭐⭐ | C | S5 | 17 | — | 7% | 2 | S3 (61–90n) | MỚI: /kien-thuc/cham-soc/duy-tri-sau-dieu-tri-nha-chu/ |
| 13 | C15 | Cross-sell: phục hình sau khi nền nướu ổn (LTV) | C | S6 | 17 | — | 2% | — | S3 (61–90n) | MỚI: /chuyen-khoa/implant/ |
| 14 | C01 | Nhận biết chảy máu nướu, hôi miệng & vôi răng | D | S1 | 17 | — | 2% | — | Nền (>90n) | MỚI: /kien-thuc/nha-chu/dau-hieu-viem-nuou/ |
| 15 | C02 | Mẹo dân gian trị viêm nướu | D | S1 | 17 | — | 1% | — | Nền (>90n) | MỚI: /kien-thuc/nha-chu/meo-tri-viem-nuou/ |

---

## 10. Nha khoa trẻ em & gói gia đình

`10-trenem.json` · NKF · Nha khoa trẻ em & Gia đình · **40 bài cần sản xuất**

**Quy mô bộ:** 255 truy vấn · 15 cụm · 8 nhóm đối tượng · 56 truy vấn CORE 80/20 (22% bộ) chiếm 50% điểm ưu tiên

**Nỗi sợ quyết định (mọi nội dung phải gỡ được ít nhất một):**

- ① SỢ — SỢ CON SỢ NHA SĨ RỒI ÁM ẢNH CẢ ĐỜI, KHÔNG CHỊU HÁ MIỆNG LẦN SAU → cụm xử lý **C06 + C09 + C13** (51 truy vấn, 25 CORE)
- ② NGỜ — SỢ BỊ CHỈ ĐỊNH NHỔ RĂNG SỮA, TRÁM, NIỀNG SỚM KHI CON CHƯA CẦN → cụm xử lý **C05 + C04 + C03** (51 truy vấn, 12 CORE)
- ③ NGẠI — SỢ ĐỂ MUỘN THÌ HỎNG CẢ HÀM VĨNH VIỄN, NHƯNG CŨNG SỢ CAN THIỆP QUÁ SỚM → cụm xử lý **C11 + C12 + C07** (51 truy vấn, 19 CORE)

**Hành trình 6 giai đoạn:**

| GĐ | Ưu tiên | Nỗi sợ chi phối | Cụm | TV | CORE | % điểm |
|---|---|---|---|---|---|---|
| S1 | ★ Nền | Bố mẹ: thấy con sâu răng sữa nhưng nghe nói 'răng sữa rồi cũng rụng'. Chưa biết răng sữa hỏng ảnh hưởng răng vĩnh viễn. | C01 · C02 · C13 | 51 | 0 | 10% |
| S2 | ★★ | Không biết mấy tuổi thì đưa con đi khám, mấy tuổi là 'tuổi vàng' để chỉnh nha. Sợ bị bán niềng sớm khi chưa cần. | C03 · C04 · C05 · C12 | 68 | 19 | 25% |
| S3 | ★★★ Quyết định | BỐ MẸ QUYẾT ĐỊNH THEO MỘT NỖI SỢ KHÁC NGƯỜI LỚN: không sợ cho mình, sợ cho con. Sợ con bị cưỡng chế, sợ con khóc, sợ bác sĩ không biết dỗ trẻ, sợ con ám ảnh. Chi phí là rào thứ hai. | C06 · C07 · C08 · C11 · C14 | 85 | 37 | 50% |
| S4 | ★★ | Sợ con không hợp tác nên một buổi không xong, phải quay lại nhiều lần. Sợ phải gây mê để điều trị cho con. | C09 | 17 | 0 | 7% |
| S5 | ★★ | Sợ không biết tập cho con đánh răng đúng; sợ tái sâu ngay sau khi trám. | C10 | 17 | 0 | 6% |
| S6 | ★ Nền | Muốn cả nhà cùng theo một nơi nhưng sợ gói gia đình chỉ là cách bán thêm. | C15 | 17 | 0 | 2% |

**Phân bổ 80/20:**

| Tầng | Cụm | TV | % điểm | Phân bổ & danh sách cụm |
|---|---|---|---|---|
| A | 5 | 85 | 50% | 70% — C06 Con sợ nha sĩ & cách xử lý không cưỡng chế · C13 Theo từng mốc tuổi: răng sữa · hỗn hợp · tuổi vàng chỉnh nha · C05 Khi nào CHƯA cần can thiệp · C07 Chi phí nha khoa trẻ em & gói gia đình · C14 Thực thể & kiểm chứng. C13 ĐƯỢC ĐẨY LÊN TẦNG A (khác mọi bộ khác) vì ở nha khoa trẻ em, 'mấy tuổi thì làm gì' chính là câu hỏi quyết định — không phải 'làm ở đâu'. C05 cũng lên Tầng A vì bố mẹ sợ bị bán sớm hơn sợ để muộn. |
| B | 5 | 85 | 31% | 20% — C03 Dịch vụ cho trẻ: trám · fluoride · trâm bít hố rãnh · nhổ răng sữa · C04 Khám định kỳ & theo dõi mọc răng · C09 Quy trình thân thiện & buổi làm quen · C08 Chọn cơ sở có bác sĩ quen trẻ · C11 Răng vĩnh viễn mọc lệch vì răng sữa hỏng. |
| C | 3 | 51 | 16% | 10% — C10 Tập đánh răng & dinh dưỡng chống sâu · C12 Y khoa: mọc răng, thở miệng, tật xấu ở trẻ (E-E-A-T) · C15 Gói gia đình & Teeth Spa (ĐÒN BẨY LTV MẠNH NHẤT CỦA PARIS: một khách hài lòng kéo cả nhà). Chạy nền nhưng C15 nên gắn CRM từ sớm. |
| D | 2 | 34 | 3% | 0% ngân sách mới — C01 Nhận biết sâu răng sữa · C02 Quan niệm 'răng sữa rồi cũng rụng'. Chỉ pillar nền — nhưng C02 là quan niệm sai phổ biến nhất, pillar này nên viết sớm. |

**Bản đồ nội dung — 15 cụm:**

| Hạng | Mã | Cụm chủ đề | Tầng | GĐ | TV | CORE | % điểm | Bài | Sóng | Trang đích |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | C06 | Con sợ nha sĩ — xử lý không cưỡng chế ⭐⭐⭐ | A | S3 | 17 | 13 | 12% | 5 | S1 (0–30n) | MỚI: /kien-thuc/tre-em/con-so-di-nha-si/ |
| 2 | C13 | Theo mốc tuổi: răng sữa · hỗn hợp · tuổi vàng chỉnh nha ⭐⭐⭐ | A | S1 | 17 | 12 | 12% | 6 | S1 (0–30n) | MỚI: /kien-thuc/tre-em/moc-tuoi-kham-rang-cho-tre/ |
| 3 | C05 | Khi nào CHƯA cần can thiệp cho trẻ ⭐⭐⭐ | A | S2 | 17 | 11 | 11% | 4 | S1 (0–30n) | MỚI: /kien-thuc/bao-ton/khi-nao-chua-can-nieng-cho-tre/ |
| 4 | C07 | Chi phí nha khoa trẻ em & gói gia đình ⭐⭐ | A | S3 | 17 | 11 | 9% | 3 | S1 (0–30n) | ⚠ đối chiếu: /hoan-my-bang-gia-dich-vu-nha-khoa.html |
| 5 | C14 | Thực thể & kiểm chứng: bác sĩ nha khoa trẻ em · giấy phép ⭐ | A | S3 | 17 | 9 | 6% | 2 | S1 (0–30n) | MỚI: /chuyen-khoa/nha-khoa-tre-em/ |
| 6 | C03 | Dịch vụ cho trẻ: trám · fluoride · trâm bít hố rãnh · nhổ răng sữa | B | S2 | 17 | — | 9% | 4 | S2 (31–60n) | MỚI: /kien-thuc/tre-em/dich-vu-nha-khoa-cho-tre/ |
| 7 | C04 | Khám định kỳ & theo dõi mọc răng | B | S2 | 17 | — | 7% | 2 | S2 (31–60n) | MỚI: /kien-thuc/tre-em/kham-rang-dinh-ky-cho-tre/ |
| 8 | C09 | Quy trình thân thiện & buổi làm quen trước điều trị ⭐⭐ | B | S4 | 17 | — | 7% | 3 | S2 (31–60n) | MỚI: /kien-thuc/tre-em/quy-trinh-than-thien-voi-tre/ |
| 9 | C08 | Chọn cơ sở có bác sĩ quen làm với trẻ ⭐ | B | S3 | 17 | — | 5% | 2 | S2 (31–60n) | ⚠ đối chiếu: /tim-phong-kham.html |
| 10 | C11 | Răng vĩnh viễn mọc lệch vì răng sữa hỏng ⭐⭐ | B | S3 | 17 | — | 3% | 3 | S2 (31–60n) | MỚI: /kien-thuc/tre-em/rang-vinh-vien-moc-lech/ |
| 11 | C12 | Y khoa: mọc răng, thở miệng & tật xấu ở trẻ (E-E-A-T) ⭐⭐ | C | S2 | 17 | — | 7% | 2 | S3 (61–90n) | MỚI: /kien-thuc/tre-em/tho-mieng-o-tre/ |
| 12 | C10 | Tập đánh răng & dinh dưỡng chống sâu ⭐ | C | S5 | 17 | — | 6% | 1 | S3 (61–90n) | MỚI: /kien-thuc/cham-soc/tap-danh-rang-cho-tre/ |
| 13 | C15 | Gói gia đình & Teeth Spa chuẩn Pháp (LTV) ⭐⭐⭐ | C | S6 | 17 | — | 3% | 2 | S3 (61–90n) | MỚI: /goi-gia-dinh.html |
| 14 | C01 | Nhận biết sâu răng sữa & dấu hiệu sớm | D | S1 | 17 | — | 2% | — | Nền (>90n) | MỚI: /kien-thuc/tre-em/dau-hieu-sau-rang-sua/ |
| 15 | C02 | Quan niệm 'răng sữa rồi cũng rụng' — viết để sửa | D | S1 | 17 | — | 1% | 1 | Nền (>90n) | MỚI: /kien-thuc/tre-em/rang-sua-co-can-dieu-tri/ |

---
