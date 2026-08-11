# 課題リスト — 提案の土台

Tài liệu chốt danh sách 課題 để bám theo khi viết 提案.

**Nguồn tổng hợp:**

1. Memo của PM (BS) sau khi đọc `vis-wdp-roadmap-overview-ja.pdf`
2. 10 câu hỏi đã được Vis trả lời — xem `10-vis-questionnaire-answers.md`
3. Toàn văn 事業計画 gồm nội dung ẩn — xem `60-quy-trinh-wd-xd-va-before-after.md`
4. Nội dung 2 bộ survey (52 / 19 câu) — xem `50-phan-tich-de-xuat-huong-di.md`

**Nguyên tắc xếp hạng:** ưu tiên theo (a) thứ tự ưu tiên Vis tự công bố（①有料化）, (b) độ mạnh của bằng chứng, (c) khả năng BS hành động được.

---

# PHẦN 0 — Đối chiếu memo PM với câu trả lời Vis

## Memo gốc của PM

```text
ヴィス側にとって良いこと
・WDPを使って勝率が良い理由は、デザイン提案の根拠づけにサーベイ結果が役立つ
 ⇨さらに勝率を強めるために欲しいものは？
・有料契約はなぜとれた？どこに需要を感じれた？

エンドクライアントにとって良いこと
・オフィスを作った後にどう使うかを顧客が自走できる
・before&afterで状況を確認できる

資料での疑問点
・WDPとは別の独立したアプリケーションはすでに開発は動き出しているものか？
・before&afterは今実装されたよね？？
・「共通URL形式」も実装されたやつよね？
・計画から見るとAIレポートとかAIでのアドバイスなどの機能が必要そうだけど
  見送られたのはなぜかを改めて確認

先方にお願いしたいこと
・コンペに出る人やコンサルタントにとって必要なwdpへの要望を聞きたい
```

## Trạng thái từng mục

| Mục trong memo | Vis trả lời | Kết quả / hiệu chỉnh |
|---|---|---|
| さらに勝率を強めるために欲しいもの | **Chưa** — hỏi ngược「勝率とは何を指す？」 | **Còn treo — mục duy nhất chưa xong** |
| 有料契約はなぜとれた | Có（Q3）| 最初から有料の after サーベイ金額込みで効果検証を訴求。価値は「オフィスプロジェクトの効果を数値化」 |
| 顧客が自走できる | Có（Q4）| **Khách hiện ưu tiên B. Before→After, KHÔNG phải 自走**. 自走 là đích FY2027+ |
| before&after で状況確認できる | Có（Q4, Q5）| Đúng là giá trị khách cần — nhưng **chỉ 5/83 case thực hiện** |
| 独立アプリはもう動いている？ | Có（Q6）| AIレポート機能のキックオフ段階、2026/10 完成目処 |
| before&after は実装済みだよね？ | —（Q5）| **Tính năng có, vận hành không có**（83→5）|
| 共通URL形式も実装済みだよね？ | —（事業計画）| Rồi, **nhưng chỉ giải 1 trong 4 khối** của quy trình 6 tuần |
| AIレポートが見送られた理由 | Có（Q7）| 社内AIツールで完結できる可能性 → ブレイブとの開発は見送り。スローペースで進行中 |
| コンペ担当・コンサルの要望 | Có（Q8）| 人員計画レイアウト / **申込・規約の WDP 内完結** / クライアント別サーベイカスタム |

**Hai chỗ memo đoán đúng nhưng cần chỉnh:**

1. 「before&after は実装された」→ chức năng có, **nhưng chỉ 6% case dùng**. Vấn đề ở vận hành, không ở tính năng.
2. 「共通URL も実装された」→ URL chỉ rút ngắn phần thu email. **申込 2 tuần và 結果 2 tuần vẫn nguyên.**

---

# TẦNG 1 — Bốn 課題 làm trục chính

