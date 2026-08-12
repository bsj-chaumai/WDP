# Phân tích tổng hợp — Từ câu trả lời của Vis đến hướng đề xuất

> **QUAN TRỌNG — đọc kèm `60-quy-trinh-wd-xd-va-before-after.md`.**
> Sau khi đọc toàn văn 事業計画, có **5 điểm trong tài liệu này cần hiệu chỉnh**:
> 1. Q8「申込・規約」**không phải backlog** — nó chiếm 2/6 tuần trên critical path
> 2. URL配信 chỉ giải một phần lead time（còn 申込 2w + 結果 2w）
> 3. **座談会 đã tồn tại** như kênh worker voice（thủ công, 10 người）→ nên nói "số hóa", không nói "thêm mới"
> 4. Chu kỳ đo After **đã được định nghĩa: nửa năm**
> 5. KPI là **3 mục**（XD đầy đủ）/ 2 mục（MVP）
>
> Ngoài ra: FY2026 WDP theo kế hoạch vẫn là **After spot**, subscription là FY2027–2028.

Tài liệu gộp toàn bộ dữ liệu và lập luận, để làm cơ sở cho 提案.

**Nguồn dữ liệu:**

1. `ヴィス質問票.xlsx` — 10 câu hỏi BS gửi, Vis đã trả lời
2. `ワークデザインサーベイ.json` — 52 câu, `createdAt` = 2024-10-25
3. `ワークデザインサーベイ（パルス）.json` — 19 câu, `createdAt` = 2025-01-09
4. `サーベイ結果画面.png` — màn hình kết quả survey trên WDP
5. 『ヴィスの現状と今後について』(WDP XD事業計画 / 小川 慧 / 2025-12-26)
6. Ghi âm họp với Vis (xem `11-meeting-notes.md`)

---

# PHẦN 1 — Câu hỏi và câu trả lời của Vis

## Q1. Khó khăn khi đưa kết quả WDS vào 提案

**質問:** 提案までの3〜4週間のなかで、WDSの結果を提案に反映する際、現在いちばんお困りの点はどのようなことでしょうか。※URL配信後も残っている課題があれば、あわせてお聞かせください。

**Vis回答:**
> サーベイ結果と提案が未接続。サーベイ結果をしっかり落とし込んだオフィス提案が難しい

**Tiếng Việt:** Kết quả survey và đề xuất chưa kết nối. Khó đưa kết quả survey vào đề xuất office một cách chắc chắn.

---

## Q2. Ngoài survey, cần gì để tăng 勝率

**質問:** サーベイ結果を提案根拠としてご活用いただく以外に、勝率をさらに高めるために必要と感じられているものはございますでしょうか。

**Vis回答:** *(chưa trả lời)* — hỏi ngược: 「ここでいう勝率とは何を指していますか？」

**Trạng thái:** Còn treo. Cần định nghĩa 勝率 rồi hỏi lại.

---

## Q3. Lý do thắng hợp đồng có phí

**質問:** 有料契約を獲得できた主な理由は何でしょうか。また、お客様はどの点に価値を感じてくださったでしょうか。

**Vis回答:**
> 最初から有料のafterサーベイの金額も踏まえて効果検証を訴求したこと。オフィスプロジェクトの効果を数値化するというコンセプトに価値を感じてもらった

**Tiếng Việt:** Ngay từ đầu đã đưa cả giá after survey có phí vào và nhấn mạnh 効果検証. Khách thấy giá trị ở concept "số hóa hiệu quả của dự án office".

---

## Q4. End-client ưu tiên điều gì

**質問:** エンドのお客様にとって、現時点でより重要と感じられているのはどちらでしょうか。A. 移転後に自走できること / B. Before→Afterで効果を確認できること

**Vis回答:**
> B. Before→Afterで効果を確認できること

---

## Q5. Mức độ thực hiện After

**質問:** After（移転後の効果測定）は、現在どの程度実施できていらっしゃいますでしょうか。

**Vis回答:**
> before 83件に対し after 5件（2025年度実績）

---

## Q6. Tình trạng độc lập アプリ

**質問:** WDPとは別の独立アプリについて、すでに開発は始まっておりますでしょうか。差し支えなければ、開発主体と想定時期もお教えください。

**Vis回答:**
> AIレポート機能のキックオフ段階。2026/10の完成目処。

---

## Q7. Bối cảnh 見送り của AIレポート

**質問:** AIレポート／AIアドバイスについて、見送られた、またはご検討中の背景と、今後の優先度、現時点で課題となっている点があればお聞かせください。

**Vis回答:**
> 社内AIツールで完結できる可能性があるためブレイブさんとの開発は見送り。スローペースながらも上記の通り進行中

---

## Q8. Cải thiện WDP mà コンペ／コンサル mong muốn

**質問:** コンペご担当者様やコンサルタントの方々が、WDPに対していちばん求めていらっしゃる改善点は何でしょうか。

**Vis回答:**
> 人員計画を踏まえたレイアウト構成を作成できる、WDP上で申込みや規約の確認が完結する仕組み、クライアントごとのサーベイカスタム機能等

**BS内部メモ（シート E9）:**
> ヴィスの提案の付加価値として利用するものと、定点的にお客様が継続利用するものの内容を分けたほうが良いかもしれない

