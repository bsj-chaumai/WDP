# Đề xuất đồng hành WDP — bravesoft（開発パートナー → 開発・活用の顧問伴走）

> **Vai trò:** bravesoft — nhà phát triển chính hiện tại của WDP, định hướng quan hệ **cố vấn phát triển / đồng hành AI・コンサル活用**（không dừng ở 通常開発）  
> **Neo Vis:**  
> - Visの目指すところ = **コンサルティング売り上げをあげていくこと**  
> - WDPの目指すところ = **コンサルティング売り上げを上げるための一助となるツールにする**  
> **大目的 đã chốt（P0–P2）:**  
> ① 受注一助の拡大 ② Before→After / 有料・XD ③ AI活用の分析・コンサル ④ 提供工数↓・利用件数↑ ⑤ 長期協業（AI・コンサル）  
> **Nguồn phân tích:** docs 01–03 +『ヴィスの現状と今後について』+ sheet 目的 + Milestone  
> **Lưu ý:** Nhãn P0/P1/P2 và 松竹梅 là **đúc kết phía bravesoft** để đề xuất; số liệu gốc lấy từ tài liệu Vis.

---

## 【背景】ngắn — vì sao cần đổi cách hợp tác

| Hiện trạng | Ý nghĩa với bravesoft |
|------------|----------------------|
| Đầu tư hệ thống WDP **一定落ち着いている** → Vis muốn **コンサル活用へシフト** | Chỉ nhận ticket feature sẽ lệch kỳ vọng |
| Vis muốn **内製化**; kỳ vọng bravesoft **giá trị ngoài 通常開発** | Cần định vị **顧問伴走**（AI・コンサル領域） |
| WDP đã có **間接売上効果 ~1.46億** nhưng **有料 ~2**, **ショット型** | Product đã chứng minh 営業支援; chưa đủ cho năm **検証（MVP）** |
| Kỳ vọng rõ: **AI工数削減**調査見積、**AI分析PoC**（精度） | Đúng cửa để vào vai cố vấn, không chỉ code |

**Định vị đề xuất:**  
bravesoft không đề xuất “làm thêm nhiều chức năng”.  
Đề xuất **cách chọn việc + PoC + enablement** để WDP trở thành **一助** thực sự cho コンサル売り上げ — đồng thời xây quan hệ **長期協業**.

---

## 【課題】現状のままでは大目的が達成できない理由（ボトルネック）

### Center pin

> WDP đã chứng minh vai trò **営業支援**（受注率↑ / 間接売上効果）,  
> nhưng **現状のまま** thì không đạt các 大目的 P0 trong năm MVP:  
> vì còn kẹt **ショット型現状把握**, thiếu **Before→After**, chưa có **有料導線**,  
> và **工数 insight / setup** còn cao — trong khi Vis đang cần WDP là **一助** cho XD・コンサル売り上げ.  
> Nếu bravesoft chỉ tiếp tục **通常開発 theo ticket**, bottleneck không được ưu tiên đúng → Vis khó đạt mục tiêu, bravesoft cũng khó giữ vị trí sau 内製化.

### Bottleneck map（gắn từng 大目的）

| 大目的 | Vì sao現状 không đạt（bottleneck） | Bằng chứng đã phân tích |
|--------|-----------------------------------|-------------------------|
| **① 受注一助の拡大** | Survey thường **không kịp** nhịp đề xuất 3–4 tuần; barrier triển khai / timing; chỉ người ý thức cao dùng | Lead time gap; WDS ~10件/月 vs ~500案件/年 |
| **② Before→After / 有料・XD** | Dùng chính **現状把握ショット型**; After chưa thành; 有料 ~2; product chưa đủ “お金を払って使いたい” | Mục「WDPの実態」; FY2026 cần Afterスポット |
| **③ AI分析・工数削減** | AIレポート **要望未確定**; còn **hardcode** nguy hiểm cho AI; chưa có PoC精度 chung | Sheet 目的; Milestone backlog923 |
| **④ 利用件数・提供工数** | Setup 稼働/空間 **分断**; 開発サイクル **重い**; adoption lệch | Mockup wizard; tài liệu XP/WDP |
| **⑤ 長期協業** | Nếu chỉ vá feature → Vis coi là 通常開発 có thể thay bằng 内製 | Sheet: それ以外の価値提供を期待 |

