# TRI THỨC — Agent PR GEO Plant (Nha khoa Paris)
> File này gộp **6 module tri thức** từ `knowledge/`. Sinh tự động ngày 2026-10-22 bằng `python tools/gop-tham-khao.py`.
> ⛔ **Không sửa file này** — sửa ở bản rời trong thư mục nguồn rồi chạy lại lệnh trên.

**Cách đọc:** mỗi phần bắt đầu bằng dòng `===== tên file =====` và là **một đơn vị tri thức riêng**. Tham chiếu dạng `[[tên-file]]` trong văn bản trỏ tới **phần cùng tên ngay trong file này**, không phải file bên ngoài.

## MỤC LỤC

| # | File | Cỡ |
|---|---|---|
| 1 | `geo-bo-truy-van-index.md` | 67.3 KB |
| 2 | `geo-kpi-framework.md` | 11.2 KB |
| 3 | `geo-output-excel-schema.md` | 12.6 KB |
| 4 | `geo-phuong-phap-luan.md` | 21.0 KB |
| 5 | `geo-rao-phap-ly.md` | 11.7 KB |
| 6 | `paris-brand-geo.md` | 16.7 KB |


===== geo-bo-truy-van-index.md =====

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


===== geo-kpi-framework.md =====

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


===== geo-output-excel-schema.md =====

# SCHEMA FILE OUTPUT — 2 TAB: KPI & CÔNG VIỆC TRIỂN KHAI · NHA KHOA PARIS

Version: 1.0 · Khoá format khi xuất.
Tên file xuất: **`GEO-NKPARIS-<Thang-bat-dau>-<Thang-ket-thuc>-<Nam>.xlsx`** — ví dụ `GEO-NKPARIS-T01-T06-2027.xlsx`.

**Workbook chỉ có đúng 2 sheet, theo thứ tự:**

1. `BẢNG TỔNG QUAN KPI`
2. `CÔNG VIỆC TRIỂN KHAI`

---

# BẢNG MÀU & FONT (bắt buộc — bám bộ nhận diện Nha khoa Paris)

Ba màu gốc của bộ NDTH Paris, **không được đổi**: **Cerulean Blue `#2A52BE`** · **Pantone Red 032 C `#ED2E38`** · **White `#FFFFFF`**.

| Vai trò | Mã màu | Token Paris | Dùng ở |
|---|---|---|---|
| Xanh thương hiệu — header chính | `#2A52BE` | `--blue` | TAB 1: dòng tiêu đề + dòng header cột |
| Xanh đậm — header điều hành | `#0C1D4D` | `--blue-deep` | TAB 2: dòng header + dải phân cách tháng · panel thống kê |
| Xanh nhạt — dòng tổng business line | `#EAF0FC` | `--blue-light` | TAB 2: dòng `▶ TỔNG …` |
| **Đỏ thương hiệu — dòng tổng tháng** | `#ED2E38` | `--red` | TAB 2: dòng `★ TỔNG SẢN LƯỢNG THÁNG` + header panel sản lượng (chữ trắng) |
| Xanh viền — ô trụ cột | `#D7E2FA` | `--blue-mid` | TAB 1: ô gộp cột TRỤ CỘT KPI |
| Kem — dòng chi tiết | `#FBF8F3` | `--cream` | TAB 2: dòng chi tiết từng bộ dịch vụ |
| Mực — chữ thường | `#131A2E` | `--ink` | Toàn bộ dữ liệu |
| Viền | `#D7E2FA` | `--blue-mid` | Border mảnh toàn bảng |

> **Tỷ lệ bắt buộc của bộ NDTH Paris: 80% trắng/kem · 15% xanh · 5% đỏ.** Trong file Excel điều này có nghĩa:
> - Toàn bộ vùng dữ liệu để **trắng hoặc kem** — không tô nền xanh cho cả khối.
> - Xanh chỉ dùng cho **header, dải tháng, dòng tổng business line, ô trụ cột**.
> - **Đỏ CHỈ dùng cho dòng `★ TỔNG SẢN LƯỢNG THÁNG` (một dòng mỗi tháng) và header panel sản lượng.** Đây là con số lãnh đạo đọc — đỏ ở đây là có chủ ý, không rải thêm chỗ nào khác.
> - ⛔ **Không đặt chữ đỏ lên nền xanh** và **không đặt vàng `#C9A24B` lên nền trắng** (không đạt tương phản AA).

**Font toàn file:** **Arial** — font hệ thống, bảo đảm mở được trên mọi máy và giữ đúng dấu tiếng Việt.
*(Font web của Paris là Bricolage Grotesque + Be Vietnam Pro, nhưng KHÔNG dùng trong Excel vì máy người nhận thường chưa cài — file sẽ bị thay font ngẫu nhiên và vỡ bố cục.)*

Header 9–12pt đậm chữ trắng. Dữ liệu 10pt. Wrap text ở mọi cột mô tả dài. Border mảnh toàn bảng.

---

# TAB 1 — `BẢNG TỔNG QUAN KPI`

## Bố cục dòng

| Dòng | Nội dung | Định dạng |
|---|---|---|
| 1 | *(để trống)* | — |
| 2 | **Gộp A2:L2** — `BẢNG TỔNG QUAN KPI & KẾ HOẠCH DỰ ÁN GEO/SEO NHA KHOA PARIS (THÁNG <X> – THÁNG <Y>)` | Nền `#2A52BE`, Arial 12 đậm, chữ trắng, canh giữa |
| 3 | 4 banner mục tiêu: `TỔNG BÀI VIẾT MỤC TIÊU` · `HẠ TẦNG WEB & CỔNG HUB` · `GEO / SEO AI SEARCH` · `TRAFFIC & LEAD CHUYỂN ĐỔI` | Nền `#2A52BE`, chữ trắng đậm |
| 4 | Dòng mô tả đích của từng banner (gộp tương ứng) | Nền `#EAF0FC`, chữ `#131A2E`, cỡ nhỏ, canh giữa |
| 5 | *(trống)* | — |
| 6 | **Dòng header cột** | Nền `#2A52BE`, Arial 9 đậm, chữ trắng, wrap, canh giữa |
| 7+ | Dữ liệu 5 trụ cột | Xem bên dưới |
| cuối +1 | `TRỌNG SỐ ĐÁNH GIÁ THÁNG` — tỷ trọng hoàn thành từng tháng, tổng = 1,00 | Nền `#2A52BE`, chữ trắng |
| cuối +2 | `TỔNG TRỌNG SỐ DANH MỤC` — tổng trọng số 5 trụ cột = 1,00 | Nền `#2A52BE`, chữ trắng |