---

## Q9. Thứ tự ưu tiên kỳ này

**質問:** 今期、特に先に強化したい項目について、優先順位をお教えいただけますでしょうか。（提案スピード／Before→After／レポート工数の削減／有料化）

**Vis回答:**
> ① 有料化
> ② レポート工数の削減（AIレポートの領域）
> ③ Before→After
> ④ 提案スピード

---

## Q10. Loại lead time nào dài

**質問:** 「リードタイムが長い」と感じていらっしゃる場合、対象は次のどちらに近いでしょうか。A. 提案準備の期間（3〜4週間）/ B. 利用から受注・売上までの期間

**Vis回答:**
> WDP単体のリードタイムは長くない。どちらかというとオフィス提案準備の3-4週間の中でサーベイの提案、実施、提案書への落とし込みまでを行う時間が足りない

---

# PHẦN 2 — Nội dung 2 bộ survey

## 2.1 ワークデザインサーベイ — 52 câu

### Thông tin người trả lời (Q1–Q4)

| # | 日本語 | Tiếng Việt | Lựa chọn |
|---|---|---|---|
| 1 | 現在の会社（組織）に在籍して何年目ですか | Đã làm ở công ty hiện tại bao lâu | <1年 / 1–3 / 3–5 / 5–10 / 10–15 / 15年以上 / 回答しない |
| 2 | 該当する年代をお選びください | Nhóm tuổi | <20 / 20–30 / 30–40 / 40–50 / 50以上 / 回答しない |
| 3 | 性別について教えてください | Giới tính | 男性 / 女性 / 回答しない |
| 4 | 所属する部署の職種をお選びください | Loại công việc của bộ phận | 15 nghề + 該当なし（複数選択） |

### Không gian / プレイス (Q5–Q15)

| # | 日本語 | Tiếng Việt | Lựa chọn |
|---|---|---|---|
| 5 | 今のオフィス環境に満足していますか | Hài lòng với môi trường văn phòng hiện tại | 満足〜満足していない 5段階 |
| 6 | 集中できる場所に満足していますか | Hài lòng với không gian tập trung | 5段階 |
| 7 | チームで働く場所に満足していますか | Hài lòng với không gian làm việc nhóm | 5段階 |
| 8 | 他部署・他部門とランダムに交流できる場所に満足していますか | Hài lòng với không gian giao lưu ngẫu nhiên liên bộ phận | 5段階 |
| 9 | ネットワーク環境に満足していますか | Hài lòng với môi trường mạng | 5段階 |
| 10 | オフィス環境は自社のブランドを反映していると思いますか | Văn phòng có phản ánh thương hiệu công ty | そう思う 5段階 |
| 11 | オンラインMTGは不具合なく実施できていると思いますか | Họp online diễn ra không sự cố | 5段階 |
| 12 | 様々な職種の特性を捉えた環境作りをされていると思いますか | Môi trường phù hợp đặc thù nhiều loại công việc | 5段階 |
| 13 | プロジェクト進行・所属者・イベントが自然とわかる環境や仕組みがあると思いますか | Có cơ chế giúp tự nhiên nắm được tiến độ, thành viên, sự kiện | 5段階 |
| 14 | 創発的な意見を出し合えたり、インスピレーションを感じられる場所があると思いますか | Có nơi trao đổi ý tưởng, tạo cảm hứng | 5段階 |
| 15 | 今のオフィスに魅力や愛着を感じていますか | Cảm thấy văn phòng hấp dẫn, gắn bó | 感じる 5段階 |

### Cách làm việc / スタイル (Q16–Q20)

| # | 日本語 | Tiếng Việt | Lựa chọn |
|---|---|---|---|
| 16 | 直近1週間で、下記の場所で働いた割合 | Tỷ lệ thời gian làm việc theo địa điểm trong tuần | オフィス / 自宅 / サテライト・シェア / 出張先 / 外出先 / その他 — nhập số, tổng 100 |
| 17 | 仕事を進める上で不足を感じる場所（複数選択） | Không gian còn thiếu khi làm việc | 来客用会議室 / 社内会議室 / オープンMTG / ベースワークスペース / チーム作業 / リフレッシュ / 集中 / オンラインブース / イベント / 荷物収納 / 該当なし |
| 18 | 会社で設定されている働き方に働きやすさを感じますか | Cách làm việc công ty quy định có thuận tiện | 感じる 5段階 |
| 19 | 現リモートワーク体制は仕事を効率化していると思いますか | Cơ chế remote hiện tại có tăng hiệu quả | そう思う 5段階 |
| 20 | 会社のデジタル化の推進度に満足していますか | Hài lòng với mức độ chuyển đổi số | 満足 5段階 |

### Giao tiếp / tổ chức (Q21–Q30)

