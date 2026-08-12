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

# PHẦN 2 — Bên trong khung 3〜4 tuần（phần đang tập trung）

Tài liệu mô tả **hai mạch chạy trong cùng khoảng thời gian**, nhưng mức chi tiết rất khác nhau.

## Mạch A — bản thân 提案書

**Chỉ có thành phần, không có thời lượng.**

> どの類似企業も一般的には**ヒアリング内容に基づいて、コンセプトを設定し、
> レイアウト案、デザイン案、予算**という形で提案を行います

Nguồn: [49][50]

Lưu ý cách viết: câu này mô tả 「どの類似企業も一般的には」 — chuẩn chung của ngành, Vis nằm trong đó.

Và [48]: 「オフィスリニューアルとしての提案は**型化**されています」

**Không có bước nào kèm số ngày.**

## Mạch B — chuỗi WDS

**Có timeline, nhưng là con số tham chiếu.**

| 工程 | 期間 |
|---|---|
| 実施意思決定 | 1w |
| 申込（リーガルチェック含）| 2w |
| 実施 | 1w |
| 結果 | 2w |
| **合計** | **6w** |

Nguồn: [403]–[406]

**Quan trọng:** phần này nằm dưới tiêu đề 「**実行シミュレーション / タイムライン参考**」[401][402]
→ đây là **số tham chiếu, không phải số đo thực tế**. Không nên trình bày như thực trạng đã đo.

## Q10 bổ sung hai bước không có trong timeline

Vis trả lời:

> 3-4週間の中で**サーベイの提案、実施、提案書への落とし込み**までを行う時間が足りない

Đối chiếu:

| Bước Vis nêu ở Q10 | Có trong timeline? | Ghi chú |
|---|---|---|
| **サーベイの提案** | **Không** | Đứng trước 実施意思決定 |
| 実施 | Có（1w）| |
| **提案書への落とし込み** | **Không** | Đứng sau 結果 |

→ **Timeline 6 tuần chỉ bao phủ phần giữa.**
Hai đầu — thuyết phục khách đồng ý làm survey, và đưa kết quả vào 提案書 — không có số.

## Ghép lại

```
提案依頼を受ける
   │
   ├─ [提案] ヒアリング → コンセプト設定 → レイアウト案 → デザイン案 → 予算
   │         構成の記載あり／所要期間の記載なし
   │
   └─ [WDS] サーベイの提案 → 実施意思決定 → 申込 → 実施 → 結果 → 提案書への落とし込み
             記載なし        1w         2w    1w    2w      記載なし
                             └────── 合計 6w（記載分のみ）──────┘
   │
提案本番

枠：3〜4週間
```

**Số học:** khung 3–4 tuần · phần WDS có ghi số đã là **6 tuần** · còn hai bước chưa có số.

Đây chính là câu:

> 3-4週間の中でWDP(WDS)の実施をしたうえで提案内容にその結果を反映させることが**困難**

Nguồn: [383]

## Câu bỏ dở trong tài liệu

Ngay sau bảng timeline:

> セイルが提案３週間前実施だとした場合、セイル時にサーベイ結果を揃える為に必要なリードタイムは

Nguồn: [407] — **câu kết thúc giữa chừng**, không có phần trả lời trong tài liệu.

---

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

# PHẦN 6 — Điều tài liệu KHÔNG nói

| # | Chưa rõ | Ảnh hưởng tới việc gì |
|---|---|---|
| 1 | **Hai mạch A và B chạy song song hay nối tiếp** | Nếu nối tiếp thì càng không kịp. Ảnh hưởng cách tính hiệu quả cải tiến |
| 2 | **Ai làm bước nào** — コンペ担当 / コンサルタント / クリエイター | Không biết cải tiến nhắm vào ai |
| 3 | **Thời lượng của mạch A**（提案書作成そのもの）| Không biết survey chiếm bao nhiêu phần trong khung |
| 4 | **「サーベイの提案」mất bao lâu** | Là bước Vis nêu **đầu tiên** ở Q10 nhưng không có số |
| 5 | **「提案書への落とし込み」mất bao lâu** | Là công đoạn ta muốn cải tiến |
| 6 | **Luồng 申込 gồm những bước gì** | Đang khảo sát（memo ghi 調査中）|
| 7 | **「セイル」là gì** | Xuất hiện ở [407], không được định nghĩa |
| 8 | **「PS」là gì** | Xuất hiện ở [348][349][351]（PS全体 / PS期間中 / PS化）, không được định nghĩa. Là chỉ số Vis dùng để đo đóng góp của nurturing |

---

# Tóm tắt cho việc thiết kế cải tiến

**Điều chắc chắn có trong tài liệu:**

1. Khung là **3–4 tuần**（[382] và cả Q1, Q10 đều xác nhận）
2. Chuỗi WDS phần được ghi số là **6 tuần**（[403]–[406]，nhưng là 参考値）
3. Vis nêu **ba** việc phải làm trong khung: サーベイの提案 / 実施 / 提案書への落とし込み（Q10）
4. Trong ba việc đó, **chỉ 実施 có số**; hai đầu không có
5. 事業計画 tự cho rằng cả hai 課題 họ liệt kê **đã có lời giải**（URL形式 + 早期実施）

**Điều nên hỏi Vis trước khi báo effort:**

- Luồng 申込 hiện tại gồm những bước nào, ai xác nhận, mất bao lâu
- 「サーベイの提案」thực tế mất bao lâu, khó ở chỗ nào
- 「提案書への落とし込み」thực tế mất bao lâu
- Mạch A và mạch B chạy song song hay nối tiếp
- 「セイル」và「PS」nghĩa là gì
