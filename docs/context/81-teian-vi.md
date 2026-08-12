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
  Là công đoạn phát sinh việc xác nhận và trao đổi.
  Luồng hiện tại đang trong quá trình khảo sát.
- **Phân tích kết quả và phản ánh vào tài liệu đề xuất**
  Việc chuyển từ điểm số sang câu chữ và hình vẽ trong đề xuất đang làm thủ công.

Việc phát hành survey qua URL đã giúp rút ngắn công đoạn thu thập địa chỉ email.
Nhưng hai công đoạn trên vẫn còn, nên tình trạng không vừa khung thời gian vẫn tiếp diễn.

## 1-4. Vấn đề 3: Không cho thấy được hiệu quả trước và sau cải tạo, nên không dẫn tới việc dùng tiếp và thu phí

**Before 83 case, trong khi After chỉ 5 case.**

Chúng tôi được biết After hiện được cung cấp **miễn phí**,
và cơ chế tự động phát hành lại tới người cần khảo sát cũng đã có.
Dù vậy, việc thực hiện vẫn không tích lũy được.

**Nguyên nhân gốc, theo chúng tôi, là hệ thống chưa cho thấy được
"cái gì đã thay đổi và thay đổi thế nào" giữa trước và sau khi cải tạo.**

Hiện tại, thứ thực sự còn lại là cảm nhận
"**không gian đã đẹp hơn**", "**việc cải tạo đã xong**".

Vì vậy phát sinh chuỗi nhân quả sau:

```
Không cho thấy được hiệu quả trước và sau cải tạo
  → Không sinh ra lý do để tiếp tục đo
  → Không có căn cứ và sức thuyết phục để đề xuất như một dịch vụ có phí
```

Bối cảnh của điều này gồm:

- Vì tập trung toàn lực cho tới ngày chuyển, nên khó còn sức cho việc kiểm chứng sau đó
- Ngay sau khi có văn phòng mới, nhìn bề ngoài mức độ hài lòng đã cao
- Bộ câu hỏi hiện tại được thiết kế để nắm hiện trạng toàn diện, khác với nội dung muốn xác nhận sau khi chuyển
- Nếu không truyền đạt được rằng nội dung đã trả lời được dùng thế nào, ý muốn trả lời lần sau sẽ giảm

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
| **Phân tích kết quả và phản ánh vào đề xuất** | Tự động tổng hợp dữ liệu trả lời để xác nhận được xu hướng.<br>Trên cơ sở đó, cho phép chọn nội dung sẽ dùng và xuất ra |

Song song đó, chuẩn bị trạng thái **có thể triển khai nhẹ nhàng từ giai đoạn sớm**
như giai đoạn nurturing.

#### Về đăng ký và điều khoản — giảm thời gian xác nhận và trao đổi

**Bằng cách gộp việc đăng ký và xác nhận điều khoản thành một luồng trên WDP,
chúng tôi cho rằng có thể giảm được thời gian xác nhận và trao đổi
đang phát sinh giữa consultant và khách hàng cuối.**

Lưu ý: luồng đăng ký và xác nhận điều khoản hiện tại đang trong quá trình khảo sát,
và nội dung điều khoản cần xác nhận thì chúng tôi dự định hỏi thêm.
Vì vậy **phạm vi cắt giảm được sẽ chốt sau khi có kết quả khảo sát và xác nhận.**

Trên cơ sở đó, chúng tôi kỳ vọng các hiệu quả sau:

| Kỳ vọng được | Nội dung |
|---|---|
| **Giảm việc trao đổi xác nhận** | Thay việc đi lại xác nhận phát sinh theo từng dự án bằng thao tác trên màn hình |
| **Thủ tục gom về một chỗ** | Không cần tiến hành đăng ký và xác nhận điều khoản một cách riêng rẽ |
| **Xác nhận được tiến độ** | Biết được đã hoàn tất tới đâu, nên giảm công đi xác nhận tình hình |
| **Dễ thực hiện từ giai đoạn sớm** | Thủ tục nhẹ hơn thì việc thực hiện ở giai đoạn nurturing trở nên khả thi |

#### Về phân tích kết quả — từ tuần tự sang song song

Chúng tôi được biết hiện tại thứ tự là: sau khi lấy được kết quả,
consultant xác nhận nội dung, chuyển từ số liệu thành câu chữ rồi phản ánh vào đề xuất.

Nếu dữ liệu trả lời được tự động tổng hợp,
**xu hướng nhìn thấy được ngay khi câu trả lời còn đang về.**
Không cần chờ đủ mới bắt đầu xem xét, nên việc phân tích chạy song song với việc thu.

Điều này rút ngắn **tổng thời gian** nhiều hơn là chỉ "phân tích nhanh hơn".

| Cải thiện được | Nội dung |
|---|---|
| **Bắt đầu xem xét song song với việc thu câu trả lời** | Xác nhận được xu hướng mà không phải chờ đủ |
| **Bắt đầu công việc từ nội dung đã tổng hợp** | Giảm phần chuyển số liệu thành câu chữ |
| **Giảm chênh lệch giữa người phụ trách** | Mọi người bắt đầu từ cùng một bản tổng hợp, nên tính phụ thuộc cá nhân giảm |
| **Thông tin dễ bỏ sót luôn được đưa lên** | Phần trả lời tự do dễ bị đọc lướt, nhưng khi được tổng hợp thì luôn xác nhận được |

#### Hiệu quả ở tầng kinh doanh

Việc cải thiện vấn đề này cũng là tiền đề cho các vấn đề khác.

```
Vừa với khung thời gian đề xuất
  → Số dự án thực hiện được survey trong thời gian đề xuất tăng
  → Số dự án đề xuất được dựa trên dữ liệu tăng (góp vào tỷ lệ thắng)
  → Số case Before tăng → mẫu số của After cũng tăng
```

**Đồng thời, tổn thất cơ hội giảm.**
Hiện tại nếu survey không kịp trong thời gian đó,
đề xuất sẽ đi ra mà không có dữ liệu, và ở dự án đó không thu được
phần đóng góp vào tỷ lệ thắng.
Việc rút ngắn lead time cũng chính là **giảm số dự án như vậy.**

#### Cách đo hiệu quả

| Chỉ số | Xem cái gì |
|---|---|
| Số ngày từ đăng ký đến thực hiện | Hiệu quả của cải tiến đăng ký, điều khoản |
| Số ngày từ lấy kết quả đến phản ánh vào đề xuất | Hiệu quả của cải tiến phân tích |
| **Tỷ lệ dự án thực hiện được survey trong thời gian đề xuất** | Chỉ số tổng của vấn đề này |
| Số case thực hiện ở giai đoạn nurturing | Hiệu quả của việc làm nhẹ thủ tục |
| Số đề xuất có kết quả survey làm căn cứ | Sự kết nối với tỷ lệ thắng |

### Vấn đề 3: Không cho thấy được hiệu quả trước và sau cải tạo, nên không dẫn tới việc dùng tiếp và thu phí

#### Xác nhận hiện trạng

- Thời điểm đánh giá là sau 6 tháng kể từ khi chuyển văn phòng
- Cơ chế **tự động phát hành lại survey tới người cần khảo sát đã có**
- Không cần thiết lập thủ công
- After **hiện được cung cấp miễn phí**

Nghĩa là **cả cơ chế phát hành và gánh nặng chi phí đều không phải vấn đề.**

#### Nguyên nhân gốc: chưa cho thấy được hiệu quả trước và sau cải tạo

**Hệ thống hiện tại chưa cho thấy được "cái gì đã thay đổi và thay đổi thế nào"
giữa trước và sau khi cải tạo.**

Thứ thực sự còn lại là cảm nhận
"**không gian đã đẹp hơn**", "**việc cải tạo đã xong**".

Vì vậy phát sinh chuỗi nhân quả sau:

```
Không cho thấy được hiệu quả trước và sau cải tạo (chỉ còn lại cảm nhận)
  ↓
Không sinh ra lý do để tiếp tục đo (không có điều kiện tạo thói quen dùng tiếp)
  ↓
Không có căn cứ và sức thuyết phục để đề xuất như dịch vụ có phí
```

Việc câu trả lời không được thu về cũng nằm trong chuỗi này.
**Khi không có gì cần xác nhận thì cũng không sinh ra lý do để trả lời.**