| # | 日本語 | Tiếng Việt | Lựa chọn |
|---|---|---|---|
| 21 | 仕事上で十分な量のコミュニケーションが取れていると思いますか | Có đủ lượng giao tiếp trong công việc | そう思う 5段階 |
| 22 | 必要だと思う人たちとコミュニケーションが取れていると思いますか | Giao tiếp được với người cần thiết | 5段階 |
| 23 | 社内コミュニケーションで齟齬なく伝わっていると思いますか | Thông tin nội bộ truyền đạt không sai lệch | 感じる 5段階 |
| 24 | 会社は短期課題より長期的な目的改善を目指していると感じますか | Công ty ưu tiên mục tiêu dài hạn hơn ngắn hạn | 感じる 5段階 |
| 25 | 解決すべき課題に対してすぐに解決を図っていると感じますか | Công ty xử lý vấn đề nhanh chóng | 感じる 5段階 |
| 26 | 得た知識や技術を会社やチームと共有しあっていると感じますか | Kiến thức, kỹ năng được chia sẻ | 感じる 5段階 |
| 27 | 会社は多様性に対して積極的に取り組んでいると思いますか | Công ty chủ động về đa dạng | そう思う 5段階 |
| 28 | 予定されていない交流をする機会が多いと感じますか | Có nhiều cơ hội giao lưu ngẫu nhiên | 感じる 5段階 |
| 29 | 信頼関係や帰属意識は対面とオンラインどちらで高まりますか | Tin tưởng, gắn bó tăng nhờ gặp trực tiếp hay online | 実際に集まる〜オンライン 5段階 |
| 30 | 下記の作業について、直近1週間の時間割合 | Tỷ lệ thời gian theo loại công việc | 高集中 / 単純 / チーム / 社内MTG / 社外MTG / 休憩 / 移動 — nhập số, tổng 100 |

### Văn hóa / カルチャー (Q31–Q37)

| # | 日本語 | Tiếng Việt | Lựa chọn |
|---|---|---|---|
| 31 | 所属企業への入社を友人・知人・家族にどの程度勧めたいですか | Mức độ muốn giới thiệu người thân vào công ty (eNPS) | 0〜10 |
| 32 | 会社の習慣は働きやすさを向上させていると思いますか | Tập quán công ty giúp làm việc thuận tiện | そう思う 5段階 |
| 33 | 会社は勉強する機会やきっかけを設けていますか | Công ty tạo cơ hội học tập | 設けている 5段階 |
| 34 | 会社の企業文化は居心地がいいと感じますか | Văn hóa doanh nghiệp thoải mái | 感じる 5段階 |
| 35 | リーダーシップやフォロワーシップを発揮する人は十分にいると感じますか | Đủ người thể hiện lãnh đạo / hỗ trợ lãnh đạo | 感じる 5段階 |
| 36 | 会社は社会課題の解決に取り組み、社会貢献していると思いますか | Công ty đóng góp xã hội | そう思う 5段階 |
| 37 | 企業風土が持つ特徴（複数選択） | Đặc điểm văn hóa tổ chức | トップダウン / ボトムアップ / 挑戦的 / 保守的 / 多様性に寛大 / イノベーティブ / クライアント重視 / 社員重視 / 該当なし |

### Well-being / 心理的安全性 (Q38–Q45)

| # | 日本語 | Tiếng Việt | Lựa chọn |
|---|---|---|---|
| 38 | 安心して自分の意見や考えを発言できますか | Có thể an tâm phát biểu ý kiến | できる 5段階 |
| 39 | 良好な人間関係の輪の中にいると思いますか | Đang ở trong quan hệ tốt | そう思う 5段階 |
| 40 | 身体的に健康に働けていると思いますか | Làm việc với thể chất khỏe mạnh | そう思う 5段階 |
| 41 | 安心感や安らぎを感じていますか | Cảm thấy an tâm, thư thái | 感じる 5段階 |
| 42 | 上機嫌でいられている日が多いと感じますか | Thường có tâm trạng tốt | 感じる 5段階 |
| 43 | 会社に誇りを持って働けていると思いますか | Làm việc với niềm tự hào | そう思う 5段階 |
| 44 | 会社の将来の方向性について共感をしていますか | Đồng cảm với định hướng tương lai | 共感 5段階 |
| 45 | メンバーたちは会社と同じ方向を向いていると感じますか | Thành viên cùng hướng với công ty | 感じる 5段階 |

### やりがい / tự thực hiện (Q46–Q52)

| # | 日本語 | Tiếng Việt | Lựa chọn |
|---|---|---|---|
| 46 | 仕事に熱中して取り組めていると思いますか | Say mê với công việc | そう思う 5段階 |
| 47 | キャリアパスを考えた時に現状の仕事はマッチしていると思いますか | Công việc phù hợp định hướng nghề nghiệp | そう思う 5段階 |
| 48 | 感謝や御礼の言葉をもらうことは日常的にありますか | Thường nhận lời cảm ơn | ある 5段階 |
| 49 | 仕事の成果が認められたと感じることは日常的にありますか | Thành quả được công nhận | ある 5段階 |
| 50 | 仕事を進める上で充実感を感じることは日常的にありますか | Cảm thấy thỏa mãn khi làm việc | ある 5段階 |
| 51 | 失敗や挑戦に恐れず新しいことに取り組めていると感じますか | Dám thử điều mới, không sợ thất bại | 感じる 5段階 |
| 52 | 仕事において自己実現をできていると感じますか | Thực hiện được bản thân trong công việc | 感じる 5段階 |

## 2.2 ワークデザインサーベイ（パルス）— 19 câu