## 課題 1 — 有料契約 2 件 → mục tiêu FY2026 là 20 件 〔XD / WDP〕

### Bằng chứng

| | Số liệu | Nguồn |
|---|---|---|
| 有料契約 hiện tại | **2 件** | 事業計画 + Q&A |
| Mục tiêu FY2026 | **20 件 / 20,920,000円** | Bảng KPI FY2026（biểu đồ EMF）|
| Khoảng cách | **×10** | |
| WDS Before/năm | ~100–120 件 | 事業計画（月10件）|
| Tỷ lệ chuyển đổi cần đạt | ~**17–20%** | Tính từ trên |

Bảng giá WDS theo bậc nhân viên（FY2026）:

| Bậc | Đơn giá | Số case | Số tiền |
|---|---|---|---|
| 51～100人 | 62万 | 6 | 3,720,000 |
| **101人～300人** | **106万** | **10** | **10,600,000** |
| 301～500人 | 150万 | 3 | 4,500,000 |
| 501～1,000人 | 210万 | 1 | 2,100,000 |
| **Tổng** | | **20** | **20,920,000** |

→ **Phân khúc trọng tâm: công ty 101–300 người**（chiếm nửa số case）.

### Cấu trúc vấn đề

Vis viết rõ trong phần KPI FY2026:

> 有料契約は**アフター経由**を対象にしており、コンスタントな受注には至っていない

→ **After là cửa vào duy nhất của doanh thu có phí.**

Và họ tự phân tích:

> 有料契約 = **商談数 × 受注率** と分解した場合…
> ①②のGapとなる課題：商談数upも必要ではあるものの、**商談プロセスの構築が命題**

Phương án họ liệt kê:
- **商談数up**: tăng dùng free qua PM/営業、**無料利用をせず、はじめから有料商談する**、marketing lấy lead
- **受注率up**: gom 商談 về **専任営業担当**、tăng tốc và độ sâu PDCA

### Ý nghĩa cho 提案

1. **Đây là thước đo.** Mọi giải pháp phải trả lời được: *"cái này giúp đi từ 2 lên 20 như thế nào?"*
2. Vì nút thắt là **quy trình bán**, đề xuất thuần tính năng sẽ **lệch trọng tâm**.
3. Cần có phần hỗ trợ 商談プロセス: đề xuất và báo giá After ngay trong WDP, bằng chứng giá trị cho client, theo dõi funnel.

---

## 課題 2 — After không chạy: 5 trên 83 〔XD〕

### Bằng chứng

| Chỉ số | Số liệu |
|---|---|
| Before（FY2025 thực tế）| **83 件** |
| **After** | **5 件**（~6%）|
| ワークショップ/năm | **5–6 件** |
| Dự án renewal/năm | ~**500 件** |

### Cấu trúc vấn đề

1. **After thuộc XD, mà XD do XP（専任コンサル）dẫn** → bị giới hạn bởi **số người**, không phải tính năng.
   Bằng chứng: After 5 件 ≈ ワークショップ 5–6 件. Hai con số gần nhau.
2. **Thời điểm đánh giá là 6 tháng sau chuyển**（bước ⑨: 半年間をひとつの区切りとして評価）→ lúc đó dự án đã đóng, **không còn ai follow**.
3. Quy trình After nặng: tạo lại survey, phát hành, thu hồi, phân tích, làm báo cáo.

### Nghịch lý cần nêu trong 提案

| Sự thật | Nguồn |
|---|---|
| Khách nói Before→After là **quan trọng nhất** | Q4 |
| Vis bán được phí **chính nhờ** nó | Q3 |
| Nhưng chỉ **6%** case thực hiện | Q5 |

→ Đây là khoảng cách giữa **nhu cầu đã được xác nhận** và **năng lực vận hành**. Không phải vấn đề "khách không cần".

### BS có thể làm gì

