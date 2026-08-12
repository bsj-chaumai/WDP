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

## 1-4. Vấn đề 3: After không được thực hiện, nên hiệu quả không được tích lũy

**Before 83 case, trong khi After chỉ 5 case.**

Chúng tôi được biết After hiện được cung cấp **miễn phí**,
và cơ chế tự động phát hành lại tới người cần khảo sát cũng đã có.
Dù vậy kết quả vẫn không được tích lũy.

Nguyên nhân, theo chúng tôi, là **động cơ thực hiện survey giảm đi sau khi chuyển văn phòng.**

- Vì tập trung toàn lực cho tới ngày chuyển, nên khó còn sức cho việc kiểm chứng sau đó
- Ngay sau khi có văn phòng mới, nhìn bề ngoài mức độ hài lòng đã cao
- Có những mục mà việc chuyển văn phòng một mình không làm thay đổi trong nửa năm, nên đo cũng khó thấy khác biệt
- Nếu không truyền đạt được rằng ý kiến lần trước đã được dùng thế nào, ý muốn trả lời lần sau sẽ giảm

Nói cách khác, đây là **cấu trúc mà nếu để tự nhiên thì sự quan tâm sẽ nhạt dần.**

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
| **Lớp hỗ trợ phán đoán** (phía kết quả) | Thêm màn hình phân tích tổng hợp "ở đâu, vì sao, với ai, ảnh hưởng bao nhiêu".<br>Cho phép chọn nội dung sẽ dùng và xuất ra ở dạng dùng được ngay |

**Không can thiệp vào bộ câu hỏi hiện tại.**
Các câu hỏi đang có được giữ nguyên, và **câu hỏi bổ sung được thêm vào phía sau**.
Mục đích là tránh làm mất khả năng so sánh với những điểm số đã tích lũy.

#### Về quan hệ với AI report

Với AI report đang được triển khai phía Vis, chúng tôi cho rằng vai trò được phân chia như sau:

| | Vai trò |
|---|---|
| **AI report** | Viết thành câu chữ |
| **Màn hình phân tích** | Để con người **phán đoán** (ưu tiên vấn đề nào, lấy khu vực nào làm đối tượng, đặt mục tiêu gì) |
| **Lớp hỏi lý do** | **Tạo dữ liệu đầu vào** cho hai phần trên |

Hiện tại thông tin có thể đưa cho AI **chỉ là điểm số**.
Vì không có thông tin về lý do, vị trí và mức ảnh hưởng,
đầu ra sẽ chỉ dừng ở việc diễn giải lại điểm số.

Khi thêm lớp hỏi lý do, **bản thân đầu ra của AI report cũng trở nên cụ thể hơn**.
Chúng tôi xem đây là đề xuất tạo tiền đề để nâng độ chính xác, không phải tính năng cạnh tranh.

Việc AI report có bao gồm cả phần sinh nội dung đề xuất hay không,
chúng tôi đã ghi ở mục 2-9 như một điểm muốn xác nhận trước.

#### Cấu trúc màn hình phân tích

Được cấu trúc theo đúng thứ tự phán đoán cần thiết khi viết đề xuất.

| # | Khối | Nội dung | Trả lời câu hỏi |
|---|---|---|---|
| 1 | **Ưu tiên** | Điểm của 6 mục, thứ hạng các mục thấp, sắp xếp theo **độ ảnh hưởng** (số người trả lời × tỷ lệ không hài lòng), so sánh với lần trước và trung bình nội bộ | Xử lý cái gì trước |
| 2 | **Vị trí** | Tổng hợp theo khu vực, thể hiện trên bản layout, loại không gian còn thiếu | Xảy ra ở đâu |
| 3 | **Lý do** | Tổng hợp phân loại câu hỏi bổ sung (ồn, thiếu chỗ, thiết bị, riêng tư, nhiệt độ, đặt chỗ…), nhóm các câu trả lời tự do | Vì sao xảy ra |
| 4 | **Đối tượng** | Cross theo bộ phận, loại công việc, số năm làm việc, nhóm tuổi. Kèm nơi làm việc và tỷ lệ loại công việc theo nghề | Xảy ra với ai |
| 5 | **Ảnh hưởng** | Mức ảnh hưởng tới công việc, đối chiếu với dữ liệu vận hành | Nghiêm trọng cỡ nào |
| 6 | **Phương án** | Phương án ứng với từng dạng vấn đề, case tương tự từ dự án trước | Nên làm gì |
| 7 | **KPI** | Đề xuất 2–3 mục làm mục tiêu, thiết lập điểm mục tiêu | Đo bằng gì |
| 8 | **Chọn và xuất** | Chọn nội dung sẽ dùng, xuất ra dạng dùng được cho tài liệu đề xuất | Giao sang đề xuất |

Khối 1–5 là **để đọc**, 6–7 là **để quyết định**, 8 là **để giao**.

Bổ sung:

- **Vì sao khối 1 sắp theo độ ảnh hưởng:** cần chọn 2–3 mục trong số nhiều mục,
  nên thứ tự phải phản ánh cả quy mô trả lời, không chỉ độ thấp của điểm
- **Vì sao có khối 4:** để đáp ứng yêu cầu "tạo môi trường phù hợp đặc thù nhiều loại công việc"
  và "cấu trúc layout dựa trên kế hoạch nhân sự" thì việc nắm theo nghề là tiền đề
- **Vì sao có khối 7:** mục được chọn ở đây chính là đối tượng so sánh ở After.
  Vấn đề 1 và vấn đề 3 nối với nhau qua khối này

