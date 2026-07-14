# Các vấn đề đang tồn tại — hệ thống WDP & tận dụng phía VIS

> **Góc nhìn:** PM bravesoft  
> **Neo:** Vis muốn tăng **コンサルティング売り上げ**; WDP phải là **一助となるツール**  
> **Nguồn:** `ヴィスの現状と今後について`、`WDPコンサル営業.xlsx`、Milestone ~2026/06、mockup setup  
> **Phạm vi:** Tập trung **vấn đề hệ thống + cách dùng hệ thống** đang cản lộ trình After / 有料 / XD MVP（không lặp lại toàn bộ phân tích thị trường office）.

---

## 0. Bản đồ vấn đề（nhìn nhanh）

```text
[A] Cách dùng còn kẹt ở 現状把握 / ショット型
        ↓ khiến
[B] Chưa nối Before→After → khó 有料・khó gắn XD
        ↓ cộng
[C] Dùng nội bộ chưa đều + lead time đề xuất không kịp survey
        ↓ cộng
[D] Product/UX nặng (setup分断, chu kỳ phát triển重い)
        ↓ cộng
[E] AIレポート / phân tích chưa chốt; còn chỗ nguy hiểm cho AI
        ↓
→ WDP chưa đủ “一助” cho năm MVP (After / 有料 / XD)
```

---

## 1. Vấn đề sản phẩm & mô hình dùng（cốt lõi）

### 1.1 Dùng chính là サーベイ現状把握 — ショット型

| Hiện trạng | Hệ quả |
|------------|--------|
| Giá trị WDP hiện được dùng chủ yếu ở **サーベイ** | Các trụ khác（稼働・空間…）chưa thành vòng đời bán consulting |
| Mục đích chính: **現状把握** trước / quanh đề xuất | Giúp **受注** tốt, nhưng **không tự sinh 継続利用** |
| **ショット型**（dùng 1 lần） | Tài liệu ghi đây là **lý do chưa monetize** |

**Vấn đề một câu:** Hệ thống đang “giỏi lấy data lúc cần đề xuất”, chưa “giỏi giữ người dùng đo lại sau renew”.

### 1.2 Before→After chưa thành

| Hiện trạng | Hệ quả |
|------------|--------|
| 有料 hóa trong kế hoạch phụ thuộc **beforeからafterの訴求** | Thiếu After → thiếu câu chuyện trả phí |
| FY2026 cần **After中心のスポット** | Nếu product/フロー không hỗ trợ After dễ dàng → trễ năm MVP |
| XD MVP cần survey Before/After + KPI + report | WDP chưa đóng vai trò chứng minh効果 đủ mượt |

**Vấn đề một câu:** Thiếu vòng **đo lại / so sánh / báo cáo hiệu quả** gắn XD.

### 1.3 有料契約 còn rất mỏng

| Hiện trạng | Hệ quả |
|------------|--------|
| **有料契約まだ２件程度** | **マネタイズには程遠い** |
| 有料 đang hướng **アフター経由**, chưa 受注 ổn định | Chưa có máy bán paid chạy đều |
| Free / nội bộ dùng nhiều hơn paid | WDP = 営業支援 mạnh, **直接売上** yếu |

---

## 2. Vấn đề tận dụng trong VIS（hệ thống có nhưng không lan）

### 2.1 Adoption lệch quy mô kinh doanh

| Chỉ số | Giá trị | Vấn đề |
|--------|---------|--------|
| Renew / năm | ~**500件** | Máy bán chính rất lớn |
| WDS | **月平均 ~10件** | Mỏng so với 500 |
| Workshop | **年間 5〜6件** | Rất thấp |
| Người dùng | Chủ yếu **意識の高い人**; nhiều người **chưa dùng lần nào** | Chưa thành mặc định trong đề xuất |

**Vấn đề một câu:** WDP chưa thấm vào quy trình chuẩn → không đủ case để nuôi After / XD / 有料.