- Tái sử dụng dữ liệu Before cho After（cùng đơn vị, cùng câu hỏi）
- Đơn giản hoá việc tạo After（nhân bản, gợi ý KPI đã chọn）
- **Nhắc mốc 6 tháng** tự động, gắn owner
- Hỗ trợ chọn KPI 2–3 mục và set goal điểm

---

## 課題 3 — Kết quả survey không nối được vào 提案 〔WD + XD〕

### Bằng chứng

Q1 nguyên văn:
> サーベイ結果と提案が未接続。サーベイ結果をしっかり落とし込んだオフィス提案が難しい

Nguyên nhân từ cấu trúc dữ liệu:

| Chỉ số | Giá trị |
|---|---|
| Tổng câu（bản đầy đủ）| 52 |
| Câu thang 5 mức / chọn sẵn | **49** |
| Câu hỏi "thiếu không gian nào" | 1（Q17, checkbox 10 lựa chọn）|
| Câu nhập số | 2（Q16, Q30）|
| **Câu tự do（free text）** | **0** |

Output là điểm số: `ワークデザインスコア 58.0pt`, `プレイス 63.0`, `スタイル 60.2`, `カルチャー 59.2`, `eNPS -65.2`.

Từ 「プレイス 63点」, consultant **không** biết: khu vực nào, vì sao thấp, xảy ra khi nào, nên sửa gì.

### Điều 事業計画 đòi hỏi

> そこでポイントとなる事は一般的なナレッジ提供に留まる提案にしない事。
> 「**個社最適化**」された提案形式を作る事になります。

### Comment nội bộ đã viết sẵn giải pháp

小西 芳樹（2025-12-24）:

> この優位性は足元の事実ではあるものの、**競合も模倣可能**なので…「価格が安いから選ばれる」という戦略は、結局**価格競争に巻き込まれます**。
> visの本当の強みは「**デザイン（空間）**」と「**コンサル（データ）**」が**分断されずにシームレスにつながる体験**にあるはず…
> そうすると、差別化要因は「**空間デザインへの即時反映力**」と定義し直すことがよいかもしれません。
> 「**サーベイ結果がこうだったから、来週のレイアウト変更案はこう変わります**」というスピード感こそが、ヴィスにしかできない付加価値の一つになると思います。

→ **Dùng chính câu này làm điểm tựa khi trình bày.** BS đang hiện thực hoá 「即時反映力」 mà nội bộ Vis đã xác định là lợi thế cạnh tranh thật.

---

## 課題 4 — Quy trình 6 tuần không vừa cửa sổ 3–4 tuần 〔WD〕

### Bằng chứng

Q10 nguyên văn:
> WDP単体のリードタイムは長くない。どちらかというとオフィス提案準備の3-4週間の中で
> サーベイの提案、実施、提案書への落とし込みまでを行う時間が足りない

Timeline trong 事業計画:

| Bước | Thời gian | URL配信 đã giải? |
|---|---|---|
| 実施意思決定 | 1 tuần | Không |
| **申込（含 リーガルチェック）** | **2 tuần** | **Không** |
| 実施 | 1 tuần | Một phần（bỏ thu email）|
| **結果** | **2 tuần** | **Không** |
| **Tổng** | **6 tuần** | vs cửa sổ **3–4 tuần** |

→ **Thiếu 2–3 tuần.** Hai khối lớn nhất chiếm **4/6 tuần**.

### Kết nối quan trọng với Q8

Yêu cầu của コンサル trong Q8:
> **WDP上で申込みや規約の確認が完結する仕組み**

→ Đánh trực tiếp vào khối **申込 2 tuần**. Đây **không phải** feature request rời rạc — **nó nằm trên critical path của 課題 4**.

**Đây là điểm hiệu chỉnh so với phân tích ban đầu**, nơi Q8 từng bị xếp vào "backlog / phase 2".

### Rào cản phi kỹ thuật kèm theo

> パートナー選定後でないとWDSの実施ができないと言われる