Nếu triển khai bản tối thiểu, ưu tiên **khối 1, 2, 3, 8**.

### Vấn đề 2: Không vừa với khung thời gian chuẩn bị đề xuất

Xử lý riêng hai công đoạn đang tốn thời gian.

| Công đoạn | Nội dung cải tiến |
|---|---|
| **Thủ tục đăng ký và xác nhận điều khoản** | Cho phép hoàn tất bên trong WDP.<br>Chuyển việc trao đổi văn bản thành thao tác trên màn hình, và làm cho trạng thái xác nhận nhìn thấy được |
| **Phân tích kết quả và phản ánh vào đề xuất** | Chọn nội dung sẽ dùng trên màn hình phân tích và xuất ra dạng dùng được ngay.<br>Rút ngắn phần "đọc hiểu rồi viết ra" vốn đang làm thủ công |

Song song đó, chuẩn bị trạng thái **có thể triển khai nhẹ nhàng từ giai đoạn sớm**
như giai đoạn nurturing.

### Vấn đề 3: After không được thực hiện, hiệu quả không tích lũy

#### Xác nhận hiện trạng

- Thời điểm đánh giá là sau 6 tháng kể từ khi chuyển văn phòng
- Cơ chế **tự động phát hành lại survey tới người cần khảo sát đã có**
- Không cần thiết lập thủ công
- After **hiện được cung cấp miễn phí**

Nghĩa là **cả cơ chế phát hành và gánh nặng chi phí đều không phải vấn đề.**

#### Nguyên nhân có thể: sự thay đổi mức quan tâm sau khi chuyển

Cơ chế phát hành đang hoạt động mà kết quả không tích lũy —
chúng tôi cho rằng bối cảnh nằm ở việc **động cơ thực hiện survey giảm đi sau khi chuyển.**

Điều này trùng với nội dung đã ghi trong kế hoạch kinh doanh:

> Dù dự án cải tạo tiêu tốn hàng chục, hàng trăm triệu yên,
> **mọi doanh nghiệp đều dốc toàn lực cho tới ngày chuyển.**

> Vì bản thân việc cải tạo văn phòng là một thay đổi lớn dễ thấy với mọi người,
> **rất ít doanh nghiệp và cá nhân đối diện một cách nghiêm túc với những kỳ vọng đã đặt ra trước đó.**

> Nhưng với văn phòng thì phần sau đó bị **bỏ lửng**.
> **Vì nhìn bề ngoài thì thấy: văn phòng đẹp đã xong, mọi người đều vui.**

Ngoài ra, cùng đoạn đó còn có ghi:

> Thực tế trong survey công ty chúng tôi thu được,
> **có những trường hợp mà trong 6 mục, không phải mục nào cũng
> có thể cải thiện chỉ bằng thời điểm chuyển văn phòng.**

#### Cần phân biệt hai trạng thái

"Kết quả không tích lũy" có hai trạng thái, và cách xử lý khác nhau:

| | Trạng thái | Nguyên nhân có thể |
|---|---|---|
| **A** | Đã phát hành nhưng **câu trả lời không được thu về** | Không có lý do để trả lời lại. Không cảm nhận được rằng nội dung đã trả lời lần trước được sử dụng |
| **B** | Có câu trả lời nhưng **điểm gần như không thay đổi** | Đang đo những mục mà việc chuyển văn phòng một mình không làm thay đổi trong nửa năm |

Nếu là trường hợp B, dù tăng thông báo hay nhắc thúc thì tình hình cũng không đổi.
Cần **xem lại chính đối tượng được đo.**

Ở thời điểm hiện tại, chưa thể xác nhận bằng số liệu là A hay B đang xảy ra.

#### Nội dung cải tiến

Mục tiêu là tạo ra trạng thái mà **động cơ thực hiện vẫn sinh ra sau khi chuyển.**

| Thứ tự | Nội dung cải tiến | Nội dung | Hiệu quả với |
|---|---|---|---|
| **1** | **Đặt mục tiêu ở thời điểm Before** | Thiết lập mục tiêu và điểm mục tiêu ngay trong luồng Before, hiển thị suốt thời gian dự án. Ở After hiển thị song song "mục tiêu đã đặt" và "thực tế" | A, B |
| **2** | **Điều chỉnh nội dung câu hỏi After theo mức quan tâm sau khi chuyển** | Giữ lại các mục để so sánh, đồng thời thêm câu hỏi về vận hành sau chuyển (quy tắc mới có hoạt động không, có khu vực nào không được dùng không, chỗ ngồi có bị cố định lại không...) | **B** |
| **3** | **Phản hồi lại cho người trả lời** | Cho phép gửi lại cho người trả lời nội dung "với những điểm đã nêu, đã xử lý như thế này". Gửi trước hoặc cùng lúc với việc phát hành After | **A** |
| **4** | **Kết hợp với dữ liệu vận hành** | Đưa dữ liệu như tỷ lệ đi làm, tỷ lệ sử dụng không gian vào báo cáo kiểm chứng hiệu quả. Bảo đảm có chỉ số không phụ thuộc câu trả lời | A, B |
| **5** | **Cách trình bày báo cáo** | Không cấu trúc theo phán định đạt hay không đạt, mà lấy "điều gì đã thay đổi" và "tiếp theo nên làm gì" làm trung tâm | A |
| **6** | **Trực quan hóa tình hình thực hiện** | Hiển thị số case từng bước: dự án đối tượng → phát hành → câu trả lời → báo cáo. Đưa về trạng thái phán đoán được A hay B đang xảy ra | Để phán đoán |