#### Bối cảnh: sự thay đổi mức quan tâm sau khi chuyển

Điều này trùng với nội dung đã ghi trong kế hoạch kinh doanh:

> Dù dự án cải tạo tiêu tốn hàng chục, hàng trăm triệu yên,
> **mọi doanh nghiệp đều dốc toàn lực cho tới ngày chuyển.**

> Vì bản thân việc cải tạo văn phòng là một thay đổi lớn dễ thấy với mọi người,
> **rất ít doanh nghiệp và cá nhân đối diện nghiêm túc với những kỳ vọng đã đặt ra trước đó.**

> Nhưng với văn phòng thì phần sau đó bị **bỏ lửng**.
> **Vì nhìn bề ngoài thì thấy: văn phòng đẹp đã xong, mọi người đều vui.**

#### "Câu trả lời không được thu về" chia thành hai bước

Để câu trả lời được thu về, cần hai chuyển động trong nội bộ khách hàng.

| Người cần chuyển động | Cần gì để chuyển động | Nếu thiếu |
|---|---|---|
| **Bộ phận hành chính, nhóm vận hành** (người thúc đẩy nội bộ) | Trạng thái mà **có ai đó sẽ hỏi về con số đó** | Không có thông báo nội bộ, nhân viên không biết có survey |
| **Nhân viên** (người trả lời) | Tin rằng **trả lời sẽ dẫn tới thay đổi gì đó** | Thấy thông báo cũng không trả lời |

Trong nhiều trường hợp, chỗ tắc trước là ở người thứ nhất.
Bối cảnh nhân viên không trả lời là vì **trong nội bộ, việc này chưa được định vị là quan trọng**.

Vì vậy, bộ câu hỏi After cần chứa **nội dung mà cả hai bên đều muốn xác nhận.**

#### Loại chỉ số nào tạo ra được "muốn xác nhận"

Chỉ số càng thỏa 5 điều sau thì động cơ thực hiện càng cao:

| # | Điều kiện | Lý do |
|---|---|---|
| 1 | **Có ai đó sẽ hỏi về nó** | Chỉ số mà ban lãnh đạo không hỏi thì bộ phận hành chính khó có lý do đo |
| 2 | **Có thể thay đổi trong nửa năm** | Chỉ số không thay đổi thì đo lại cũng không có ý nghĩa |
| 3 | **Từ kết quả biết được bước tiếp theo** | Nếu không biết, có số cũng không dẫn tới hành động |
| 4 | **Bản thân người trả lời thấy liên quan** | Là tiền đề của tỷ lệ trả lời |
| 5 | **So với lần trước có ý nghĩa** | Để Before và After thành một cặp |

Sắp xếp 6 mục hiện tại theo góc nhìn này:

| Mục | Có được hỏi | Đổi trong nửa năm | Biết bước tiếp | Liên quan người trả lời |
|---|---|---|---|---|
| **Place (không gian)** | ○ | ○ | ○ | ◎ |
| **Style (tỷ lệ đi làm, nơi làm việc)** | ◎ | ○ | ○ | ○ |
| Engagement | △ (○ nếu là mục tiêu đã nêu) | △ | △ | ○ |
| Well-being | △ | △ | △ | ◎ |
| Culture | △ | × | × | △ |
| Ý nghĩa công việc | △ | × | × | ○ |

Kế hoạch kinh doanh cũng ghi:

> Thực tế trong survey công ty chúng tôi thu được,
> **có những trường hợp mà trong 6 mục, không phải mục nào cũng
> có thể cải thiện chỉ bằng thời điểm chuyển văn phòng.**

Bộ câu hỏi hiện tại là **cấu trúc để nắm hiện trạng một cách toàn diện**,
không phải cấu trúc nhằm mục đích xác nhận sau khi chuyển.
Nếu phát hành lại nguyên vẹn, sẽ chứa nhiều câu hỏi ngoài những mục muốn xác nhận.

#### Nội dung cải tiến

Mục tiêu là tạo ra trạng thái sinh ra "muốn xác nhận" đối với After.

| Thứ tự | Nội dung cải tiến | Nội dung |
|---|---|---|
| **1** | **Xác nhận những nội dung đã nêu lần trước** | Tạo câu hỏi tự động từ các mục có điểm thấp ở Before, dưới dạng "những điểm đã nêu lần trước có được giải quyết chưa" |
| **2** | **Đặt mục tiêu ở thời điểm Before** | Thiết lập mục tiêu và điểm mục tiêu trong luồng Before. Ở After hiển thị song song "mục tiêu đã đặt" và "thực tế" |
| **3** | **Thêm câu hỏi về vận hành sau khi chuyển** | Không gian mới có được dùng đúng ý định không, quy tắc mới có hoạt động không, chỗ ngồi có bị cố định lại không, hiện đang gặp khó gì |
| **4** | **Phản hồi lại cho người trả lời** | Truyền đạt "nội dung đã nêu lần trước → nội dung đã xử lý" ở đầu phần trả lời |
| **5** | **Xây dựng cấu trúc câu hỏi theo mục tiêu** | Không thu hẹp một cách đồng loạt, mà chia thành: mục giữ chung, mục đã đặt làm mục tiêu, và câu hỏi theo từng dự án (chi tiết bên dưới) |
| **6** | **Hiển thị tình hình trả lời theo bộ phận** | Để bộ phận hành chính xác nhận bộ phận nào chưa trả lời và thúc đẩy trong nội bộ |
| **7** | **Mẫu văn thông báo** | Chuẩn bị mẫu văn thông báo có kèm mục tiêu đã đặt và nội dung đã xử lý lần trước |

**Không can thiệp vào cơ chế phát hành.**
Tất cả đều là cải tiến về **nội dung được phát hành**, hoặc **chuyển động trong nội bộ sau khi phát hành**.

#### Vì sao đặt "xác nhận nội dung đã nêu lần trước" lên đầu tiên

Câu hỏi này thỏa **đồng thời điều kiện 4 (người trả lời thấy liên quan)
và điều kiện 5 (so với lần trước có ý nghĩa)** trong 5 điều kiện.

- Người trả lời biết được rằng **ý kiến của mình đã được đọc**
- Nội dung trở thành **những việc cụ thể họ đang thực sự cảm nhận**
- Với bộ phận hành chính, đây là việc xác nhận điểm đã xử lý được và điểm còn tồn

Ngoài ra, câu hỏi này **không thành lập nếu không có Before.**
Nó làm cho Before và After thành một cặp, và trở thành chính lý do để thực hiện After.

#### Cấu trúc bộ câu hỏi After (phương án)

Chúng tôi đề xuất **chia thành ba lớp** thay vì thu hẹp số câu một cách đồng loạt.

| Lớp | Nội dung | Cách quyết định | Thay đổi |
|---|---|---|---|
| **1. Lõi chung** | Thông tin người trả lời, tỷ lệ nơi làm việc, mức hài lòng tổng thể, eNPS | Cố định | **Không thay đổi** |
| **2. Mục đã đặt làm mục tiêu** | Các câu hỏi cấu thành 2–3 mục đã chọn ở Before | Consultant, XP đề xuất và khách hàng đồng ý | Chốt ở Before, cố định cho cặp Before/After đó |
| **3. Câu hỏi theo từng dự án** | Xác nhận nội dung đã nêu lần trước (sinh tự động), câu hỏi về không gian và quy tắc mới, trả lời tự do | Theo từng dự án | Thiết lập theo dự án |

#### Tiền đề: cần tách hai thứ

| | Nội dung | Cách xử lý |
|---|---|---|
| **Bản thân câu hỏi** | Câu chữ, các lựa chọn, thang đo | **Không thay đổi** |
| **Phạm vi phát hành và phần thêm** | Phát hành câu nào / thêm câu nào | Quyết theo mục tiêu dự án |

**Thứ bảo vệ logic tính toán là phần thứ nhất.**
Điểm của từng câu hỏi được tính từ câu trả lời cho chính câu hỏi đó,
nên miễn không thay đổi bản thân câu hỏi thì phương pháp tính vẫn còn hiệu lực.

Nói cách khác, đề xuất này là cách nghĩ:
**không can thiệp chút nào vào bộ câu hỏi hiện có,
mà quyết định theo từng dự án là "phát hành cái nào" và "thêm cái gì".**