### 3 bottleneck “ghế ngồi” (ưu tiên giải thích với Vis)

1. **Bottleneck giá trị:** Có data trước thầu, **chưa có vòng chứng minh効果 sau**（After）→ không mở 有料 / XD MVP đúng nghĩa.  
2. **Bottleneck tốc độ dùng:** Setup + report tốn 工数 → không tăng 利用件数 dù đã có 受注率 proof.  
3. **Bottleneck hợp tác:** Yêu cầu AI/một phần update treo → phát triển bị động; thiếu lớp **cố vấn ưu tiên theo コンサル売り上げ**.

### Ranh giới（tránh overclaim）

Bottleneck **phía Vis ngoài hệ thống**（認知 XD thị trường, rule đề xuất nội bộ, máy bán 有料）bravesoft **không giải triệt để bằng code**.  
Đề xuất dưới đây giải **phần enablement hệ thống + đồng hành ưu tiên / PoC / đo hiệu quả** — điều kiện cần để Vis tự chạy được phần còn lại.

---

## 【方針】解決アプローチ（コンセプト）の選定

### Concept đề xuất（1 câu）

> **「受注で証明済みの一助を、After・有料・XDまで伸ばす」**  
> — bravesoft đồng hành theo trục **コンサルティング売り上げ**,  
> bằng **Product enablement（After / setup） + AI活用の分析・コンサル（PoC先行） + 活用伴走（優先順位の顧問）**,  
> không phải “feature backlog lớn hơn”.

### Vì sao chọn concept này（so với hướng khác）

| Hướng | Nội dung | Đánh giá |
|--------|----------|----------|
| A. Tiếp tục 通常開発 theo ticket | Vá theo backlog hiện tại | **Loại.** Lệch Vis（コンサル活用へシフト）; dễ mất chỗ khi 内製化 |
| B. Xây SaaS đầy đủ ngay | Full 継続課金 / platform lớn trong 1 phase | **Loại cho lần này.** FY2026 Vis chỉ cần Afterスポット + 数値化文化; quá sớm vs năm MVP |
| C. Chỉ làm AIレポート lớn | Một feature AI end-to-end | **Loại đơn độc.** 要望未確定 + hardcode risk; trái “PoCで精度すり合わせ” |
| **D. 一助最大化（khuyến nghị）** | Giữ sức 受注 + mở After + AI PoC/工数削減 + giảm setup工数; bravesoft vào vai ưu tiên theo売上 | **Chọn.** Khớp 大目的 P0 + kỳ vọng sheet 目的 |

### 3 trụ trong concept D

```text
① 受注一助を止めない（giữ / mở rộng cái đã chứng minh）
② After導線を作る（điều kiện 有料・XD MVP）
③ AI×コンサルをPoCで先に価値検証（đúng cửa cố vấn; giảm工数 insight）
        ＋
   活用伴走: cùng Vis xếp Must theo コンサル売り上げ（không theo cảm tính feature）
```

### Nguyên tắc làm việc cố vấn（thay 通常開発）

| Trước（thường） | Sau（đề xuất） |
|----------------|----------------|
| Nhận yêu cầu → ước tính → code | Cùng Vis hỏi: việc này tăng **受注 / After / 有料 / 工数削減** thế nào? |
| Làm hết simulation / tích hợp nếu có ticket | Hoãn Want nếu không phục vụ năm MVP |
| Chờ Vis chốt AIレポート rồi mới đụng | **PoC nhỏ + tiêu chí精度** trước, rồi mới scale |
| Báo cáo tiến độ task | Báo cáo **chỉ số一助**（利用、After、工数、間接効果 giả định） |

---

## 【絞込】要求の優先順位付け（マスト / ウォント）

### Tiêu chí chẻ Must / Want

Một hạng mục là **マスト** chỉ khi thỏa ≥2:

