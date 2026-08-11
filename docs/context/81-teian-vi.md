# Nội dung đề xuất (bản tiếng Việt)

Bản tiếng Việt của `80-teian-genjo-kadai-scratch.md`, dùng để chia sẻ và rà soát nội bộ.
Bản tiếng Nhật là bản chính thức gửi khách.

**Quy ước thuật ngữ:** giữ nguyên các từ khoá tiếng Nhật/Anh mà team đang dùng hằng ngày
(WDP, WD, XD, XP, survey, Before/After, コンペ) và ghi nghĩa ở lần xuất hiện đầu.

---

## Nguyên tắc dùng số liệu

**Lập luận trước, số liệu sau — và chỉ dùng số khi thật cần.**

Số liệu trong 事業計画 (kế hoạch kinh doanh) là dành cho báo cáo nội bộ Vis. Nếu đưa nhiều vào đề xuất:

- người đọc phải đối chiếu số thay vì theo dõi mạch lập luận
- đề xuất trở nên giống bản báo cáo lại tình hình của chính khách
- có rủi ro sai lệch nếu số đã thay đổi so với thời điểm tháng 12/2025

### Số được phép dùng

| Loại | Ví dụ | Lý do |
|---|---|---|
| Số do **chính Vis trả lời** trong bảng câu hỏi | Before 83 case / After 5 case | Là câu trả lời cho câu hỏi của bravesoft, nên là bối cảnh chung của hai bên |
| Số thuộc **điều kiện làm việc** hai bên đều biết | Thời gian chuẩn bị đề xuất 3–4 tuần | Không phải số nội bộ |
| Tính chất của **tài liệu khách đã cung cấp** | Phần lớn câu hỏi là thang 5 mức, không có câu trả lời tự do | Nói tính chất, không cần con số chính xác |

### Số không đưa vào đề xuất

| Loại | Vì sao |
|---|---|
| Mục tiêu doanh thu / KPI từng năm | Báo cáo nội bộ |
| Số hợp đồng có phí mục tiêu | Chỉ tiêu nội bộ |
| Bảng giá theo bậc số nhân viên | Nội bộ |
| Tỷ lệ thắng và hiệu quả doanh thu gián tiếp | Nội bộ — chuyển thành lập luận: "giá trị dẫn tới việc thắng dự án đã được xác nhận" |
| Cỡ mẫu của bằng chứng | Là phê bình bằng chứng của khách, không đưa vào |
| Bảng chi tiết 6 tuần từng bước | Chuyển thành: "hai công đoạn nặng nhất là làm thủ tục đăng ký và phân tích kết quả" |

Số liệu chi tiết vẫn giữ trong `60-...md` và `70-...md` để bravesoft dùng nội bộ khi thiết kế và tính effort.

---

# 1. Vấn đề hiện tại và trạng thái muốn hướng tới

## 1-1. Nhìn lại hiện trạng

WDP đã tạo ra kết quả ở giai đoạn đề xuất. Việc dùng kết quả survey làm căn cứ cho đề xuất
giúp thuyết minh dựa trên dữ liệu thay vì giả định, và điều đó đã dẫn tới việc thắng dự án —
giá trị này đã được xác nhận qua quá trình triển khai vừa qua.

Tuy nhiên, **điều đó chưa dẫn tới hợp đồng có phí.**

Nguyên nhân không phải do thiếu tính năng, mà nằm ở chỗ cách sử dụng hiện nay
vẫn dừng ở mức **"đo một lần rồi kết thúc"**.

Vậy vì sao không tiếp tục được? Chúng tôi nhìn nhận có ba nguyên nhân mang tính cấu trúc.

## 1-2. Vấn đề 1: Kết quả survey không chuyển thành ngôn ngữ của đề xuất

Survey cho ra điểm số. Nhưng **"khu vực nào"**, **"vì sao"**, **"cần thay đổi điều gì"**
thì không nằm trong điểm số đó.

Phần lớn câu hỏi được thiết kế theo thang 5 mức và không có câu trả lời tự do,
nên **lý do mà người trả lời cảm nhận không được lưu lại dưới dạng dữ liệu.**

Kết quả là việc đọc hiểu điểm số rồi chuyển thành nội dung đề xuất
phụ thuộc vào kinh nghiệm của từng consultant.
Cùng một kết quả, sẽ có người vận dụng được vào đề xuất và người không.

## 1-3. Vấn đề 2: Toàn bộ quy trình survey không vừa với khung thời gian chuẩn bị đề xuất

Từ lúc nhận yêu cầu đề xuất đến buổi trình bày thường chỉ có 3–4 tuần.