### 2.2 Lead time đề xuất vs thời gian chạy WDS

| Hiện trạng | Vấn đề |
|------------|--------|
| Từ nhờ đề xuất → nộp đề xuất: **3〜4 tuần** | Cửa sổ ngắn |
| Chạy WDS kịp phản ánh vào đề xuất: **khó** | Mất cơ hội tăng 受注 bằng data |
| Barrier cũ: survey **メールアドレスベース**（thu list email） | Kéo dài lead time（đã có hướng URL） |
| KH hay nói: phải chọn partner rồi mới cho làm WDS | Survey bị đẩy muộn / bị chặn |

**Vấn đề một câu:** Dù tool có giá trị 受注, **nhịp bán hàng thường không khớp nhịp triển khai hệ thống**.

### 2.3 Hardle phía KH & nội bộ chưa được chốt sạch

Tài liệu ghi cần整理（hướng 3月末）các barrier:

- Phía **クライアント**
- Phía **社内**

→ Chưa rõ / chưa xử lý xong thì 利用件数 khó tăng ổn định（mục tiêu kiểu **月10件ベース**）.

---

## 3. Vấn đề hệ thống / UX / vận hành kỹ thuật

### 3.1 Chu kỳ phát triển WDP **重い**

Từ tài liệu XD×WDP:

> XP muốn dùng WDP khi提供 XD, nhưng **開発サイクルが非常に重たい** — khó **クイック** thêm chức năng nhẹ.

**Hệ quả:** XD cần xoay nhanh trong năm MVP, còn WDP không theo kịp → VIS từng tính app tạm song song rồi mới thay bằng WDP.

### 3.2 Setup 稼働 / 空間 còn分断（bằng chứng mockup）

| Hiện trạng UX | Vấn đề |
|---------------|--------|
| 空間分析: upload data & upload図面 **tách modal**, chọn version/floor thủ công | Dễ sai, tốn 工数 consultant |
| 稼働分析: nhiều nguồn（Wifi / 入退室 / Excel / Meraki）tách luồng | Onboarding nặng |
| Mockup đề xuất wizard gộp 1 luồng | Cho thấy pain hiện tại đã được nhận diện |

**Vấn đề một câu:** Chi phí **đưa data vào hệ thống** còn cao → cản 利用件数 và After.

### 3.3 Ổn định / chất lượng chức năng còn điểm nóng（milestone）

Các tín hiệu gần đây trên milestone:

| Vấn đề | Chi tiết |
|--------|----------|
| 稼働分析 | Functional test từng có **nhiều phần không chạy đúng**; từng phải siết phạm vi release（ưu tiên một phần Meraki） |
| Logic改修 | Cần verify rộng; rủi ro phát sinhバグ giống đợt稼働 → **lịch có thể không đủ** trong milestone hiện tại |
| AIレポート | **Yêu cầu VIS chưa chốt** → schedule tụt, tạm **giảm体制** chờ xác định |
| 稼働×サーベイ方式追加 | Đang chờ VIS合意実装イメージ |
| Ưu tiên lung lay | UI có thể ưu tiên hơn tích hợp / account phase 2; simulation ưu tiên thấp |
| Môi trường / nợ kỹ thuật | Dev env / vulnerability đã xử lý; vẫn còn修正 phụ thuộc scenario test, STG một phần trượt lịch |

**Vấn đề một câu:** Nền tảng đo（稼働・空間・サーベイ）đã launch từng phần, nhưng **độ tin cậy + tốc độ cải tiến + độ rõ yêu cầu** còn là điểm nghẽn.

### 3.4 “Có dashboard” chưa đủ thành “có insight cho consulting”

Từ hướng kinh doanh sheet 目的:

- Đầu tư hệ thống **一定落ち着いている** → muốn **シフト sang コンサル活用**
- Cần **AIを活用した分析・コンサルティング**（không bán AI thuần）
- Kỳ vọng: **AI工数削減**, **AI分析**, **PoC**（精度 quan trọng）