**Freeze panes:** `D7` (khoá 6 dòng đầu + 3 cột đầu).

## Cột

| Cột | Header | Nội dung | Rộng |
|---|---|---|---|
| A | `TRỤ CỘT KPI` | 5 trụ cột, **gộp ô dọc** theo khối, nền `#D7E2FA` | 23 |
| B | *(nhóm phụ)* | Phân nhóm trong trụ cột (vd `google.com.vn`, `Traffic AI`, `Top từ khoá Google Search`, `Tối ưu GEO AI Search`, `Chuỗi sau form`) | 22 |
| C | `HẠNG MỤC / CHỈ TIÊU TRỌNG TÂM` | Tên business line / hạng mục cụ thể | 44 |
| D | `Số lượng` | Tổng chỉ tiêu cả chu kỳ | 10 |
| E | *(mức)* | Mức đo: `Top 3` `Top 5` `Top 10` `ChatGPT` `Gemini` `AI-ov` | 10 |
| F | `Hiện tại` | Mốc gốc. Chưa có → `⚠ Cần xác minh từ Nha khoa Paris` | 26 |
| G…(G+n-1) | `THÁNG <MM>/<YYYY>` | **Một cột cho mỗi tháng trong chu kỳ** (n tháng → n cột) | 12 |
| kế tiếp | `ĐÍCH ĐẾN CHU KỲ (TARGET)` | Mô tả đích bằng lời | 44 |
| kế tiếp | `TRỌNG SỐ` | Trọng số dòng/nhóm nhỏ | 10 |
| cuối | `TRỌNG SỐ` | Trọng số **trụ cột** (gộp ô dọc cả khối), tổng 5 khối = 1,00 | 10 |

> **Số cột tháng co giãn theo yêu cầu người dùng.** Kế hoạch 6 tháng → 6 cột tháng; 12 tháng → 12 cột tháng. Các cột phía sau dịch sang phải tương ứng.

## Khối dữ liệu bắt buộc (theo thứ tự)

```
1. Hạ tầng Web & Hub          — Kiến trúc hệ thống & UI/UX các chuyên khoa
                              — Phân line chuyên khoa & Cổng Hub liên kết
2. Sản lượng Bài viết         — BRAND · Thương hiệu tổng
                              — NKI · Implant & Phục hình mất răng
                              — NKC · Chỉnh nha — Niềng răng
                              — NKT · Nha khoa thẩm mỹ
                              — NKG · Nha khoa tổng quát & Nha chu
                              — NKF · Nha khoa trẻ em & Gia đình
                              — Trang local — 7 hub cơ sở
3. SEO & GEO AI Search        ├ Top từ khoá Google Search → mỗi line × {Top 3, Top 5, Top 10}
                              └ Tối ưu GEO AI Search      → mỗi line × {ChatGPT, Gemini, AI-ov}
4. Traffic                    ├ google.com.vn  → mỗi line
                              └ Traffic AI     → mỗi line
5. Form Lead & Chuyển đổi     — mỗi line
                              (dưới khối: công cụ kiểm tra online · sđt xác nhận · KH đến phòng khám · doanh số)
```

---

# TAB 2 — `CÔNG VIỆC TRIỂN KHAI`

Đây là bảng **giao việc điều hành**: mỗi dòng là một đầu việc có người phụ trách và hạn chót.

## Cột (A→J)

| Cột | Header | Nội dung | Rộng |
|---|---|---|---|
| A | `Mã KPI` | `KPI-01`, `KPI-06.1`, `KPI-TỔNG`… — mã ổn định giữa các tháng | 11 |
| B | `Trụ cột KPI` | `1. Hạ tầng Web & Hub` · `2. Tuyến nội dung theo hành trình` · `3. Sản lượng — <Line>` · `4. SEO & GEO AI Search` · `5. Traffic & Chuyển đổi` · `0. Pháp lý` | 32 |
| C | `Hạng mục` | Tên bộ dịch vụ cụ thể. Dòng tổng dùng tiền tố `▶` (business line) và `★` (toàn hệ thống) | 44 |
| D | `Tháng` | `Tháng 1`, `Tháng 2`… | 10 |
| E | `CHỈ TIÊU (số bài)` | Số bài phải hoàn thành. Đầu việc không phải nội dung → để trống | 14 |
| F | `Trong đó CORE` | Số bài thuộc CORE 80/20 (Tầng A) | 13 |
| G | `Công việc chi tiết` | **Mô tả hành động cụ thể** — không viết chung chung. Xem quy tắc bên dưới | 80 |
| H | `Người phụ trách` | `Team Content` · `Team SEO` · `Team Tech/Dev` · `Team Data/SEO` · `Lead Content/SEO` · `BS + Pháp chế` · `Sale ops` · `CSKH` · `Pháp chế` | 18 |
| I | `Hạn chót` | Ngày cuối tháng tương ứng, định dạng `DD/MM/YYYY` | 12 |
| J | `Hoàn thành` | Checkbox boolean, mặc định `FALSE` | 12 |

## Dải phân cách tháng

Trước mỗi khối tháng, chèn một dòng **gộp A:J**:

```
════  THÁNG 1/2027  ·  giai đoạn SETUP  ·  hạn chót 31/01/2027  ════
```

Nền `#0C1D4D`, chữ trắng đậm, canh giữa.

## Ba cấp dòng trong mỗi khối tháng

| Cấp | Nhận dạng | Nền | Ý nghĩa |
|---|---|---|---|
| Chi tiết | `KPI-06.1`, `KPI-08.2`… | `#FBF8F3` kem | Từng bộ dịch vụ |
| Tổng business line | `C` bắt đầu bằng `▶ TỔNG …` | `#EAF0FC` xanh nhạt | Cộng các dòng chi tiết của line |
| **Tổng tháng** | `KPI-TỔNG`, `C` = `★ TỔNG SẢN LƯỢNG THÁNG (toàn hệ thống)` | **`#ED2E38` đỏ, chữ trắng** | **Con số lãnh đạo đọc** |

## Panel phụ bên phải (cột L–M)

| Vị trí | Nội dung | Nền |
|---|---|---|
| `L1:M1` | `TỔNG SẢN LƯỢNG THEO THÁNG` | `#ED2E38`, chữ trắng |
| `L2:M…` | Từng tháng → tổng số bài; dòng cuối `TỔNG CHU KỲ` | trắng / `#EAF0FC` |
| dưới đó | `THỐNG KÊ TIẾN ĐỘ` | `#0C1D4D`, chữ trắng |
| dưới đó | `Tổng số đầu việc KPI` · `Đã hoàn thành` · `Chưa hoàn thành` · `Tiến độ chung` (%) | trắng |
| dòng chú giải | *"Dòng nền đỏ ★ là con số tổng của tháng — đọc trực tiếp ở cột CHỈ TIÊU. Dòng nền xanh ▶ là tổng của từng business line. Các dòng nền kem là chi tiết từng bộ dịch vụ."* | `#EAF0FC` |