| # | 日本語 | Tiếng Việt | Lựa chọn | Tương ứng bản 52 |
|---|---|---|---|---|
| 1 | 在籍して何年目ですか | Số năm làm việc | 7 lựa chọn | = Q1 |
| 2 | 年代をお選びください | Nhóm tuổi | 6 lựa chọn | = Q2 |
| 3 | 性別について教えてください | Giới tính | 3 lựa chọn | = Q3 |
| 4 | 所属する部署の職種 | Loại công việc | 15 + 該当なし | = Q4 |
| 5 | 今のオフィス環境に満足していますか | Hài lòng với văn phòng | 満足 5段階 | = Q5 |
| 6 | 今のオフィスに魅力や愛着を感じていますか | Hấp dẫn, gắn bó | 感じる 5段階 | = Q15 |
| 7 | 直近1週間で働いた場所の割合 | Tỷ lệ nơi làm việc | 6 mục, tổng 100 | = Q16 |
| 8 | 設定されている働き方に働きやすさを感じますか | Cách làm việc thuận tiện | 感じる 5段階 | = Q18 |
| 9 | 十分な量のコミュニケーションが取れていると思いますか | Đủ lượng giao tiếp | そう思う 5段階 | = Q21 |
| 10 | 直近1週間の作業別時間割合 | Tỷ lệ theo loại công việc | 7 mục, tổng 100 | = Q30 |
| 11 | 入社をどの程度勧めたいと思いますか | eNPS | 0〜10 | = Q31 |
| 12 | 企業文化はあなたに合っていますか | Văn hóa có hợp với bạn | そう思う 5段階 | ≈ Q34（biến thể）|
| 13 | リーダーシップやフォロワーシップを発揮する人は十分にいると感じますか | Đủ người lãnh đạo / hỗ trợ | 感じる 5段階 | = Q35 |
| 14 | 健康的に働けていますか | Làm việc khỏe mạnh | そう思う 5段階 | ≈ Q40（rút gọn）|
| 15 | 安心して自分の意見や考えを発言できますか | An tâm phát biểu | できる 5段階 | = Q38 |
| 16 | 企業ビジョンに対して共感していますか | Đồng cảm với tầm nhìn | そう思う 5段階 | ≈ Q44（biến thể）|
| 17 | キャリアパスと現状の仕事はマッチしていると思いますか | Công việc hợp career | そう思う 5段階 | = Q47 |
| 18 | 今の仕事にやりがいを感じますか | Công việc có ý nghĩa | 感じる 5段階 | ≈ Q50（biến thể）|
| 19 | 仕事の成果が認められたと感じることは日常的にありますか | Thành quả được công nhận | ある 5段階 | = Q49 |

### Đặc điểm cấu trúc

- Pulse là **bản rút gọn** của bản 52, giữ nguyên 属性 Q1–4.
- Mỗi trục chỉ giữ **1–2 câu đại diện**.
- **4 câu là biến thể chữ khác** (pulse Q12, Q14, Q16, Q18) → **không map 1:1 tuyệt đối** với bản 52.
  Cần lưu ý khi so sánh Before/After giữa hai bộ.

---

# PHẦN 3 — Phân tích theo từng luận điểm

Mỗi luận điểm trình bày theo: **Dữ kiện → Suy luận → Kết luận**.

## Luận điểm 0 — Hai service của Vis quyết định cách đọc toàn bộ dữ liệu

Đây là luận điểm nền, cần đọc trước các luận điểm còn lại.

**Dữ kiện — hai service Vis đang cung cấp**

| | WORKPLACE DESIGN (WD) | EXPERIENCE DESIGN (XD) |
|---|---|---|
| Nội dung | 空間プログラミング / デザイン / クリエイト・アップデート | ビジョン策定 / 企画 / 運営 |
| Survey dùng để làm gì | **根拠 cho 提案** | **効果検証 Before→After** |
| Thời điểm | Trước khi chốt dự án (cửa sổ 3〜4週間) | Sau renewal, lặp lại |
| Tính chất doanh thu | **Gián tiếp** — tăng 受注率 | **Trực tiếp** — có phí, 継続 |
| Hiện ai vận hành | Consultant / コンペ担当 | **Consultant phụ trách** |
| Đích tương lai | Vẫn cần người | **WDP thay consultant → 自走・商用化** |

Trong 事業計画 Vis cũng viết đúng cấu trúc này:

> ヴィスは**労働集約型**のワークプレイスデザインと**持続型**のエクスペリエンスデザインの2本柱で

**Suy luận**

Các pain trong bảng câu hỏi thuộc **hai service khác nhau**, không phải cùng một vấn đề:

| Câu trả lời | Thuộc service | Bản chất |
|---|---|---|
| Q1（サーベイ結果と提案が未接続）| **WD** | Survey → 提案 |
| Q10（3-4週間で時間が足りない）| **WD** | Tốc độ trong cửa sổ đề xuất |
| Q3（有料は after + 数値化で獲得）| **XD** | Mô hình bán có phí |
| Q4（end-client ưu tiên Before→After）| **XD** | Giá trị khách cần |
| Q5（before 83 / after 5）| **XD** | Năng lực vận hành |

**Kết luận**