**Vì sao lõi chung được cố định:**
Trong khi phạm vi phát hành thay đổi theo dự án,
vẫn cần giữ lại phần để việc so sánh với công ty khác
và đồ thị diễn biến còn thành lập.
Vì vậy thông tin người trả lời, tỷ lệ nơi làm việc, mức hài lòng tổng thể và eNPS
được cố định thành lõi chung.

#### Về việc ở After cần so sánh tới mức nào

Kế hoạch kinh doanh có ghi:

> Chọn **3 mục** có liên quan nhất trong 52 câu của WDS,
> và thiết lập điểm mục tiêu so với hiện trạng

Chúng tôi hiểu rằng ở XD, mục tiêu được thiết lập ở **cấp từng câu hỏi**.
Trong trường hợp đó, nếu ở After phát hành nguyên các câu hỏi tương ứng
thì việc so sánh với Before thành lập ở cấp câu hỏi.

Mặt khác, để tính điểm của 6 mục và điểm Work Design
thì cần toàn bộ các câu hỏi thuộc mục đó.

Số câu hỏi cần phát hành thay đổi tùy theo ở After cần so sánh tới mức nào.

| Điều cần có ở After | Câu hỏi cần phát hành | Số câu |
|---|---|---|
| So sánh các câu hỏi đã đặt làm mục tiêu | Chỉ những câu đó | 2–3 câu |
| + Điểm của mục tương ứng | Toàn bộ câu thuộc mục đó | Khoảng 8–18 câu |
| + Điểm Work Design | Toàn bộ câu hỏi | 52 câu |

Chúng tôi muốn xác nhận **hiện tại ở After đang sử dụng tới mức nào**,
rồi quyết định cấu trúc theo phạm vi cần thiết (xem mục 2-9).

Ngoài ra, chúng tôi hiểu rằng bộ câu hỏi bản pulse đã là cấu trúc
dùng một phần trong toàn bộ câu hỏi,
nên cách nghĩ đo bằng một phần câu hỏi vốn đã được vận hành.

#### Số câu hỏi thay đổi theo lượng can thiệp

Với cấu trúc trên, số câu hỏi sẽ khác nhau theo từng dự án.

| Nội dung dự án | Lớp 2 gồm gì | Số câu dự kiến |
|---|---|---|
| **Chỉ Workplace Design** | Chủ yếu Place, Style | Khoảng 12–15 câu |
| **Workplace Design + XD** | Bao gồm cả Engagement, Culture | Khoảng 20–28 câu |

**Vì sao dự án có XD thì tăng số mục:**

Kế hoạch kinh doanh có ghi:

> **Trong 6 mục, không phải mục nào cũng có thể cải thiện chỉ bằng
> thời điểm chuyển văn phòng.**

Chúng tôi hiểu đây chính là lý do XD được cần đến.
Nếu XD là việc tác động vào những mục khó thay đổi chỉ bằng việc chuyển,
thông qua workshop và các sự kiện,
thì **ở dự án có XD, chính những mục đó mới là thứ cần đo.**

Ngược lại, nếu đo những mục đó ở dự án không có XD,
vì không có biện pháp tác động nên thay đổi khó nhìn thấy,
chỉ còn lại gánh nặng trả lời.

**Về mặt vận hành cũng nhất quán.**
Chúng tôi được biết ở dự án có XD, phía khách hàng sẽ lập nhóm vận hành.
Ở những dự án có người thúc đẩy trong nội bộ, dù số câu nhiều hơn
thì câu trả lời vẫn dễ được thu về.
Còn ở dự án không có cơ chế đó, cấu trúc ngắn sẽ dễ được trả lời hơn.

Nói cách khác, **mục đích không phải "làm cho ngắn",
mà là khớp số câu hỏi với lượng can thiệp và mức độ kết quả được cần đến.**

Lưu ý là không can thiệp vào bản thân bộ câu hỏi hiện có (xem mục 2-9).

#### Điều này cũng góp phần cho việc kiểm chứng hiệu quả của XD

Vì các mục ở lớp 2 được thiết lập theo nội dung triển khai của XD,
**ở những dự án có XD, ghi nhận về các mục được nhắm tới sẽ tự động được lưu lại.**

Nhờ đó có thể so sánh:

- So với mục tiêu đã đặt thì thực tế đã thay đổi thế nào
- Khác biệt giữa dự án có XD và dự án không có XD

Kế hoạch kinh doanh có ghi "việc có đưa XD vào hay không tạo ra khác biệt một trời một vực",
nhưng chúng tôi hiểu rằng ở thời điểm hiện tại,
tư liệu để thể hiện điều đó bằng số liệu còn hạn chế.
Cấu trúc này cũng là hình thức để tư liệu đó được tích lũy dần.

#### Về nội dung truyền đạt ở đầu phần trả lời

Bộ câu hỏi hiện tại đã dùng cơ chế hiển thị nội dung giải thích,
nên chúng tôi cho rằng **việc chèn nội dung vào đầu phần trả lời
có thể thực hiện được với cấu trúc hiện tại.**

Hiển thị ở đó "nội dung đã nêu lần trước" và "việc đã xử lý sau đó"
sẽ đồng thời tạo lý do trả lời và chia sẻ tiền đề cho các câu hỏi phía sau.

#### Về cách đo tỷ lệ thực hiện

Before được thực hiện ở giai đoạn đề xuất, After ở nửa năm sau khi chuyển,
nên giữa hai mốc có khoảng thời gian triển khai dự án.

Vì vậy nếu đặt cạnh nhau "số case Before và số case After trong cùng một năm tài chính"
thì sẽ là so sánh những dự án ở các thời điểm khác nhau.

Để nắm đúng tỷ lệ thực hiện, cần tổng hợp
**với mẫu số là "các dự án đã qua nửa năm kể từ khi chuyển"**.

Đây cũng là nội dung tương ứng với việc nắm bắt
`số case và tỷ lệ đề xuất After, số case và tỷ lệ thực hiện After` mà Vis đã nêu ra.

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
| **Giai đoạn 1** | Câu hỏi xác nhận nội dung đã nêu lần trước, hiển thị phản hồi ở đầu phần trả lời, thu hẹp số câu hỏi | Đưa về trạng thái câu trả lời được thu về |
| **Giai đoạn 2** | Đặt mục tiêu ở Before, câu hỏi về vận hành sau khi chuyển | Cho After có lý do để xác nhận |
| **Giai đoạn 3** | Tình hình trả lời theo bộ phận, mẫu văn thông báo, trực quan hóa tình hình thực hiện | Đưa về trạng thái thúc đẩy được trong nội bộ |
| **Giai đoạn 4** | Báo cáo so sánh Before/After (gồm dữ liệu vận hành), cách trình bày báo cáo | Đưa về dạng dùng được như bản kiểm chứng hiệu quả |
| **Giai đoạn 5** | Lớp hỏi lý do, màn hình phân tích và phần xuất, hoàn tất đăng ký và điều khoản, layout | Chuyển thành ngôn ngữ đề xuất và vừa khung thời gian |

**Vì sao giai đoạn 1 bắt đầu từ tỷ lệ trả lời:**

Vấn đề hiện tại được nhận thức là sau khi phát hành thì câu trả lời không được thu về.
Vì vậy trước tiên ưu tiên tạo **trạng thái có câu trả lời**.

Ba việc ở giai đoạn 1 đều liên quan tới **nội dung câu hỏi và cách trình bày**,
không can thiệp vào cơ chế phát hành hiện có.
Nhờ đó có thể bắt tay sớm, và hiệu quả cũng xác nhận được ngay dưới dạng tỷ lệ trả lời.

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

> **Muốn biết bộ phận nào chưa trả lời.**
> Vì chỉ với tỷ lệ trả lời tổng thể thì không biết nên tác động vào đâu.

> **Muốn không phải tự soạn văn thông báo cho nhân viên mỗi lần.**
> Vì nội dung thông báo ảnh hưởng tới tỷ lệ trả lời,
> nhưng không có thời gian viết lại từ đầu mỗi lần.

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