## Quy tắc viết cột `Công việc chi tiết` (G)

Đây là nơi **phương pháp luận biến thành hành động**. Mỗi ô phải trả lời được: *làm gì · cho cụm nào (mã + tầng + giai đoạn) · gỡ rào cản nào (SỢ/NGỜ/NGẠI) · rào pháp lý nào*.

| ❌ Không chấp nhận | ✅ Bắt buộc |
|---|---|
| "Viết bài SEO cho line Implant" | "Sản xuất 8 bài cụm **C11 Đào thải trụ & làm lại** (Tầng A · S3 · gỡ rào NGỜ): 1 trang chuyên biệt + 7 bài tình huống — BLUF, có số liệu, **không phán xét nơi khách từng làm (R6)**, case có văn bản đồng ý (**R5**)" |
| "Tối ưu GEO" | "Chạy 20 prompt dịch vụ + 7 prompt hub + 10 prompt thương hiệu ở chế độ ẩn danh trên ChatGPT · Gemini · AI Overview, 3 lần lấy đa số, ghi mốc gốc tháng đầu và ghi lại đối thủ được AI nhắc" |
| "Làm trang chi nhánh" | "Dựng 2 trang local chuẩn NAP cho hub Hải Phòng & Quảng Ninh — **lấy địa chỉ, SĐT và số giấy phép của chính cơ sở đó tại `/tim-phong-kham.html` tại thời điểm chạy**, nêu đúng phạm vi chuyên môn, kỹ thuật ngoài phạm vi thì ghi rõ điều hướng (**R3**)" |
| "Viết bài giá Implant 20 triệu" | "Dựng trang giá Implant: bóc tách **trụ – abutment – mão**, dải min–max **lấy từ trang bảng giá tại thời điểm chạy**, ghi ngày cập nhật, nêu điều kiện trả góp hiện hành — **KHÔNG ghi số vào kế hoạch (R12)**" |

Khi đầu việc gắn với một cụm, **luôn ghi mã cụm + tầng + giai đoạn**. Khi có rào pháp lý, ghi mã rào `R0`–`R13` trong ngoặc. Tham chiếu bảng ánh xạ cụm → rào ở `geo-rao-phap-ly.md` §5.

---

# QUY TẮC XUẤT FILE

1. **Xuất tự động, không hỏi.** Sau khi trình bảng kế hoạch trong chat và được xác nhận, Agent xuất thẳng `.xlsx` — không đặt câu hỏi "(có/không)".
2. **Bảng phẳng khi cần dán:** nếu người dùng ở Gemini → xuất thêm bảng phẳng đúng số cột, **mỗi ô một giá trị, không gộp ô**, lặp lại tên business line ở mỗi dòng để bấm *Export to Sheets*.
3. **Không để ô trống ở cột bắt buộc:** Mã KPI · Trụ cột · Hạng mục · Tháng · Người phụ trách · Hạn chót. Thiếu dữ liệu → ghi `⚠ Cần xác minh từ Nha khoa Paris`.
4. **Kiểm tra trước khi xuất:**
   - [ ] Tổng trọng số 5 trụ cột = 1,00
   - [ ] Tổng trọng số tháng = 1,00
   - [ ] `★ TỔNG SẢN LƯỢNG THÁNG` = Σ các dòng `▶ TỔNG` của tháng đó + trang local
   - [ ] Panel `TỔNG SẢN LƯỢNG THEO THÁNG` khớp với dòng `★` từng tháng
   - [ ] Mọi dòng có Hạn chót = ngày cuối tháng tương ứng
   - [ ] Chênh lệch sản lượng tháng cao nhất / thấp nhất ≤ 25% (trừ tháng Setup)
   - [ ] Không có số tuyệt đối nào bị bịa ở cột `Hiện tại`
   - [ ] **Không có con số giá / % ưu đãi / lãi suất nào trong file (R12)**
   - [ ] Màu đỏ `#ED2E38` chỉ xuất hiện ở dòng `★` và header panel sản lượng
5. **Sinh file bằng script:** khi chạy cục bộ, dùng `tools/build-geo-plan.py` — script khoá sẵn toàn bộ màu, gộp ô, freeze panes và công thức tổng.


===== geo-phuong-phap-luan.md =====

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


===== geo-rao-phap-ly.md =====

# RÀO PHÁP LÝ GEO — SOÁT TRƯỚC KHI ĐƯA ĐẦU VIỆC VÀO KẾ HOẠCH

Version: 1.0 · Áp cho MỌI đầu ra của Agent. **Tài liệu nội bộ, không thay thế ý kiến Pháp chế.**

> **Nguyên tắc nền: KHÔNG CHẮC → DỪNG → HỎI PHÁP CHẾ → RỒI MỚI ĐĂNG.**

**Nền pháp lý:** nha khoa là **dịch vụ khám chữa bệnh** — nội dung quảng cáo chịu quản lý của pháp luật quảng cáo y tế Việt Nam, **cộng thêm** chính sách hạn chế của Google Ads và Meta với ngành nha khoa / làm đẹp.

Khi Agent viết cột **Công việc chi tiết** của TAB 2, phải ghi mã rào `R0`–`R13` trong ngoặc để Pháp chế biết đường duyệt.

---

# 1. BẢNG 14 RÀO

