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

# 2. Đề xuất: Phát triển mới từ đầu (scratch)

## 2-1. Vì sao chọn phát triển từ đầu

### Lý do 1: Trùng khớp với định hướng đã ghi trong kế hoạch kinh doanh

Trong 事業計画 có đoạn sau:

> WDPの開発サイクルは非常に重たくクイックな機能開発がライトに実施できない性質があります。
> ここでそれを補うのは**WDPとは別のアプリケーションを並行して開発**しておくことです。
> XPは事業提供に必要な機能をそのアプリケーションに持たせてサービス提供をしていきます。
> ここではアプリケーションはクライアントに利用してもらわなくて良いです。
> …社内ツールとして使われたアプリケーションはその後に**WDPに置換**していく事にします。

Tạm dịch: *vòng phát triển của WDP rất nặng, không thể triển khai tính năng mới một cách nhanh
và nhẹ. Để bù cho điều đó, cần phát triển song song một ứng dụng riêng, tách khỏi WDP.
XP sẽ đưa các tính năng cần thiết cho việc cung cấp dịch vụ vào ứng dụng đó.
Ở giai đoạn này, khách hàng không cần phải sử dụng ứng dụng.
Ứng dụng được dùng như công cụ nội bộ, sau đó sẽ thay thế dần vào WDP.*

Đề xuất này chính là việc cùng phát triển **ứng dụng riêng đó**.
Đây không phải một định hướng mới, mà là việc hiện thực hóa định hướng Vis đã có.

### Lý do 2: Ở giai đoạn kiểm chứng, tốc độ làm–thử–sửa quyết định kết quả

Chúng tôi hiểu rằng FY2026 là giai đoạn kiểm chứng XD MVP,
tức là thời kỳ vừa xác nhận "ai cần, cái gì hiệu quả, vì sao" vừa điều chỉnh nội dung.

Ở giai đoạn này, điều cần thiết không phải độ đầy đủ của tính năng
mà là **tốc độ phản ánh**.
Với vòng cải tiến của WDP hiện tại, có khả năng không theo kịp tốc độ kiểm chứng.

### Lý do 3: Có thể thiết kế trên tiền đề "đo lặp lại"

WDP hiện nay được thiết kế trên tiền đề **nắm bắt hiện trạng (sử dụng một lần)**.

Nếu thêm những điều sau vào sau, cấu trúc sẽ trở nên nặng:

- Đo lặp lại cùng một đối tượng và so sánh
- Thu thập lý do "vì sao, ở đâu"
- Xuất kết quả ra dưới dạng tài liệu đề xuất

Nếu làm mới từ đầu, có thể thiết kế ngay từ đầu trên tiền đề
**Before/After, đo định kỳ, và tiếng nói của worker**.

## 2-2. Cách triển khai

| Phase | Thời điểm dự kiến | Người dùng | Nội dung |
|---|---|---|---|
| **Phase 1** | Nửa đầu FY2026 | **XP (chỉ nội bộ)** | Vận hành After, tiếng nói worker, thiết lập KPI. Khách hàng không sử dụng |
| **Phase 2** | Nửa sau FY2026 | + Người phụ trách コンペ | Hỗ trợ đề xuất (xuất block nội dung từ kết quả, hoàn tất đăng ký và điều khoản trực tuyến) |
| **Phase 3** | FY2027 | + Khách hàng | Kiểm chứng màn hình hướng tới việc khách tự vận hành (survey định kỳ, báo cáo kiểm chứng hiệu quả) |
| **Phase 4** | FY2028 | — | Tích hợp và thay thế vào WDP |

Các giai đoạn được thiết lập theo đúng lộ trình trong kế hoạch kinh doanh:
`XD MVP → XD PMF → có hợp đồng năm của XD → phát triển ứng dụng → thay thế vào WDP`

**Vì sao Phase 1 không mở cho khách hàng:**
Theo đúng định hướng trong kế hoạch, việc vận hành như công cụ nội bộ trước
cho phép thử và sửa trước khi đưa ra trước khách hàng.

## 2-3. User story

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

## 2-4. Danh sách tính năng

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

## 2-5. Về các tính năng có phí — "vì sao tính năng này tốt"

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

## 2-6. Việc lồng ghép các tính năng khách hàng đã nêu

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

## 2-7. Quan hệ với WDP

| Mục | Định hướng |
|---|---|
| Vị trí | Phase 1–3 **cùng tồn tại** với WDP. Phase 4 tích hợp và thay thế |
| Dữ liệu | Nhận kết quả survey từ WDP, kết nối Before/After của cùng một khách hàng |
| Quản lý trùng lặp | Không tạo tình trạng phải nhập cùng một thông tin ở hai nơi. Điểm nhập dồn về một phía |
| Dễ thay thế | Thiết kế tách rời cấu trúc dữ liệu và API, hướng tới việc nội bộ hóa và thay thế trong tương lai |

## 2-8. Thứ tự phát huy hiệu quả của đề xuất

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

## Bốn điểm cần cẩn thận

1. **Đừng gọi F7 là "survey pulse mới"** — Vis đã tự tạo bộ survey rút gọn.
   Nên nói là "vận hành định kỳ", "chọn nội dung", "so sánh theo thời gian".
2. **Đừng gọi F2 là "thêm mới tiếng nói worker"** — buổi 座談会 đã có trong quy trình XD.
   Nên nói là "số hóa và mở rộng".
3. **Đừng đề xuất self-service hay SaaS ngay** — theo kế hoạch là giai đoạn sau.
   Đặt ở Phase 3–4.
4. **F1 cần được thấy là nặng, không phải phụ** — nhưng diễn đạt bằng lập luận
   ("công đoạn khó dự đoán số ngày") thay vì trưng bảng số liệu.

## Vì sao thêm mục 2-8 "thứ tự phát huy hiệu quả"

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
| 1 | Định nghĩa của 勝率 (tỷ lệ thắng) — chưa được trả lời | Cách viết phần hiệu quả |
| 2 | Ai làm ứng dụng riêng và làm khi nào | Ảnh hưởng trực tiếp tới Phase 1 |
| 3 | Chi tiết luồng đăng ký và kiểm tra pháp lý hiện tại | Biết cắt được bao nhiêu → F1 |
| 4 | Dữ liệu Before trong WDP có xuất ra được không | Điều kiện cho F9 |
| 5 | Ai sẽ là người chịu trách nhiệm về After phía Vis | F9 có nhắc nhưng cần người nhận |

Mục 3 và 4 nên đưa vào brief khảo sát của dev (`30-dev-survey-brief.md`)
trước khi báo effort.