**Không can thiệp vào cơ chế phát hành.**
Nội dung 1–5 đều là cải tiến ở phần trước và sau việc phát hành,
hoặc ở nội dung được đo.

#### Vì sao đặt "đặt mục tiêu" lên đầu tiên

Động cơ với After sinh ra khi **có điều cần phải xác nhận.**

Nếu trước khi chuyển đã đặt mục tiêu, After trở thành "nơi xác nhận mục tiêu đã đặt".
Nếu không có mục tiêu, After chỉ là "đo lại một lần nữa" và dễ bị để lại sau.

Việc đặt mục tiêu là nội dung đã có trong quy trình XD,
nhưng vì cách tiến hành kèm workshop nên chúng tôi được biết
số dự án thực hiện được là có hạn.

Vì vậy chúng tôi đề xuất hình thức **đặt mục tiêu được ngay trong luồng Before,
không lấy workshop làm tiền đề**. Hướng tới trạng thái mà cả những dự án
không có XD tham gia cũng lưu lại được mục tiêu.

#### Về cách đo tỷ lệ thực hiện

Before được thực hiện ở giai đoạn đề xuất, After ở nửa năm sau khi chuyển,
nên giữa hai mốc có khoảng thời gian triển khai dự án.

Vì vậy, nếu đặt cạnh nhau "số case Before và số case After trong cùng một năm tài chính"
thì sẽ là so sánh những dự án ở các thời điểm khác nhau.

Để nắm đúng tỷ lệ thực hiện, chúng tôi cho rằng cần tổng hợp
**với mẫu số là "các dự án đã qua nửa năm kể từ khi chuyển"**.
Phần "trực quan hóa tình hình thực hiện" ở trên tồn tại để làm được phép tổng hợp này.

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
| **Giai đoạn 1** | Đặt mục tiêu ở Before, trực quan hóa tình hình thực hiện | Cho After có lý do để xác nhận, và nắm được hiện trạng |
| **Giai đoạn 2** | Xem lại nội dung câu hỏi After, phản hồi lại cho người trả lời | Đưa về trạng thái có câu trả lời và thấy được thay đổi |
| **Giai đoạn 3** | Báo cáo so sánh Before/After (gồm dữ liệu vận hành), cách trình bày báo cáo | Đưa về dạng dùng được như một bản kiểm chứng hiệu quả |
| **Giai đoạn 4** | Lớp hỏi lý do (câu hỏi bổ sung, trả lời tự do), màn hình phân tích và phần xuất | Đưa về trạng thái chuyển thành ngôn ngữ của đề xuất |
| **Giai đoạn 5** | Hoàn tất đăng ký và điều khoản, mở rộng màn hình phân tích, layout từ kế hoạch nhân sự, tùy biến theo khách hàng | Đưa vào khung thời gian đề xuất và tối ưu theo từng khách hàng |

**Vì sao giai đoạn 1 có hai việc:**

**Đặt mục tiêu** là tiền đề để sinh ra động cơ với After.
Nếu không có mục tiêu để so sánh, After chỉ còn là "đo lại một lần nữa".
Ngoài ra vì được đưa vào trong luồng Before nên có thể triển khai
trong phạm vi ít ảnh hưởng tới hoạt động hiện có.

**Trực quan hóa** là để phân biệt trạng thái đang xảy ra.
Tùy theo là "câu trả lời không được thu về" hay "có câu trả lời nhưng điểm không đổi",
trọng tâm từ giai đoạn 2 sẽ khác nhau.

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

> **Muốn cho khách thấy mục tiêu đã đặt trước khi chuyển, đặt cạnh kết quả After.**
> Vì nếu không trình bày được "so với mục tiêu thì thế nào"
> thì sẽ không được đánh giá như một bản kiểm chứng hiệu quả.

> **Muốn xem danh sách dự án nào đã thực hiện After và đang tắc ở đâu.**
> Vì nếu không thì không phán đoán được là câu trả lời không được thu về,
> hay ngay từ đầu đã không được thực hiện.

## 2-6. Danh sách tính năng

| # | Tính năng | Người dùng chính | Phân loại | Vấn đề | Hiện trạng |
|---|---|---|---|---|---|
| **F1** | Hoàn tất đăng ký và xác nhận điều khoản trực tuyến | Phụ trách コンペ / Khách hàng | Dùng cho đề xuất | 2 | Mới |
| **F2** | Tiếng nói worker (câu hỏi bổ sung theo điều kiện + trả lời tự do + chỉ vị trí trên layout) | Worker / XP | Có thể thu phí sau | 1 | Mới |
| **F3** | Màn hình phân tích và phần xuất nội dung đã chọn | Consultant | Dùng cho đề xuất | 1, 2 | Mới |
| **F4** | Phương án layout dựa trên kế hoạch nhân sự | Consultant | Dùng cho đề xuất | 1, 2 | Mới |
| **F5** | **Đặt mục tiêu ở Before** (mục và điểm mục tiêu, hiển thị suốt dự án) | Consultant / XP | Dùng cho đề xuất | 3 | Mới |
| **F6** | **Báo cáo kiểm chứng hiệu quả Before/After** (gồm dữ liệu vận hành) | Khách hàng / XP | Có thể thu phí sau | 3 | Mới |
| **F7** | **Nội dung câu hỏi After** (mục so sánh + câu hỏi về vận hành sau chuyển) | Khách hàng / XP | Dùng cho đề xuất | 3 | **Cơ chế phát hành đã có**; thêm nội dung câu hỏi |
| **F8** | Tùy biến survey theo từng khách hàng | Khách hàng / XP | Có thể thu phí sau | 3 | Mới |
| **F9** | **Phản hồi lại cho người trả lời** (trả lại nội dung đã xử lý) | Khách hàng / Worker | Dùng cho đề xuất | 3 | Mới |
| **F10** | **Trực quan hóa tình hình thực hiện** (đối tượng, phát hành, câu trả lời, báo cáo) | Kinh doanh / CS / XP | Dùng cho đề xuất (nội bộ) | 3 | Mới |
| **F11** | Xác nhận tình hình trả lời và nhắc thúc | XP / Khách hàng | Dùng cho đề xuất | 3 | Mới |