1. Bám trực tiếp **コンサルティング売り上げ** hoặc **一助** đo được（受注 / After / 有料 / 工数）  
2. Cần cho **FY2026 検証（MVP）**（Afterスポット、XD starter、有料準備）  
3. bravesoft **giao được trong 1–2 quý** hoặc mở được quyết định（PoC）  
4. Giảm rủi ro quan hệ（AI・コンサル伴走 vs chỉ 通常開発）

### マスト（Must）

| ID | Hạng mục | Gắn 大目的 | Ghi chú |
|----|----------|------------|---------|
| M1 | **Before→After** tối thiểu trên WDP（so sánh / lưu mốc / hỗ trợ report hiệu quả） | ② | Trung tâm năm MVP |
| M2 | Giảm barrier **đưa survey vào đề xuất sớm**（timing / URL đã có hướng /フロー活用） | ① | Giữ & mở 受注一助 |
| M3 | **Setup 工数↓** cho 稼働・空間（wizard / gộp luồng — hướng mockup đã có） | ④① | Điều kiện tăng 利用件数 |
| M4 | **AI工数削減 調査・見積もり** + **AI分析 PoC**（phạm vi an toàn, có tiêu chí精度） | ③⑤ | Đúng kỳ vọng Vis; cửa vào cố vấn |
| M5 | Chuẩn bị kỹ thuật an toàn cho AI（xử lý / cô lập chỗ **hardcode** nguy hiểm trong phạm vi PoC） | ③ | Sheet 課題 AI開発 |
| M6 | **伴走 ưu tiên**: nhịp định kỳ xếp Must theo コンサル売り上げ + đo chỉ số一助 | ⑤ | Khác 通常開発 |

### ウォント（Want）— làm sau hoặc chỉ khi dư sức / có ROI rõ

| ID | Hạng mục | Lý do xếp Want |
|----|----------|----------------|
| W1 | 空間・コストシミュレーション hoàn chỉnh | Milestone: ưu tiên không cao; không phải nút After/有料 năm MVP |
| W2 | 統合分析 / 販売代理店フル | Hữu ích trung hạn; sau UI/After |
| W3 | AIレポート full production ngay | Chưa chốt要望; trái PoC先行 |
| W4 | Account改修第2弾 rộng | Milestone nghiêng UI/活用 trước |
| W5 | SaaS hóa đầy đủ / 自走 platform lớn | Đích FY2027–28; không phải scope lần này |
| W6 | Mọi nguồn 稼働 còn lại nếu không tăng After/受注 | Tránh phình scope kỹ thuật |

### Quy tắc khi Vis thêm yêu cầu mới

> Nếu không chứng minh được đóng góp **受注↑ / After↑ / 有料準備 / 工数↓** trong năm MVP → mặc định **Want**, đưa vào backlog sau khuyến nghị案.

---

## 【提案】フェーズ分け（松竹梅）と推奨案

### Tổng quan 3 gói

| | **梅（Mhẹ）** | **竹（Khuyến nghị）** | **松（Rộng）** |
|--|---------------|----------------------|----------------|
| **Ý tưởng** | PoC + chỉ số; ít đụng product | Enablement After/setup + AI PoC + 伴走 cố vấn | Bamboo + roadmap SaaS/自走 sớm hơn |
| **Must cover** | M4 M5 M6（một phần M1 phân tích） | M1–M6 | M1–M6 + một phần Want chọn lọc |
| **Rủi ro** | Không đủ để Vis thấy product đổi | Cân bằng | Scope/chi phí cao; lệch năm MVP |
| **Phù hợp khi** | Vis chỉ muốn thử quan hệ cố vấn | Vis muốn tiến After/有料/XD MVP trong FY2026 | Vis muốn tăng tốc mạnh sau khi Bamboo chạy |

---

### 梅 — “顧問PoC先行”

**Nội dung chính**

1. Điều tra / 見積 **AI工数削減**（report / phân tích hiện tại tốn bao nhiêu）  
2. **AI分析 PoC** 1 phạm vi hẹp（ví dụ: gợi ý insight từ survey kết quả; có rubric精度 với Vis）  
3. Rà soát / cô lập điểm **hardcode** trong phạm vi PoC  
4. Nhịp **伴走 ưu tiên**（bi-weekly）: xếp backlog theo コンサル売り上げ; dashboard chỉ số一助 đơn giản（利用、After提案、工数仮説）  
5. Blueprint Before→After（chưa build full）để Vis thấy đích product  

