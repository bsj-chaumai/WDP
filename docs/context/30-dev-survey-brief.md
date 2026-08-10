# 調査ブリーフ（dev向け）— 有料化 & Survey

Mục tiêu: khảo sát hệ thống hiện tại để chốt nội dung 提案, **không lệch scope**.
Trục chính: **有料化** và **survey (gắn 有料化)**.

## 0. 原則（đọc trước khi khảo sát）

- Mọi phát hiện phải trả lời được: **"cái này giúp 有料化 / 継続 như thế nào?"**
- Phân biệt 2 lớp xuyên suốt:
  - **提案用** = dùng 1 lần để thắng 提案（付加価値）
  - **継続用 / 定点** = KH dùng lặp lại → nguồn 有料
- **AIレポート ngoài scope** lần này (chỉ ghi nhận nếu chạm dữ liệu chung).

---

## A. 有料化 — vì sao bán được / không bán được

### A1. 現状の課金モデル
- WDP hiện phân biệt **free vs paid** ở đâu? (data model / flag / plan)
- After survey có phí đang được tạo và quản lý thế nào? Thủ công hay có luồng riêng?
- Có chỗ nào ghi nhận **契約 / 単価 / プラン** không, hay hoàn toàn nằm ngoài WDP?

### A2. After のボトルネック（Before 83 / After 5）
- Từ 1 dự án Before → tạo After cần thao tác gì? Ai làm? Có tự động liên kết Before–After không?
- Cái gì đang cản việc tạo After: thiếu chức năng nhân bản? thiếu nhắc lịch sau 移転? report tốn công?
- Dữ liệu Before có **tái sử dụng cho After** để so sánh được không (cùng đơn vị / câu hỏi)?

### A3. 繰り返し課金の技術要件
- Muốn bán "gói 効果検証 định kỳ": hệ hiện tại thiếu gì?
  (subscription / kỳ hạn / quyền theo gói / giới hạn tính năng theo plan)
- Có thể tách quyền **提案用（Vis社内）** vs **継続用（エンド顧客）** không?

---

## B. Survey — gắn vào 有料化

### B1. サーベイ内容
- Survey hiện **cố định** hay đã có URL配信 / template? Cấu trúc câu hỏi lưu ở đâu?
- Có hỗ trợ **custom theo từng client** không (Q8 Vis yêu cầu)? Nếu chưa, chặn ở tầng nào?

### B2. 定点サーベイ（ユーザーが内容を選ぶ）— 有料化の本線
- Hệ thống có khái niệm **定期実行 / スケジュール** cho survey không?
- Có thể cho **user tự chọn / tự soạn nội dung survey** rồi phát định kỳ không?
- Nếu làm được → đây chính là **điểm gắn 有料**. Khảo sát khả thi + việc cần build.

### B3. サーベイ → 提案（Q1 の断絶）
- Kết quả survey xuất ra dạng gì? Đưa thẳng vào 提案書 / レイアウト được không, hay phải làm tay?
- Trong cửa sổ **3–4 tuần**, bước nào tốn thời gian nhất về mặt hệ thống?
  (thu thập / tổng hợp / xuất báo cáo)

---

## C. 顧客から既出の要望（Q8）— phải có phương án

Khảo sát khả thi + gắn về 有料 / 継続:

1. **人員配置マップ / 人員計画を踏まえたレイアウト** — dữ liệu người + không gian đang có gì, dựng tới đâu?
2. **申込・規約が WDP 上で完結** — luồng hiện tại đứt ở đâu?
3. **クライアントごとのサーベイカスタム** — trùng B1 / B2.

Với mỗi mục ghi rõ: **提案用 hay 継続用**, effort (S/M/L), phụ thuộc gì.

---

## D. 進行中の case（顧客視点ストーリー用）

- Chọn **1 case cụ thể** đang chạy để lấy dữ liệu thật (Before/After nếu có, kết quả survey).
- Dev xác nhận: dữ liệu case đó **lấy ra được từ hệ thống** để dựng story không?

---

## 提出フォーマット

Mỗi mục A / B / C trả lời theo bảng:

| 項目 | 現状（システム） | 有料化・定点サーベイに向けて足りないもの | 工数 (S/M/L) | 提案用 / 継続用 |
|---|---|---|---|---|
|  |  |  |  |  |

**ゴール:** sau khảo sát chốt được **cái gì đưa vào 提案 lần này（松竹梅）**
mà **trực tiếp phục vụ 有料化 + 定点サーベイ**.
