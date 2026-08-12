# Quy trình 提案 của Vis với end user — bản dựng lại từ tài liệu

Mục đích: có một bản mô tả quy trình **chỉ dựa trên tài liệu**, để đối chiếu khi thiết kế cải tiến.

**Nguyên tắc của file này:** mỗi mục đều ghi nguồn. Chỗ nào không có trong tài liệu thì ghi rõ là không có, không suy diễn.

**Nguồn:**

- 『ヴィスの現状と今後について』WDP XD事業計画 / 小川 慧 / 2025-12-26 — ký hiệu `[số]` là số đoạn văn
- `ヴィス質問票.xlsx` — câu trả lời của Vis, ký hiệu `Q1`–`Q10`
- Website chính thức: <https://vis-produce.com/service/data-solution/wdp>

---

# PHẦN 1 — Luồng tổng thể

```
① 案件発生
    ├─ コンペ案件（3社程度のコンペ形式）
    └─ 特命案件・ナーチャリング案件

② 提案依頼を受ける ──────── ここから提案本番まで 3〜4週間

③ ヒアリング

④ 提案書の作成
    コンセプト設定 → レイアウト案 → デザイン案 → 予算

⑤ 提案本番（コンペ）

⑥ 受注

⑦ 設計・施工 → 移転

⑧（XDが入る場合）XPによる10ステップ
```

## Dẫn nguồn

| Bước | Nội dung nguyên văn | Nguồn |
|---|---|---|
| ① | 「移転先の物件やコンサル設計会社の選定においても、**3社程度のコンペ形式**でその中から最も相性の良いコストパフォーマンスの良い企業と進行していく」 | [92] |
| ① | Phân loại 「コンペ案件」「特命案件・ナーチャリング案件」 | [226][227] |
| ② | 「クライアントからの提案依頼から提案までのスケジュールは**3-4週間程度**」 | [382] · Q1 · Q10 |
| ③④ | 「どの類似企業も一般的には**ヒアリング内容に基づいて、コンセプトを設定し、レイアウト案、デザイン案、予算**という形で提案を行います」 | [49][50] |
| ④ | 「オフィスリニューアルとしての提案は**型化**されています」 | [48] |
| ⑧ | XD 10ステップ（プログラミング／構成要員／チェンジマネジメント／移転説明会／実施計画／KPI設計／座談会／イベント実施支援／評価改善／継続支援）| [106]–[154] |

## Khung 4 phase trên website chính thức

> 「PROGRAMMING」「DESIGN」「CREATE」「UPDATE」の4つのフェーズを継続させることで、
> 理想的な「はたらく」をデザインします。

Nguồn: vis-produce.com（WDPページ）

---

# PHẦN 2 — Chuỗi survey trong khung 3〜4 tuần（phần đang tập trung）

> **Phạm vi:** chỉ chuỗi liên quan tới survey.
> Các bước của bản 提案 tự thân（ヒアリング・コンセプト・レイアウト・デザイン・予算）
> không thuộc phạm vi lần này — xem PHẦN 1 nếu cần đối chiếu.

## Câu gốc từ Vis

> どちらかというとオフィス提案準備の3-4週間の中で
> **サーベイの提案、実施、提案書への落とし込み**までを行う時間が足りない

Nguồn: Q10

Vis nêu **ba việc**. Bảng timeline trong 事業計画 lại chia thành **bốn công đoạn khác**.
Ghép hai nguồn lại được chuỗi 6 bước sau.

## Chuỗi 6 bước

| # | Bước | Thời lượng | Nguồn | Đã có lời giải chưa |
|---|---|---|---|---|
| ① | **サーベイの提案** | *không có số* | Q10 | Rào cản ghi ở [392]–[395]; giải pháp trong kế hoạch là **cách nói**, không phải hệ thống |
| ② | **実施意思決定** | 1w | [403] | Giải pháp: thực hiện sớm từ ナーチャリング段階 [390][398] |
| ③ | **申込（リーガルチェック含）** | **2w** | [404] | **Chưa có** |
| ④ | **実施** | 1w | [405] | URL形式 rút ngắn phần thu danh sách email [388][389] |
| ⑤ | **結果** | **2w** | [406] | **Chưa có** |
| ⑥ | **提案書への落とし込み** | *không có số* | Q10 · Q1 | **Chưa có** |

```
① サーベイの提案 → ② 実施意思決定 → ③ 申込 → ④ 実施 → ⑤ 結果 → ⑥ 提案書への落とし込み
   記載なし          1w             2w        1w       2w        記載なし
                    └──────── 合計 6w（記載分のみ）────────┘

枠：3〜4週間
```