**Không làm trong 梅:** wizard setup lớn; After product hoàn chỉnh; AI report production.

**Kết quả kỳ vọng:** Vis và bravesoft **đồng thuận精度 & ROI giả định**; chứng minh bravesoft ≠ chỉ 通常開発.  
**Hạn chế:** Product vẫn ショット型 → 大目的② chỉ được “thiết kế”, chưa “chạy”.

---

### 竹 — “一助をAfterまで伸ばす”（**推奨案**）

**Nội dung chính = 梅 + product Must năm MVP**

| Trụ | Việc cụ thể（mức đề xuất） |
|-----|---------------------------|
| **A. After導線** | Luồng Before→After tối thiểu: lưu mốc survey / so sánh chỉ số / xuất khung report hiệu quả cho XP・営業 |
| **B. 受注一助の運用改善** | Cùng Vis chốtフロー dùng sớm（nurturing/early）; giảm ma sát còn lại phía tool sau URL survey |
| **C. Setup工数↓** | Wizard gộp setup 空間・稼働（theo hướng mockup đã có）— ưu tiên case dùng nhiều |
| **D. AI×コンサル** | Hoàn tất 調査見積 + PoC; nếu PoC đạt ngưỡng精度 → kế hoạch phase-2 AIレポート（không bung full ngay） |
| **E. 顧問伴走** | Hàng tháng: review Must/Want theo số 利用・After・工数; đề xuất cắt Want; đồng hành Vis đo 間接効果 / giả định 有料 |

**Không làm trong 竹（giữ Want）:** simulation đầy đủ, tích hợp lớn, SaaS billing đầy đủ, AI production không qua PoC.

**Vì sao là khuyến nghị**

- Khớp **FY2026**: Afterスポット + 数値化 + chuẩn bị 有料 + hỗ trợ XD MVP  
- Khớp kỳ vọng sheet: **AI工数削減 / PoC** + **コンサル活用**  
- Đủ để đổi quan hệ sang **cố vấn**, nhưng chưa phình như làm SaaS sớm  
- Cover toàn bộ 大目的 P0 + nền P1（setup）+ P2（伴走）

---

### 松 — “MVP加速＋自走準備”

** = 竹 + **

- AIレポート hướng production sau PoC（phạm vi GW trừ nếu cần）  
- UI ưu tiên consulting rộng hơn  
- Một phần Want có ROI（ví dụ nền tảng cho 代理店 / tích hợp nhẹ）  
- Blueprint **自走 / SaaS** rõ cho FY2027（chưa nhất thiết build full billing）  

**Phù hợp khi:** Vis chốt ngân sách lớn hơn và muốn rút ngắn đường tới FY2027 PMF.  
**Rủi ro:** Dễ quay lại “làm nhiều feature”; cần kỷ luật Must/Want chặt hơn.

---

### 今回通したい推奨案

> **推奨: 竹（一助をAfterまで伸ばす）**  
> Có thể bắt đầu **2–4 tuần 梅相当（PoC kickoff）** trong phase 0 của 竹 để giảm rủi ro精度 / hardcode — rồi mới khóa scope product After/setup.

**Message cho Vis（1 đoạn）:**

> Hiện WDP đã là 一助 ở khâu 受注（+22.9pt / +25.4pt, 間接 ~1.46億）.  
> Năm MVP cần thêm 一助 ở khâu **After / 有料準備 / XD**.  
> bravesoft đề xuất không phải “dev thêm ticket”, mà **đồng hành cố vấn**:  
> mở **Before→After**, giảm **setup工数**, và **AI PoC giảm工数 phân tích** —  
> đo bằng chỉ số gắn コンサルティング売り上げ.

---

## 【効果】推奨案（竹）の投資対効果（ROI）とスケジュール

### Cách nhìn ROI（trung thực）

ROI Vis nhận từ 竹 = tổng 4 dòng:

```text
(1) Bảo vệ / mở rộng 間接売上効果（受注一助）
(2) Tăng khả năng tạo コンサル売上 XD（starter / After chứng minh）
(3) Chuẩn bị 有料・WDP直接売上（FY2026 mục tiêu WDP 0.2億 là khung）
(4) Giảm 工数レポート・分析（AI PoC + setup↓）
```

Số **(1)** đã có trong tài liệu Vis.  
Số **(2)(3)(4)** là **khung mục tiêu / giả định** — cần chốt baseline cùng Vis ở phase 0（không bịa thành “đã đạt”).

### (1) Neo số đã có — giá trị không được làm tụt

| Chỉ số gốc（tài liệu） | Ý nghĩa ROI |
|------------------------|-------------|
| コンペ受注率 +**22.9pt**（30.9%→53.8%） | Data đề xuất đã đổi thắng thầu |
| 特命・ナーチャリング +**25.4pt**（49.6%→75.0%） | Dùng sớm càng mạnh |
| 間接売上効果 **≈1.46億** | `WDP活用完工売上 × 受注率上昇分` |

**Hiệu quả 竹 với (1):** Không “tạo mới từ 0”, mà **giảm rủi ro mất hiệu ứng** + **tăng tỷ lệ案件 kịp dùng WDS**（xử lý lead time / setup /フロー）.  
Dù chỉ cải thiện thêm một phần nhỏ tỷ lệ活用 trên ~500案件, biên 間接効果 vẫn có trọng số lớn — đây là lý do Must gồm M2/M3.

### (2)(3) Khung mục tiêu năm MVP（từ kế hoạch Vis）

| Khung | Số Vis đã viết | 竹 đóng góp gì |
|-------|----------------|----------------|
| FY2026 XD+WDP | **0.7億**（XD 0.55 + WDP 0.2） | Tool đủ để Vis chạy Afterスポット + hỗ trợ starter |
| XD starter | **40件** | After + report工数↓ → giao được nhiều hơn với cùng headcount |
| WDP 有料 | Từ ~**2** → hướng **コンスタント**（đích quản trị Vis） | Before→After訴求 = điều kiện cần（không đủ một mình） |

**Cách nói ROI với Vis（an toàn）:**  
> 竹 không cam kết một mình đạt 0.7億.  
> 竹 cam kết **gỡ bottleneck hệ thống** đang chặn đường tới 0.7億 / After / 有料 — và cùng đo chỉ số dẫn（利用、After実施、工数/レポート、PoC精度）.

### (4) ROI工数（cần đo ở phase 0）

| Hạng mục | Cách đo đề xuất |
|----------|-----------------|
| Thời gian setup 稼働/空間 | Trước/sau wizard（phút / case） |
| Thời gian làm report / phân tích survey | Trước/sau PoC AI（giờ người） |
| 見積コスト削減 | Đổi giờ người → ¥（đơn giá Vis cung cấp） |

Sheet Vis đã yêu cầu đúng việc này: **AIを活用してどれだけ工数・コスト削減できるか調査・見積もり**.

### Lợi ích phía quan hệ（bravesoft & Vis）

| Bên | Hiệu quả phi doanh thu trực tiếp |
|-----|----------------------------------|
| **Vis** | Có đối tác xếp việc theo コンサル売り上げ; giảm lệch “làm feature không ra tiền” |
| **bravesoft** | Chuyển từ 通常開発 → **AI・コンサル領域の長期協業**（đúng 目指す姿 sheet）; chỗ đứng sau 内製化 rõ hơn |

---

### Schedule khuyến nghị（竹）

> Mốc mang tính **đề xuất triển khai**; chốt lại khi ước tính chi tiết. Phase 0 có thể chạy như 梅.