Lý do: 不平等感 / パートナーでない企業のサービスへの抵抗感 / 全社巻き込みで決裁が取れない

Giải pháp 事業計画 đã ghi: nói rõ **kết quả survey vẫn dùng được dù chọn công ty khác**; khuyến khích làm từ giai đoạn sớm; nói rõ không cần thu email.

---

# TẦNG 2 — Ba 課題 nền, phải giải để Tầng 1 thành lập

## 課題 5 — Không thu được "vì sao / ở đâu" từ worker 〔WD + XD〕

### Bằng chứng

- **0 câu tự do** trong cả 52 và 19 câu（đã kiểm tra JSON）
- **Nhưng** XD đã có bước ⑦**座談会**:
  > オフィスリニューアル後に運用プロジェクトメンバーとは別で**ランダムで社員の方を10名程度**選出し、
  > 移転後利用してみてどのように感じているかをヒアリング、ディスカッションします。
  > そこで想定外の事象が発生していないか、どの様な効果が出ているかという**生の意見**を吸い上げ、
  > 運用プロジェクトメンバーに共有していきます。
- Và bước ⑧ có **khảo sát ngắn tại event**

### Vậy vấn đề thực sự là gì

Không phải "thiếu kênh", mà là kênh đó:

| Đặc điểm hiện tại | Hệ quả |
|---|---|
| **Thủ công** | Không scale |
| **Mẫu ~10 người** | Không đủ làm căn cứ 提案 |
| **Phụ thuộc XP** | Dính vào 課題 6 |
| **Dữ liệu nằm ngoài WDP** | Không tái sử dụng, không so sánh được theo thời gian |

### Cách phát biểu trong 提案

| Cách nói sai | Cách nói nên dùng |
|---|---|
| "Thêm Worker Voice vào survey" | "**Số hóa và mở rộng 座談会 đang làm thủ công cho 10 người**" |

Lý do: không phủ nhận quy trình Vis đang có, đồng thời trực tiếp giảm phụ thuộc consultant.

### Nguyên tắc thiết kế

**Không** làm 52 câu chi tiết hơn cho tất cả — survey dài ra sẽ giảm response rate, mà response rate chính là thứ cần giữ để đo định kỳ.

Thay vào đó dùng **follow-up có điều kiện**:
- Chỉ ai chọn 不満 / điểm thấp mới được hỏi sâu: khu vực nào / lý do gì / ảnh hưởng công việc ra sao
- Thêm **自由記述** cho ý kiến cải thiện
- Có thể gắn **layout map** để worker chỉ trực tiếp vị trí

→ Đây là gốc của cả **課題 3**（không viết được 提案）và **課題 6**（属人性）.

---

## 課題 6 — XD phụ thuộc XP nên không scale 〔XD〕

### Bằng chứng

事業計画:
> このビジネスの課題としては**コンサルタント、クリエイターの数を増やし続ける必要がある**という特性

Thực tế: ワークショップ **5–6 件/năm** trên **500 dự án renewal**.

### Câu hỏi then chốt từ comment nội bộ

小西 芳樹:
> 「低価格だから幅広い顧客層にリーチ」できるわけではなく、セールス・マーケティングを含めて
> 効率よく中堅企業・中小企業にリーチでき、利益を残せるモデルが必要です。
> つまり、「**なぜ低価格にできるのか**」という点が大事であり、そこが競争優位性になります。

→ Nếu mỗi case vẫn cần XP làm tay thì **không thể hạ giá**. Đây là **lý lẽ mạnh nhất** cho việc chuẩn hoá việc của consultant.

Comment khác cũng nêu vấn đề nhân lực:
> XDのような無形商材は、高い専門知識がないと顧客の課題に刺さりにくいため、
> 営業同席も考えると、**XDの人数が足りているかは精査必要**
> **CSは2026年時点で少なくとも1人置く**か、セールスが兼務する必要はある