1. **Không thể giải cả hai bằng một giải pháp.** WD cần *nhanh và nối được vào提案*. XD cần *bán được và vận hành lặp lại*.
2. Đây chính là nội dung ghi chú nội bộ ở Q8 — tách **ヴィスの提案の付加価値（WD）** và **定点的にお客様が継続利用するもの（XD）**. Hai lớp đó đã có tên thật là WD và XD.
3. Trong 提案, nên gắn nhãn rõ mỗi giải pháp thuộc **WD** hay **XD**, để không lẫn giữa "giúp thắng đề xuất" và "tạo doanh thu継続".

## Luận điểm 0b — Vì sao 5/83 gắn với việc XD phụ thuộc consultant

**Dữ kiện**

- After thuộc **XD**
- XD là service **mới ra mắt**, hiện **do consultant phụ trách**
- WD chạy khoảng **500 dự án/năm** (事業計画), WDS đang khoảng **10 件/月**
- Vis kỳ vọng tương lai: WDP thương mại hóa để doanh nghiệp **自走**, không cần consultant

**Suy luận**

- Survey Before phục vụ WD → gắn vào luồng 提案 vốn đã có khối lượng lớn → dễ nhân rộng
- After phục vụ XD → phụ thuộc **số consultant và năng lực từng người** → bị giới hạn bởi **con người**, không phải bởi tính năng

**Kết luận**

Muốn After tăng, **không đủ** nếu chỉ làm chức năng After dễ dùng hơn. Phải **giảm phần việc buộc phải có consultant**.

Đây là cách phát biểu lại mục tiêu 自走 của Vis dưới dạng bài toán kỹ thuật:

> Consultant đang làm gì bằng tay trong XD, và phần nào có thể encode vào WDP?

## Luận điểm 0c — Căng thẳng giữa 自走 và nhu cầu hiện tại

**Dữ kiện**

| Nguồn | Nội dung |
|---|---|
| Kỳ vọng của Vis | WDP thương mại hóa để doanh nghiệp **自走**, không cần consultant |
| Q4 | End-client ưu tiên **B. Before→After**, **không** phải A. 自走 |
| 事業計画 | FY2026 = **検証（MVP）** phase |

**Suy luận**

Đây không phải mâu thuẫn để bác bỏ, mà là **vấn đề thứ tự**:

- **Ngắn hạn:** bán **効果検証** — đó là thứ khách đang thực sự trả tiền (Q3)
- **Dài hạn:** 自走 / SaaS là cấu trúc để scale mà không phải tăng số consultant

**Kết luận**

- **Rủi ro nếu làm sai thứ tự:** đề xuất một WDP self-service ngay bây giờ → khách chưa cần 自走, Vis chưa có case 継続 để chứng minh → không bán được.
- **Cách trình bày an toàn trong 提案:** 自走 **không** phải tính năng bán cho khách, mà là **kết quả** của việc chuẩn hóa công việc consultant vào WDP.

## Luận điểm 1 — Con số 83/5 nói lên điều gì

**Dữ kiện**

| Nguồn | Nội dung |
|---|---|
| Q4 | End-client ưu tiên **Before→After** |
| Q3 | Hợp đồng có phí thắng nhờ **bán after + số hóa hiệu quả** |
| Q5 | Thực tế chỉ **After 5 / Before 83** |

**Suy luận**

Nếu 効果検証 không có giá trị:
- khách đã không xếp nó là ưu tiên (nhưng Q4 nói ngược lại)
- khách đã không trả tiền cho nó (nhưng Q3 nói ngược lại)

Vậy nhu cầu **có**, giá trị **đã được chứng minh**, nhưng thực thi **không chạy**.

**Kết luận**

Nghẽn nằm ở **khoảng giữa** — tức là ở khâu bán, vận hành, follow-up — **không phải** ở giá trị sản phẩm.

**Không nên** đặt giả thuyết "so sánh Before/After không hiệu quả nên khách không dùng". Dữ liệu bác bỏ điều đó.

**Các khả năng cần kiểm chứng**

1. After không được đưa vào báo giá ngay từ đầu (case thành công thì có — Q3)
2. Sau khi bàn giao office, mất người phụ trách follow-up
3. Quy trình After nặng: tạo lại survey, phát hành, thu hồi, phân tích, làm báo cáo
4. Doanh nghiệp ngại bắt nhân viên trả lời lại 52 câu
5. Kết quả After không dẫn tới hành động cụ thể → khách không thấy lý do làm tiếp
6. Chưa chuẩn hóa thời điểm đo After (sau 1 / 3 / 6 tháng?)

## Luận điểm 2 — "Chưa nối" và "không đủ thời gian" là hai vấn đề khác nhau

**Dữ kiện**

| Câu hỏi | Vis trả lời | Bản chất |
|---|---|---|
| Q1 — khó nhất khi đưa WDS vào 提案 | サーベイ結果と提案が**未接続** | Đã có kết quả rồi vẫn khó → vấn đề **nội dung** |
| Q10 — lead time nào dài | WDP単体は長くない、3-4週間で**時間が足りない** | Vấn đề **thời gian / quy trình** |

**Suy luận**

Đây là hai câu hỏi riêng, hai câu trả lời riêng, mô tả hai hiện tượng khác nhau:

- Q1: khó **biến kết quả thành đề xuất**
- Q10: **không kịp chạy hết chu trình** trong cửa sổ 3–4 tuần

**Kết luận**

