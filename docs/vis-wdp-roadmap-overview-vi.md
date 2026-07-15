# Tài liệu cho đội WDP：Bức tranh tổng thể về chiến lược, 課題 và định hướng của Vis

Tài liệu chuẩn hóa dành cho PM, BrSE và toàn bộ thành viên.

**Nguồn**
- 『ヴィスの現状と今後について』（WDP XD事業計画 / 小川 慧 / 2025/12/26）
- Vis chính thức：https://vis-produce.com/service/data-solution/wdp
- Vis chính thức：https://vis-produce.com/lp/experience-design

> Số liệu lấy tại thời điểm tài liệu（2025/12）. Trước khi dùng chính thức, hãy xác nhận lại với Vis.

---

## I. Mục tiêu lớn và sự dịch chuyển của Vis

### Mục tiêu doanh thu năm 2030
- Toàn công ty Vis hướng tới **250億 Yên**
- Mảng mới（XD＋WDP）hướng tới khoảng **25億 Yên** vào năm thứ 5（2030）  
  （Trong bảng kế hoạch chi tiết, mục tiêu FY2030 là **19.45億 Yên**）

### Sự dịch chuyển định vị（Rebranding）
Chuyển từ 「thiết kế văn phòng（chỉ làm không gian đẹp）」sang cung cấp **Work Design** — thiết kế toàn diện trải nghiệm làm việc.

### Công thức cốt lõi mới
**Work Design ＝ Workplace Design × Experience Design（XD）**

---

## II. Các vấn đề cốt lõi（課題）của Vis và hệ thống WDP hiện tại

### A. Vấn đề vĩ mô phía Vis

#### 1. Khoảng cách giữa 「văn phòng mới」và 「hiệu quả thực tế」
Khách hàng bỏ nhiều tiền để làm mới văn phòng, nhưng sau đó thường không dùng được đúng kỳ vọng（quy tắc mới bị hình thức hóa, chỗ ngồi lại cố định）. Cách làm cũ 「làm xong không gian là hết」chưa giải quyết được bài toán 「sau khi làm xong thì vận hành thế nào」.

#### 2. Phụ thuộc sức người và giới hạn mở rộng quy mô（Scalability）
- Mảng chủ lực hiện tại là **Workplace Design** đang ở trạng thái thâm dụng lao động（労働集約型）: muốn tăng doanh thu thì phải tăng thêm Consultant / Creator
- Mảng XD mới nếu chỉ dựa vào năng lực của chuyên viên tư vấn（XP）cũng sẽ rất khó scale

**【Hướng giải quyết】** Cần có hệ thống（WDP）giúp khách hàng tự vận hành văn phòng（自走）, giảm phụ thuộc vào tư vấn viên.

### B. 3 rào cản kỹ thuật & vận hành trên hệ thống WDP
（Các vấn đề sản phẩm mà đội phát triển cần xử lý）

#### 1. Rào cản công nghệ: chu kỳ phát triển chậm, hệ thống nặng
- **Thực trạng:** WDP hiện tại nặng, khó thêm tính năng mới hoặc chỉnh sửa nhỏ một cách nhanh（lightweight & quick）
- **Định hướng của Vis:** Phát triển song song một ứng dụng độc lập ngoài WDP, dùng trước như công cụ nội bộ cho XP; khi tính năng ổn định sẽ tích hợp / thay thế ngược vào WDP  
  ※Lưu ý: Vis chưa chỉ định bên nào làm app này và chưa có timeline chi tiết

#### 2. Rào cản thương mại hóa: khách hàng chỉ 「dùng 1 lần」（Shot-type）
- **Thực trạng:** Survey dùng khoảng **100案件/năm**, hỗ trợ bán hàng cho mảng thiết kế với hiệu ứng gián tiếp khoảng **1.4億 Yên**, nhưng hợp đồng trả phí trực tiếp mới khoảng **2件**. Lý do: chủ yếu dùng để nắm現状 rồi dừng（spot 1 lần）
- **Định hướng của Vis:** Mở rộng mô hình survey **Before & After**（trước và sau chuyển VP）, kết hợp với dịch vụ XD để chuyển sang dùng liên tục（継続利用）. Khoảng **6 tháng** sau chuyển VP sẽ chạy lại WDS để so điểm trước–sau