### Đây đúng là track trong kế hoạch

> WDPの開発サイクルは非常に重たくクイックな機能開発がライトに実施できない性質があります。
> ここでそれを補うのは**WDPとは別のアプリケーションを並行して開発**しておくことです。
> XPは事業提供に必要な機能をそのアプリケーションに持たせてサービス提供をしていきます。
> **ここではアプリケーションはクライアントに利用してもらわなくて良いです。**
> …社内ツールとして使われたアプリケーションはその後に**WDPに置換**していく事にします。

Lộ trình: `XD MVP → XD PMF → XD年間契約 → アプリ開発 → WDPへ置換 → 両面で継続契約`

**Hai điều rút ra:**
1. Lý do tồn tại của 別アプリ chính là **vòng phát triển WDP quá nặng** — đúng lập luận BS đã nêu trong họp（「1から作る方が作りやすい」）
2. 別アプリ là **tool nội bộ cho XP**, không phải sản phẩm cho khách → hướng "encode việc consultant" **đã nằm trong kế hoạch**

### Phân chia scope

Đánh giá từng việc trong 10 bước XD:

| Việc của XP | Encode vào hệ thống? | Ghi chú |
|---|---|---|
| Chọn KPI（3 mục / MVP 2 mục）+ set goal | **Được** — gợi ý theo loại dự án và điểm thấp | Đồng thời giải 課題 9 |
| Đọc điểm → xác định vấn đề | **Được** — cần dữ liệu từ 課題 5 | Chính là Survey-to-Proposal |
| Đề xuất event / hành động | **Một phần** — thư viện phương án theo loại vấn đề | Không thay hoàn toàn |
| 座談会 thu ý kiến | **Được** — số hóa, mở rộng mẫu | 課題 5 |
| Điều phối workshop | **Khó** — cần người | Giữ cho XP |
| Làm báo cáo | Vis tự làm AIレポート | **Ngoài scope BS** |
| Theo dõi và đo lại định kỳ | **Được** — nhắc mốc 6 tháng, so sánh | Chỗ gắn 継続 |

**Nguyên tắc:** BS nhận phần **lặp lại và có quy tắc**; giữ cho XP phần **workshop và tư vấn sâu**.

**Cách trình bày:** không nói "thay thế consultant", mà nói 「**consultantの判断を仕組みに落とす**」.

---

## 課題 7 — Chưa có chỗ chứa việc dùng liên tục 〔XD / WDP〕

### Bằng chứng

事業計画:
> 現時点では現状把握のための利用が主な活用手段の為、**ショット型で継続利用に繋がっていない点が
> マネタイズに至らない背景**となります。

### Điểm phải cẩn thận — pulse đã tồn tại

| File | `createdAt` | Ngày |
|---|---|---|
| ワークデザインサーベイ（52 câu）| 1729839740 | 2024-10-25 |
| ワークデザインサーベイ（パルス）（19 câu）| 1736406861 | **2025-01-09** |

→ Vis **đã tự tạo** bộ pulse rút gọn. Nghĩa là **không thiếu công cụ pulse** — thiếu **mô hình bán và vận hành định kỳ**.

**Hệ quả:** không đề xuất build lại pulse. Nếu làm, sẽ bị phản hồi "đã có rồi".

### Phải đúng thứ tự theo kế hoạch của Vis

| Năm | WDP売上 | Phase | Trạng thái WDP |
|---|---|---|---|
| FY2026 | **0.2億** | 検証（MVP）| **After 中心のスポット利用に留め** |
| FY2027 | 0.5億 | PMF | **XD卒業顧客の自走ツール** として bắt đầu có giá trị |
| FY2028 | 1億 | スケール開始 | **SaaS として商品化** + 開発内製化 |
| FY2029 | 2億 | 拡張 | 属人性低減, quá nửa doanh thu là stock |
| FY2030 | 4億 | 事業確立 | Platform hàng trăm công ty |