Trong khoảng đó phải đưa vào toàn bộ: đề xuất làm survey, làm thủ tục đăng ký,
triển khai, phân tích kết quả, và phản ánh vào tài liệu đề xuất.

Hai công đoạn tốn thời gian nhất là:

- **Thủ tục đăng ký và xác nhận điều khoản**
  Có trao đổi văn bản và kiểm tra pháp lý, nên số ngày khó dự đoán.
- **Phân tích kết quả và phản ánh vào tài liệu đề xuất**
  Việc chuyển từ điểm số sang câu chữ và hình vẽ trong đề xuất đang làm thủ công.

Việc phát hành survey qua URL đã giúp rút ngắn công đoạn thu thập địa chỉ email.
Nhưng hai công đoạn trên vẫn còn, nên tình trạng không vừa khung thời gian vẫn tiếp diễn.

## 1-4. Vấn đề 3: After không được thực hiện, nên cửa vào hợp đồng có phí không mở ra

**Before 83 case, trong khi After chỉ 5 case.**

Vì hợp đồng có phí đi qua đường After, nên việc After không được thực hiện
trở thành giới hạn trực tiếp của việc thu phí.

Chúng tôi cho rằng lý do không nằm ở ý chí, mà ở **cấu trúc**:

- Thời điểm đánh giá là nửa năm sau khi chuyển văn phòng. Lúc đó dự án đã kết thúc và người phụ trách đã rời đi.
- Việc chuẩn bị After phải lặp lại đúng những công đoạn đã làm ở Before.
- Phía khách hàng cũng phát sinh gánh nặng khi phải đề nghị nhân viên trả lời lại một lần nữa.

Nói cách khác, đây là **cấu trúc mà nếu để tự nhiên thì việc đó sẽ không xảy ra.**

## 1-5. Trạng thái muốn hướng tới

| | Hiện tại | Trạng thái mong muốn |
|---|---|---|
| Căn cứ của đề xuất | Consultant tự đọc hiểu bằng kinh nghiệm | **Nội dung đề xuất được dẫn ra từ kết quả survey** |
| Chuẩn bị đề xuất | Không vừa khung thời gian | **Nằm gọn trong khung thời gian** |
| After | Nếu để tự nhiên thì không được thực hiện | **Có dòng chảy để việc đó diễn ra tự nhiên** |
| Sử dụng liên tục | Đo một lần rồi kết thúc | **Đo định kỳ và dẫn tới cải thiện** |
| Cung cấp XD | Phụ thuộc vào việc làm thủ công của XP | **Phần lặp lại được thì đưa lên hệ thống** |

Và diễn đạt trạng thái đích bằng một câu:

> **"Vì kết quả survey như thế này, nên phương án thay đổi layout tuần tới sẽ thay đổi như thế kia."**

Dữ liệu (phần tư vấn) và không gian (phần thiết kế) kết nối với nhau mà không bị chia cắt —
và chính **tốc độ phản ánh này** trở thành điểm khác biệt.

---

# 2. Đề xuất: Làm lại từ đầu (scratch development)

## 2-1. Tóm lược đề xuất

Thay vì tiếp tục cải tiến từng phần trên WDP hiện tại,
đây là đề xuất **làm lại WDP trên nền tảng mới và di chuyển theo từng giai đoạn**.

Đề xuất này là cách triển khai cụ thể để đi tới **「新生WDP」** (WDP tái sinh)
đã được nêu trong kế hoạch kinh doanh.

**Tiền đề: những gì đã tích lũy được sẽ được kế thừa.**
Bộ câu hỏi survey, dữ liệu trả lời đã có, và cơ chế phát hành qua URL đều là
đối tượng di chuyển. Đây không phải đề xuất bỏ đi những gì đã xây dựng để làm lại từ số không.

## 2-2. Vì sao là làm lại, không phải cải tiến

### Lý do 1: Cả ba vấn đề đều sinh ra từ cùng một tiền đề

WDP hiện nay được thiết kế trên tiền đề **"đo một lần để nắm bắt hiện trạng"**.

Ba vấn đề đã nêu ở trên đều nằm ngoài tiền đề đó.

| Vấn đề | Điều cần có | Quan hệ với tiền đề hiện tại |
|---|---|---|
| Kết quả không chuyển thành ngôn ngữ đề xuất | Thu thập lý do và xuất ra dưới dạng đề xuất | Là vùng mà việc đo một lần không xử lý |
| Không vừa khung thời gian | Nối liền từ thủ tục đăng ký đến phản ánh vào đề xuất | Các công đoạn trước và sau việc đo đều nằm ngoài phạm vi |
| After không được thực hiện | Đo lặp lại cùng một đối tượng và so sánh | Trái ngược nhất với tiền đề đo một lần |