**Vấn đề một câu:** Hệ thống đang mạnh ở **hiển thị số**, chưa đủ mạnh ở **rút insight / làm report nhanh** cho consultant — đúng chỗ VIS đang đau khi muốn tăng consulting売上.

---

## 4. Vấn đề AI trên hệ thống（đã ghi nhận với VIS）

| Vấn đề | Nội dung tài liệu |
|--------|-------------------|
| An toàn dữ liệu / logic | Còn chỗ **ハードコード** — **nguy hiểm nếu giao cho AI** → cần **システム改善 ưu tiên** |
| AIレポート | Backlog có, nhưng **要望未確定** |
| Kỳ vọng bravesoft | Điều tra / ước tính **AI giảm được bao nhiêu 工数・コスト**; PoC khớp **精度** |

→ Đây vừa là **vấn đề kỹ thuật hệ thống**, vừa là **vấn đề giá trị consulting**（giảm工数 report / phân tích）.

---

## 5. Vấn đề ngoài “bug” nhưng gắn hệ thống（để khỏi nhầm）

Không phải defect thuần, nhưng làm hệ thống **không đạt mục tiêu**:

| Vấn đề | Bản chất |
|--------|----------|
| XD mới, thị trường **認知 còn thấp** | Khó bán kèm → WDP After thiếu “đầu kéo” dịch vụ |
| WD vẫn **請負・労働集約**; khác biệt design bị thu hẹp | Áp lực phải dùng WDP+XD để khác biệt — trong khi tool chưa sẵn cho After/有料 |
| Hướng **内製化** | VIS kỳ vọng bravesoft vượt **通常開発** — nếu chỉ vá feature lẻ, không giải pain consulting |

---

## 6. Gói lại: vấn đề hệ thống Vis đang gặp（list ưu tiên)

### P0 — cản trực tiếp năm MVP / コンサル売り上げ

1. **Mô hình dùng ショット型 / 現状把握** — chưa có vòng Before→After đủ mạnh trên product + quy trình  
2. **Chưa đủ giá trị “お金を払って使いたい”** — 有料 ~2; After chưa thành ống bán  
3. **工数 đưa data + đọc insight còn cao** — setup分断; thiếu AI phân tích/report ổn định  
4. **Lead time đề xuất ↔ WDS không khớp** — khó scale tận dụng dù 受注率 đã chứng minh  

### P1 — cản scale nội bộ & tốc độ

5. **Adoption nội bộ lệch**（10件/月 WDS vs 500案件; workshop 5–6/năm）  
6. **開発サイクル重い** — khó đáp ứng nhanh nhu cầu XP/XD  
7. **Yêu cầu AI/một số update chưa chốt** — đội hình & lịch bị treo  

### P2 — nợ kỹ thuật / ổn định

8. Điểm nóng **稼働ロジック / verify rộng / môi trường STG**  
9. Chỗ **hardcode** chưa an toàn cho AI  

---

## 7. Câu chuyển sang bước đề xuất

Mỗi vấn đề trên, khi viết【課題】, nên gắn 1 hệ quả kinh doanh:

| Vấn đề hệ thống | Nếu không xử lý |
|-----------------|-----------------|
| Không có After mượt | Không vào được 有料 & XD MVP đúng nghĩa |
| Setup/insight nặng | Không tăng 利用件数 → không scale consulting |
| Lead time survey | Không mở rộng 間接売上 / 受注支援 |
| AI未決 + hardcode | Không giảm 工数 consultant đúng kỳ vọng Vis |
| Chu kỳ nặng | XD đi trước, WDP tụt → lệch lộ trình 自走/SaaS |

**Center pin【課題】:**

> Hệ thống WDP đã chứng minh được giá trị **lấy data để thắng thầu WD**,  
> nhưng **chưa giải được các nút After / 有料 / giảm工数 insight** —  
> nên chưa đủ để Vis đạt mục tiêu **コンサルティング売り上げ** trong lộ trình năm MVP.