| # | Tính năng | Người dùng chính | Vấn đề | Hiện trạng |
|---|---|---|---|---|
| **F1** | Hoàn tất đăng ký và xác nhận điều khoản trực tuyến | Phụ trách コンペ / Khách hàng | 2 | Mới |
| **F2** | Tiếng nói worker (câu hỏi bổ sung theo điều kiện + trả lời tự do + chỉ vị trí trên layout) | Worker / XP | 1 | Mới |
| **F3** | Màn hình phân tích và phần xuất nội dung đã chọn | Consultant | 1, 2 | Mới |
| **F4** | Phương án layout dựa trên kế hoạch nhân sự | Consultant | 1, 2 | Mới |
| **F5** | **Câu hỏi xác nhận nội dung đã nêu lần trước** (sinh tự động từ kết quả Before) | Worker / XP | 3 | Mới |
| **F6** | **Hiển thị phản hồi ở đầu phần trả lời** (nội dung lần trước và việc đã xử lý) | Worker | 3 | Dùng cơ chế hiển thị nội dung đã có |
| **F7** | **Cấu trúc bộ câu hỏi After** (lõi chung + mục tiêu + câu hỏi theo dự án, 3 lớp) | Khách hàng / XP | 3 | **Cơ chế phát hành đã có**; thêm cấu trúc câu hỏi |
| **F8** | **Đặt mục tiêu ở Before** (mục và điểm mục tiêu, hiển thị suốt dự án) | Consultant / XP | 3 | Mới |
| **F9** | **Tình hình trả lời theo bộ phận** và mẫu văn thông báo | Hành chính / XP | 3 | Mới |
| **F10** | Trực quan hóa tình hình thực hiện (đối tượng, phát hành, câu trả lời, báo cáo) | Kinh doanh / CS / XP | 3 | Mới |
| **F11** | Báo cáo so sánh Before/After (gồm dữ liệu vận hành) | Khách hàng / XP | 3 | Mới |
| **F12** | Tùy biến survey theo từng khách hàng | Khách hàng / XP | 3 | Mới |

**Về những tính năng đã được trang bị:**
Cơ chế **tự động phát hành lại survey là cái đã có**, và đề xuất này không can thiệp vào đó.
Các tính năng liên quan tới vấn đề 3 đều là về **nội dung được phát hành**,
hoặc **chuyển động trong nội bộ sau khi phát hành**.

**Về việc thu phí:**
Chúng tôi được biết After hiện được cung cấp miễn phí.
Đề xuất này trước tiên lấy mục tiêu là **tạo trạng thái để câu trả lời được thu về
và việc thực hiện tích lũy được**.

## 2-7. Về từng tính năng — "vì sao tính năng này tốt"

### F5: Câu hỏi xác nhận nội dung đã nêu lần trước

**Đây là câu hỏi mà lý do trả lời trở nên rõ ràng nhất với người trả lời.**

Đặt dưới dạng "lần trước điểm được nêu là chỗ này. Hiện tại đã được giải quyết chưa?"
Lấy các mục có điểm thấp từ kết quả Before và sinh câu hỏi tự động.

Ba hiệu quả:

- Người trả lời nhận ra rằng **ý kiến của mình đã được đọc**
- Nội dung trở thành **những việc cụ thể họ đang thực sự cảm nhận**
- Với bộ phận hành chính, đây là việc xác nhận điểm đã xử lý và điểm còn tồn

Ngoài ra câu hỏi này **không thành lập nếu không có Before.**
Nó làm Before và After thành một cặp, và trở thành chính lý do thực hiện After.

### F6: Hiển thị phản hồi ở đầu phần trả lời

**Giải quyết trạng thái "trả lời cũng không thay đổi gì".**

Nếu không truyền đạt được rằng với nội dung đã trả lời ở Before thì điều gì đã thay đổi,
ý muốn trả lời lần sau sẽ giảm.

Hiển thị ở đầu phần trả lời "nội dung đã nêu lần trước" và "việc đã xử lý sau đó"
sẽ đồng thời tạo lý do trả lời và chia sẻ tiền đề cho các câu hỏi phía sau.

Vì bộ câu hỏi hiện tại đã dùng cơ chế hiển thị nội dung giải thích,
chúng tôi cho rằng **thực hiện được với cấu trúc hiện tại** — nên dễ bắt tay.

### F7: Cấu trúc bộ câu hỏi After

**Đo được nội dung muốn xác nhận sau khi chuyển, trong thời gian trả lời ngắn.**

Điều khách hàng muốn biết ở nửa năm sau khi chuyển là những nội dung cụ thể về vận hành:

- Không gian mới có được dùng đúng ý định không
- Quy tắc mới có hoạt động không
- Chỗ ngồi có bị cố định lại không
- Hiện đang gặp khó gì

Đây vừa là **nội dung đang được quan tâm**, vừa là **nội dung có thể thay đổi trong nửa năm**.

Mặt khác, để so sánh thì cần đo cùng những mục giống nhau.
Vì vậy cấu trúc là **giữ lại các mục đã đặt làm mục tiêu, đồng thời thêm câu hỏi về vận hành**.

**Tuy nhiên chúng tôi không thu hẹp một cách đồng loạt.**

Vì điểm của 6 mục được tính từ toàn bộ bộ câu hỏi,
nếu giảm câu hỏi thì không thể tính điểm theo cùng phương pháp như Before,
và tiền đề của việc so sánh bị phá vỡ.
Việc so sánh với các công ty khác và đồ thị diễn biến cũng không còn thành lập.

Vì vậy cấu trúc gồm **lõi chung (cố định) + mục đã đặt làm mục tiêu +
câu hỏi theo từng dự án** — chỉ lớp 2 và lớp 3 là thay đổi.

Kết quả là số câu hỏi khác nhau theo từng dự án.

| Nội dung dự án | Số câu dự kiến |
|---|---|
| Chỉ Workplace Design | Khoảng 12–15 câu |
| Workplace Design + XD | Khoảng 20–28 câu |

**Vì sao dự án có XD thì tăng số mục:**
Nếu XD là việc tác động vào những mục khó thay đổi chỉ bằng việc chuyển văn phòng,
thì ở dự án có XD, chính những mục đó mới là thứ cần đo.
Ngược lại ở dự án không có XD, vì không có biện pháp tác động nên
thay đổi khó nhìn thấy, chỉ còn lại gánh nặng trả lời.

Ngoài ra chúng tôi được biết ở dự án có XD, phía khách hàng sẽ lập nhóm vận hành —
có người thúc đẩy trong nội bộ thì dù số câu nhiều hơn, câu trả lời vẫn dễ được thu về.

Lưu ý là không can thiệp vào bản thân bộ câu hỏi hiện có (xem mục 2-9).

### F8: Đặt mục tiêu ở Before

**Tạo cho After "điều cần phải xác nhận".**

Nếu trước khi chuyển đã đặt mục tiêu, After trở thành "nơi xác nhận mục tiêu đã đặt".
Không có thì After chỉ là "đo lại một lần nữa", và dễ bị để lại sau.

Việc đặt mục tiêu là nội dung đã có trong quy trình XD (thiết kế KPI),
nhưng vì kèm workshop nên số dự án thực hiện được là có hạn.

Tính năng này nhằm đưa về hình thức **đặt mục tiêu được ngay trong luồng Before,
không lấy workshop làm tiền đề** — để cả dự án không có XD cũng lưu lại được mục tiêu.

**Về việc thu hẹp mục mục tiêu:**
Survey cũng đo cả những yếu tố ngoài văn phòng như văn hóa, lộ trình nghề nghiệp,
quan hệ con người, sức khỏe.
Nếu theo dõi tất cả thì khó thuyết minh dưới dạng hiệu quả của đầu tư văn phòng.
Ngoài ra như kế hoạch cũng ghi, không phải cả 6 mục đều thay đổi chỉ bằng việc chuyển.

Vì vậy mục tiêu được thu hẹp còn vài mục,
và **gợi ý những mục dễ thay đổi làm phương án lựa chọn**.

### F9: Tình hình trả lời theo bộ phận và mẫu văn thông báo

**Tạo trạng thái để người thúc đẩy nội bộ có thể hành động.**

Để câu trả lời được thu về, cần bộ phận hành chính và nhóm vận hành
thông báo trong nội bộ.
Chỉ với tỷ lệ trả lời tổng thể thì không biết nên tác động vào đâu.

Nếu thấy được tình hình theo từng bộ phận thì biết cụ thể cần thúc ai.