Nói cách khác, không thể giải quyết bằng cách thêm từng tính năng một,
mà cần **thay thế chính nền tảng bằng tiền đề mới: "đo lặp lại, thu thập lý do,
và dẫn tới hành động tiếp theo"**.

### Lý do 2: Nếu chồng các bản cải tiến lên nhau thì không đạt được tốc độ cần thiết

Từ vị trí đang phụ trách phát triển, chúng tôi cảm nhận rằng
với nền tảng hiện tại, dù chỉ thêm một phần nhỏ thì phạm vi ảnh hưởng cũng rộng
và mất công kiểm tra.

Chúng tôi hiểu rằng FY2026 là giai đoạn kiểm chứng XD MVP —
thời kỳ vừa xác nhận "ai cần, cái gì hiệu quả, vì sao" vừa điều chỉnh nội dung.
Ở giai đoạn đó, điều cần thiết không phải độ đầy đủ của tính năng mà là **tốc độ phản ánh**.

Nếu giữ nguyên vòng cải tiến hiện nay, có khả năng không theo kịp tốc độ kiểm chứng.

### Lý do 3: Xét tới việc nội bộ hóa phát triển trong tương lai, một nền tảng được sắp xếp gọn sẽ dễ tiếp nhận hơn

Chúng tôi được biết trong kế hoạch kinh doanh có định hướng
dần nội bộ hóa việc phát triển trong tương lai.

Khi đó, **việc chuyển giao ở trạng thái đã được sắp xếp gọn sẽ thực tế hơn**
so với việc tiếp nhận nguyên một nền tảng đã tích tụ nhiều lớp qua thời gian.

Việc làm lại cũng là bước chuẩn bị cho điều đó.

## 2-3. Kế thừa cái gì / Làm lại cái gì

| Đối tượng | Xử lý | Ghi chú |
|---|---|---|
| Bộ câu hỏi survey (Work Design Survey và bản pulse) | **Kế thừa** | Có thể di chuyển nguyên theo định dạng hiện tại |
| Dữ liệu trả lời đã có | **Di chuyển** | Cần thiết cho việc so sánh Before/After, nên đặt là yêu cầu bắt buộc |
| Cơ chế phát hành qua URL | **Kế thừa** | Là phần đã cho thấy hiệu quả trong việc giảm rào cản triển khai |
| Việc phát hành và thu hồi survey | **Kế thừa** | Không thuộc đối tượng làm lại |
| Cách lưu giữ dữ liệu (tiền đề đo một lần) | **Làm lại** | Chuyển thành cấu trúc so sánh được cùng một đối tượng theo thời gian |
| Việc quản lý câu hỏi | **Làm lại** | Hỗ trợ thiết lập theo từng khách hàng và câu hỏi bổ sung theo điều kiện |
| Phân tích và xuất kết quả | **Mới** | Phần chuyển từ kết quả sang hình thức đề xuất |
| Vận hành After | **Mới** | Thông báo thời điểm đánh giá, người phụ trách, theo dõi KPI |

**Ý đồ của cách phân chia này:**
Phần được làm lại là **nền tảng và những vai trò mới đặt lên nền tảng đó**.
Những phần đang hoạt động tốt (câu hỏi, phát hành, dữ liệu đã tích lũy)
được kế thừa như tài sản.

## 2-4. Di chuyển theo từng giai đoạn

| Phase | Thời điểm dự kiến | Nội dung | WDP hiện tại |
|---|---|---|---|
| **Phase 1** | Nửa đầu FY2026 | Xây nền tảng mới. Di chuyển câu hỏi và dữ liệu trả lời. Đưa việc vận hành After và tiếng nói worker lên nền tảng mới | Chạy song song |
| **Phase 2** | Nửa sau FY2026 | Đưa phần hỗ trợ đề xuất lên nền tảng mới (hoàn tất đăng ký và điều khoản trực tuyến, xuất block nội dung từ kết quả) | Chạy song song |
| **Phase 3** | FY2027 | Hoàn tất di chuyển các tính năng hiện có. Mở survey định kỳ và báo cáo kiểm chứng hiệu quả cho khách hàng | Dừng sau khi di chuyển xong |
| **Phase 4** | FY2028 | Hợp nhất về WDP mới. Chuẩn bị chuyển giao cho việc nội bộ hóa | Dừng |

**Vì sao đặt giai đoạn chạy song song:**
Để không làm dừng các dự án đang triển khai.
Chuyển đổi lần lượt theo từng tính năng đã đưa sang nền tảng mới,
và thu hẹp môi trường cũ trong phạm vi đã xác nhận được.