| Phase | Thời lượng（mức đề xuất） | Việc chính | Đầu ra |
|-------|--------------------------|------------|--------|
| **0. 顧問キックオフ / PoC準備** | 2–4 tuần | Baseline工数; chốt phạm vi AI PoC + tiêu chí精度; Must/Want lock; blueprint After | Báo cáo 調査見積骨格; backlog Must khóa |
| **1. AI PoC + hardcode安全化（phạm vi PoC）** | 4–6 tuần | PoC chạy trên data mẫu; đối chiếu精度 với Vis | Go / No-go AI phase-2; số 工数削減仮 |
| **2. After導線 MVP** | 6–10 tuần（song song một phần với 1） | Before/After lưu mốc + so sánh + khung report | Vis dùng được trên case XD starter / Afterスポット |
| **3. Setup wizard（優先ソース）** | 6–10 tuần（song song） | Gộp luồng 空間・稼働 chính | Giảm thời gian setup đo được |
| **4. 活用伴走安定** | Toàn kỳ + 1–2 tháng sau release | Monthly review chỉ số一助; cắt Want; hỗ trợ Vis đo 受注活用率 / After率 | Báo cáo hiệu quả đồng hành |

**Đường tới quyết định Vis**

```text
Tuần 0–4:  Vis thấy bravesoft ở vai cố vấn（baseline + PoC design）
Tuần 4–10: PoC có số精度 / 工数
Tuần 10–20: After + setup lên môi trường dùng thật
Cuối phase: Cùng review: có mở 松 / AI phase-2 / siết Want không
```

---

### Bảng quyết định nhanh cho Vis

| Câu hỏi Vis | Trả lời của 推奨案（竹） |
|-------------|-------------------------|
| Có bỏ 受注支援 không? | Không — giữ & mở rộng |
| Có nhảy SaaS ngay không? | Không — Afterスポット đúng năm MVP |
| AI làm full luôn không? | Không — **PoC先行**（đúng sheet） |
| bravesoft khác 通常開発 chỗ nào? | Ưu tiên theo コンサル売り上げ + đo一助 + AI/活用伴走 |
| Rủi ro nếu không làm? | WDP mãi ショット型; 有料/XD khó tiến; bravesoft chỉ còn việc 内製 sẽ lấy |

---

## Phụ lục A — Chuỗi logic đầy đủ（1 trang）

```text
【大目的】WDP = 一助 → コンサルティング売り上げ↑
   （受注 / After・有料・XD / AI工数↓ / 利用↑ / 長期協業）

【課題】現状: 営業支援は証明済みだが
   ショット型・After欠如・有料薄い・工数高い・伴走不足
   → 大目的（năm MVP）に届かない

【方針】一助をAfterまで伸ばす
   Product enablement + AI PoC + 活用顧問伴走
   （≠ 通常開発 / ≠ SaaS一括）

【絞込】Must = After / 受注運用 / setup↓ / AI調査・PoC / 安全化 / 伴走
        Want = simulation・統合・AIフル・SaaSフル…

【提案】梅=PoC伴走 / 竹=推奨（After+setup+AI PoC+伴走） / 松=加速

【効果】Giữ・mở 間接効果 + mở đường 0.7億/After/有料
        + 工数削減 đo được + quan hệ長期協業
```

## Phụ lục B — Thuật ngữ nhanh

| Từ | Nghĩa ngắn |
|----|------------|
| 一助 | Công cụ hỗ trợ（không thay consulting） |
| ショット型 | Dùng một lần |
| Before→After | Đo trước/sau để chứng minh効果 |
| 間接売上効果 | Doanh thu gián tiếp nhờ 受注率 tăng |
| 検証（MVP）年 | FY2026 — năm kiểm chứng, chưa scale |
| 顧問伴走 | Đồng hành cố vấn ưu tiên / đo hiệu quả — hơn là chỉ nhận ticket |
| 松竹梅 | 3 gói: rộng / chuẩn / nhẹ |

---

## Phụ lục C — Việc cần Vis xác nhận ở kickoff

1. Baseline: thời gian setup & làm report hiện tại（để tính 工数削減）  
2. Ngưỡng **精度** chấp nhận cho AI PoC  
3. 1–2 case XD starter / After thật để gắn phase 2–3  
4. Người Vis đầu mối（営業 / XP / プロダクト）cho nhịp 伴走  
5. Ngân sách hướng 竹 hay muốn bắt đầu 梅 rồi upgrade  

---

*Tài liệu này kế thừa: `docs/01-phan-tich-muc-tieu-lon.md`, `docs/02-vis-genjo-cu-the.md`, `docs/03-van-de-he-thong-vis.md`.*
