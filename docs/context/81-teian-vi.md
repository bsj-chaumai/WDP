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

# 2. Đề xuất: Cải tiến WDP (スクラッチ開発)

> **Lưu ý về cách gọi:** tiêu đề gốc tiếng Nhật là 「ご提案：スクラッチ開発」.
> Ở đây スクラッチ開発 nghĩa là **phát triển custom** — tự xây tính năng theo quy trình
> riêng của Vis, thay vì mua hoặc áp dụng tool có sẵn.
> **Không** mang nghĩa "xóa WDP đi làm lại".

## 2-1. Tóm lược đề xuất

**Đây là đề xuất phát triển các tính năng nhằm giải quyết ba vấn đề đã nêu,
trên chính WDP hiện tại.**

Không phải đưa vào một tool có sẵn, mà **phát triển custom (scratch)**
theo đúng quy trình đề xuất của Vis và cách triển khai XD.
Vì nội dung đi sâu vào phần đề xuất riêng cho từng khách hàng,
chúng tôi cho rằng tool phổ thông sẽ không cho ra được hình thức mà Vis cần.

**Những tài sản hiện có được giữ nguyên và tận dụng.**
Bộ câu hỏi survey, dữ liệu trả lời đã có, cơ chế phát hành qua URL
đều không bị làm lại — các tính năng cần thiết sẽ được thêm lên trên đó.

## 2-2. Nội dung cải tiến theo từng vấn đề

### Vấn đề 1: Kết quả survey không chuyển thành ngôn ngữ của đề xuất

Hiện nay quy trình dừng ở chỗ "ra được điểm số".
Chúng tôi bổ sung hai phần vào trước và sau điểm đó.

| Phần bổ sung | Nội dung |
|---|---|
| **Lớp hỏi lý do** (phía câu hỏi) | Chỉ hiển thị câu hỏi bổ sung với những câu trả lời có mức độ hài lòng thấp.<br>Thu thập: khu vực nào, điểm gì, ảnh hưởng tới công việc thế nào.<br>Thêm phần trả lời tự do, và cho phép chỉ vị trí trên bản layout |
| **Lớp chuyển thành đề xuất** (phía kết quả) | Thêm màn hình phân tích tổng hợp "ở đâu, vì sao, ảnh hưởng gì".<br>Thêm chức năng xuất ra dưới dạng dán được vào tài liệu đề xuất |

**Không can thiệp vào bộ câu hỏi hiện tại.**
Các câu hỏi đang có được giữ nguyên, và **câu hỏi bổ sung được thêm vào phía sau**.
Mục đích là tránh làm mất khả năng so sánh với những điểm số đã tích lũy.

### Vấn đề 2: Không vừa với khung thời gian chuẩn bị đề xuất

Xử lý riêng hai công đoạn đang tốn thời gian.

| Công đoạn | Nội dung cải tiến |
|---|---|
| **Thủ tục đăng ký và xác nhận điều khoản** | Cho phép hoàn tất bên trong WDP.<br>Chuyển việc trao đổi văn bản thành thao tác trên màn hình, và làm cho trạng thái xác nhận nhìn thấy được |
| **Phân tích kết quả và phản ánh vào đề xuất** | Sinh ra các block nội dung đề xuất từ kết quả.<br>Rút ngắn phần "đọc hiểu rồi viết ra" vốn đang làm thủ công |

Song song đó, chuẩn bị trạng thái **có thể triển khai nhẹ nhàng từ giai đoạn sớm**
như giai đoạn nurturing.

### Vấn đề 3: After không được thực hiện, nên cửa vào hợp đồng có phí không mở ra

Thay đổi trạng thái "nếu để tự nhiên thì không được thực hiện" bằng cơ chế.

| Tính năng bổ sung | Nội dung |
|---|---|
| **Thông báo thời điểm đánh giá** | Gắn kế hoạch After vào các dự án đã làm Before, và thông báo cho người phụ trách khi đến thời điểm đánh giá |
| **Hỗ trợ tạo After** | Cho phép tạo After bằng cách kế thừa thiết lập của Before, không phải thiết lập lại từ đầu |
| **Quản lý KPI** | Thiết lập và theo dõi các mục survey mục tiêu cùng điểm mục tiêu |
| **Chạy định kỳ** | Thiết lập lịch triển khai để có thể thực hiện lặp lại |
| **Báo cáo so sánh Before/After** | Tổng hợp diễn biến điểm và mức chênh lệch của các mục mục tiêu vào một báo cáo |
| **Danh sách trạng thái thực hiện** | Xem được dự án nào đã đề xuất After và dự án nào đã thực hiện |

## 2-3. Cách triển khai để hạn chế ảnh hưởng tới tính năng hiện có