**Quan hệ với kế hoạch kinh doanh:**
Trong kế hoạch có vạch ra con đường "phát triển song song một ứng dụng riêng,
sau đó thay thế vào WDP".
Đề xuất này là cách triển khai **làm lại chính WDP trên nền tảng mới**
để đi tới đích đến đó, tức là 「新生WDP」.
Chúng tôi cho rằng có thể phân định rõ ranh giới với những phần đang được
triển khai trước ở phía XP hoặc bằng công cụ AI nội bộ.

## 2-5. User story

### Người phụ trách コンペ và consultant (Workplace Design)

> **Muốn hoàn thành tài liệu đề xuất trong khoảng thời gian giới hạn kể từ khi nhận yêu cầu.**
> Vì nếu vượt khung thời gian đó thì không thể tham gia コンペ.

> **Muốn đưa trực tiếp "khu vực nào, vì sao, thay đổi thế nào" từ kết quả survey vào tài liệu đề xuất.**
> Vì hiện nay việc đọc hiểu kết quả rồi viết thành câu chữ phụ thuộc từng người và mất thời gian.

> **Muốn chỉ cần nhập kế hoạch nhân sự (bộ phận, số người, loại công việc) là có được phương án layout ban đầu.**
> Vì việc tính diện tích và phân vùng là phần tốn thời gian nhất trong quá trình làm đề xuất.

### XP (Experience Partner)

> **Muốn được thông báo tự động về thời điểm đánh giá sau khi chuyển văn phòng.**
> Vì sau khi dự án kết thúc, người phụ trách rời đi và việc thực hiện After bị bỏ sót.

> **Muốn được gợi ý các mục survey dùng làm KPI, dựa trên các dự án tương tự.**
> Vì việc chọn ra vài mục từ rất nhiều câu hỏi đang phụ thuộc vào kinh nghiệm.

> **Muốn lưu lại nội dung nghe được trong buổi 座談会 (trao đổi nhóm với nhân viên) ngay tại chỗ, dưới dạng có cấu trúc.**
> Vì hiện nay nội dung phỏng vấn chỉ nằm ở chỗ từng cá nhân, không dùng được cho dự án sau.

### Khách hàng cuối (bộ phận hành chính, nhóm vận hành)

> **Muốn thuyết minh hiệu quả của khoản đầu tư văn phòng cho ban lãnh đạo bằng số liệu.**
> Vì với một khoản đầu tư lớn thì luôn bị yêu cầu "kết quả".

> **Muốn định kỳ kiểm tra xem các quy tắc sau khi chuyển có bị hình thức hóa hay không.**
> Vì những việc như chỗ ngồi bị cố định hóa diễn ra dần theo thời gian, đến khi nhận ra thì khó quay lại.

> **Muốn tự chọn câu hỏi phù hợp với công ty mình.**
> Vì tuỳ ngành và cách làm việc, những mục cần đo là khác nhau.

### Worker (nhân viên)

> **Muốn truyền đạt cụ thể địa điểm và lý do khiến mình không hài lòng.**
> Vì chỉ với thang 5 mức thì không nói được "không tập trung được" là do
> "thiếu chỗ ngồi" hay do "ồn".

> **Muốn trả lời xong trong thời gian ngắn.**
> Vì nếu mỗi lần đều bị yêu cầu trả lời bộ câu hỏi dài thì sẽ không trả lời nữa.

### Bộ phận kinh doanh và Customer Success của Vis

> **Muốn đưa ra đề xuất và báo giá After ngay từ màn hình kết quả của Before.**
> Vì hợp đồng có phí đi qua đường After, không đề xuất thì không phát sinh cơ hội bán.

> **Muốn xem danh sách dự án nào đã đề xuất After và dự án nào đã thực hiện.**
> Vì nếu không thì không phán đoán được vấn đề nằm ở số lượng dự án hay ở tỷ lệ chuyển đổi.

## 2-6. Danh sách tính năng

Phân loại theo **dùng cho đề xuất** (giá trị gia tăng khi Vis đi đề xuất)
và **có phí** (khách hàng sử dụng liên tục).