**Về cột "Phân loại":**
Chúng tôi được biết After hiện được cung cấp miễn phí.
Vì vậy đề xuất này trước tiên lấy mục tiêu là **tạo trạng thái để việc thực hiện tích lũy được**,
còn việc thu phí được xếp là bước sau.

**Về những tính năng đã được trang bị:**
Cơ chế **tự động phát hành lại survey là cái đã có**, và đề xuất này không can thiệp vào đó.
F7, F9, F10, F11 đều là nội dung liên quan tới **trước và sau khi phát hành,
hoặc nội dung được đo**.

## 2-7. Về từng tính năng — "vì sao tính năng này tốt"

Chúng tôi được biết After hiện được cung cấp miễn phí.
Vì vậy đề xuất này trước tiên lấy mục tiêu là **tạo trạng thái để việc thực hiện tích lũy được**,
và với những tính năng có thể dẫn tới việc thu phí sau này thì ghi kèm vị trí của nó.

### F5: Đặt mục tiêu ở Before

**Tạo cho After "điều cần phải xác nhận".**

Động cơ với After sinh ra khi trước khi chuyển đã có mục tiêu được đặt.
Có mục tiêu thì After trở thành "nơi xác nhận mục tiêu đã đặt".
Không có thì After chỉ là "đo lại một lần nữa", và dễ bị để lại sau.

Việc đặt mục tiêu là nội dung đã có trong quy trình XD (thiết kế KPI),
nhưng vì kèm workshop nên số dự án thực hiện được là có hạn.

Tính năng này nhằm đưa về hình thức **đặt mục tiêu được ngay trong luồng Before,
không lấy workshop làm tiền đề** — hướng tới trạng thái mà cả dự án không có XD
cũng lưu lại được mục tiêu.

Khi sau này Vis đưa việc kiểm chứng hiệu quả thành hạng mục có phí,
chúng tôi cho rằng việc trình bày được "so với mục tiêu thì thế nào" sẽ là tiền đề.

### F6: Báo cáo kiểm chứng hiệu quả Before/After

**Tạo trạng thái có thể thuyết minh về khoản đầu tư.**

Khi giành được hợp đồng có phí, chúng tôi được biết điều khách hàng cảm nhận
được giá trị chính là bản thân ý tưởng **"số hóa hiệu quả của dự án văn phòng"**.

Nghĩa là trung tâm của giá trị không phải tính năng của công cụ,
mà là **trạng thái có thể thuyết minh được với ban lãnh đạo**.

Về tính năng, báo cáo tổng hợp diễn biến điểm của các mục đã đặt làm mục tiêu,
mức chênh lệch Before/After, và mối tương ứng với các biện pháp đã thực hiện.

**Điểm quan trọng là đưa cả dữ liệu vận hành vào.**
Tỷ lệ đi làm và tỷ lệ sử dụng không gian không phụ thuộc vào câu trả lời,
nên ngay cả khi câu trả lời không thu về đủ vẫn có thể chỉ ra được thay đổi.
Ngoài ra nó còn trả lời được đúng điểm mà sau khi chuyển người ta quan tâm nhất —
"thực tế có được sử dụng không".

**Về cách trình bày báo cáo:**
Nếu cấu trúc theo dạng phán định đạt hay không đạt thì việc xác nhận kết quả
dễ trở thành gánh nặng.
Vì kế hoạch kinh doanh cũng ghi rằng khó cải thiện cả 6 mục chỉ bằng việc chuyển,
chúng tôi đề xuất cấu trúc lấy **"điều gì đã thay đổi"** và **"tiếp theo nên làm gì"**
làm trung tâm.

### F7: Nội dung câu hỏi After

**Đưa về trạng thái đo được nội dung mà sau khi chuyển người ta đang quan tâm.**

Điều khách hàng muốn biết ở nửa năm sau khi chuyển, theo chúng tôi,
là những nội dung cụ thể về vận hành hơn là các mục như văn hóa hay lộ trình nghề nghiệp:

- Quy tắc mới có đang hoạt động không
- Có khu vực nào không được sử dụng không
- Chỗ ngồi có bị cố định lại không
- Phòng họp và không gian tập trung đã đủ chưa

Đây vừa là **nội dung đang được quan tâm**,
vừa là **nội dung có thể thay đổi trong nửa năm**.

Mặt khác, để so sánh thì cần đo cùng những mục giống nhau.
Vì vậy cấu trúc sẽ là **giữ lại các mục đã đặt làm mục tiêu,
đồng thời thêm câu hỏi về vận hành**.

Lưu ý là không can thiệp vào bản thân bộ câu hỏi hiện có (xem mục 2-9).

### F9: Phản hồi lại cho người trả lời

**Tạo trạng thái để người trả lời cảm thấy "trả lời có ý nghĩa".**

Nếu không truyền đạt được rằng với nội dung đã trả lời ở Before thì điều gì đã thay đổi,
ý muốn trả lời lần sau sẽ giảm. Chúng tôi cho rằng đây là phần ảnh hưởng
trực tiếp tới tỷ lệ trả lời.