→ **FY2026 mục tiêu là tăng tỷ lệ chuyển đổi spot**, không phải bán subscription.
→ Nhưng **kiến trúc cho 継続** nên dựng từ giờ để FY2027–28 không phải làm lại.

### Mô hình đích để tham chiếu

| Nguồn | Mô hình |
|---|---|
| Bảng kế hoạch 2025/6（FY2030）| **300社 × 600千円/年**（≈5万円/tháng）, 粗利率 100%, 10 người vận hành |
| Comment 小西（FY2028）| **80–100社 × MRR 10万円** |

Cả hai đều chỉ ra: cần **hàng chục đến hàng trăm công ty trả phí định kỳ**, so với **2 công ty hiện tại**.

---

# TẦNG 3 — Tiền đề và rủi ro（nêu trong 提案, không làm trục）

## 課題 8 — Bằng chứng 受注率 còn mỏng（n=13 / n=8）

### Bằng chứng

**コンペ案件:**

| | 件数 | 受注件数 | 受注率 | 受注額 |
|---|---|---|---|---|
| Toàn bộ | 418 | 129 | 30.90% | 8,012,451,000 |
| **Có dùng WDP** | **13** | 7（完工）| 53.80% | 415,200,000 |

→ 上昇 23.00% → 貢献額 95,433,346円

**ナーチャリング・特命:**

| | 件数 | 受注件数 | 受注率 | 受注額 |
|---|---|---|---|---|
| Toàn bộ | 669 | 332 | 49.60% | 12,597,144,000 |
| **Có dùng WDS** | **8** | 6 | 75.00% | 201,700,000 |

→ 上昇 25.40% → 貢献額 51,178,737円

### Nhận xét

Con số **+22.9pt / +25.4pt** — nền tảng của toàn bộ **1.466億 間接効果** — dựa trên mẫu **n=13** và **n=8**.
Văn bản viết 「統計的に有意に改善している」nhưng cỡ mẫu này còn mỏng.

### Cách dùng trong 提案（biến thành lợi thế）

- Tăng số case dùng WDP vừa **tăng doanh thu gián tiếp**, vừa **làm dày bằng chứng** cho chính lập luận giá trị của WDP
- Khớp với cảnh báo của 小西: lợi thế hiện tại là 「足元の事実」mà 「競合も模倣可能」→ cần liên tục nâng độ phân giải
- Là lý lẽ tốt để đề xuất **đo và theo dõi funnel hệ thống** — trùng với các chỉ số Vis đã tự liệt kê:
  > ・PS全体に対してのサーベイ実施件数と率
  > ・PS期間中に実施した案件での活用度合い、満足度
  > ・**after提案件数と率、after実施数と率**
  > ・ナーチャリング実施件数からのPS化貢献数、率
  > 全体数が足りていないのか、転換率が足りていないのか、どちらもなのか

→ **BS phân tích funnel = giúp Vis trả lời câu hỏi họ đã tự đặt.**

---

## 課題 9 — Khó chứng minh nhân quả

### Bằng chứng

Thứ Vis bán（Q3）: 「**オフィスプロジェクト**の効果を数値化」

Nhưng survey đo cả:

| Nhóm câu | Yếu tố ngoài tầm ảnh hưởng của office |
|---|---|
| Q32–37 | Văn hóa doanh nghiệp, cơ hội học tập, đóng góp xã hội |
| Q39 | Quan hệ con người |
| Q40 | Sức khỏe thể chất |
| Q44 | Tầm nhìn công ty |
| Q47 | Career path |

Những mục này chịu ảnh hưởng bởi quản lý, nhân sự, khối lượng công việc, biến động tổ chức.

### Vis đã có sẵn cách xử lý

| Phạm vi | Số mục KPI |
|---|---|
| XD đầy đủ（bước ⑥）| **3 mục** trong 52 câu |
| XD MVP（FY2025/2026）| **2 mục** |