| # | Tính năng | Người dùng chính | Phân loại | Vấn đề tương ứng |
|---|---|---|---|---|
| **F1** | Hoàn tất đăng ký và xác nhận điều khoản trực tuyến | Phụ trách コンペ / Khách hàng | Dùng cho đề xuất | Vấn đề 2 |
| **F2** | Tiếng nói worker (câu hỏi bổ sung theo điều kiện + trả lời tự do + chỉ vị trí trên layout) | Worker / XP | **Có phí** | Vấn đề 1 |
| **F3** | Từ kết quả survey xuất ra block nội dung đề xuất | Consultant | Dùng cho đề xuất | Vấn đề 1, 2 |
| **F4** | Phương án layout dựa trên kế hoạch nhân sự | Consultant | Dùng cho đề xuất (bản cập nhật là có phí) | Vấn đề 1, 2 |
| **F5** | Hỗ trợ thiết lập KPI (gợi ý vài mục từ bộ câu hỏi + điểm mục tiêu) | XP | **Có phí** | Vấn đề 3 |
| **F6** | Báo cáo kiểm chứng hiệu quả Before/After | Khách hàng / XP | **Có phí** | Vấn đề 3 |
| **F7** | Survey định kỳ (chọn nội dung, chạy theo lịch) | Khách hàng | **Có phí** | Vấn đề 3 |
| **F8** | Tùy biến survey theo từng khách hàng | Khách hàng / XP | **Có phí** | Vấn đề 3 |
| **F9** | Nhắc thời điểm đánh giá + hỗ trợ tạo After (tái sử dụng dữ liệu Before) | XP | Dùng cho đề xuất → cửa vào có phí | Vấn đề 3 |
| **F10** | Trực quan hóa tình hình cơ hội bán (trạng thái đề xuất và thực hiện After) | Kinh doanh / CS | Dùng cho đề xuất (nội bộ) | Vấn đề 3 |

## 2-7. Về các tính năng có phí — "vì sao tính năng này tốt"

### F6: Báo cáo kiểm chứng hiệu quả Before/After

**Lý do việc thu phí thành lập là vì điều này đã được chứng minh.**

Khi giành được hợp đồng có phí, chúng tôi được biết rằng ngay từ đầu Vis đã đưa cả
mức giá của After survey có phí vào và nhấn mạnh việc kiểm chứng hiệu quả.
Và điều khách hàng cảm nhận được giá trị chính là bản thân ý tưởng
**"số hóa hiệu quả của dự án văn phòng"**.

Nghĩa là điều khách hàng trả tiền cho không phải quyền sử dụng công cụ,
mà là **trạng thái có thể thuyết minh được về khoản đầu tư của mình**.

Về mặt tính năng, hệ thống sẽ tổng hợp trong một báo cáo: diễn biến điểm của các mục
đã đặt làm mục tiêu, mức chênh lệch giữa Before và After, và mối tương ứng
với các biện pháp đã thực hiện.

### F7: Survey định kỳ

**Lý do trả phí liên tục nằm ở chỗ "phát hiện được sự xấu đi từ sớm".**

Ngay sau khi chuyển văn phòng, mức độ hài lòng dễ tăng lên.
Nhưng theo thời gian, các quy tắc dần trở nên hình thức và chỗ ngồi dần bị cố định hóa.

Thay đổi này sẽ bị phát hiện muộn nếu chỉ đánh giá nửa năm một lần.
Khi đo định kỳ, có thể nắm được sớm việc **"đang bắt đầu quay trở lại như trước"**
và phán đoán được biện pháp tiếp theo cần làm.

Đây là giá trị không có được từ việc đo một lần,
tức là lý do sử dụng liên tục đã nằm ngay trong bản thân tính năng.

### F2: Tiếng nói worker

**Giải quyết tình trạng "biết điểm thấp nhưng không biết sửa ở đâu và sửa thế nào".**

Hiện nay việc nghe ý kiến được thực hiện qua buổi 座談会 với một phần nhân viên,
nhưng không thể khẳng định là đại diện cho toàn thể, và nội dung cũng chỉ lưu ở
ghi chép cá nhân.

Nếu thu được từ toàn bộ người trả lời thông tin **"khu vực nào, điểm gì, ảnh hưởng thế nào
tới công việc"** thông qua câu hỏi phân nhánh theo điều kiện, thì các biện pháp cải thiện
sẽ trở nên cụ thể.

Lưu ý: thiết kế theo hướng **không bắt tất cả mọi người trả lời bộ câu hỏi dài.**
Chỉ hiển thị câu hỏi bổ sung cho những người có điểm không hài lòng,
nhờ đó duy trì được tỷ lệ trả lời.

### F5: Hỗ trợ thiết lập KPI

**Tạo ra trạng thái dễ thuyết minh với tư cách là "hiệu quả của khoản đầu tư văn phòng".**

Survey cũng đo cả những yếu tố ngoài văn phòng như văn hóa doanh nghiệp,
lộ trình nghề nghiệp, quan hệ con người, sức khỏe.
Nếu theo dõi tất cả thì sẽ khó thuyết minh dưới dạng hiệu quả của đầu tư văn phòng.