Dự kiến cho phép gửi lại cho người trả lời nội dung
"những điểm đã nêu → nội dung đã xử lý", trước hoặc cùng lúc với việc phát hành After.

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

**Đây cũng là phần liên quan tới độ chính xác của AI report.**
Hiện tại thứ có thể đưa cho AI chỉ là điểm số. Khi có thêm thông tin về lý do,
vị trí và mức ảnh hưởng, độ cụ thể của đầu ra sẽ khác.

### Về việc thu hẹp mục mục tiêu (bổ sung cho F5)

Survey cũng đo cả những yếu tố ngoài văn phòng như văn hóa, lộ trình nghề nghiệp,
quan hệ con người, sức khỏe.
Nếu theo dõi tất cả thì sẽ khó thuyết minh dưới dạng hiệu quả của đầu tư văn phòng.

Ngoài ra, như kế hoạch kinh doanh cũng ghi,
không phải cả 6 mục đều thay đổi chỉ bằng việc chuyển văn phòng.

Vì vậy mục tiêu sẽ được **thu hẹp còn vài mục**.
Đây là phán đoán vốn đã được thực hiện trong thiết kế KPI của XD,
và tính năng này chỉ đưa phán đoán đó lên hệ thống dưới dạng **gợi ý lựa chọn**.

Việc thu hẹp cũng làm cho mức chênh lệch Before/After dễ đọc hơn.

### F8: Tùy biến survey theo từng khách hàng

**Khi đứng trên tiền đề đo lặp lại, việc tùy biến trở thành điều kiện tiên quyết.**

Nếu không phải là những mục có ý nghĩa với công ty đó, động lực đo lặp lại
sẽ không duy trì được.
Tùy theo ngành, cơ cấu loại công việc và cách làm việc, những mục muốn đo là khác nhau.

Đây cũng là tính năng được người phụ trách コンペ và các consultant nêu ra như một yêu cầu.

Để giữ khả năng so sánh, **chúng tôi muốn xác định trước phạm vi được phép thay đổi**
(xem mục 2-9).

### F4: Phương án layout

**Hiện thực hóa tốc độ phản ánh "kết quả survey → phương án thay đổi layout tuần tới".**

Ngoài việc tạo layout ở thời điểm đề xuất, hướng tới trạng thái
khi phát hiện vấn đề sau khi bắt đầu vận hành thì có thể phản ánh ngay
vào phương án thay đổi layout.

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
| **Số case đã phát hành và tỷ lệ trả lời thực tế** | Cần để phân biệt là "câu trả lời không được thu về" hay "có câu trả lời nhưng điểm không đổi" |
| **Biên độ thay đổi điểm ở những After đã thực hiện** | Nếu thay đổi nhỏ thì cần xem lại đối tượng được đo |
| **Phạm vi dự kiến của AI report** — có bao gồm việc sinh nội dung đề xuất không, dùng gì làm đầu vào | Phạm vi thiết kế của màn hình phân tích và phần xuất sẽ thay đổi. Để tránh trùng lặp, muốn xác nhận sớm |
| **Những vấn đề vận hành hay được hỏi sau khi chuyển** | Là căn cứ để quyết định nên thêm gì vào câu hỏi After |
| **Có thể đưa dữ liệu phân tích vận hành vào báo cáo không** | Cần để bảo đảm có chỉ số không phụ thuộc câu trả lời |
| **Mốc tính của cơ chế tự động phát hành** — tính từ ngày thiết lập, hay có thể chỉ định ngày khác | Để xác nhận có khớp với chuẩn "nửa năm sau khi chuyển" không |
| **WDP có đang lưu ngày hoàn tất chuyển văn phòng không** | Cần nếu phải đổi mốc tính |
| Dữ liệu trả lời đã có có tham chiếu được theo dạng so sánh Before/After không | Là tiền đề để báo cáo so sánh thành lập |
| Luồng đăng ký và xác nhận điều khoản hiện tại (đang mất mấy ngày ở bước nào) | Cần cho việc phán đoán chuyển được bao nhiêu lên màn hình |
| Sẽ đặt ai làm người phụ trách After | Cần người chuyển sang thực hiện |
| Cho phép tùy biến câu hỏi theo khách hàng tới mức nào | Cần xác định phạm vi được phép thay đổi, để giữ khả năng so sánh |
| Có được phép can thiệp vào câu hỏi hiện có, hay chỉ thêm mới | Để giữ khả năng so sánh với điểm số cũ, chúng tôi khuyến nghị chỉ thêm mới |

**Về cách xử lý bộ câu hỏi:**
Nếu thay đổi các câu hỏi hiện có thì sẽ không so sánh được với điểm số đã tích lũy.
Vì vậy chúng tôi đề xuất phương án **không thay đổi câu hỏi hiện có,
chỉ thêm câu hỏi bổ sung**.

**Về những tính năng đã được trang bị:**
Trong đề xuất này, những cơ chế **đã hoạt động — như tự động phát hành —
sẽ không làm lại mà được tận dụng**.
Nếu còn những tính năng tương tự khác, mong được thông báo trước
để chúng tôi điều chỉnh nội dung, tránh trùng lặp.

## 2-10. Thứ tự phát huy hiệu quả của đề xuất