- Chỉ làm survey nhanh hơn → vẫn còn vấn đề Q1
- Chỉ cải thiện nội dung → vẫn không kịp 3–4 tuần

**Phải giải cả hai.** Đây là lý do đề xuất cần tách rõ hai nhánh: *tốc độ quy trình* và *chuyển kết quả thành đề xuất*.

## Luận điểm 3 — Survey đo được "bao nhiêu" nhưng không nắm được "vì sao / ở đâu"

**Dữ kiện đếm từ file JSON**

| Chỉ số | Giá trị |
|---|---|
| Tổng câu bản đầy đủ | 52 |
| Câu dạng thang 5 mức hoặc chọn sẵn | 49 |
| Câu hỏi về "thiếu không gian nào" | 1 (Q17, checkbox 10 lựa chọn) |
| Câu nhập số (tỷ lệ %) | 2 (Q16, Q30) |
| **Câu tự do (free text)** | **0** |

Màn hình kết quả trả về dạng điểm số: `ワークデザインスコア 58.0pt`, `プレイス 63.0`, `スタイル 60.2`, `カルチャー 59.2`, `eNPS -65.2`.

**Suy luận**

Từ "プレイス 63 điểm", consultant **không** biết được:
- Khu vực nào trong văn phòng có vấn đề
- Nguyên nhân là gì (ồn / thiếu chỗ / thiết bị / privacy / ánh sáng)
- Xảy ra vào thời điểm nào
- Nên sửa cụ thể cái gì

Consultant buộc phải **tự suy đoán** để viết đề xuất.

**Kết luận**

Chính khoảng trống này **là** cái Vis mô tả bằng từ 「未接続」ở Q1.

Nhận định này không phải cảm tính — nó nối trực tiếp **cấu trúc dữ liệu của survey** với **câu trả lời Q1 của khách**.

## Luận điểm 4 — Worker không có kênh nói cụ thể

**Dữ kiện**

Trong cả hai file JSON (52 câu + 19 câu), **không có** trường nhập text tự do. Chỉ có:
- radiogroup (chọn 1)
- checkbox (chọn nhiều)
- text với `inputType: number` (nhập số cho Q16, Q30)

**Kết luận**

Nhận định của bạn là **đúng và là fact**: worker hiện **không có chỗ** để mô tả 不満 cụ thể, đề xuất cải thiện, hay chia sẻ tình huống thực tế.

Đây là khoảng trống rõ ràng nhất, và cũng là nguồn dữ liệu mà consultant đang thiếu để viết đề xuất.

## Luận điểm 5 — Pulse đã tồn tại, nên vấn đề không nằm ở công cụ

**Dữ kiện**

| File | `createdAt` | Ngày |
|---|---|---|
| ワークデザインサーベイ (52 câu) | 1729839740 | 2024-10-25 |
| ワークデザインサーベイ（パルス）(19 câu) | 1736406861 | 2025-01-09 |

**Suy luận**

Vis **đã tự tạo** bộ pulse rút gọn sau bản đầy đủ khoảng 2 tháng rưỡi → họ **đã nghĩ đến việc đo định kỳ**.

Nhưng số liệu After vẫn chỉ 5/83 (FY2025).

**Kết luận**

Vấn đề **không phải "thiếu tính năng pulse"**, mà là **chưa có mô hình bán và vận hành định kỳ**.

**Hệ quả cho đề xuất:** không đề xuất build lại thứ đã có. Nên đề xuất phần **vận hành, kết nối, và hành động sau khi đo**.

## Luận điểm 6 — Rủi ro về quan hệ nhân quả

**Dữ kiện**

- Q3: giá trị bán được là 「**オフィスプロジェクトの効果**を数値化」
- Nhưng survey đo cả: văn hóa công ty (Q32–37), career (Q47), quan hệ con người (Q39), sức khỏe (Q40), tầm nhìn công ty (Q44)

**Suy luận**

Những mục này chịu ảnh hưởng bởi quản lý, nhân sự, khối lượng công việc, biến động tổ chức — **không phải do office quyết định**.

Khi điểm After thay đổi, khó khẳng định "nhờ dự án office".

**Kết luận**

Đây là **rủi ro cho chính lời chào bán có phí**. Khi bán gói 効果検証 cần:
- Chọn **KPI mục tiêu gắn với office**
- Tách rõ chỉ số nào office ảnh hưởng trực tiếp, chỉ số nào là bối cảnh

**Điểm tựa quan trọng:** Vis **đã tự nghĩ tới điều này**. XD MVP trong 事業計画 ghi:

> 目標設定のターゲットとする**サーベイの項目を2個選択**し、スコアのゴール設定も行います

Nghĩa là XD chỉ chọn **2 mục** làm KPI, không đo cả 6 trục.

→ Đề xuất của BS về việc chọn KPI gắn office **không phải ý tưởng mới lạ**, mà là **hệ thống hóa đúng thứ Vis đã định làm bằng tay**. Đây là cách trình bày dễ được chấp nhận nhất.

---

# PHẦN 3b — Việc của consultant trong XD: phần nào encode được vào WDP

Đây là phần cụ thể hóa Luận điểm 0b. Nếu đích của Vis là "WDP thay consultant trong XD", thì phải bóc tách từng việc consultant đang làm.

**XD MVP trong 事業計画 gồm:**