Khi thu hẹp lại còn vài mục, việc giải thích quan hệ nhân quả trở nên dễ hơn.
Đây là phán đoán vốn đã được thực hiện trong quy trình XD,
và tính năng này chỉ **đưa phán đoán đó lên hệ thống dưới dạng gợi ý lựa chọn**.

### F8: Tùy biến survey theo từng khách hàng

**Khi đứng trên tiền đề đo định kỳ, việc tùy biến trở thành điều kiện tiên quyết
để khách sử dụng liên tục.**

Nếu không phải là những mục có ý nghĩa với công ty đó, động lực đo lặp lại sẽ không duy trì được.
Tùy theo ngành, cơ cấu loại công việc và cách làm việc, những mục muốn đo là khác nhau.

Đây cũng là tính năng được người phụ trách コンペ và các consultant nêu ra như một yêu cầu.

### F4 (chức năng cập nhật): Cập nhật phương án layout

**Hiện thực hóa tốc độ phản ánh "kết quả survey → phương án thay đổi layout tuần tới".**

Việc tạo layout ở thời điểm đề xuất được cung cấp như giá trị gia tăng của đề xuất,
còn **việc cập nhật sau khi bắt đầu vận hành** được thiết kế thành tính năng có phí.

Khi survey định kỳ phát hiện ra vấn đề, hướng tới trạng thái
có thể phản ánh ngay vào phương án thay đổi layout.

## 2-8. Việc lồng ghép các tính năng khách hàng đã nêu

| Yêu cầu | Nguồn | Tính năng tương ứng |
|---|---|---|
| Tạo được cấu trúc layout dựa trên kế hoạch nhân sự | Câu trả lời cho bảng câu hỏi | **F4** |
| Cơ chế hoàn tất đăng ký và xác nhận điều khoản trên WDP | Câu trả lời cho bảng câu hỏi | **F1** |
| Chức năng tùy biến survey theo từng khách hàng | Câu trả lời cho bảng câu hỏi | **F8** |
| Chọn mục survey làm KPI và đặt điểm mục tiêu | XD bước ⑥ Thiết kế KPI | **F5** |
| Thu thập ý kiến thực tế qua buổi 座談会 | XD bước ⑦ 座談会 | **F2** |
| Đánh giá theo mốc sau khi chuyển văn phòng | XD bước ⑨ Đánh giá và cải thiện | **F9, F6** |
| Triển khai survey từ giai đoạn nurturing | Kế hoạch kinh doanh | **F1** (làm nhẹ thủ tục đăng ký) |
| Mở rộng số lượng sử dụng Before & After | Kế hoạch kinh doanh | **F9, F6** |

**Tính năng nằm ngoài phạm vi:**

| Tính năng | Lý do |
|---|---|
| AI report / AI advice | Được biết đang triển khai bằng công cụ AI nội bộ của Vis |

## 2-9. Rủi ro dự kiến khi di chuyển và cách xử lý

Việc làm lại, nếu triển khai sai cách, sẽ ảnh hưởng tới công việc đang chạy.
Dưới đây là các điểm dự kiến và định hướng xử lý.

| Rủi ro dự kiến | Định hướng xử lý |
|---|---|
| Các dự án đang triển khai bị dừng | Phase 1–2 **chạy song song**, chuyển đổi lần lượt theo từng tính năng đã di chuyển được |
| Dữ liệu trả lời cũ bị chia cắt, không so sánh được Before/After | Đặt việc di chuyển dữ liệu là **yêu cầu bắt buộc** và xử lý ngay từ đầu. Nếu không đảm bảo được điểm này thì các tính năng có phí không thành lập |
| Phải nhập cùng một thông tin ở hai nơi trong thời gian chuyển đổi | Với từng loại thông tin, quy định rõ nơi nhập là một phía, không tạo tình trạng nhập cả hai |
| Người đang sử dụng phải chịu thêm gánh nặng thao tác | Không thay đổi lớn luồng thao tác hiện tại; các điểm thay đổi sẽ được tổng hợp và gửi trước |
| Tiêu chí chuyển đổi không rõ ràng, khiến việc di chuyển kéo dài | Quyết định trước **tiêu chí chuyển đổi** cho từng tính năng |

**Về tiêu chí chuyển đổi:**
Chúng tôi muốn lấy tiêu chí không chỉ là "bên mới làm được điều tương tự",
mà là **"đã chạy trọn một lần trong dự án thực tế"**.

## 2-10. Thứ tự phát huy hiệu quả của đề xuất