| Thứ tự | Nội dung | Hiệu quả |
|---|---|---|
| **1** | Cho After có lý do để xác nhận (F5) và phân biệt hiện trạng (F10) | Có động cơ thực hiện, và biết tiếp theo cần sửa gì |
| **2** | Đưa về trạng thái có câu trả lời (F7, F9, F11) | Nội dung khớp mối quan tâm sau chuyển, nên câu trả lời quay về |
| **3** | Đưa về dạng dùng được như bản kiểm chứng hiệu quả (F6) | Thuyết minh được với ban lãnh đạo |
| **4** | Đưa về trạng thái chuyển thành ngôn ngữ đề xuất (F2, F3) | Kết quả survey kết nối được với đề xuất |
| **5** | Đưa vào khung thời gian và tối ưu theo khách hàng (F1, F4, F8) | Chuẩn bị đề xuất vừa khung, nội dung phù hợp từng khách |

**Vì sao đặt bước 1 trước:**

Động cơ với After sinh ra khi **có điều cần phải xác nhận**.
Nếu trước khi chuyển không có mục tiêu nào được đặt, After chỉ là "đo lại một lần nữa".
Vì vậy việc đặt mục tiêu được đưa lên đầu.

Cùng với đó là phân biệt trạng thái đang xảy ra.
Tùy theo là "câu trả lời không được thu về" hay "có câu trả lời nhưng điểm không đổi",
trọng tâm từ bước 2 sẽ khác nhau.

**Vì sao bước 3 đứng sau bước 2:**
Báo cáo kiểm chứng hiệu quả chỉ có ý nghĩa khi câu trả lời được thu về.
Dù chuẩn bị báo cáo trước, nếu không có dữ liệu gốc thì cũng không phát huy hiệu quả.

**Về quan hệ với việc thu phí:**
Chúng tôi được biết After hiện được cung cấp miễn phí.
Đề xuất này trước tiên lấy mục tiêu là **tạo trạng thái để việc thực hiện tích lũy được**
qua các bước 1–3.
Khi Vis xem xét việc thu phí, chúng tôi cho rằng
"trình bày được so với mục tiêu thì thế nào" (F5, F6) sẽ là tiền đề.

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

## Vấn đề 3 — ba giả thuyết đã bị loại, và hướng hiện tại

### Những gì đã được xác nhận là SAI

| Giả thuyết đã loại | Sự thật |
|---|---|
| ~~Thiếu chức năng nhắc mốc đánh giá~~ | Cơ chế tự động gửi lại sau 6 tháng **đã có** |
| ~~Cần người thiết lập thủ công~~ | **Tự động chạy**, không cần thiết lập |
| ~~Hợp đồng có phí chặn việc thực hiện~~ | **After hiện miễn phí** — không có rào cản thương mại |

Ba lần sai đều cùng một dạng: **suy diễn khi chưa xác thực**.
Đây là lỗi cần tránh cho phần còn lại của đề xuất.

### Hướng hiện tại: động cơ, không phải cơ chế

Cơ chế gửi đã tự động và miễn phí — nghĩa là **không có rào cản kỹ thuật hay chi phí**.
Nhưng kết quả vẫn không tích lũy. Vậy vấn đề nằm ở **động cơ thực hiện sau khi cải tạo**.

Giả thuyết này **được chính kế hoạch kinh doanh xác nhận**, và đây là điểm tựa mạnh nhất:

> どの企業も…**リニューアルの日を迎える事に精一杯**になる実態があります
>
> **その手前で掲げられていた期待に対してシビアに向き合う企業や人が少ない**
>
> オフィスではその先が**おざなり**になっています。
> **いいオフィスができてみんな喜んでいる。と一見は映るからです。**

Nghĩa là: đây **chính là bài toán mà XD được sinh ra để giải**.
Đề xuất của bravesoft là đưa nó vào hệ thống.

### Hai trạng thái cần phân biệt

| | Trạng thái | Nguyên nhân | Giải bằng |
|---|---|---|---|
| **A** | Gửi rồi nhưng **ít người trả lời** | Không có lý do trả lời lại; không thấy ý kiến lần trước được dùng | F5 (mục tiêu), F9 (vòng phản hồi), F11 (nhắc thúc) |
| **B** | Có trả lời nhưng **điểm gần như không đổi** | Đang đo thứ không thể thay đổi trong 6 tháng bằng việc chuyển văn phòng | **F7 (đổi nội dung After)**, F6 (thêm dữ liệu vận hành) |

**Kế hoạch kinh doanh gợi ý mạnh cho trường hợp B:**

> 実際に当社で取得したサーベイでは**6項目の内、すべてが移転というタイミングだけでは
> 向上させるのが難しい**というケースもでてきています

Nếu là B thì thêm bao nhiêu nhắc nhở cũng vô nghĩa — phải đổi thứ được đo.

**Chưa biết A hay B đang xảy ra** → đây là lý do F10 (làm hiện ra bằng số)
vẫn nằm ở giai đoạn 1.

### Cơ chế mạnh nhất: có lời hứa trước thì mới có việc phải kiểm sau

Đây là logic trung tâm của vấn đề 3 trong bản hiện tại.

Nếu ở Before đã đặt mục tiêu, After trở thành **"kiểm tra lời hứa"** — có lý do tồn tại.
Nếu không, After chỉ là "đo lại cho biết" và dễ bị bỏ.

Việc đặt mục tiêu **đã có trong XD (bước ⑥ thiết kế KPI)** — nhưng workshop XD
chỉ chạy 5–6 dự án/năm trên 500 dự án renewal.
Nghĩa là **hầu hết dự án không có mục tiêu nào được đặt**.

→ Nên F5 được thiết kế là **đặt mục tiêu không cần workshop**, nằm trong luồng Before
bình thường. Cách nói an toàn: 「XDのKPI設計を、ワークショップを前提とせず仕組みに載せる」.

