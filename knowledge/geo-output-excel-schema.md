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