| Mã | Rào | KHÔNG được làm | THAY BẰNG | Người duyệt |
|---|---|---|---|---|
| **R0** | Thấp — nội dung kiến thức | Quảng cáo dịch vụ trong bài kiến thức; CTA bán hàng dồn dập | Giữ giọng giáo dục; CTA mềm cuối bài; vẫn ghi ngày cập nhật + bác sĩ thẩm định | Content lead |
| **R1** | **Cam kết kết quả & mức độ đau** | "khỏi 100%", "chắc chắn thành công", "**niềng không bao giờ đau**", "không đau", "không biến chứng", "an toàn tuyệt đối", "răng sứ dùng vĩnh viễn / trọn đời", "cam kết kết quả như hình" | "tỷ lệ thành công cao khi đúng chỉ định và chăm sóc đúng*"; "giảm cảm giác khó chịu nhờ công nghệ, bác sĩ theo dõi từng giai đoạn"; "độ bền theo khuyến cáo của hãng, có chế độ bảo hành"; "kết quả tuỳ tình trạng răng và cơ địa, bác sĩ đánh giá riêng*" | Pháp chế |
| **R2** | Danh mục kỹ thuật & phạm vi chuyên môn | Đăng kỹ thuật không có trong danh mục kỹ thuật đã được phê duyệt của **đúng cơ sở**; thổi phồng "công nghệ độc quyền" | Chỉ nêu kỹ thuật có trong danh mục; tên thương mại phải soi chiếu được về tên kỹ thuật chuyên môn | Pháp chế + Chuyên môn |
| **R3** | **Đúng pháp nhân & đúng cơ sở** | Gắn số giấy phép của cơ sở Hà Nội (`2032/HNO-GPHĐ/CL1`) cho trang local của tỉnh khác; quảng cáo một kỹ thuật trên trang của cơ sở không được phép làm kỹ thuật đó; dựng trang local cho tỉnh **không có cơ sở** | Mỗi trang local gắn **đúng số giấy phép của chính cơ sở đó**; cơ sở không đủ phạm vi thì ghi rõ "tư vấn và điều hướng về cơ sở thực hiện"; tỉnh không có cơ sở → viết bài kiến thức, nêu cơ sở gần nhất | Pháp chế |
| **R4** | **Bác sĩ** | Gắn bác sĩ vào dịch vụ khi chưa xác minh chuyên khoa; quảng cáo bác sĩ tại cơ sở chưa đăng ký hành nghề; **dùng tên bác sĩ không có trong hồ sơ thương hiệu** | Chỉ dùng 3 bác sĩ đã có hồ sơ (`paris-brand-geo.md` §5) + đăng ký hành nghề đúng cơ sở; author box `"Thẩm định chuyên môn: [chức danh + tên]"`; tên khác → `⚠ Cần xác minh` | Chuyên môn + HR |
| **R5** | Hình ảnh khách hàng & before–after | Dùng ảnh/video khách khi mới có thoả thuận miệng; suy đoán "khách không phản đối"; dùng ngoài phạm vi đã đồng ý; **tạo ảnh kết quả giả / ảnh AI mô phỏng rồi trình bày như case thật** | **Văn bản đồng ý minh thị** nêu rõ: loại dữ liệu, mục đích marketing, kênh, thời hạn, quyền rút lại — lưu để xuất trình. Before–after phải là case thật đã duyệt; kiểm tra thêm policy Google/Meta vì ngành nha bị hạn chế định dạng này | CSKH + Pháp chế |
| **R6** | So sánh đối thủ | Nêu tên, so sánh trực tiếp, hạ thấp cơ sở khác; ám chỉ "nơi khác làm hỏng" | Đưa **bộ tiêu chí khách quan** để khách tự đánh giá; với khách sửa lại ca cũ thì **tuyệt đối không phán xét nơi cũ** | Pháp chế |
| **R7** | **"CHÍNH HÃNG" & vật tư** ⚠ rào đặc thù nha khoa | Gắn chữ "chính hãng" cho vật liệu ngoài 4 hãng có hồ sơ; suy diễn "đối tác hãng X" thành "mọi dịch vụ đều dùng hàng hãng X"; mượn hình máy nơi khác; nêu vật tư cơ sở không thực sự có | **Chỉ dùng "chính hãng" cho: Straumann · Invisalign · Nacera · Ormco.** Vật liệu khác → không dùng chữ này, ghi `⚠ Cần xác minh`. Phải có **văn bản chứng minh quan hệ đối tác** trước khi phát hành | Kho vật tư + Pháp chế |
| **R8** | Khách nước ngoài & Việt kiều | Đăng nội dung tiếp nhận khách nước ngoài khi thiếu bất kỳ điều kiện bắt buộc | Đủ: kỹ thuật trong danh mục · cơ sở đủ phạm vi chuyên môn · năng lực ngôn ngữ/phiên dịch · văn bản đồng ý song ngữ | Pháp chế |
| **R9** | **Giấy xác nhận nội dung quảng cáo (GXNNDQC)** | Phát hành nội dung quảng cáo dịch vụ KCB chưa xin GXNNDQC | Xin tại **Sở Y tế** trước chiến dịch. Số GXNNDQC của từng nội dung: `⚠ Cần xác minh`. **Phải là một đầu việc riêng trong tháng Setup** | Pháp chế (Sở Y tế) |
| **R10** | KOL / người chuyển tải quảng cáo | KOL nói về dịch vụ mà không công khai là quảng cáo | KOL phải xác minh tính trung thực, công khai `#quảng_cáo`, chịu trách nhiệm liên đới — ràng buộc trong hợp đồng | Brand + Pháp chế |
| **R11** | Người nổi tiếng | Nêu tên hoặc dùng hình người nổi tiếng; suy đoán họ đã làm răng | Phân tích xu hướng chung, không cá nhân hoá | Brand + Pháp chế |
| **R12** | **GIÁ · ƯU ĐÃI · TRẢ GÓP = DỮ LIỆU ĐỘNG** ⚠ rào đặc thù Paris | Đưa con số giá, % ưu đãi, lãi suất trả góp vào kế hoạch hoặc vào bài; dùng số cũ | **Lấy tại thời điểm chạy** từ `/hoan-my-bang-gia-dich-vu-nha-khoa.html` và trang ưu đãi hiện hành. Kế hoạch chỉ ghi đầu việc "cập nhật dải giá min–max + ngày cập nhật", **không ghi số** | Sale ops + Pháp chế |
| **R13** | **Chẩn đoán & hứa thời gian** ⚠ rào đặc thù nha khoa | **Chẩn đoán** tình trạng răng của khách qua ảnh/mô tả; **kê đơn**; **báo giá ca cụ thể**; hứa thời gian điều trị cứng ("niềng xong trong 12 tháng") | Tư vấn định hướng rồi mời thăm khám; nêu **dải** thời gian và nói rõ phụ thuộc tình trạng từng ca | Chuyên môn + Pháp chế |

---

# 2. BA RÀO CHI PHỐI KHỐI LƯỢNG LỚN NHẤT CỦA PARIS

## 2.1 R9 — GXNNDQC: nút thắt tiến độ lớn nhất

Phần lớn cụm **Tầng A** của mọi bộ là nội dung **quảng cáo dịch vụ KCB** (chi phí, chọn cơ sở, phương pháp, thực thể) → chạm R9.
→ **Bắt buộc đưa "xin GXNNDQC" thành một đầu việc riêng trong tháng Setup**, không để đến lúc sắp đăng mới xin. Nếu bỏ bước này, toàn bộ Tầng A bị tắc giữa chu kỳ.

## 2.2 R7 — "chính hãng": rào đặc thù và dễ sai nhất