Ngoài ra vì survey được phát từ phía khách hàng ra nội bộ,
việc chuẩn bị **mẫu văn thông báo có kèm mục tiêu đã đặt và nội dung đã xử lý lần trước**
sẽ giảm công soạn thảo mà vẫn giữ được nội dung thống nhất.

### F11: Báo cáo kiểm chứng hiệu quả Before/After

**Tạo trạng thái có thể thuyết minh về khoản đầu tư.**

Khi giành được hợp đồng có phí, chúng tôi được biết điều khách hàng cảm nhận
được giá trị chính là bản thân ý tưởng **"số hóa hiệu quả của dự án văn phòng"**.

Về tính năng, báo cáo tổng hợp diễn biến điểm của các mục đã đặt làm mục tiêu,
mức chênh lệch Before/After, và mối tương ứng với các biện pháp đã thực hiện.

**Điểm quan trọng là đưa cả dữ liệu vận hành vào.**
Tỷ lệ đi làm và tỷ lệ sử dụng không gian không phụ thuộc vào câu trả lời,
nên ngay cả khi câu trả lời không thu về đủ vẫn chỉ ra được thay đổi.
Ngoài ra nó trả lời đúng điểm mà sau khi chuyển người ta quan tâm nhất —
"thực tế có được sử dụng không".

**Về cách trình bày báo cáo:**
Nếu cấu trúc theo dạng phán định đạt hay không đạt thì việc xác nhận kết quả
dễ trở thành gánh nặng.
Chúng tôi đề xuất cấu trúc lấy **"điều gì đã thay đổi"** và **"tiếp theo nên làm gì"**
làm trung tâm.

### F2: Tiếng nói worker

**Giải quyết tình trạng "biết điểm thấp nhưng không biết sửa ở đâu và sửa thế nào".**

Hiện nay việc nghe ý kiến được thực hiện qua buổi 座談会 với một phần nhân viên,
nhưng không thể khẳng định là đại diện cho toàn thể, và nội dung cũng chỉ lưu ở
ghi chép cá nhân.

Nếu thu được từ toàn bộ người trả lời thông tin **"khu vực nào, điểm gì, ảnh hưởng thế nào
tới công việc"** thông qua câu hỏi phân nhánh theo điều kiện, thì các biện pháp cải thiện
sẽ trở nên cụ thể.

Lưu ý: thiết kế theo hướng **không bắt tất cả mọi người trả lời bộ câu hỏi dài.**
Chỉ hiển thị câu hỏi bổ sung cho những người có điểm không hài lòng.

**Đây cũng là phần liên quan tới độ chính xác của AI report.**
Hiện tại thứ có thể đưa cho AI chỉ là điểm số. Khi có thêm thông tin về lý do,
vị trí và mức ảnh hưởng, độ cụ thể của đầu ra sẽ khác.

### F12: Tùy biến survey theo từng khách hàng

**Khi đứng trên tiền đề đo lặp lại, việc tùy biến trở thành điều kiện tiên quyết.**

Nếu không phải là những mục có ý nghĩa với công ty đó, động lực đo lặp lại
sẽ không duy trì được.
Tùy theo ngành, cơ cấu loại công việc và cách làm việc, những mục muốn đo là khác nhau.

Đây cũng là tính năng được người phụ trách コンペ và các consultant nêu ra như một yêu cầu.

**Tuy nhiên chúng tôi muốn tránh hình thức cho phép thay đổi tự do.**

| Vấn đề dự kiến | Nội dung |
|---|---|
| Không còn so sánh được với công ty khác | Nếu mỗi khách hàng có mục khác nhau, việc so sánh với dữ liệu đã tích lũy không thành lập |
| Những mục quan trọng bị loại ra | Có khả năng chọn những mục dễ trả lời, còn mục thực sự cần xác nhận thì không còn |
| Không theo được diễn biến | Nếu mỗi lần thực hiện lại đổi mục, việc so sánh theo thời gian không thực hiện được |

Vì vậy chúng tôi đề xuất hình thức sau:

- **Lõi chung không thay đổi được** (nền của việc so sánh)
- Phần thay đổi được là **chọn từ những mục đã chuẩn bị sẵn**, không phải nhập tự do
- Tiêu chí chọn là "mục tiêu của dự án đó", do consultant và XP đề xuất
- Mục đã chốt thì **không thay đổi trong cặp Before/After đó**
- Việc thay đổi được thực hiện ở thời điểm bắt đầu chu kỳ tiếp theo

Nói cách khác, tùy biến được thiết kế như **cơ chế để khớp với mục tiêu của dự án**,
không phải hình thức chỉ do mong muốn của khách hàng quyết định (xem mục 2-9).

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
| Chức năng tùy biến survey theo từng khách hàng | Câu trả lời cho bảng câu hỏi | **F12** |
| Chọn mục survey làm KPI và đặt điểm mục tiêu | XD bước ⑥ Thiết kế KPI | **F8** |
| Thu thập ý kiến thực tế qua buổi 座談会 | XD bước ⑦ 座談会 | **F2** |
| Đánh giá theo mốc sau khi chuyển văn phòng | XD bước ⑨ Đánh giá và cải thiện | **F7, F11** |
| Triển khai survey từ giai đoạn nurturing | Kế hoạch kinh doanh | **F1** (làm nhẹ thủ tục đăng ký) |
| Mở rộng số lượng sử dụng Before & After | Kế hoạch kinh doanh | **F5, F6, F7, F9** |

**Tính năng nằm ngoài phạm vi:**

| Tính năng | Lý do |
|---|---|
| AI report / AI advice | Được biết đang triển khai bằng công cụ AI nội bộ của Vis |

## 2-9. Tiền đề và các điểm cần xác nhận khi triển khai

| Điều muốn xác nhận | Vì sao cần |
|---|---|
| **Tỷ lệ trả lời hiện tại** (so với Before ở mức nào, có khác biệt theo bộ phận không) | Là chuẩn để đo hiệu quả cải tiến |
| **Luồng thông báo trong nội bộ** — ai, thông báo cho nhân viên bằng cách nào | Là tiền đề để thiết kế cơ chế thúc đẩy |
| **Những vấn đề vận hành hay được hỏi sau khi chuyển** | Là căn cứ để quyết định nên thêm gì vào câu hỏi After |
| **Có được phép can thiệp vào câu hỏi hiện có, hay chỉ thêm mới** | Để giữ khả năng so sánh với điểm số cũ, chúng tôi khuyến nghị chỉ thêm mới |
| **Ở After đang sử dụng so sánh tới mức nào** — chỉ so sánh câu mục tiêu, tới điểm của mục, hay tới điểm Work Design | **Số câu hỏi cần phát hành thay đổi rất nhiều.** Là điểm muốn xác nhận nhất |
| **Phương pháp tính điểm của 6 mục** — câu hỏi nào tương ứng với mục nào | Cần để xác định phạm vi phát hành và lõi chung |
| **Ở dự án có XD, những mục nào đặc biệt muốn xác nhận** | Là căn cứ để quyết định đưa gì vào lớp 2 |
| **Việc so sánh với công ty khác đang được dùng ở phạm vi nào** | Là căn cứ xác nhận mức cần thiết của việc cố định lõi chung |
| **Cấu trúc có hỗ trợ thiết lập điều kiện hiển thị câu hỏi không** | Cách hiện thực việc hiển thị câu hỏi theo kết quả lần trước sẽ thay đổi |
| **Có tham chiếu được kết quả Before để sinh câu hỏi không** | Liên quan tới cách hiện thực F5 |
| **Dữ liệu phân tích vận hành có đưa vào báo cáo được không** | Cần để bảo đảm có chỉ số không phụ thuộc câu trả lời |
| Dữ liệu trả lời đã có có tham chiếu được theo dạng so sánh Before/After không | Là tiền đề để báo cáo so sánh thành lập |
| Luồng đăng ký và xác nhận điều khoản hiện tại (đang mất mấy ngày ở bước nào) | Cần cho việc phán đoán chuyển được bao nhiêu lên màn hình |
| **Phạm vi dự kiến của AI report** | Phạm vi thiết kế của màn hình phân tích và phần xuất |
| Cho phép tùy biến câu hỏi theo khách hàng tới mức nào | Cần xác định phạm vi được phép thay đổi, để giữ khả năng so sánh |