| Thứ tự | Nội dung | Hiệu quả |
|---|---|---|
| **1** | Tạo dòng chảy để After được thực hiện (F9, F5) | Cửa vào việc thu phí mở ra |
| **2** | Chuẩn bị phần nội dung để khách dùng tiếp có phí (F6, F7, F2, F8) | Không còn kết thúc sau một lần |
| **3** | Đưa vào khung thời gian chuẩn bị đề xuất (F1, F3) | Số lượng sử dụng phía Before tăng, làm tăng mẫu số cho bước 1 |
| **4** | Nâng chất lượng đề xuất (F4, F2) | Đề xuất trở nên tối ưu theo từng khách hàng |

**Vì sao đặt bước 1 trước:**
Vì hợp đồng có phí đi qua cửa After, nếu chỗ đó chưa mở
thì những cải thiện khác không dẫn tới doanh thu.

**Vì sao bước 3 đứng sau bước 1:**
Hiệu quả của việc tăng sử dụng phía Before chỉ phát huy sau khi dòng chảy After đã thông.
Nếu làm ngược thứ tự, Before tăng nhưng vẫn không dẫn được sang After.

---

# Phụ lục — Lưu ý khi trình bày

## Vị trí của bravesoft và ý nghĩa của "scratch development"

**bravesoft là bên phát triển WDP.** Nên đề xuất này là **làm lại chính WDP**
trên nền tảng mới, không phải xây một app riêng chạy song song mãi mãi.

Cần phân biệt rõ hai thứ dễ lẫn:

| | Là gì | Ai làm |
|---|---|---|
| **別アプリ trong kế hoạch kinh doanh** | Công cụ nội bộ cho XP, khách không dùng, sau đó nhập vào WDP | Track Vis đang tự làm (AI report) |
| **Scratch development trong đề xuất này** | Làm lại chính WDP trên nền tảng mới, di chuyển dần | bravesoft |

Cả hai đều hướng tới cùng một đích mà kế hoạch gọi là **「新生WDP」**.
Vì vậy mục 2-4 có ghi rõ "có thể phân định ranh giới", để không tạo cảm giác
bravesoft lấn sang phần Vis đang tự làm.

## Ba lý do làm lại — thứ tự có chủ ý

1. **Ba vấn đề đều sinh ra từ cùng một tiền đề** (đo một lần) → đây là lý do
   **về bản chất**, không phải về công nghệ. Đặt đầu tiên vì nối trực tiếp với phần 1.
2. **Cải tiến chồng lên nhau không đủ nhanh** → nói từ vị trí bên đang phát triển,
   nên là **trải nghiệm thực tế**, không phải phỏng đoán.
3. **Nội bộ hóa sau này dễ hơn** → dùng chính kế hoạch của Vis làm lợi ích cho họ.

## Mục 2-3 là mục quan trọng nhất về mặt tâm lý

Bảng **kế thừa / làm lại** tồn tại để trả lời trước một lo ngại chắc chắn xuất hiện:
*"vậy khoản đã đầu tư vào WDP thành vô nghĩa?"*

Điểm cần nhấn khi trình bày:

- Bộ câu hỏi survey (52 câu và pulse) **giữ nguyên** — định dạng hiện tại cho phép di chuyển
- Dữ liệu trả lời cũ **bắt buộc phải di chuyển**, vì thiếu nó thì không so sánh
  Before/After được, tức là không bán được
- Cơ chế URL **giữ** — đây là thứ đã có hiệu quả rõ
- Chỉ làm lại **nền tảng** và **những vai trò mới** đặt lên đó

## Cách phân biệt "dùng cho đề xuất" và "có phí"

Theo đúng ghi chú nội bộ của Vis trong bảng câu hỏi:

> ヴィスの提案の付加価値として利用するものと、定点的にお客様が継続利用するものの内容を分けたほうが良い
>
> *Tạm dịch: nên tách riêng phần dùng làm giá trị gia tăng cho đề xuất của Vis
> và phần khách hàng sử dụng liên tục theo định kỳ.*

| Phân loại | Ai dùng | Ai trả tiền | Cơ chế thu hồi |
|---|---|---|---|
| **Dùng cho đề xuất** | Vis (phụ trách コンペ, consultant, XP) | Không thu riêng | Qua tỷ lệ thắng dự án → hiệu quả gián tiếp |
| **Có phí** | Khách hàng cuối dùng lặp lại | Khách hàng cuối | Trực tiếp |

Đây là lý do F1 (đăng ký, điều khoản) được xếp vào nhóm dùng cho đề xuất:
nó giúp Vis thắng dự án nhanh hơn, chứ không phải thứ khách hàng cuối trả phí.

## Logic của từng tính năng có phí