WDP đang hoạt động, và trong lúc cải tiến thì các dự án vẫn tiếp tục.
Vì vậy chúng tôi triển khai theo các nguyên tắc sau.

| Nguyên tắc | Nội dung |
|---|---|
| **Lấy việc thêm mới làm nền** | Giữ lại tối đa các màn hình và câu hỏi hiện có, triển khai theo hướng bổ sung |
| **Cô lập phạm vi ảnh hưởng** | Tính năng mới được tách khỏi xử lý hiện có, cấu trúc sao cho không ảnh hưởng tới hoạt động hiện tại |
| **Phát hành nhỏ** | Phát hành theo từng tính năng, kiểm chứng trong dự án thực tế rồi mới đi tiếp |
| **Không làm hỏng dữ liệu hiện có** | Giữ trạng thái dữ liệu trả lời đã có vẫn tham chiếu được như trước |

**Vì sao đặt nguyên tắc "phát hành nhỏ":**
Chúng tôi hiểu rằng FY2026 là giai đoạn kiểm chứng XD MVP —
thời kỳ vừa xác nhận "ai cần, cái gì hiệu quả, vì sao" vừa điều chỉnh nội dung.
Ở giai đoạn đó, **vừa đưa ra vừa kiểm chứng** sẽ phù hợp hơn là làm gộp một lần.

## 2-4. Thứ tự phát triển

| Giai đoạn | Nội dung | Mục tiêu |
|---|---|---|
| **Giai đoạn 1** | Vận hành After (thông báo thời điểm, hỗ trợ tạo, quản lý KPI) | Mở cửa vào việc thu phí |
| **Giai đoạn 2** | Lớp hỏi lý do (câu hỏi bổ sung, trả lời tự do) và báo cáo so sánh | Chuẩn bị phần nội dung để khách dùng tiếp có phí |
| **Giai đoạn 3** | Hoàn tất đăng ký và điều khoản, xuất block nội dung đề xuất | Đưa vào khung thời gian chuẩn bị đề xuất |
| **Giai đoạn 4** | Layout từ kế hoạch nhân sự, tùy biến theo khách hàng | Làm cho đề xuất tối ưu theo từng khách hàng |

Cách suy nghĩ về thứ tự được ghi ở mục 2-10.

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

## 2-9. Tiền đề và các điểm cần xác nhận khi triển khai

Dưới đây là những điểm chúng tôi muốn xác nhận trước khi bắt tay vào cải tiến.

| Điều muốn xác nhận | Vì sao cần |
|---|---|
| Dữ liệu trả lời đã có có tham chiếu được theo dạng so sánh Before/After không | Là tiền đề để báo cáo so sánh thành lập |
| Luồng đăng ký và xác nhận điều khoản hiện tại (đang mất mấy ngày ở bước nào) | Cần cho việc phán đoán chuyển được bao nhiêu lên màn hình |
| Sẽ đặt ai làm người phụ trách After | Cần người nhận thông báo và chuyển sang thực hiện |
| Cho phép tùy biến câu hỏi theo khách hàng tới mức nào | Cần xác định phạm vi được phép thay đổi, để giữ khả năng so sánh |
| Có được phép can thiệp vào câu hỏi hiện có, hay chỉ thêm mới | Để giữ khả năng so sánh với điểm số cũ, chúng tôi khuyến nghị chỉ thêm mới |

**Về cách xử lý bộ câu hỏi:**
Nếu thay đổi các câu hỏi hiện có thì sẽ không so sánh được với điểm số đã tích lũy.
Vì vậy chúng tôi đề xuất phương án **không thay đổi câu hỏi hiện có,
chỉ thêm câu hỏi bổ sung**.

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

## Phạm vi của đề xuất — điểm dễ lẫn

**Đây là đề xuất cải tiến trên WDP hiện tại** — không phải làm lại nền tảng,
và không phải xây app riêng.

Ba thứ rất dễ lẫn, cần phân biệt khi trình bày:

| | Là gì | Ai làm |
|---|---|---|
| **Đề xuất này** | **Thêm tính năng vào WDP hiện tại**, phát triển custom theo quy trình của Vis | bravesoft |
| **別アプリ trong kế hoạch kinh doanh** | Công cụ nội bộ cho XP, khách không dùng, sau đó nhập vào WDP | Track Vis đang tự làm (AI report) |
| **新生WDP trong kế hoạch** | Đích dài hạn ở FY2028, sau khi hợp nhất | Chưa thuộc phạm vi đề xuất lần này |

**Ý nghĩa của スクラッチ開発 ở đây:** phát triển **custom** thay vì mua hoặc áp dụng
tool có sẵn — vì nội dung đi sâu vào quy trình đề xuất riêng của Vis,
tool phổ thông không đáp ứng được. Không mang nghĩa "xóa đi làm lại".

## Cấu trúc phần 2 và vai trò từng mục