→ Đề xuất của BS về KPI gắn office **không phải ý mới**, mà là **hệ thống hóa điều họ đã định làm bằng tay**. Đây là cách trình bày dễ được chấp nhận nhất.

### BS có thể làm gì

- Hỗ trợ chọn KPI theo loại dự án và điểm thấp
- **Tách rõ** chỉ số nào office ảnh hưởng trực tiếp（Place, Style）vs chỉ số nào là bối cảnh（Culture, Career）

---

## 課題 10 — Lan tỏa nội bộ lệch về người có ý thức cao

### Bằng chứng

> 徐々にWDSに関しては導入件数が月平均10件と徐々に利活用が進んできていますが、
> **ワークショップは年間を通しても5,6件**にとどまっています。
> 一方でオフィスリニューアルプロジェクト自体は**年間で500件**程度進んでいます。
> **意識の高い人に利活用が進み、意識の高くない人はまだ一度も活用したことが無い人も多く存在している**

### Cách Vis định giải — không phải bằng tool

> 通常のリニューアルプロジェクトの提案時に**盛り込むことを社内ルールとする**事です。
> ワークプレイスデザインとしてはこれ、エクスペリエンスデザインとしてはこう。といった形で
> 提案をしているか否かが**一目で判別**する分かりやすい状態で行います。

> 提示する金額面はMVPに絞ったリーズナブルで且つハードルの低いものとします。
> 具体的には**100万円程度**が目安…そのスタートは**2026年4月から**の提案にて実施を予定します。
> ここに対しても**プロトタイプ提案を事前に3件程度**実施しておくべきです。

### Vị trí của BS

**Không cạnh tranh với quy tắc đó, mà làm cho nó chạy được:**

| Nhu cầu từ quy tắc | BS có thể cung cấp |
|---|---|
| Dễ **đề xuất** XD/After | Template, một cú bấm từ kết quả Before |
| Dễ **báo giá** | Gói ~100万円 chuẩn hóa, bảng giá theo bậc |
| Dễ **vận hành** | Giảm việc tay của XP trong 10 bước |
| **一目で判別** | Dashboard: dự án nào đã đưa XD vào 提案 |

---

# PHẦN 4 — Ngoài scope（nên nói rõ trong 提案）

| Mục | Lý do | Nguồn |
|---|---|---|
| **AIレポート / AIアドバイス** | Vis tự làm bằng AI nội bộ, ~2026/10, 「ブレイブさんとの開発は見送り」 | Q6, Q7 |
| **独立アプリ bán cho khách** | Kế hoạch: giai đoạn đầu là tool nội bộ cho XP, 「クライアントに利用してもらわなくて良い」. Cung cấp cho khách là FY2027+ | 事業計画 |
| **Self-service / SaaS ngay** | Theo kế hoạch là FY2028. Đề xuất bây giờ là **sớm 1–2 năm** | Bảng kế hoạch |

**Lưu ý về AIレポート:** có ý kiến nội bộ BS cho rằng vì Vis tiến chậm nên vẫn còn cửa thảo luận（xem `11-meeting-notes.md`）. Nhưng **không lấy làm trục 提案** — chỉ nhắc như bối cảnh về tốc độ nếu cần.

---

# PHẦN 5 — Map 課題 sang trục 提案