## Ba điều đáng chú ý

**1. Vis nêu ① và ⑥, nhưng timeline không có.**
Q10 liệt kê 「サーベイの**提案**、実施、**提案書への落とし込み**」.
Bảng timeline chỉ đi từ ② tới ⑤.
→ **Hai bước Vis nhắc đầu tiên và cuối cùng đều không được đo.**

**2. Hai khối 2 tuần nằm ở ③ và ⑤** — chiếm 4 trong 6 tuần có số.
② và ④ mỗi cái chỉ 1 tuần, nên dư địa lớn nằm ở ③ và ⑤.

**3. Timeline là 参考値.**
Nằm dưới tiêu đề 「実行シミュレーション / タイムライン参考」[401][402],
**không phải số đo thực tế**.

## Số học

| | |
|---|---|
| Khung | **3–4 tuần**（[382] · Q1 · Q10）|
| Phần chuỗi survey có ghi số | **6 tuần**（[403]–[406]，参考値）|
| Bước chưa có số | **2**（① và ⑥）|

Đây chính là câu:

> 3-4週間の中でWDP(WDS)の実施をしたうえで提案内容にその結果を反映させることが**困難**

Nguồn: [383]

## Câu bỏ dở trong tài liệu

Ngay sau bảng timeline:

> セイルが提案３週間前実施だとした場合、セイル時にサーベイ結果を揃える為に必要なリードタイムは

Nguồn: [407] — **câu kết thúc giữa chừng**, không có phần trả lời.

## Câu hỏi sắc nhất cần hỏi Vis

### ⑤ 結果 2 tuần gồm những gì?

WDP tự tính điểm và hiển thị kết quả — màn hình `サーベイ結果` đã có biểu đồ,
điểm 6 trục, phân tích thuộc tính.

Vậy 2 tuần đó là:

| Khả năng | Nếu đúng thì cải tiến khác nhau thế nào |
|---|---|
| Thời gian **chờ nhân viên trả lời** | Phải tác động vào tỷ lệ phản hồi（nhắc, rút gọn, cách thông báo）|
| Thời gian **xử lý tay sau khi có kết quả** | Phải tự động hóa（tổng hợp, xuất nội dung）|

Hai khả năng này dẫn tới hai hướng hoàn toàn khác. **Cần xác định trước khi thiết kế.**

### ④ và ⑤ ranh giới ở đâu

④ 実施 1w và ⑤ 結果 2w — cái nào là thời gian survey mở, cái nào là xử lý?

### URL形式 đã rút ngắn bước nào

Memo ghi 「サーベイ実施 đã được giải quyết bằng 共通ID」.
Nhưng 事業計画 viết cụ thể hơn:

> **メールアドレス一覧の回収におけるリードタイム**の短縮 ⇒ 配信形式をURL形式にする

Nguồn: [388][389]

Việc thu danh sách email có thể nằm ở **③申込**（chuẩn bị đối tượng）chứ không hẳn ở ④実施.

→ Cần xác nhận **URL đã cắt vào bước nào, và con số hiện tại của bước đó là bao nhiêu.**
Nếu nó cắt vào ③ thì con số 2 tuần đã khác rồi.

# PHẦN 3 — Cách 事業計画 tự phân tích khúc này

## 課題分解

> ① WDSの実施におけるリードタイム
> ② WDSの実施タイミング

Nguồn: [384]–[386]

**Đáng chú ý:** họ chia theo **lead time** và **timing**, không chia theo từng công đoạn như bảng timeline.
Trong 課題分解 của họ **không có** mục 申込 hay 結果分析.

## 課題別解決策

| 課題 | 解決策 | Nguồn |
|---|---|---|
| ① 実施リードタイム | メールアドレス一覧の回収におけるリードタイムの短縮 ⇒ **配信形式をURL形式にする** | [388][389] |
| ② 実施タイミング | **ナーチャリングやヒアリング段階から**行う | [390] |

## その他課題 — rào cản phi kỹ thuật

> パートナー選定後でないとWDSの実施ができないと言われる
> 背景：不平等感につながる／パートナーでない企業のサービスを使う事への抵抗感／
> 全社巻き込みの企画となるため決裁が取れない

Nguồn: [392]–[395]

**Giải pháp ghi trong kế hoạch là cách nói, không phải hệ thống:**

- 他企業に選定されたとしてもサーベイ結果は活用してもらっても良いと伝える [396][400]
- メールアドレス一覧は回収せずとも実施できる旨を伝える [399]
- ナーチャリング段階や早期段階からサーベイの実施を促す [398]

---