**Về cách xử lý bộ câu hỏi:**

Trong đề xuất này, chúng tôi muốn theo phương châm sau:

> **Không thay đổi chút nào các câu hỏi hiện có (câu chữ, lựa chọn, thang đo).**
> **Điều quyết định theo từng dự án là: phát hành câu nào, và thêm câu gì.**

Nếu thay đổi bản thân câu hỏi thì sẽ không so sánh được với điểm số đã tích lũy.
Việc sửa nhẹ câu chữ hay đổi thang đo cũng là nguyên nhân
phá vỡ khả năng so sánh mà không ai nhận ra.
Vì vậy chúng tôi đề xuất xử lý bằng **phạm vi phát hành và phần thêm**,
không phải bằng việc thay đổi.

**Về những tính năng đã được trang bị:**
Trong đề xuất này, những cơ chế **đã hoạt động — như tự động phát hành lại —
sẽ không làm lại mà được tận dụng**.
Nếu còn những tính năng tương tự khác, mong được thông báo trước
để chúng tôi điều chỉnh nội dung, tránh trùng lặp.

## 2-10. Thứ tự phát huy hiệu quả của đề xuất

| Thứ tự | Nội dung | Hiệu quả |
|---|---|---|
| **1** | Đưa về trạng thái được trả lời (F5, F6, F7) | Câu trả lời After bắt đầu được thu về |
| **2** | Cho After có lý do để xác nhận (F8) | Trở thành việc xác nhận đối với mục tiêu |
| **3** | Đưa về trạng thái thúc đẩy được trong nội bộ (F9, F10) | Bộ phận hành chính có thể tác động |
| **4** | Đưa về dạng dùng được như bản kiểm chứng hiệu quả (F11) | Thuyết minh được với ban lãnh đạo |
| **5** | Chuyển thành ngôn ngữ đề xuất (F2, F3, F1, F4, F12) | Kết quả survey kết nối được với đề xuất |

**Vì sao đặt bước 1 trước:**

Gốc của vấn đề là chưa cho thấy được hiệu quả trước và sau cải tạo.
Nhưng trước đó, **nếu câu trả lời không được thu về thì không có tư liệu để cho thấy.**

Ba việc ở bước 1 đều liên quan tới **nội dung câu hỏi và cách trình bày**,
không can thiệp vào cơ chế phát hành.
Nhờ đó có thể bắt tay sớm, và hiệu quả xác nhận được dưới dạng tỷ lệ trả lời.

**Vì sao bước 2 đứng sau bước 1:**
Việc đặt mục tiêu là yếu tố quan trọng làm thay đổi vị trí của After,
nhưng hiệu quả chỉ xuất hiện từ những dự án thực hiện Before tiếp theo.
Trong khi đó bước 1 **có hiệu quả cả với những dự án đã thực hiện Before rồi**.

**Vì sao bước 4 đứng sau:**
Báo cáo kiểm chứng hiệu quả chỉ có ý nghĩa khi câu trả lời được thu về.

**Về quan hệ với việc thu phí:**
Chúng tôi được biết After hiện được cung cấp miễn phí.
Đề xuất này trước tiên lấy mục tiêu là **tạo trạng thái để việc thực hiện tích lũy được**
qua các bước 1–4.

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

## Vấn đề 3 — bốn giả thuyết đã bị loại, và hướng hiện tại

### Những gì đã được xác nhận là SAI

| Giả thuyết đã loại | Sự thật |
|---|---|
| ~~Thiếu chức năng nhắc mốc đánh giá~~ | Cơ chế tự động gửi lại sau 6 tháng **đã có** |
| ~~Cần người thiết lập thủ công~~ | **Tự động chạy**, không cần thiết lập |
| ~~Hợp đồng có phí chặn việc thực hiện~~ | **After hiện miễn phí** |
| ~~Chưa rõ là A hay B~~ | Theo mô tả và số liệu thì **nghiêng về A — ít người trả lời** |

Bốn lần điều chỉnh đều cùng một dạng: **suy diễn khi chưa xác thực**.

### Hướng đã chốt: làm cho survey có giá trị đủ để người ta muốn xác nhận

Cơ chế gửi đã tự động và miễn phí. Vấn đề là **gửi rồi nhưng ít người trả lời**.

Nên câu hỏi trung tâm là: **survey cần chứa những giá trị gì để end user muốn xác nhận lại?**

### Hai người cần được thuyết phục, không phải một

| Người | Cần gì | Nếu thiếu |
|---|---|---|
| **Hành chính / nhóm vận hành** | Chỉ số mà **có ai đó sẽ hỏi họ** | Không phát động nội bộ → nhân viên không biết |
| **Nhân viên** | Tin rằng **câu trả lời sẽ dẫn tới thay đổi** | Thấy thông báo cũng bỏ qua |

Thường tắc ở người thứ nhất trước. Nên nội dung survey phải có sức kéo với **cả hai**.

### Năm tiêu chí để một chỉ số có sức kéo

1. **Có ai sẽ hỏi về nó** — nếu ban lãnh đạo không hỏi, hành chính không có lý do đo
2. **Có thể thay đổi trong 6 tháng** — nếu không, đo lại vô nghĩa
3. **Biết số rồi thì biết làm gì tiếp** — nếu không, chỉ là con số
4. **Người trả lời thấy liên quan tới mình** — điều kiện của tỷ lệ trả lời
5. **So với lần trước có ý nghĩa** — điều kiện để Before/After thành một cặp

### Sàng 6 trục hiện tại

| Trục | Sức kéo | Ghi chú |
|---|---|---|
| **Place** | **Mạnh** | Do office gây ra, đổi được, actionable, nhân viên cảm nhận trực tiếp |
| **Style** (tỷ lệ đi làm, nơi làm việc) | **Mạnh nhất** | Là câu ban lãnh đạo hỏi đầu tiên sau khi đầu tư |
| Engagement | Trung bình | Mạnh nếu đó là mục tiêu đã nêu của dự án |
| Well-being | Yếu | Chậm, nhiều yếu tố ngoài office |
| Culture | **Yếu nhất** | Gần như không đổi trong 6 tháng |
| Ý nghĩa công việc | Yếu | Tương tự |

→ **Bộ 52 câu vốn không được thiết kế để làm bản After.**
Nó là bản đo hiện trạng toàn diện. Dùng lại nguyên vẹn thì phần lớn câu hỏi không có sức kéo.

Điều này khớp câu trong kế hoạch kinh doanh:
「6項目の内、すべてが移転というタイミングだけでは向上させるのが難しい」.

### Tính năng mạnh nhất: F5 — xác nhận những điều đã nêu lần trước

Đây là ý quan trọng nhất trong toàn bộ vấn đề 3.

Cấu trúc: *"Lần trước những điểm được nêu nhiều nhất là A, B, C.
Hiện tại A đã được giải quyết chưa?"* — sinh tự động từ các mục điểm thấp của Before.

Vì sao mạnh: nó thỏa **cả tiêu chí 4 và 5 cùng lúc**.

- Nhân viên thấy **ý kiến của mình đã được đọc**
- Câu hỏi về thứ **họ đang thực sự cảm thấy**, không phải khái niệm
- Với hành chính là bằng chứng "đã xử lý" hoặc "còn tồn"

Và quan trọng: tính năng này **không thể có nếu không có Before**
→ biến Before/After thành một cặp thật, không phải hai lần đo rời rạc.
Đó chính là lý do tồn tại của After.

### Tính năng rẻ nhất mà tác động trực tiếp: F6

Bộ câu hỏi hiện tại **đã dùng `type: "html"`** (thấy ở Q16 và Q30 để hiện hướng dẫn nhập).
Nghĩa là chèn một trang nội dung vào đầu survey **khả thi ngay với cấu trúc hiện tại**.

Nội dung: "lần trước mọi người đã nêu gì → công ty đã làm gì".

Làm ba việc cùng lúc với chi phí gần bằng không: đóng vòng phản hồi,
tạo lý do trả lời, đặt bối cảnh cho các câu hỏi phía sau.

### Giảm số câu — thay đổi lớn nhất về tỷ lệ trả lời

Bộ After không dùng lại nguyên 52 câu. Cấu trúc theo lớp（xem 2-2）:

| Khối | Số câu |
|---|---|
| Mục tiêu đã đặt | 2–3 |
| Xác nhận vấn đề lần trước | 2–3 |
| Nơi làm việc thực tế | 1 |
| Cách dùng không gian mới | 2–3 |
| Quy tắc còn sống không | 1–2 |
| Vấn đề đang gặp | 1 |

Với dự án chỉ WD thì khoảng 12–15 câu — từ 10–15 phút xuống 3–4 phút.
Với dự án có XD thì 20–28 câu, nhưng có nhóm vận hành để thúc đẩy nên chịu được.

Bộ pulse 19 câu đã có sẵn làm điểm khởi đầu — nhưng cần thay phần văn hóa
và career bằng phần vận hành.

### Hai tính năng nhắm vào người thúc đẩy (F9)

**Tỷ lệ trả lời theo bộ phận.** Thấy 30% mà không biết bộ phận nào chưa trả lời
thì không biết thúc ai.

**Mẫu văn thông báo.** Survey phát từ phía khách, nên cách họ giới thiệu quyết định
tỷ lệ trả lời. Mẫu có sẵn phần "mục tiêu đã đặt" và "lần trước đã xử lý gì"
giúp họ không phải tự viết mà vẫn giữ thông điệp đúng.

### Điểm quan trọng: không cắt câu hỏi theo quy tắc cứng

Bản trước viết "giảm xuống 10–13 câu" cho mọi trường hợp. **Sai** — có hai rủi ro:

**1. Ảnh hưởng tới XD.**
Đã xếp Culture và Well-being là sức kéo yếu vì không đổi trong 6 tháng.
Nhưng bỏ qua điều kiện: **sức kéo phụ thuộc vào có can thiệp nào nhắm vào nó hay không.**

Kế hoạch kinh doanh viết 「6項目の内、すべてが移転というタイミングだけでは向上させるのが難しい」
— câu này **chính là lý do XD tồn tại**, không phải lý do bỏ đo.

| Loại dự án | Có can thiệp vào culture/engagement | Sức kéo |
|---|---|---|
| Chỉ WD | Không — chỉ có bản thân văn phòng | Yếu |
| WD + XD | Có — workshop, event, change management | **Mạnh, và bắt buộc đo** |

→ Với dự án XD, cắt culture/engagement là **cắt đúng bằng chứng XD cần**
để chứng minh giá trị.

**2. Phá điểm số và benchmark.**
Điểm 6 trục và điểm Work Design tính từ toàn bộ bộ câu hỏi. Cắt câu thì:
- Không tính được điểm theo cùng cách như Before → **so sánh mất căn cứ**
- Không so được với dữ liệu tích lũy của Vis (8.500 case thực tế) — tài sản của họ
- Đường xu hướng theo thời gian bị đứt

### Cách phát biểu nguyên tắc cho chính xác

Đừng nói "giữ bộ chuẩn + thêm" — câu đó gộp hai quyết định khác nhau. Nói:

> **Không sửa câu hỏi nào đang có. Quyết định theo mục tiêu dự án là:
> gửi những câu nào, và thêm những câu gì.**

| | Nội dung | Trạng thái |
|---|---|---|
| **Bất biến** | Câu hỏi, lựa chọn, thang đo | **Không bao giờ đổi** |
| **Khả biến** | (a) Gửi câu nào · (b) Thêm câu gì | Theo mục tiêu dự án |

**Cái bảo vệ logic tính toán là phần bất biến** — điểm của một mục tính từ câu trả lời
của chính câu hỏi đó, nên miễn câu hỏi không đổi thì cách tính vẫn đúng.

Cách nói này chặt hơn "giữ bộ chuẩn" vì nó **cấm cả việc sửa nhẹ chữ hay đổi thang đo**
— thứ dễ bị bỏ qua nhưng làm hỏng so sánh mà không ai nhận ra.

### Giải pháp: cấu trúc 3 lớp, cắt theo mục tiêu

| Lớp | Nội dung | Đổi được? |
|---|---|---|
| **1. Lõi chung** | Thông tin người trả lời, tỷ lệ nơi làm việc, hài lòng tổng thể, eNPS | **Không** — giữ benchmark và đường xu hướng |
| **2. Mục tiêu dự án** | Các câu KPI chọn ở Before | Chốt ở Before, khóa cho cặp Before/After |
| **3. Theo dự án** | Xác nhận vấn đề lần trước (tự sinh), câu hỏi vận hành, tự do | Có |

### Phát hiện quan trọng: KPI của XD ở cấp câu hỏi, không phải cấp trục

Kế hoạch kinh doanh viết: 「52問あるWDSの中から最も関連性の高い**項目を3つ選択**し」
— chọn **3 câu hỏi** trong 52, không phải 3 trục. Bản MVP thì 2 câu.

Nghĩa là **cách so sánh của chính XD đã làm việc ở cấp câu hỏi**.
Nếu After giữ nguyên 3 câu đó, so sánh hợp lệ — **không cần tính lại điểm trục**.

Điều này làm việc gửi tập con dễ chấp nhận hơn nhiều.

### Ba mức so sánh — cần Vis quyết

| Muốn có gì ở After | Phải gửi gì | Số câu |
|---|---|---|
| So sánh câu KPI ở cấp câu hỏi | Đúng 2–3 câu đó | 2–3 |
| + điểm của trục chứa câu KPI | Toàn bộ câu thuộc trục đó | ~8–18 |
| + điểm tổng Work Design | Toàn bộ 52 câu | 52 |

Ba mức khác nhau **rất nhiều** về gánh nặng trả lời.
Chưa biết Vis đang dùng tới mức nào ở After — đã đưa lên **đầu danh sách xác nhận** ở 2-9.

### Tiền lệ hỗ trợ: pulse 19 câu đã là tập con

Bộ pulse Vis tự tạo tháng 1/2025 **chính là một tập con của 52 câu**.
Nghĩa là họ **đã chấp nhận nguyên tắc đo bằng tập con** —
nên đề xuất gửi tập con ở After không phải ý lạ.
Đây là lập luận tốt để dùng khi trình bày.

Độ dài tự điều chỉnh: **chỉ WD khoảng 12–15 câu · WD+XD khoảng 20–28 câu**.

Lý do vận hành hỗ trợ điều này: **dự án XD có nhóm vận hành phía khách**
(bước ② quy trình XD). Có người sở hữu thì chịu được bộ dài hơn.
Dự án chỉ WD không có ai sở hữu — bộ ngắn mới có cơ hội được trả lời.

→ Cách phát biểu: **không phải "cắt cho ngắn", mà "độ dài tương ứng với việc
có ai thực sự cần kết quả"**.

### Về custom theo client (F12) — là cơ chế đúng nhưng cần ràng buộc

Custom giải quyết được vấn đề XD, nhưng tự do thì sinh ba rủi ro:

| Rủi ro | Hậu quả |
|---|---|
| Mỗi khách chọn khác nhau | Mất benchmark liên công ty |
| Chọn theo cái dễ trả lời | Bỏ mất mục quan trọng |
| Mỗi kỳ đổi mục | Mất so sánh theo thời gian |

Ràng buộc đã đưa vào đề xuất: lõi chung không đổi · chọn từ thư viện,
không tự do nhập · tiêu chí chọn là **mục tiêu dự án**, không phải sở thích khách ·
khóa cho cặp Before/After · đổi chỉ ở đầu chu kỳ mới.

**Điểm cần nhấn khi trình bày:** tiêu chí quyết định là **mục tiêu dự án**,
không phải khách muốn gì. Cùng một khách, dự án chỉ WD và dự án có XD
cần bộ khác nhau.

### Lợi ích phụ cho XD — đáng nêu khi trình bày

Nếu lớp 2 bắt buộc chứa các trục XD nhắm tới, thì hệ thống tự tạo ra bằng chứng
cho XD ở **mọi dự án có XD**, không chỉ 5–6 dự án có workshop.

Và cho phép so sánh **dự án có XD vs không có XD**.

Kế hoạch kinh doanh viết 「XDを取り入れるか否かで天と地の差が出る」— nhưng hiện chưa có
số để nói. Cấu trúc này làm số đó tích lũy dần.
Đây là lập luận bán hàng mạnh cho XD mà họ đang thiếu.

### Vì sao F8 (mục tiêu) xếp sau F5–F7