| Trục đề xuất | Giải 課題 | Service | Ghi chú |
|---|---|---|---|
| **Rút ngắn cửa sổ 3–4 tuần** — 申込・規約 hoàn tất trên WDP + 結果→提案書 | 4, 3 | WD | Q8 nằm trên critical path |
| **Survey-to-Proposal** — điểm → nguyên nhân → ưu tiên → phương án layout/XD → block 提案書 | 3, 5 | WD chính, XD phụ | Khớp comment「即時反映力」|
| **Số hóa 座談会** — follow-up có điều kiện + free text + chỉ vị trí trên layout | 5, 3, 6 | Cả hai | Mở rộng cái đang có, không tạo mới |
| **Vận hành After** — tái dùng dữ liệu Before, nhắc mốc 6 tháng, hỗ trợ chọn KPI | 2, 9, 1 | XD | Cửa vào doanh thu có phí |
| **Hỗ trợ 商談プロセス** — đề xuất/báo giá After trong WDP, funnel `after提案率・after実施率` | 1, 2, 7 | XD | Vis nói đây là 命題 |
| **Chuẩn hóa việc của XP** — phần lặp lại và có quy tắc trong 10 bước | 6, 7, 10 | XD | Trả lời「なぜ低価格にできるのか」|

**Ba trục đầu** phục vụ **WD（thắng đề xuất）**. **Ba trục sau** phục vụ **XD（doanh thu có phí）**.
Đúng cách tách **提案用 / 継続用** mà ghi chú nội bộ ở Q8 đã nêu.

## Câu hỏi kiểm tra mọi đề xuất

1. Cái này giúp đi từ **2 件 lên 20 件** như thế nào?
2. Cái này giúp trả lời câu 「**なぜ低価格にできるのか**」 như thế nào?
3. Cái này thuộc **提案用（WD）** hay **継続用（XD）**?
4. Cái này có nằm trong **cửa sổ 3–4 tuần** không?

---

# PHẦN 6 — Còn phải xác nhận với Vis

| # | Nội dung | Vì sao quan trọng |
|---|---|---|
| 1 | **Định nghĩa 勝率**（Q2）| Vis hỏi ngược, chưa trả lời. Là mục **duy nhất** trong memo PM còn treo |
| 2 | **Starter 40 件 hay 21 件?** | Text ghi 40, bảng KPI ghi 21. Giả thuyết: 21 XD + 20 WDS = 41. Ảnh hưởng cách hiểu quy mô 検証 FY2026 |
| 3 | **WDP FY2030 là 4億 hay 1.8億?** | Bảng XD計画（12/2025）ghi 4億; bảng toàn công ty（6/2025）ghi 1.8億（300社 × 600千円/年）|
| 4 | **20 件 有料 FY2026 phân bổ thế nào** | 「有料契約はアフター経由を対象」nhưng cũng có 「無料利用をせず、はじめから有料商談する」→ cần biết tỷ lệ để thiết kế đúng luồng |
| 5 | Ai làm 別アプリ và khi nào | Tài liệu roadmap ghi 「まだ決まっていない」. Ảnh hưởng trực tiếp tới vị trí của BS |

---

# Tổng kết

**Bốn 課題 trục chính:**

1. **有料契約 2 → 20 件**（FY2026）, cửa vào là After, nút thắt là **商談プロセス**
2. **After chỉ 5/83**, do phụ thuộc XP và không có ai follow ở mốc 6 tháng
3. **Survey → 提案 chưa nối**, vì chỉ có điểm số, không có nguyên nhân và vị trí
4. **6 tuần không vừa cửa sổ 3–4 tuần**, với 申込 2w và 結果 2w là hai khối lớn nhất

**Ba 課題 nền:** thiếu dữ liệu "vì sao/ở đâu"（座談会 thủ công）, XD phụ thuộc XP, chưa có chỗ chứa 継続.

**Ba tiền đề/rủi ro:** bằng chứng n=13/n=8, khó chứng minh nhân quả, lan tỏa nội bộ lệch.

**Một câu tóm gọn 課題 cho 提案:**

> WDP đã chứng minh giá trị ở **đầu phễu**（受注率 +22.9pt / +25.4pt）, nhưng chưa đi được tới **cuối phễu**（有料 2 件）. Nguyên nhân không phải thiếu tính năng, mà là: kết quả survey **chưa chuyển được thành đề xuất**, quy trình **không vừa cửa sổ 3–4 tuần**, và After **phụ thuộc vào consultant** nên không lặp lại được.