# PHẦN 4 — Thời điểm dùng WDP: hiện trạng vs định hướng

| | Nội dung | Nguồn |
|---|---|---|
| **Hiện trạng** | 「3-4週間の中でWDP(WDS)の実施をしたうえで提案内容にその結果を反映させることが**困難**」 | [383] |
| **Định hướng** | 「**提案初期やナーチャリング段階**でWDPを活用することで、仮説ベースではなくデータに基づいた提案が可能となり、提案の説得力・納得度が向上する」 | [224] |
| **Định hướng** | 「実施タイミングを**ナーチャリングやヒアリング段階から**行う」 | [390] |
| **Định hướng** | 「ナーチャリング段階や早期段階からサーベイの実施を促す」 | [398] |

→ Việc đưa WDS lên sớm là **điều Vis muốn làm**, không phải điều đang làm.

---

# PHẦN 5 — Thay đổi dự kiến từ 2026/4

> 通常のリニューアルプロジェクトの提案時に**盛り込むことを社内ルールとする**事です。
> ワークプレイスデザインとしてはこれ、エクスペリエンスデザインとしてはこう。といった形で
> 提案をしているか否かが**一目で判別**する分かりやすい状態で行います。

Nguồn: [304]

> 提示する金額面はMVPに絞ったリーズナブルで且つハードルの低いものとします。
> 具体的には**100万円程度**が目安となるでしょう。
> そしてそのスタートは**2026年4月から**の提案にて実施を予定します。
> ここに対しても**プロトタイプ提案を事前に3件程度**実施しておくべきです。

Nguồn: [306]

---

# PHẦN 6 — Điều tài liệu KHÔNG nói（chuỗi survey）

| # | Chưa rõ | Liên quan bước | Ảnh hưởng tới việc gì |
|---|---|---|---|
| 1 | **「サーベイの提案」mất bao lâu, khó ở chỗ nào** | ① | Là bước Vis nêu **đầu tiên** ở Q10 nhưng không có số |
| 2 | **Luồng 申込 gồm những bước gì, ai xác nhận** | ③ | Đang khảo sát（memo ghi 調査中）. Là khối 2 tuần |
| 3 | **URL形式 đã cắt vào bước nào** | ③ hay ④ | Nếu cắt vào ③ thì con số 2 tuần đã khác |
| 4 | **④ và ⑤ ranh giới ở đâu** | ④⑤ | Không biết đâu là thời gian mở survey, đâu là xử lý |
| 5 | **⑤ 結果 2 tuần gồm những gì** | ⑤ | **Câu quan trọng nhất** — quyết định hướng cải tiến |
| 6 | **「提案書への落とし込み」mất bao lâu** | ⑥ | Là công đoạn muốn cải tiến nhưng không có số |
| 7 | **Ai làm bước nào** | Toàn bộ | Không biết cải tiến nhắm vào ai |
| 8 | **「セイル」là gì** | — | Xuất hiện ở [407], không được định nghĩa |
| 9 | **「PS」là gì** | — | Xuất hiện ở [348][349][351]（PS全体 / PS期間中 / PS化）. Là chỉ số Vis dùng để đo đóng góp của nurturing |

---

# Tóm tắt

**Điều chắc chắn có trong tài liệu:**

1. Khung là **3–4 tuần**（[382]，Q1 và Q10 đều xác nhận）
2. Chuỗi survey phần được ghi số là **6 tuần**（[403]–[406]，nhưng là 参考値）
3. Vis nêu **ba** việc trong khung: サーベイの提案 / 実施 / 提案書への落とし込み（Q10）
4. Trong ba việc đó, **chỉ 実施 có số**; hai đầu không có
5. Hai khối lớn nhất trong phần có số là **③申込 2w** và **⑤結果 2w**
6. 事業計画 tự cho rằng cả hai 課題 họ liệt kê **đã có lời giải**（URL形式 + 早期実施）

**Thứ tự hỏi Vis:**

| Ưu tiên | Câu hỏi | Vì sao |
|---|---|---|
| 1 | ⑤結果 2 tuần gồm những gì | Quyết định hướng cải tiến（tỷ lệ phản hồi vs tự động hóa）|
| 2 | Luồng ③申込 gồm những bước nào | Khối 2 tuần, và là yêu cầu đã có ở Q8 |
| 3 | URL đã cắt vào bước nào, còn lại bao nhiêu | Con số hiện tại có thể đã khác 参考値 |
| 4 | ⑥落とし込み mất bao lâu | Công đoạn muốn cải tiến |
| 5 | ①サーベイの提案 khó ở chỗ nào | Vis nêu đầu tiên nhưng ta chưa chạm tới |