Đây là **điểm nóng riêng của ngành nha khoa** mà ngành thẩm mỹ không có. Khách tìm *"trụ nào tốt"*, *"sứ có chính hãng không"*, *"khay Invisalign thật hay giả"* chính là đang lo **bị tráo vật liệu**.
- Rào này rơi đúng vào cụm **C03** (vật liệu) và **C14** (thực thể) — hai cụm Tầng A của các bộ Implant · Invisalign · Răng sứ, tức là **nơi khách quyết định**.
- Nghịch lý vận hành: **bằng chứng mạnh nhất của Paris cũng là rào pháp lý dễ sai nhất.** Phải xử lý bằng checklist 4 hãng áp cho toàn đội content + văn bản đối tác lưu sẵn, **không duyệt từng bài**.

## 2.3 R1 — cam kết kết quả & mức độ đau

Chạm hầu hết cụm **C06** (đau, biến chứng) — cụm Tầng A hạng 1 ở 6/10 bộ. Xử lý bằng **checklist từ cấm** áp cho toàn đội content, không duyệt từng bài. Mọi con số và mức độ đau phải gắn `*` dẫn *"Hiệu quả phụ thuộc cơ địa mỗi người"*.

---

# 3. QUY TRÌNH BẮT BUỘC (đưa vào cột Công việc chi tiết như một đầu việc thường trực)

```
Content/Chi nhánh soạn
   → tự kiểm checklist rào R0–R13
   → BS thẩm định chuyên môn (phát ngôn y khoa: cơ chế · hiệu quả · chỉ định · an toàn · mức độ đau)
   → Pháp chế duyệt nội dung & hình ảnh & chữ "chính hãng"
   → (nếu là quảng cáo dịch vụ KCB) xin GXNNDQC tại Sở Y tế
   → phát hành
   → lưu hồ sơ
```

**Hệ quả cho lập kế hoạch:** mọi đầu việc sản xuất nội dung phải cộng thêm **thời gian duyệt 2 lớp (BS + Pháp chế)** vào hạn chót. **Không đặt hạn chót sản xuất trùng ngày phát hành.**

**Human-in-the-loop bắt buộc duyệt trước khi chạy:** nội dung có số liệu y khoa · nội dung so sánh phương pháp · mọi phát ngôn bác sĩ · before–after · **mọi tuyên bố "chính hãng"** · trang local (địa chỉ + giấy phép) · landing page trước khi publish.

---

# 4. BỐN CÂU CẤM TUYỆT ĐỐI (Agent tự soát mọi đầu ra)

1. Không cam kết **100% / tuyệt đối / vĩnh viễn / trọn đời / không đau / không rủi ro / không biến chứng**.
2. Không **tự tạo** số liệu · review · giá · ưu đãi · lãi suất trả góp · chính sách bảo hành · thông tin bác sĩ (bằng cấp, kinh nghiệm, giải thưởng, số ca).
3. Không **hạ thấp đối thủ**, không xem cơ sở KCB chuyên khoa RHM là tiệm làm răng thẩm mỹ, không lấy giảm giá làm trọng tâm.
4. Không **chẩn đoán qua ảnh/mô tả**, không **báo giá ca cụ thể**, không **hứa thời gian điều trị cứng**.

Mọi con số, case, giá, giấy phép, danh sách bác sĩ trong kế hoạch phải **xác minh trước khi chạy**. Thiếu → ghi `⚠ Cần xác minh từ Nha khoa Paris`, **không bịa để lấp bảng**.

---

# 5. BẢNG ÁNH XẠ CỤM → RÀO (dùng khi viết cột Công việc chi tiết)

| Cụm | Rào phải ghi | Lý do |
|---|---|---|
| C03 Phương pháp & vật liệu | **R7** · R2 | Chữ "chính hãng" + danh mục kỹ thuật |
| C04 Chẩn đoán & kế hoạch điều trị | **R13** · R2 | Không chẩn đoán qua mô tả |
| C05 Khi nào KHÔNG nên làm | R0 · R6 | Nội dung bảo tồn, dễ bị hiểu là chê nơi khác |
| C06 Nỗi sợ, đau & biến chứng | **R1** · R9 | Cam kết mức độ đau + quảng cáo dịch vụ KCB |
| C07 Chi phí & bảng giá | **R12** · R9 | Giá là dữ liệu động |
| C08 Chọn cơ sở & bác sĩ | **R3** · **R4** · R6 | Pháp nhân + bác sĩ + so sánh |
| C09 Quy trình & số buổi | **R13** · R1 | Không hứa thời gian cứng |
| C10 Chăm sóc & tái khám | R0 · R13 | Hướng dẫn, không kê đơn |
| C11 Hỏng & làm lại / bảo hành | **R6** · R1 · R5 | Không phán xét nơi cũ + chính sách bảo hành + ảnh case |
| C12 Y khoa & chức năng | R0 · **R4** | E-E-A-T cần bác sĩ thẩm định |
| C13 Nhóm khách đặc thù | **R13** · R8 | Bệnh lý nền, mang thai, trẻ em, khách nước ngoài |
| C14 Thực thể & kiểm chứng | **R3** · **R4** · **R7** | Giấy phép + bác sĩ + đối tác hãng — rào nặng nhất |
| C15 Cross-sell & gói gia đình | R0 · **R12** | Gói giá là dữ liệu động |
| Trang local 7 hub | **R3** · R2 | Giấy phép + phạm vi chuyên môn từng cơ sở |


===== paris-brand-geo.md =====

# NHA KHOA PARIS — HỒ SƠ THƯƠNG HIỆU CHO GEO

Version: 1.0 · Agent đọc file này để biết **Nha khoa Paris là ai, làm gì, ở đâu, ai là bác sĩ** trước khi lập bất kỳ kế hoạch GEO nào.
Website chính thức: `nhakhoaparis.vn`

> **Quy ước:** thông tin có `⚠` là **chưa xác minh hoặc là dữ liệu động** — Agent được phép nhắc đến để đặt câu hỏi, nhưng **KHÔNG được đưa vào nội dung xuất bản hoặc vào ô số liệu của kế hoạch** cho đến khi Paris xác nhận.

---

# 1. ĐỊNH VỊ

> **HỆ THỐNG NHA KHOA TIÊU CHUẨN PHÁP ĐẦU TIÊN TẠI VIỆT NAM**

**Slogan:** *Nụ cười mới, cuộc sống mới* / *New Smile, New Life*.

**Vai trò:** chuỗi nha khoa chuyên sâu **điều trị + chăm sóc + thẩm mỹ răng toàn diện** — một cơ sở khám chữa bệnh chuyên khoa Răng Hàm Mặt, KHÔNG phải một tiệm làm răng thẩm mỹ. Đây là điểm phân định phải xuất hiện trong mọi nội dung GEO: khi AI được hỏi "làm răng ở đâu an toàn", Paris phải nằm ở phía **cơ sở y tế có giấy phép KCB**.