#### 3. Rào cản vận hành: lead time triển khai survey quá dài
- **Thực trạng:** Từ lúc khách gửi yêu cầu đề xuất đến buổi đề xuất / コンペ thường chỉ còn **3–4 tuần**. Trong thời gian ngắn này, việc thu thập email toàn bộ nhân viên rồi chạy survey và đưa kết quả vào đề xuất thường không kịp. Ngoài ra, trước khi ký HĐ khách cũng ngại cung cấp email sớm
- **Định hướng của Vis:** Chuyển sang phát survey bằng **URL dùng chung**（không bắt buộc đăng ký email）để rút ngắn chuẩn bị. Đồng thời thúc đẩy chạy survey sớm từ giai đoạn nuôi dưỡng KH（ナーチャリング）hoặc hearing ban đầu

---

## III. Lộ trình dịch chuyển chiến lược của Vis

Sự phát triển dịch vụ XD và hệ thống WDP（phần đội mình tham gia）sẽ tiến hóa cùng nhau như sau.

### FY2025 - FY2026（Thử nghiệm / MVP）

**Về dịch vụ**  
Vis kiểm chứng giá trị bằng gói dùng thử 「XD MVP」（giá khoảng **100万 Yên**）, gắn kèm vào đề xuất renew văn phòng thông thường.

Nội dung MVP tối thiểu:
- Survey Before & After
- Workshop Abstraction Ladder
- Event sau renew tối thiểu **2企画**
- Thiết lập KPI（điểm mục tiêu WDS）
- Follow event và báo cáo cuối

**Về sản phẩm WDP**  
FY2026 ưu tiên dùng WDP theo hướng **After-spot**（đo sau chuyển VP）để tạo thói quen đo lường dữ liệu cho khách.  
※Bản thân gói dịch vụ MVP vẫn gồm Before & After. After-spot là ưu tiên cách dùng WDP trong năm này.

**Về công cụ hỗ trợ**  
Định hướng phát triển / dùng song song một ứng dụng độc lập ngoài WDP để XP dùng nội bộ（giai đoạn này khách chưa nhất thiết phải tự thao tác app）.

### FY2027（PMF）
Thiết lập được đường trải nghiệm dịch vụ theo bậc: **Starter → Full XD → hợp đồng năm**.  
Phía WDP cũng kiểm chứng giá trị hỗ trợ 「自走」của khách và giá trị gắn với hợp đồng năm.

### FY2028（Thương mại hóa SaaS）
Khoảng năm 2028, khi đối thủ bắt đầu sao chép dịch vụ kiểu XD, Vis tạo khác biệt bằng công nghệ giá thấp, tiếp cận được tệp khách rộng.  
Các tính năng đã chạy ổn trên ứng dụng song song sẽ được tích hợp / thay thế hoàn toàn vào WDP chính（**新生WDP**）, và chính thức chạy mô hình **SaaS**（thu phí định kỳ）.

### FY2030（Quy mô lớn / trở thành trụ cột thứ 2）
Khách hàng giảm phụ thuộc consultant（XP）, dùng 「WDP（SaaS）」để tự đo dữ liệu, tự chạy hoạt động nội bộ và tự vận hành văn phòng（自走）.

Vis thoát dần mô hình phụ thuộc sức người, đưa mảng 「XD × WDP」đạt quy mô khoảng **25億 Yên**（theo bảng chi tiết FY2030 là **19.45億 Yên**）, trở thành trụ cột vững chắc thứ 2 bên cạnh Workplace Design.