F8 quan trọng về mặt định vị — có mục tiêu thì After thành "kiểm tra lời hứa".
Nhưng **hiệu quả chỉ đến từ dự án Before tiếp theo**.

Còn F5–F7 **có hiệu quả ngay với các dự án đã làm Before rồi**. Nên xếp trước.

### Còn về con số 83 và 5

Before ở giai đoạn đề xuất; After ở 6 tháng sau chuyển, nên cộng lại dễ tới 1,5–2 năm.
Cách đo đúng phải lấy mẫu số là **dự án đã chuyển trên 6 tháng**.

**Lưu ý khi trình bày:** không nói "con số của Vis sai".
Nói *"để đo đúng thì cần mẫu số là dự án đã qua 6 tháng"*.

### Về việc phân loại có phí

**After hiện miễn phí.** Nên bản hiện tại **bỏ hẳn cột có phí** trong bảng tính năng —
thay bằng cột **hiện trạng** (đã có / mới).

Lý do: phân loại có phí khi khách chưa quyết định thu phí là
**áp mô hình kinh doanh lên họ**.

Vẫn giữ tinh thần ghi chú nội bộ của Vis, nhưng thể hiện qua **thứ tự phát triển**,
không qua nhãn giá.

## Logic của từng tính năng — trả lời "vì sao cái này tốt"

| Tính năng | Lý do |
|---|---|
| **F5** | **Mạnh nhất** — thỏa cả tiêu chí "liên quan tới người trả lời" và "so sánh có ý nghĩa". Không thể có nếu không có Before |
| **F6** | **Rẻ nhất** — cấu trúc hiện tại đã hỗ trợ. Đóng vòng phản hồi |
| **F7** | Đo thứ đang được quan tâm và **có thể đổi trong 6 tháng**. Giảm số câu |
| **F8** | Cho After vị trí "kiểm tra lời hứa" — nhưng hiệu quả từ dự án Before tiếp theo |
| **F9** | Nhắm vào **người thúc đẩy nội bộ**, không phải người trả lời |
| **F10** | Đo được hiệu quả của F5–F9 |
| **F11** | Nói được với ban lãnh đạo. Dữ liệu vận hành không phụ thuộc tỷ lệ trả lời |
| **F2** | Biết **sửa ở đâu**, thay vì chỉ biết điểm thấp |
| **F12** | Tiền đề để đo lặp lại có ý nghĩa |
| **F4** | Hiện thực hóa "tốc độ phản ánh vào thiết kế không gian" |

## Mười điểm cần cẩn thận khi trình bày

1. **Đừng nói After là hàng có phí** — hiện miễn phí.
2. **Đừng nói thiếu chức năng nhắc hay gửi tự động** — đã có.
   Chỉ nói phần nội dung và phần sau khi gửi.
3. **Đừng nói "cần người thiết lập"** — tự động chạy.
4. **Đừng gọi F7 là "pulse survey mới"** — Vis đã tự tạo bộ rút gọn.
   Nói là "điều chỉnh nội dung và giảm số câu cho bản After".
5. **Đừng gọi F2 là "thêm mới tiếng nói worker"** — 座談会 đã có.
   Nói là "số hóa và mở rộng".
6. **Đừng gọi F8 là "thêm KPI"** — thiết kế KPI đã có trong XD bước ⑥.
   Nói là "đưa lên hệ thống mà không cần workshop".
7. **Đừng đề xuất self-service hay SaaS ngay** — theo kế hoạch là FY2027–2028.
8. **F1 cần được thấy là nặng, không phải phụ** — nói bằng lập luận,
   không trưng bảng 6 tuần.
9. **Đừng để chữ "scratch" nghe thành "bỏ WDP làm lại"** —
   luôn kèm câu "những tài sản hiện có được giữ nguyên".
10. **Nhấn nguyên tắc "không sửa câu hỏi hiện có, chỉ thêm mới"** —
    bảo vệ dữ liệu đã tích lũy.

**Quy tắc chung sau bốn lần điều chỉnh:** trước khi viết tính năng nào vào đề xuất,
hỏi *"cái này đã có chưa, ai đang chịu chi phí, và ai là người sẽ dùng nó?"*

## Vì sao thêm mục 2-10 "thứ tự phát huy hiệu quả"

Mục này thay cho bảng đối chiếu KPI bằng số. Nó cho thấy bravesoft hiểu
**thứ tự nhân quả**:

- Có câu trả lời trước → mọi thứ sau mới có nghĩa
- Rồi mới cho After một vị trí (mục tiêu)
- Rồi mới giúp hành chính thúc đẩy được
- Rồi mới làm báo cáo — vì báo cáo cần dữ liệu

Điểm quan trọng khi trình bày: **F5–F7 có hiệu quả ngay với dự án đã làm Before**,
còn F8 phải chờ dự án Before tiếp theo. Đây là lý do thứ tự như vậy.

## Những điểm cần xác nhận trước khi chốt

| # | Nội dung | Ảnh hưởng | Ai xác nhận |
|---|---|---|---|
| 1 | **Tỷ lệ trả lời hiện tại** — Before vs After, có khác theo bộ phận không | Chuẩn để đo hiệu quả cải tiến | Dev |
| 2 | **Luồng thông báo nội bộ** — ai gửi, gửi thế nào cho nhân viên | Điều kiện thiết kế F9 | Vis |
| 3 | **Sau khi chuyển, khách hay hỏi hoặc phàn nàn về điều gì** | Nội dung cần thêm vào After (F7) | Vis |
| 4 | Có được phép **thêm câu hỏi vào bộ hiện tại** không | Điều kiện cho F5, F7 | Vis + Dev |
| 5 | Cấu trúc có hỗ trợ **điều kiện hiển thị câu hỏi** không | Cách hiện thực F5 | Dev |
| 6 | Có **tham chiếu được kết quả Before để sinh câu hỏi** không | Điều kiện cho F5 | Dev |
| 7 | Dữ liệu **phân tích vận hành có ghép vào báo cáo** được không | Chỉ số không phụ thuộc tỷ lệ trả lời (F11) | Dev |
| 8 | Dữ liệu trả lời cũ có **truy vấn theo cùng đối tượng qua thời gian** không | Điều kiện cho báo cáo so sánh | Dev |
| 9 | **Phạm vi AI report** | Phạm vi màn hình phân tích và phần xuất | Vis |
| 10 | Luồng đăng ký và xác nhận điều khoản hiện tại — gồm những bước nào, ai xác nhận, mất bao lâu | Biết F1 cắt được bao nhiêu | Vis |
| 11 | Cho phép tùy biến setting tới mức nào | Cân bằng F12 và khả năng so sánh | Vis |
| 12 | Định nghĩa của 勝率 (tỷ lệ thắng) — chưa được trả lời | Cách viết phần hiệu quả | Vis |

**Mục 1 là chuẩn đo.** Không có nó thì sau này không chứng minh được cải tiến có tác dụng.
**Mục 3 quyết định nội dung F7** — nên hỏi Vis sớm, vì họ có sẵn câu trả lời
từ kinh nghiệm hiện trường.
**Mục 4, 5, 6 đưa vào brief dev** trước khi báo effort.

## Việc cần làm tiếp cho phần 2

| Việc | Vì sao |
|---|---|
| **Lấy tỷ lệ trả lời Before và After từ DB, chia theo bộ phận nếu được** | Chuẩn đo, và xác nhận lại hướng A |
| **Rà soát toàn bộ tính năng WDP đang có, đối chiếu với F1–F12** | Đã bốn lần suy diễn sai về hiện trạng |
| **Hỏi Vis: sau khi chuyển, khách hay hỏi hoặc phàn nàn gì** | Là nội dung cốt lõi của F7 |
| Kiểm tra cấu trúc setting có hỗ trợ điều kiện hiển thị không | Cách hiện thực F5 |
| Kiểm tra có tham chiếu kết quả Before để sinh câu hỏi được không | Điều kiện F5 |
| Kiểm tra dữ liệu phân tích vận hành có ghép vào báo cáo được không | Phòng rủi ro cho tỷ lệ trả lời thấp |
| **Thiết kế thử 2 bộ After（chỉ WD / có XD）để xem với Vis** | Cụ thể hóa F7, dễ lấy phản hồi |
| Ước lượng effort theo từng giai đoạn | Để Vis phán đoán mức đầu tư |