**Khác biệt cốt lõi:** Tiêu chuẩn Pháp + **đối tác hãng hạng cao nhất** (Straumann · Invisalign · Nacera · Ormco) + bác sĩ tốt nghiệp ĐH Y có chứng chỉ quốc tế.
**Phân khúc:** trung – cao cấp; cạnh tranh bằng **bằng chứng kiểm chứng được**, không bằng giá thấp.

**Điều khách nha khoa thật sự mua:** **chức năng + sự tự tin**. Ăn nhai tốt lại · hết đau, ê buốt · nụ cười đẹp. Khác với thẩm mỹ thuần: ở nha khoa **chức năng và thẩm mỹ đi đôi** — người trồng Implant vừa muốn ăn được vừa muốn không ai nhận ra. **Nội dung chỉ nói một vế là mất một nửa động cơ mua.**

---

# 2. DOANH NGHIỆP

- **Tên:** Nha khoa Paris — Công ty CP Nha khoa Paris
- **MSDN:** `0111123127`
- **Trụ sở chính:** Tầng 1 + Tầng 2, số 12 Thái Thịnh, P. Đống Đa, Hà Nội
- **Giấy phép KCB:** `2032/HNO-GPHĐ/CL1` (Sở Y tế Hà Nội, 23/10/2025)
- **Hotline:** `0943.776.699` (24/7) · email `tuvan@nhakhoaparis.vn` · `cskh@nhakhoaparis.vn`
- **Giờ làm việc:** 8h30 – 18h30

> ⚠ **Giấy phép `2032/HNO-GPHĐ/CL1` là giấy phép của cơ sở Hà Nội do Sở Y tế Hà Nội cấp.** Mỗi cơ sở ở tỉnh khác có giấy phép riêng do Sở Y tế tỉnh đó cấp. **Không gắn số giấy phép Hà Nội cho trang local của tỉnh khác** — đó là rào **R3**. Danh sách giấy phép từng cơ sở: `⚠ Cần xác minh từ Nha khoa Paris`.

---

# 3. HỆ SINH THÁI 6 BUSINESS LINE

Đây là 6 dòng dùng làm **trục phân nhóm KPI sản lượng** trong file output.

| Mã | Business line | Phạm vi | Bộ truy vấn tương ứng |
|---|---|---|---|
| **BRAND** | **Thương hiệu tổng** | Thực thể thương hiệu, chọn cơ sở, giấy phép, bảo hành, review | `01-thuonghieu` |
| **NKI** | **Implant & Phục hình mất răng** | Trồng răng Implant · các loại trụ · ghép xương · nâng xoang · All-On 4/6 · toàn hàm | `02-implant` `03-allon` |
| **NKC** | **Chỉnh nha — Niềng răng** | Mắc cài kim loại · sứ · pha lê · mặt trong · **Invisalign trong suốt** | `04-niengmaccai` `05-invisalign` |
| **NKT** | **Nha khoa thẩm mỹ** | Bọc răng sứ · cầu răng sứ · răng toàn sứ · răng sứ toàn hàm · **mặt dán Veneer** | `06-rangsu` `07-veneer` |
| **NKG** | **Nha khoa tổng quát & Nha chu** | Nhổ răng Piezotome · nhổ răng sữa · cắt lợi trùm · tẩy trắng WhiteMax · trám thẩm mỹ · cạo vôi · đính đá · điều trị tuỷ RECIPROC BLUE · nha chu · viêm nướu · tụt lợi | `08-tongquat` `09-nhachu` |
| **NKF** | **Nha khoa trẻ em & Gia đình** | Nha khoa trẻ em · gói **Teeth Spa chuẩn Pháp** · gói gia đình | `10-trenem` |

**Dịch vụ giá trị lớn** (ưu tiên khi xếp Giá trị DT = Cao): **Implant · All-On 4/6 · Invisalign · răng sứ toàn hàm**.

---

# 4. HỆ THỐNG CƠ SỞ — DỮ LIỆU LOCAL CHO GEO

**7 tỉnh thành có cơ sở:** Hà Nội · Hải Phòng · Quảng Ninh · Vinh (Nghệ An) · Đà Nẵng · TP.HCM · Bình Dương.

| # | Hub | Trạng thái dữ liệu |
|---|---|---|
| 1 | Hà Nội (trụ sở — 12 Thái Thịnh, P. Đống Đa) | Địa chỉ đã xác nhận · GP `2032/HNO-GPHĐ/CL1` |
| 2 | Hải Phòng | ⚠ Địa chỉ đường phố & số GP: cần lấy tại `/tim-phong-kham.html` |
| 3 | Quảng Ninh | ⚠ như trên |
| 4 | Vinh (Nghệ An) | ⚠ như trên |
| 5 | Đà Nẵng | ⚠ như trên |
| 6 | TP.HCM | ⚠ như trên |
| 7 | Bình Dương | ⚠ như trên |

> 🔧 **Luật bắt buộc trước khi giao việc trang local:**
> **① Lấy địa chỉ, số điện thoại và số giấy phép từng cơ sở tại `/tim-phong-kham.html` ngay tại thời điểm chạy — KHÔNG dùng số hoặc địa chỉ cũ.**
> **② Nêu đúng phạm vi chuyên môn của từng cơ sở.** Nếu một cơ sở không được phép thực hiện một kỹ thuật (ví dụ đại phẫu ghép xương), trang local của cơ sở đó **không được quảng cáo kỹ thuật đó** — phải ghi rõ "tư vấn và điều hướng về cơ sở thực hiện". Sai ở đây là chạm rào **R3**.
> **③ Hotline campaign có thể khác số tổng đài** — xác minh trước khi in lên trang.
>
> **Trang "dịch vụ × tỉnh KHÔNG có cơ sở"** (ví dụ "trồng implant ở Cần Thơ") không nằm trong phạm vi chu kỳ và **không được dựng như trang local** — nếu làm, phải là bài kiến thức, nói rõ cơ sở gần nhất ở đâu.

**Vì sao local quan trọng với GEO:** mẫu truy vấn *"địa chỉ [dịch vụ] ở [tỉnh]"* là ý định mua mạnh và là khoảng trống rẻ nhất để chiếm trong AI Search. Mỗi trang cơ sở phải chuẩn **NAP** (Name–Address–Phone) + `LocalBusiness`/`Dentist` schema + nêu đúng phạm vi giấy phép.

---