### Về nội dung After (F7) — điểm mới quan trọng

Sáu tháng sau khi chuyển, câu hỏi thật của bộ phận hành chính không phải văn hóa
hay career, mà là:

- Quy tắc mới còn được tuân thủ không
- Khu vực nào đang bị bỏ trống
- Chỗ ngồi đã bị cố định lại chưa
- Phòng họp, chỗ tập trung đã đủ chưa

Những thứ này vừa là **điều họ đang quan tâm**, vừa **có thể thay đổi trong 6 tháng**.

Nên After = **mục tiêu (để so sánh) + câu hỏi vận hành (mới)**.

### Về dữ liệu phân tích vận hành (F6)

WDP đã có phân tích vận hành. Dữ liệu này **không cần ai trả lời**,
nên là cách phòng rủi ro cho tỷ lệ phản hồi thấp.
Và nó trả lời đúng câu hỏi họ quan tâm nhất — *"có ai dùng không"*.

### Về cách trình bày báo cáo

Nếu After bị coi là **chấm điểm dự án** thì có động cơ tránh,
vì điểm xấu là rủi ro cho người phụ trách.
Mà kế hoạch đã nói 6 mục khó cùng tăng — nên rủi ro đó là thật.

→ Báo cáo đóng khung là **"điều gì đã chuyển, điều gì nên làm tiếp"**,
không phải đạt/không đạt.

### Còn về con số 83 và 5

Before ở giai đoạn đề xuất; After ở 6 tháng sau chuyển.
Cộng chuỗi lại dễ tới 1,5–2 năm.
Kế hoạch cũng ghi lead time từ lúc dùng WDP tới lúc ghi nhận doanh thu là 4 tháng–1 năm.

→ Cách đo đúng phải lấy mẫu số là **dự án đã chuyển trên 6 tháng**.

**Lưu ý khi trình bày:** không nói "con số của Vis sai".
Nói theo hướng *"để đo đúng thì cần mẫu số là dự án đã qua 6 tháng"*.

### Về việc có phí

**After hiện miễn phí.** Nên đề xuất **không lấy việc thu phí làm mục tiêu trực tiếp**
của vấn đề 3 nữa — mục tiêu là **làm cho việc thực hiện tích lũy được**.

Việc thu phí chỉ được nhắc như bước sau, với điều kiện tiên quyết là
"trình bày được so với mục tiêu" (F5 + F6).
Cách này an toàn hơn: không áp đặt mô hình kinh doanh, mà chuẩn bị điều kiện cho nó.

## Cách phân biệt "dùng cho đề xuất" và "có thể thu phí sau"

**Quan trọng:** After **hiện miễn phí**.
Nên không còn phân đôi thành "có phí ngay" và "dùng cho đề xuất" như bản trước.

| Phân loại | Nghĩa | Ví dụ |
|---|---|---|
| **Dùng cho đề xuất** | Phục vụ việc Vis đi đề xuất và vận hành, không thu riêng | F1, F3, F5, F7, F9, F10, F11 |
| **Có thể thu phí sau** | Có thể thành hạng mục thu phí khi Vis quyết định thu phí | F2, F6, F8 |

Vẫn theo tinh thần ghi chú nội bộ của Vis trong bảng câu hỏi:

> ヴィスの提案の付加価値として利用するものと、定点的にお客様が継続利用するものの内容を分けたほうが良い

Nhưng **không áp mô hình kinh doanh lên khách**.
Đề xuất chỉ nói: nếu sau này thu phí thì điều kiện tiên quyết là
**trình bày được so với mục tiêu** — tức là có mục tiêu (F5)
và có báo cáo đối chiếu được (F6).

## Logic của từng tính năng — trả lời "vì sao cái này tốt"

| Tính năng | Lý do |
|---|---|
| **F5** | **Cơ chế trung tâm** — có mục tiêu trước thì After mới có việc phải kiểm |
| **F7** | Đo thứ khách đang quan tâm và **có thể thay đổi trong 6 tháng** — giải trường hợp gap nhỏ |
| **F9** | Người trả lời thấy ý kiến được dùng → chịu trả lời lần sau |
| **F6** | Nói được với ban lãnh đạo. Thêm dữ liệu vận hành để không phụ thuộc tỷ lệ trả lời |
| **F2** | Biết **sửa ở đâu**, thay vì chỉ biết điểm thấp |
| **F8** | Tiền đề để đo lặp lại có ý nghĩa |
| **F10** | Phân biệt được A (ít trả lời) và B (gap nhỏ) |
| **F4** | Hiện thực hóa "tốc độ phản ánh vào thiết kế không gian" |

## Chín điểm cần cẩn thận khi trình bày

1. **Đừng nói After là hàng có phí** — hiện miễn phí.
   Việc thu phí chỉ nhắc như bước sau, có điều kiện.
2. **Đừng nói thiếu chức năng nhắc hay gửi tự động** — đã có.
   Chỉ nói phần trước và sau việc gửi.
3. **Đừng gọi F7 là "survey pulse mới"** — Vis đã tự tạo bộ survey rút gọn.
   Nói là "thêm câu hỏi về vận hành sau chuyển".
4. **Đừng gọi F2 là "thêm mới tiếng nói worker"** — buổi 座談会 đã có trong quy trình XD.
   Nói là "số hóa và mở rộng".
5. **Đừng gọi F5 là "thêm KPI"** — thiết kế KPI đã có trong XD bước ⑥.
   Nói là "đưa lên hệ thống mà không cần workshop".