1. Before/After 効果検証
2. アブストラクションラダー workshop
3. Chốt tối thiểu **2 kế hoạch event** sau renewal
4. Chọn **2 mục tiêu survey** + đặt goal điểm số
5. Event follow + báo cáo cuối

**Đánh giá khả năng encode:**

| Việc của consultant | Encode vào WDP? | Ghi chú |
|---|---|---|
| Chọn 2 mục tiêu survey + set goal | **Được** — gợi ý theo điểm thấp và loại dự án | Đồng thời giải rủi ro nhân quả (Luận điểm 6) |
| Đọc điểm số → xác định vấn đề | **Được** — nhưng cần Worker Voice làm dữ liệu đầu vào | Đây chính là Survey-to-Proposal |
| Đề xuất event / hành động cải thiện | **Một phần** — thư viện phương án theo loại vấn đề | Không thay thế hoàn toàn |
| Điều phối workshop | **Khó** — cần người | Giữ cho consultant |
| Làm báo cáo | Vis đang tự làm AIレポート | **Ngoài scope BS**（Q6, Q7）|
| Theo dõi và đo lại định kỳ | **Được** — pulse + nhắc lịch + so sánh | Đây là chỗ gắn 継続課金 |

**Nguyên tắc phân chia:**

- **BS nhận:** phần việc **lặp lại và có quy tắc**
- **Giữ cho consultant:** phần **workshop và tư vấn sâu**

→ Cách này vừa tiến tới mục tiêu 自走 của Vis, vừa không đòi hỏi thay thế consultant ngay lập tức.

---

# PHẦN 4 — Năm vấn đề cốt lõi

Mỗi vấn đề được gắn nhãn thuộc **WD** hay **XD** theo Luận điểm 0.

## Core 1 — 有料化 chưa thành quy trình lặp lại được 〔XD〕

**Cơ sở:** Q9①（ưu tiên số 1）+ Q3（đã có case thắng）+ Q5（5/83）

**Câu hỏi trung tâm:**
> Làm sao biến 効果検証 từ "option bán được trong vài case" thành **gói tiêu chuẩn** bán và vận hành lặp lại?

## Core 2 — Survey đo "mức độ" nhưng chưa đủ để tạo đề xuất 〔WD + XD〕

**Cơ sở:** Q1（未接続）+ cấu trúc JSON（49/52 câu là thang điểm, 0 câu tự do）

**Câu hỏi trung tâm:**
> Làm sao chuyển từ **điểm số** sang **insight** rồi sang **phương án office / XD cụ thể**?

Vấn đề này xuất hiện ở **cả hai** service: WD cần insight để viết 提案, XD cần insight để đề xuất hành động cải thiện.

## Core 3 — Quy trình survey không vừa cửa sổ 3–4 tuần 〔WD〕

**Cơ sở:** Q10

**Câu hỏi trung tâm:**
> Bước nào trong chuỗi dưới đây chiếm nhiều thời gian nhất, và bước nào có thể chuẩn hóa hoặc tự động hóa?

```text
Đề xuất survey → Khách duyệt → Chuẩn bị danh sách → Phát hành
→ Thu hồi → Phân tích → Tạo insight → Đưa vào 提案書
```

## Core 4 — Before/After chưa tạo vòng cải tiến liên tục 〔XD〕

**Cơ sở:** Q5（After 5件）+ pulse đã tồn tại nhưng chưa gắn 有料

**Hiện trạng có nguy cơ:**
```text
Before → Office project → After → Báo cáo → Kết thúc
```

**Mô hình cần cho 有料化:**
```text
Baseline survey → Đề xuất → Cải thiện → Pulse định kỳ
→ Phát hiện vấn đề → Hành động → Đo lại
```

**Câu hỏi trung tâm:**
> Sau khi có kết quả After, khách có **lý do gì** để tiếp tục trả tiền cho lần đo tiếp theo?

## Core 5 — XD bị giới hạn bởi số consultant 〔XD〕

**Cơ sở:** XD hiện do consultant phụ trách + Vis kỳ vọng WDP thay consultant（自走・商用化）+ Q5（5/83）

**Câu hỏi trung tâm:**
> Trong công việc XD của consultant, phần nào **lặp lại và có quy tắc** để encode vào WDP, phần nào **bắt buộc cần người**?

Chi tiết phân tích: xem PHẦN 3b.

**Lưu ý về thứ tự（Luận điểm 0c）:** 自走 là **đích cấu trúc**, không phải điểm bán ngắn hạn. Ngắn hạn vẫn bán **効果検証**.

---

# PHẦN 5 — Hướng đề xuất

## Hướng 1 — Worker Voice: bổ sung "vì sao / ở đâu" 〔WD + XD〕

**Giải:** Core 2, Core 3（gián tiếp）, Core 5（cung cấp dữ liệu để encode phán đoán của consultant）

**Nguyên tắc:** không làm 52 câu chi tiết hơn cho tất cả mọi người — sẽ làm survey dài và giảm response rate.

**Cách làm — câu hỏi follow-up có điều kiện:**

- Khi chọn 不満 hoặc điểm thấp → hiện thêm câu hỏi đào sâu:
  - どの場所について不満がありますか（chọn khu vực / zone）
  - 具体的にどのような点ですか（ồn / thiếu chỗ / thiết bị / privacy / nhiệt độ / đặt chỗ）
  - 仕事にどのような影響がありますか