| Mục | Vai trò |
|---|---|
| 2-1 | Nói rõ phạm vi: thêm vào WDP hiện tại, giữ nguyên tài sản |
| **2-2** | **Ruột của đề xuất** — với từng vấn đề, cải tiến cụ thể cái gì trên WDP |
| 2-3 | Trả lời trước lo ngại "sửa WDP có ảnh hưởng vận hành không" |
| 2-4 | Thứ tự phát triển |
| 2-5 → 2-8 | User story, danh sách tính năng, lý giải tính năng có phí, lồng ghép yêu cầu |
| 2-9 | Tiền đề và câu hỏi cần xác nhận |
| 2-10 | Lý do của thứ tự |

**Mục 2-2 là chỗ quan trọng nhất.** Nó trả lời trực tiếp câu hỏi
"khắc phục những gì ở WDP": mỗi vấn đề được gắn với một bảng cải tiến cụ thể,
thay vì chỉ nói định hướng chung.

## Hai nguyên tắc kỹ thuật đã đưa vào đề xuất

**1. Không sửa bộ câu hỏi hiện có, chỉ thêm câu hỏi bổ sung.**
Nếu sửa 52 câu hiện tại thì mất khả năng so sánh với dữ liệu đã tích lũy —
mà so sánh Before/After chính là thứ bán được tiền.
Nguyên tắc này xuất hiện ở cả mục 2-2 và 2-9.

**2. Tách biệt xử lý mới khỏi xử lý cũ.**
Đây là cách xử lý thực tế cho vấn đề "phạm vi ảnh hưởng rộng" của WDP hiện tại —
thay vì đề xuất làm lại nền tảng, ta giảm rủi ro bằng cách cô lập phần mới.

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

## Bảy điểm cần cẩn thận

1. **Đừng gọi F7 là "survey pulse mới"** — Vis đã tự tạo bộ survey rút gọn.
   Nên nói là "vận hành định kỳ", "chọn nội dung", "so sánh theo thời gian".
2. **Đừng gọi F2 là "thêm mới tiếng nói worker"** — buổi 座談会 đã có trong quy trình XD.
   Nên nói là "số hóa và mở rộng".
3. **Đừng đề xuất self-service hay SaaS ngay** — theo kế hoạch là giai đoạn sau
   (FY2027–2028).
4. **F1 cần được thấy là nặng, không phải phụ** — nhưng diễn đạt bằng lập luận
   ("công đoạn khó dự đoán số ngày") thay vì trưng bảng số liệu.
5. **Đừng để chữ "scratch" nghe thành "bỏ WDP làm lại"** — luôn kèm câu
   "những tài sản hiện có được giữ nguyên" ở mục 2-1.
   Nghĩa đúng là **phát triển custom**, không phải xóa đi làm lại.
6. **Đừng lấn vào phần Vis đang tự làm** — AI report và phần XP nội bộ để riêng.
7. **Nhấn nguyên tắc "không sửa câu hỏi hiện có, chỉ thêm mới"** —
   đây là điểm khiến khách yên tâm nhất, vì nó bảo vệ dữ liệu đã tích lũy.

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
| 1 | Dữ liệu trả lời cũ có **truy vấn được theo cùng một đối tượng qua thời gian** không | Điều kiện cho báo cáo so sánh Before/After (F6) |
| 2 | Chi tiết luồng đăng ký và kiểm tra pháp lý — đang mất mấy ngày ở bước nào | Biết cắt được bao nhiêu → F1 |
| 3 | Có được phép **thêm câu hỏi vào bộ hiện tại** không, và cấu trúc cho phép tới đâu | Điều kiện cho F2 |
| 4 | Ai sẽ là người chịu trách nhiệm về After phía Vis | F9 gửi thông báo nhưng cần người nhận |
| 5 | Cho phép tùy biến setting tới mức nào | Cân bằng giữa F8 và khả năng so sánh |
| 6 | Định nghĩa của 勝率 (tỷ lệ thắng) — chưa được trả lời | Cách viết phần hiệu quả |

Mục 1, 2, 3 phải đưa vào brief khảo sát của dev (`30-dev-survey-brief.md`)
**trước khi** báo effort.

## Việc cần làm tiếp cho phần 2

| Việc | Vì sao |
|---|---|
| Khảo sát cấu trúc dữ liệu survey hiện tại | Biết Before/After có nối được không — điều kiện của nhóm tính năng có phí |
| Khảo sát cách setting survey đang được quản lý | Biết thêm câu hỏi phân nhánh có khả thi không |
| Đo thời gian thực tế từng bước của đăng ký và điều khoản | Biết F1 cắt được bao nhiêu, để nói con số có căn cứ |
| Ước lượng effort theo từng giai đoạn | Để Vis phán đoán được mức đầu tư |