6. **Đừng đề xuất self-service hay SaaS ngay** — theo kế hoạch là giai đoạn sau
   (FY2027–2028).
7. **F1 cần được thấy là nặng, không phải phụ** — nhưng diễn đạt bằng lập luận
   ("công đoạn khó dự đoán số ngày") thay vì trưng bảng số liệu.
8. **Đừng để chữ "scratch" nghe thành "bỏ WDP làm lại"** — luôn kèm câu
   "những tài sản hiện có được giữ nguyên" ở mục 2-1.
9. **Nhấn nguyên tắc "không sửa câu hỏi hiện có, chỉ thêm mới"** —
   điểm khiến khách yên tâm nhất, vì nó bảo vệ dữ liệu đã tích lũy.

**Quy tắc chung rút ra sau ba lần sai:** trước khi viết bất kỳ tính năng nào
vào đề xuất, hỏi *"cái này đã có chưa, và ai đang chịu chi phí?"*

## Vì sao thêm mục 2-10 "thứ tự phát huy hiệu quả"

Mục này thay cho bảng đối chiếu KPI bằng số. Nó cho thấy bravesoft hiểu
**thứ tự nhân quả**, không chỉ liệt kê tính năng:

- Có mục tiêu trước → After mới có việc phải kiểm
- Có lý do trả lời → mới có dữ liệu
- Có dữ liệu → báo cáo mới có nghĩa
- Rồi mới tăng Before; nếu ngược lại, Before tăng mà After vẫn tắc

## Những điểm cần xác nhận trước khi chốt

| # | Nội dung | Ảnh hưởng | Ai xác nhận |
|---|---|---|---|
| 1 | **Số phát hành thực tế và tỷ lệ phản hồi** | Phân biệt A (ít trả lời) và B (gap nhỏ). Cơ sở của toàn bộ vấn đề 3 | Dev |
| 2 | **Biên độ thay đổi điểm ở các After đã làm** | Nếu nhỏ thì phải đổi nội dung đo (F7), không phải thêm nhắc nhở | Dev / Vis |
| 3 | **Phạm vi AI report** — có sinh nội dung đề xuất không, đầu vào là gì | Phạm vi thiết kế màn hình phân tích và phần xuất | Vis |
| 4 | **Những vấn đề vận hành hay được hỏi sau khi chuyển** | Quyết định nội dung câu hỏi thêm vào After (F7) | Vis |
| 5 | **Dữ liệu phân tích vận hành có đưa vào báo cáo được không** | Điều kiện để không phụ thuộc tỷ lệ trả lời (F6) | Dev |
| 6 | **Gốc tính mốc tự động gửi** — từ ngày thiết lập hay chỉ định được ngày khác | Xác nhận có khớp chuẩn "6 tháng sau chuyển" không | Dev |
| 7 | WDP có **lưu ngày chuyển văn phòng** không | Điều kiện nếu cần đổi gốc tính | Dev |
| 8 | Dữ liệu trả lời cũ có **truy vấn được theo cùng đối tượng qua thời gian** không | Điều kiện cho báo cáo so sánh (F6) | Dev |
| 9 | Có được phép **thêm câu hỏi vào bộ hiện tại** không, cấu trúc cho phép tới đâu | Điều kiện cho F2 và F7 | Vis + Dev |
| 10 | Luồng đăng ký và kiểm tra pháp lý — mất mấy ngày ở bước nào | Biết F1 cắt được bao nhiêu | Vis |
| 11 | Ai là người chịu trách nhiệm về After phía Vis | Cần người chuyển sang thực hiện | Vis |
| 12 | Cho phép tùy biến setting tới mức nào | Cân bằng F8 và khả năng so sánh | Vis |
| 13 | Định nghĩa của 勝率 (tỷ lệ thắng) — chưa được trả lời | Cách viết phần hiệu quả | Vis |

**Mục 1 và 2 quan trọng nhất.** Chúng quyết định trọng tâm của vấn đề 3:

| Kết quả kiểm tra | Trọng tâm |
|---|---|
| Gửi nhiều, phản hồi ít | Vòng phản hồi (F9), nhắc thúc (F11), mục tiêu (F5) |
| Có phản hồi, điểm không đổi | **Đổi nội dung đo (F7)** + dữ liệu vận hành (F6) |
| Cả hai | Làm F5 trước, rồi F7 và F9 song song |

## Việc cần làm tiếp cho phần 2

| Việc | Vì sao |
|---|---|
| **Lấy số phát hành, tỷ lệ phản hồi, và biên độ thay đổi điểm từ DB** | Phân biệt A và B — quyết định trọng tâm |
| **Rà soát toàn bộ tính năng WDP đang có, đối chiếu với F1–F11** | Đã ba lần suy diễn sai về hiện trạng — cần loại trừ trước |
| Hỏi Vis: sau khi chuyển, khách hay hỏi hoặc phàn nàn về điều gì | Là nội dung cần thêm vào After (F7) |
| Kiểm tra dữ liệu phân tích vận hành có ghép vào báo cáo được không | Cách phòng rủi ro cho tỷ lệ trả lời thấp |
| Xác nhận gốc tính mốc 6 tháng trong code | Xem có khớp chuẩn "6 tháng sau chuyển" không |
| Khảo sát cấu trúc dữ liệu survey | Biết Before/After có nối được không |
| Khảo sát cách setting survey được quản lý | Biết thêm câu hỏi có khả thi không |
| Hỏi Vis về phạm vi AI report | Tránh trùng lặp phần xuất |
| Ước lượng effort theo từng giai đoạn | Để Vis phán đoán được mức đầu tư |