Mỗi tính năng phải trả lời được **"vì sao khách trả tiền lặp lại"**,
không phải "vì sao tính năng này hay":

| Tính năng | Lý do khách trả tiền |
|---|---|
| F6 | **Đã được chứng minh** — chính cách bán này đã giành được hợp đồng có phí |
| F7 | Phát hiện **sự xấu đi từ sớm** (hình thức hóa, cố định hóa chỗ ngồi) — thứ đo một lần không có |
| F2 | Biết **sửa ở đâu**, thay vì chỉ biết điểm thấp |
| F5 | **Giải thích được nhân quả** với văn phòng, không lẫn yếu tố bên ngoài |
| F8 | **Điều kiện tiên quyết** để việc đo định kỳ có ý nghĩa |
| F4 bản cập nhật | Hiện thực hóa "tốc độ phản ánh vào thiết kế không gian" |

## Sáu điểm cần cẩn thận

1. **Đừng gọi F7 là "survey pulse mới"** — Vis đã tự tạo bộ survey rút gọn.
   Nên nói là "vận hành định kỳ", "chọn nội dung", "so sánh theo thời gian".
2. **Đừng gọi F2 là "thêm mới tiếng nói worker"** — buổi 座談会 đã có trong quy trình XD.
   Nên nói là "số hóa và mở rộng".
3. **Đừng đề xuất self-service hay SaaS ngay** — theo kế hoạch là giai đoạn sau.
   Đặt ở Phase 3–4.
4. **F1 cần được thấy là nặng, không phải phụ** — nhưng diễn đạt bằng lập luận
   ("công đoạn khó dự đoán số ngày") thay vì trưng bảng số liệu.
5. **Đừng để nghe thành "bỏ WDP làm lại"** — luôn đi kèm mục 2-3 (phần kế thừa).
   Từ khoá an toàn: 「土台を置き換える」 (thay thế nền tảng),
   không dùng 「捨てて作り直す」 (bỏ đi và làm lại).
6. **Đừng lấn vào phần Vis đang tự làm** — AI report và phần XP nội bộ để riêng,
   dùng chữ 「棲み分け」 (phân định ranh giới).

## Vì sao thêm mục 2-10 "thứ tự phát huy hiệu quả"

Mục này thay cho bảng đối chiếu KPI bằng số. Nó cho thấy bravesoft hiểu
**thứ tự nhân quả**, không chỉ liệt kê tính năng:

- After mở trước thì mới có cửa cho doanh thu có phí
- Sau đó mới tăng Before; nếu làm ngược thì Before tăng mà After vẫn tắc

Đây cũng là chỗ trả lời ngầm cho việc chính Vis nhận định rằng
việc xây dựng quy trình thương thảo là mệnh đề then chốt —
thứ tự này chính là việc xây quy trình đó.

## Những điểm cần xác nhận trước khi chốt

| # | Nội dung | Ảnh hưởng |
|---|---|---|
| 1 | **Vis có đồng ý hướng làm lại nền tảng** hay muốn cải tiến dần | Quyết định toàn bộ phần 2 |
| 2 | Dữ liệu trả lời cũ **xuất ra và di chuyển được không** | **Điều kiện tiên quyết** — thiếu thì không có Before/After |
| 3 | Chi tiết luồng đăng ký và kiểm tra pháp lý hiện tại | Biết cắt được bao nhiêu → F1 |
| 4 | Định nghĩa của 勝率 (tỷ lệ thắng) — chưa được trả lời | Cách viết phần hiệu quả |
| 5 | Ai sẽ là người chịu trách nhiệm về After phía Vis | F9 có nhắc nhưng cần người nhận |
| 6 | Quan hệ với phần Vis đang tự làm (AI report, công cụ cho XP) | Tránh trùng lặp phạm vi |

Mục 2 và 3 phải đưa vào brief khảo sát của dev (`30-dev-survey-brief.md`)
**trước khi** báo effort. Riêng mục 2 là điều kiện chặn: nếu dữ liệu cũ không
di chuyển được thì toàn bộ nhóm tính năng có phí mất cơ sở.

## Việc cần làm tiếp cho phần 2

| Việc | Vì sao |
|---|---|
| Khảo sát khối lượng và cấu trúc dữ liệu hiện tại | Ước lượng công di chuyển — phần khó dự đoán nhất của một lần làm lại |
| Lập danh sách tính năng WDP đang được dùng thực tế | Biết cái gì phải di chuyển, cái gì có thể bỏ |
| Xác định tiêu chí chuyển đổi cho từng tính năng | Tránh Phase 3–4 kéo dài vô hạn |
| Ước lượng effort theo từng Phase | Để Vis phán đoán được mức đầu tư |