- Thêm **自由記述** (free text) cho ý kiến cải thiện
- Có thể gắn **layout map** để worker chỉ trực tiếp vị trí

**Lợi ích:** thu được dữ liệu cụ thể mà **không** làm dài survey cho người không có vấn đề.

## Hướng 2 — Survey-to-Proposal: nối kết quả với đề xuất 〔WD chính, XD phụ〕

**Giải:** Core 2（trực tiếp giải Q1「未接続」）, Core 5

**Luồng:**
```text
Điểm thấp → Nguyên nhân từ worker → Mức ưu tiên
→ Giải pháp layout / XD tương ứng → Block nội dung xuất vào 提案書
```

**Ví dụ:**
```text
集中スペース満足度 thấp
+ thiếu booth（Q17）
+ ảnh hưởng online meeting（Q11）
→ Đề xuất: số lượng booth / zoning / chính sách đặt chỗ
```

## Hướng 3 — Chuẩn hóa quy trình trong 3–4 tuần 〔WD〕

**Giải:** Core 3

- Template survey theo loại dự án
- Phát hành URL ngay ở giai đoạn sớm (nurturing)
- Theo dõi response rate + tự động reminder
- Định nghĩa điều kiện đủ mẫu để phân tích sớm
- Dashboard insight tự động
- Export block nội dung sang 提案書
- Chuẩn hóa SLA từng bước

## Hướng 4 — Gói có phí: Before + After + Pulse 〔XD〕

**Giải:** Core 1, Core 4

| Thành phần | Nội dung |
|---|---|
| Baseline | WDS 52 câu |
| After | Đo lại các KPI mục tiêu đã chọn |
| Pulse | 19 câu hoặc câu chọn theo mục tiêu |
| Worker Voice | Follow-up + free text |
| Action review | Đề xuất hành động sau mỗi lần đo |

**Điểm mấu chốt:** giá trị có phí không phải "được dùng survey", mà là **継続的な効果検証と改善提案**.

**Lưu ý từ Luận điểm 6:** khi bán gói này, phải chọn **KPI gắn office** để hiệu quả quy được về dự án. Cách này khớp với XD MVP（サーベイ項目2個選択）.

## Hướng 5 — Chuẩn hóa công việc XD của consultant 〔XD〕

**Giải:** Core 5 — đây là con đường tiến tới mục tiêu 自走 của Vis mà không phủ nhận vai trò consultant.

Theo bảng ở PHẦN 3b, ưu tiên encode các phần sau vào WDP:

1. **Gợi ý chọn 2 KPI mục tiêu** theo loại dự án và điểm thấp
2. **Chu trình theo dõi định kỳ**: nhắc lịch pulse, so sánh với baseline, phát hiện lệch mục tiêu
3. **Thư viện phương án hành động** ứng với từng loại vấn đề (nền tảng cho việc đề xuất event)

Không đưa vào scope: **workshop điều phối**（cần người）và **AIレポート**（Vis tự làm）.

**Cách trình bày trong 提案:** không nói "thay thế consultant", mà nói **"consultantの判断を仕組みに落とす"** — giúp XD scale mà không phải tăng số người.

---

# PHẦN 6 — Thứ tự điều tra ưu tiên

Trước khi chốt nội dung 提案, cần xác minh các giả thuyết ở trên:

1. **Phân tích funnel 83 Before → 5 After**
   - After có nằm trong báo giá ban đầu không?
   - Dừng ở bước nào: không đề xuất / khách từ chối / đề xuất rồi không chạy?
2. **Phỏng vấn case có phí và case không chuyển sang After**
   - Vì sao case đó mua được?
   - Case khác khác gì?
3. **Đo lead time từng bước trong 3–4 tuần**
   - Bước nào lâu nhất?
4. **Xem consultant hiện chuyển điểm số thành 提案 như thế nào**
   - Thao tác tay ở đâu? Suy đoán ở đâu?
5. **Xác định dữ liệu worker còn thiếu**
   - Cần thêm gì để viết được đề xuất cụ thể?
6. **Sau đó mới quyết định**: sửa câu hỏi survey, sửa workflow, hay bổ sung chức năng

Chi tiết ブリーフ cho dev: xem `30-dev-survey-brief.md`.

---

# Kết luận

Không nên khóa vấn đề thành "survey chưa đủ chi tiết" ngay từ đầu. Giả thuyết tổng thể hợp lý hơn, dựa trên toàn bộ dữ kiện ở trên:

> **WDP đã đo được trạng thái, nhưng chưa thu đủ nguyên nhân, và chưa có quy trình chuyển kết quả thành đề xuất và hành động liên tục. Vì vậy After khó vận hành, và giá trị có phí chưa được tái lập.**

**Trục đề xuất:**

> **Worker Voice × Survey-to-Proposal × Before/After/Pulse による継続的な効果検証**

Ba phần này đồng thời giải quyết **survey**, **有料化**, và **kết nối với 提案** — đúng ba điều Vis xếp ưu tiên.

**Còn treo:** định nghĩa 勝率 ở Q2 (Vis hỏi ngược, chưa trả lời).