# 5. BÁC SĨ — TRẠNG THÁI XÁC MINH

**Nguyên tắc tuyệt đối:** chỉ gắn tên bác sĩ vào một dịch vụ khi bác sĩ đó **có trong danh sách dưới đây** VÀ **đã đăng ký hành nghề tại đúng cơ sở**. Vi phạm là rào pháp lý **R4**.

| Bác sĩ | Vai trò & bằng chứng đã có hồ sơ | Dùng cho cụm / dịch vụ |
|---|---|---|
| **TS-BS. Đàm Ngọc Trâm** | Cố vấn chuyên môn · thành viên **ESCD** (nha khoa thẩm mỹ châu Âu) · **ICOI** (implant thế giới) · hiệp hội nha sĩ Mỹ · **ITI** (Thuỵ Sỹ) · Phó trưởng Bộ môn Phục hình RHM — Viện đào tạo RHM, ĐH Y Hà Nội | C14 Thực thể toàn hệ thống · bộ Răng sứ · Veneer · Implant |
| **BS. Hồ Hiệp Anh Tuấn** | Phó GĐ chuyên môn · **Top 1 case Invisalign 2024** | C14 + C08 bộ Invisalign & Chỉnh nha |
| **BS.CKI Nguyễn Ngọc Linh** | **>5.000 ca Implant** · kỹ thuật nhanh – an toàn | C14 + C08 bộ Implant & All-On |

**Chung cho toàn hệ thống:** **100% bác sĩ tốt nghiệp Đại học Y, có chứng chỉ hành nghề**; tuân thủ **vô khuẩn theo Bộ Y tế**.

| Trạng thái | Nội dung |
|---|---|
| ⚠ Danh sách đầy đủ đội ngũ từng cơ sở | `Cần xác minh từ Nha khoa Paris` |
| ⚠ Bác sĩ nha chu & nha khoa trẻ em | `Cần xác minh` — hai bộ `09-nhachu` và `10-trenem` hiện **chưa có bác sĩ gán được**; cụm C14 của hai bộ này bị chặn bởi R4 cho tới khi có danh sách |

**Cơ hội GEO lớn nhất chưa khai thác:** ba bác sĩ trên có bằng chứng hiệp hội quốc tế rất mạnh (ESCD · ICOI · ITI) mà **chưa được gắn schema `ProfilePage` / `IndividualPhysician` + `sameAs`**. Xác minh → gắn bác sĩ vào dịch vụ → chiếm truy vấn *"bác sĩ implant giỏi"*, *"bác sĩ Invisalign giỏi"*. Đây là cụm **C14** — Tầng A ở hầu hết 10 bộ.

---

# 6. CHÂN DUNG KHÁCH & BA RÀO CẢN CHỐT

Chi tiết khung 6 giai đoạn ở `geo-phuong-phap-luan.md` §2. Tóm lại:

| Rào cản | Bằng chứng Paris dùng để gỡ |
|---|---|
| **① SỢ** đau & sợ mất răng thật | Piezotome (nhổ siêu âm, giảm đau) · RECIPROC BLUE (điều trị tuỷ) · Invisalign trong suốt · bác sĩ theo dõi từng giai đoạn |
| **② NGỜ** vật liệu & tay nghề | **4 hãng đối tác** · 100% BS ĐH Y có chứng chỉ hành nghề · GP Sở Y tế · bảng giá công khai |
| **③ NGẠI** lộ trình dài & chi phí lớn | Lộ trình rõ số buổi · **trả góp** niềng & bọc sứ · 7 cơ sở · đặt lịch linh hoạt |

**Thứ tự ưu tiên dùng bằng chứng:** đối tác hãng chính hãng → BS ĐH Y + chứng chỉ quốc tế → giấy phép Sở Y tế → công nghệ giảm đau → bảo hành/trả góp → báo chí.

**Nhận diện giai đoạn từ một từ khoá lạ:** có *giá / ở đâu / đặt lịch / ưu đãi / trả góp* → S4 · có *có đau không / có hại không / review / trụ nào tốt / bao lâu* → S3 · có *loại nào tốt / so sánh / nha khoa nào uy tín* → S2 · có *là gì / có nên / phải làm sao* → S1 · có *sau khi / kiêng / chăm sóc / siết niềng* → S5 · không khớp nhóm nào → **hỏi lại người dùng, không đoán bừa**.

---

# 7. USP & BẰNG CHỨNG (dùng làm "bằng chứng" trong nội dung)

## 7.1 Đối tác hãng — USP mạnh nhất, đối thủ khó sao chép nhất

| Hãng | Hạng / vai trò | Dùng cho bộ |
|---|---|---|
| **Straumann** | Đối tác **top 1** | `02-implant` `03-allon` |
| **Invisalign** | **Black Diamond** | `05-invisalign` |
| **Nacera** | Đối tác hàng đầu | `06-rangsu` `07-veneer` |
| **Ormco** | Hạng **Diamond Star** | `04-niengmaccai` |

> ⚠ **Chữ "chính hãng" là một tuyên bố pháp lý, không phải từ marketing.** Chỉ dùng cho đúng 4 hãng trên. **Không suy diễn** "đối tác hãng X" thành "mọi dịch vụ đều dùng hàng hãng X". Vật liệu khác hoặc không rõ hãng → **không dùng chữ này**, ghi `⚠ Cần xác minh`. Đây là rào **R7** — rào đặc thù và dễ sai nhất của ngành nha khoa.
> ⚠ **Văn bản chứng minh quan hệ đối tác với từng hãng:** `Cần xác minh từ Nha khoa Paris` — phải có trước khi phát hành nội dung dùng chữ "chính hãng".

## 7.2 Công nghệ

- Nhổ răng siêu âm **Piezotome** — giảm đau (gỡ rào SỢ ở bộ `08-tongquat`)
- Điều trị tuỷ **RECIPROC BLUE**
- Tẩy trắng **WhiteMax**
- **Công cụ online kiểm tra răng miệng / niềng / răng sứ / trồng răng** → dùng làm **micro-conversion** trước form, và là **điểm neo thực thể** rất tốt cho cụm C01 (tự đánh giá)

## 7.3 Trust khác

- **Trả góp** niềng răng & bọc răng sứ — ⚠ điều kiện và lãi suất hiện hành là **dữ liệu động** (R12)
- **Báo chí đã đưa tin:** Afamily · Tiền Phong · Znews · 24h · Dân Trí
- Tuân thủ **vô khuẩn theo Bộ Y tế**

## 7.4 Những cụm từ PHẢI THAY khi lập kế hoạch GEO

Các cụm sau xuất hiện trong tài liệu marketing nhưng **vi phạm rào R1**:

| ⛔ Không dùng | ✅ Thay bằng |
|---|---|
| "niềng không bao giờ đau" · "không đau" | "giảm cảm giác khó chịu nhờ công nghệ, bác sĩ theo dõi từng giai đoạn" |
| "răng sứ dùng vĩnh viễn / trọn đời" | "độ bền theo khuyến cáo của hãng, có chế độ bảo hành" |
| "khỏi 100%" · "chắc chắn thành công" | "tỷ lệ thành công cao khi đúng chỉ định và chăm sóc đúng*" |
| "cam kết kết quả như hình" | "kết quả tuỳ tình trạng răng và cơ địa, bác sĩ đánh giá riêng*" |
| "số 1 / tốt nhất / duy nhất / hàng đầu" | nêu USP đo được: đối tác Straumann, Invisalign Black Diamond, GP `2032/HNO-GPHĐ/CL1` |

Mọi con số và cam kết mức độ phải gắn dấu `*` dẫn **"Hiệu quả phụ thuộc cơ địa mỗi người"**.

---

# 8. HIỆN TRẠNG TRAFFIC AI — CHƯA CÓ MỐC GỐC

> ⚠ **Nha khoa Paris CHƯA cung cấp dữ liệu GA4 về traffic AI.** Đây là khoảng trống dữ liệu lớn nhất của bộ này và Agent **phải nói rõ điều đó mỗi khi lập kế hoạch**.

| Chỉ số cần | Trạng thái | Hệ quả nếu thiếu |
|---|---|---|
| Phiên từ ChatGPT · Gemini · Claude · Perplexity · Brave | `⚠ Cần xác minh từ Nha khoa Paris` | Trụ cột KPI 4 chỉ đặt được % tăng trưởng |
| Organic traffic `google.com.vn` theo chuyên khoa | `⚠ Cần xác minh` | Trụ cột KPI 4 không có mốc |
| Thứ hạng từ khoá hiện tại (Top 3/5/10) | `⚠ Cần xác minh` | Trụ cột KPI 3 không đặt được số tuyệt đối |
| Số lead / sđt xác nhận / KH đến phòng khám | `⚠ Cần xác minh` | Trụ cột KPI 5 không có mốc |
| Landing page nào đang hút traffic AI | `⚠ Cần xác minh` | **Cơ hội GEO của mọi cụm phải lấy mặc định = 1** → thứ tự ưu tiên hiện tại dựa trên rào cản khách, chưa hiệu chỉnh bằng bằng chứng traffic |

**Hệ quả vận hành bắt buộc:**

1. **Tháng Setup của mọi chu kỳ là THÁNG LẤY MỐC GỐC** — không đặt chỉ tiêu tăng trưởng cho tháng đó.
2. Trụ cột 3, 4, 5 trong TAB KPI để `⚠ Cần xác minh từ Nha khoa Paris` ở cột "Hiện tại" và ghi **% tăng trưởng** ở cột chỉ tiêu. **Tuyệt đối không bịa số tuyệt đối.**
3. Sau tháng Setup, chạy lại bước ④ để **xếp lại Cơ hội GEO của từng cụm** theo traffic thật, rồi điều chỉnh kế hoạch các tháng sau.

---

# 9. TONE OF VOICE

**Brand Voice:** chuyên nghiệp – chuẩn Pháp – cao cấp – hiện đại – thân thiện. Y khoa nhưng **không khô cứng**. Nói đúng, có căn cứ, không phô trương, không giật gân.

**Luôn:** chuyên gia · tận tâm · dễ hiểu · đáng tin cậy · có chiều sâu · hướng hành động.
**Không:** giật tít · gây sốc · khoa trương · đe doạ · hạ thấp đối thủ · ép mua · lạm dụng thuật ngữ y khoa.

**Từ ưu tiên:** an toàn · bảo tồn · tự nhiên · đồng hành · chuyên môn · bác sĩ · chính hãng (đúng 4 hãng) · minh bạch · phù hợp · tư vấn.
**Từ cấm (trừ khi có căn cứ + Pháp chế duyệt):** tuyệt đối · 100% · vĩnh viễn · trọn đời · hoàn hảo · không đau · không rủi ro · không biến chứng · rẻ nhất · tốt nhất · số 1 · duy nhất · hàng đầu.
**CTA nhẹ:** "Đăng ký tư vấn cùng bác sĩ" · "Đặt lịch thăm khám" · "Kiểm tra răng miệng online". Cấm: "Mua ngay / Chốt ngay / Kẻo hết".

---

# 10. ĐỐI THỦ — CHỈ DÙNG NỘI BỘ

Elite Dental · Nha khoa Thuỳ Anh · Nha khoa Kim · Việt Pháp · I-Dent · Lạc Việt Intech · Parkway.

**Dùng để:** chọn góc khác biệt (chuẩn Pháp + đối tác hãng top + BS ĐH Y có chứng chỉ quốc tế) và ước lượng mức cạnh tranh của cụm; **ghi lại đối thủ nào được AI nhắc** khi đo GEO hằng tháng.

⛔ **Không nêu tên để hạ thấp. Không ám chỉ "nơi khác làm hỏng".** Với khách đến sửa lại ca cũ: **tuyệt đối không phán xét nơi cũ** — đưa bộ tiêu chí khách quan để khách tự đánh giá. Đây là rào **R6**.

---

# 11. DỮ LIỆU CẦN CẬP NHẬT ĐỊNH KỲ

| Hạng mục | Tần suất | Vì sao |
|---|---|---|
| **Bảng giá** `/hoan-my-bang-gia-dich-vu-nha-khoa.html` | Mỗi đợt | Giá Implant / All-On / số khay Invisalign đổi theo đợt (**R12**) |
| **Ưu đãi hiện hành & điều kiện trả góp** | Mỗi đợt | Dữ liệu động (**R12**) |
| **Địa chỉ + SĐT + giấy phép từng cơ sở** `/tim-phong-kham.html` | Mỗi chu kỳ | Rào **R3** cho trang local |
| Danh sách bác sĩ đã xác minh theo cơ sở | Mỗi chu kỳ | Rào **R4** chặn cụm C14 |
| Văn bản chứng minh quan hệ đối tác 4 hãng | Khi đổi hợp đồng | Rào **R7** cho chữ "chính hãng" |
| Số GXNNDQC của từng nội dung/chiến dịch | Trước mỗi đợt phát hành | Rào **R9** |
| Danh sách case + ảnh đã có giấy đồng ý | Liên tục | Rào **R5** |
| Số liệu GA4, traffic AI, kết quả đo prompt GEO | Hằng tháng | Trụ cột KPI 3 · 4 · 5 |

