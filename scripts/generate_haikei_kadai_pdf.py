#!/usr/bin/env python3
"""Generate 【背景】【課題】PDFs (JA / VI) for proposal framing."""

from pathlib import Path

from weasyprint import HTML

OUT_DIR = Path(__file__).resolve().parents[1] / "docs"

CSS = """
  @page {
    size: A4;
    margin: 16mm 14mm 16mm 14mm;
    @bottom-center {
      content: counter(page);
      font-family: "Noto Sans CJK JP", "Noto Sans JP", sans-serif;
      font-size: 9pt;
      color: #999;
    }
  }
  body {
    font-family: "Noto Sans CJK JP", "Noto Sans JP", sans-serif;
    font-size: 10pt;
    line-height: 1.65;
    color: #4F4D4D;
  }
  .eyebrow { color: #b28e00; font-weight: 700; font-size: 10.5pt; margin: 0 0 4px; }
  h1 { font-size: 16pt; color: #2f2d2d; margin: 0 0 8px; line-height: 1.35; }
  h2 {
    font-size: 13pt; color: #2f2d2d; margin: 18px 0 8px;
    padding: 6px 10px; background: #f7f1d6; border-radius: 4px;
  }
  h3 { font-size: 11pt; color: #1f4e79; margin: 12px 0 5px; }
  h4 { font-size: 10.2pt; color: #2f2d2d; margin: 10px 0 4px; }
  p { margin: 0 0 7px; }
  ul { margin: 0 0 8px; padding-left: 1.15em; }
  li { margin: 0 0 3px; }
  .note {
    background: #fff4e8; border-radius: 4px; padding: 7px 9px;
    margin: 6px 0 10px; font-size: 9.2pt; color: #6b4a12;
  }
  .box {
    background: #e8f0f8; border-radius: 4px; padding: 8px 10px;
    margin: 6px 0 10px; font-size: 9.5pt;
  }
  .core {
    background: #fff1eb; border-left: 4px solid #9a3412;
    border-radius: 0 4px 4px 0; padding: 8px 10px; margin: 8px 0 10px;
    font-size: 9.8pt;
  }
  .meta { font-size: 9pt; color: #7a7777; margin-bottom: 8px; }
  table.data {
    width: 100%; border-collapse: collapse; font-size: 9.3pt; margin: 4px 0 10px;
  }
  table.data th, table.data td {
    border: 1px solid #e6e4e0; padding: 6px 7px; text-align: left; vertical-align: top;
  }
  table.data th { background: #faf9f7; white-space: nowrap; }
  pre.flow {
    background: #f6f5f2; border-radius: 4px; padding: 8px 10px;
    font-family: "Noto Sans CJK JP", "Noto Sans JP", sans-serif;
    font-size: 9.2pt; white-space: pre-wrap; margin: 6px 0 10px;
  }
"""

HTML_JA = f"""<!DOCTYPE html>
<html lang="ja"><head><meta charset="UTF-8"/><style>{CSS}</style></head><body>
<div class="eyebrow">提案整理メモ / 事業計画ベース</div>
<h1>【背景】【課題】Vis × WDP</h1>
<p class="meta">
根拠：『ヴィスの現状と今後について』（WDP XD事業計画 / 小川 慧 / 2025/12/26）<br/>
数字は資料時点。正式利用前にVisへ最新確認すること。
</p>

<h2>【背景】現在の状況と、達成すべき大目的</h2>

<h3>1. Visが目指す方向</h3>
<ul>
  <li><strong>2030年</strong>：会社全体で売上高 <strong>250億円</strong></li>
  <li>第2の柱として <strong>XD＋WDP</strong> を育てる（目安約<strong>25億円</strong>／詳細計画FY2030は<strong>19.45億円</strong>）</li>
  <li>定義：<strong>ワークデザイン ＝ WD × XD</strong></li>
</ul>

<h3>2. いまの事業の中心（WD）</h3>
<ul>
  <li>FY2025時点の売上の多くはオフィスの<strong>移転・改装</strong></li>
  <li>モデル：<strong>請負契約</strong>＋<strong>労働集約型</strong></li>
  <li>オフィスリニューアル：およそ<strong>年間500件</strong></li>
</ul>

<h3>3. WDPのいま（証明済み／未達）</h3>
<table class="data">
  <tr><th>項目</th><th>事業計画上の事実</th></tr>
  <tr><td>主用途</td><td>サーベイ（現状把握）</td></tr>
  <tr><td>利用量</td><td>およそ<strong>年間100件ペース</strong></td></tr>
  <tr><td>有料契約</td><td>まだ<strong>約2件</strong>（マネタイズには程遠い）</td></tr>
  <tr><td>使い方</td><td><strong>ショット型</strong>（1回で終わり）</td></tr>
  <tr><td>証明済みの価値</td><td><strong>営業支援</strong>（受注率アップ→間接売上効果）</td></tr>
  <tr><td>受注率</td><td>コンペ<strong>＋22.9pt</strong>／特命・ナーチャリング<strong>＋25.4pt</strong></td></tr>
  <tr><td>間接売上効果</td><td>約<strong>1.4〜1.46億円</strong></td></tr>
</table>
<div class="box">
WDPは「提案・受注の一助」としては効いている。<br/>
一方で「効果検証・継続利用・有料化」までは届いていない。
</div>

<h3>4. FY2026の位置づけ（検証年）</h3>
<ul>
  <li>フェーズ：<strong>検証（MVP）</strong></li>
  <li>XD＋WDP合計：<strong>0.7億円</strong>（XD 0.55＋WDP 0.2）</li>
  <li>WDP：<strong>After中心のスポット利用</strong>（いきなりSaaS化しない）</li>
  <li>XD：通常リニューアル提案に <strong>XD MVP</strong>（目安約100万円）をセットして検証</li>
</ul>

<h3>5. 「スターター約40件」の意味</h3>
<p>事業計画FY2026：</p>
<div class="box">
スタータープラン<strong>40件</strong>を通じて「誰に・何が・なぜ刺さるか」を検証。<br/>
年間契約はPoC扱いで最大1社。
</div>
<p><strong>スターター約40件とは：</strong></p>
<ul>
  <li><strong>XDの入口商品（スターター／MVP）を約40件実施・検証する目標件数</strong></li>
  <li>目的は売上最大化そのものではなく、<strong>勝ち筋（誰に／何が／なぜ）を学ぶこと</strong></li>
  <li>価格目安約<strong>100万円</strong>。WD（リニューアル）提案にセットしやすい形</li>
</ul>
<p><strong>スターター約40件ではないもの：</strong></p>
<ul>
  <li>WDP有料契約40件、ではない</li>
  <li>WD案件40件、ではない（WDは約500件/年）</li>
  <li>SaaS年間契約40件、ではない</li>
</ul>
<div class="note">
背景としての意味：FY2026は「XDを大きく売る年」ではなく、
<strong>40件のスターターで勝ち筋を見つける年</strong>。
その検証を支えるため、WDP側にも After／Before→After の計測が必要になる。
</div>

<div class="core">
<strong>背景の一言：</strong>
Visの大目的は2030年に向けてXD×WDPを第2の柱にすること。
いまWDPは受注支援としては成功しているが、FY2026はまずXDスターター約40件とAfter活用で“検証”する段階にある。
</div>

<h2>【課題】現状のままでは大目的が達成できない理由（ボトルネック）</h2>
<p>事業計画から読み取れるボトルネックを5つに整理する（資料に書かれた構造）。</p>

<h4>ボトルネック① ショット型のままでは有料化・SaaS化できない</h4>
<ul>
  <li>現状把握の1回利用が中心 → 継続にならない → 有料約2件</li>
  <li>マネタイズには <strong>before and after の拡大</strong> と <strong>XD連携</strong> が必要、と明記</li>
</ul>
<p><strong>影響：</strong>間接効果（受注）はあっても、WDP直接売上・SaaS柱が育たない。</p>

<h4>ボトルネック② After（効果検証）が弱い</h4>
<ul>
  <li>移転後の効果測定まで回りにくい</li>
  <li>XD MVPの中核も before and after 効果検証</li>
  <li>FY2026のWDPは After中心のスポット利用</li>
</ul>
<p><strong>影響：</strong>「作って終わり」を超えられず、XD価値証明も有料化訴求も弱い。</p>

<h4>ボトルネック③ 提案リードタイムにWDSが間に合わない</h4>
<ul>
  <li>提案まで通常 <strong>3〜4週間</strong></li>
  <li>メール収集→実施→反映が難しい</li>
  <li>方針：URL形式・ナーチャリング早期実施</li>
</ul>
<p><strong>影響：</strong>受注支援効果を案件ごとに取りこぼす。</p>

<h4>ボトルネック④ WDPが重く、XD検証速度に追従しにくい</h4>
<ul>
  <li>クイックな機能追加が難しい</li>
  <li>別アプリ並行開発→後でWDP置換、という方針</li>
</ul>
<p><strong>影響：</strong>XDスターター検証（約40件）の学習速度が落ちる。</p>

<h4>ボトルネック⑤ 労働集約のままでは第2の柱にスケールしない</h4>
<ul>
  <li>WDは人を増やし続けないと伸びにくい</li>
  <li>XDもXP依存のままだとスケールしにくい</li>
  <li>顧客の<strong>自走</strong>を支えるWDPが必要</li>
</ul>
<p><strong>影響：</strong>2030年のXD×WDP柱（約25億目安）に届かない。</p>

<h3>課題の中心（ボトルネックの核）</h3>
<pre class="flow">受注の一助（Before）は証明済み
    ↓ ここで途切れている
After効果検証 → 継続利用 → 有料化 → SaaS
    ↓
XDスターター検証（約40件）も、第2の柱も進みにくい</pre>

<div class="core">
<strong>課題の一言：</strong>
現状のボトルネックは「WDPが受注で終わっていること」。
大目的達成には、<strong>After／継続／有料</strong>へつなぐ必要がある。
</div>
</body></html>
"""

HTML_VI = f"""<!DOCTYPE html>
<html lang="vi"><head><meta charset="UTF-8"/><style>{CSS}</style></head><body>
<div class="eyebrow">Memo đề xuất / dựa trên事業計画</div>
<h1>【背景】【課題】Vis × WDP</h1>
<p class="meta">
Nguồn：『ヴィスの現状と今後について』（WDP XD事業計画 / 小川 慧 / 2025/12/26）<br/>
Số liệu tại thời điểm tài liệu. Trước khi dùng chính thức cần xác nhận lại với Vis.
</p>

<h2>【背景】Tình hình hiện tại &amp; mục tiêu lớn cần đạt</h2>

<h3>1. Hướng Vis đang nhắm tới</h3>
<ul>
  <li><strong>2030:</strong> toàn công ty <strong>250億 Yên</strong></li>
  <li>Nuôi trụ cột 2: <strong>XD＋WDP</strong>（mục tiêu tham chiếu khoảng <strong>25億</strong>／bảng chi tiết FY2030: <strong>19.45億</strong>）</li>
  <li>Định nghĩa: <strong>Work Design ＝ WD × XD</strong></li>
</ul>

<h3>2. Trung tâm kinh doanh hiện tại（WD）</h3>
<ul>
  <li>FY2025: phần lớn売上 từ <strong>chuyển / cải tạo văn phòng</strong></li>
  <li>Mô hình: <strong>請負</strong>＋<strong>労働集約</strong></li>
  <li>Office renew: khoảng <strong>500件/năm</strong></li>
</ul>

<h3>3. WDP hôm nay（đã chứng minh / còn thiếu）</h3>
<table class="data">
  <tr><th>Hạng mục</th><th>Sự thật trong事業計画</th></tr>
  <tr><td>Dùng chính</td><td>Survey（現状把握）</td></tr>
  <tr><td>Lượng dùng</td><td>khoảng <strong>100件/năm</strong></td></tr>
  <tr><td>Hợp đồng trả phí</td><td>còn khoảng <strong>2件</strong></td></tr>
  <tr><td>Cách dùng</td><td><strong>ショット型</strong>（dùng 1 lần）</td></tr>
  <tr><td>Giá trị đã chứng minh</td><td><strong>Hỗ trợ bán hàng</strong>（tăng 受注率 → hiệu ứng gián tiếp）</td></tr>
  <tr><td>受注率</td><td>コンペ <strong>＋22.9pt</strong>／特命・ナーチャリング <strong>＋25.4pt</strong></td></tr>
  <tr><td>Hiệu ứng gián tiếp</td><td>khoảng <strong>1.4〜1.46億 Yên</strong></td></tr>
</table>
<div class="box">
WDP đã hiệu quả như trợ thủ đề xuất / nhận thầu.<br/>
Nhưng chưa tới đo hiệu quả / dùng liên tục / thu phí trực tiếp.
</div>

<h3>4. Vị trí FY2026（năm検証）</h3>
<ul>
  <li>Phase: <strong>検証（MVP）</strong></li>
  <li>Tổng XD＋WDP: <strong>0.7億</strong>（XD 0.55＋WDP 0.2）</li>
  <li>WDP: ưu tiên <strong>After-spot</strong>（không nhảy SaaS ngay）</li>
  <li>XD: gắn <strong>XD MVP</strong>（khoảng 100万 Yên） vào đề xuất renew để kiểm chứng</li>
</ul>

<h3>5. 「Starter khoảng 40件」nghĩa là gì?</h3>
<p>Trong事業計画 FY2026:</p>
<div class="box">
Thông qua starter plan <strong>40件</strong> để kiểm chứng「誰に・何が・なぜ刺さるか」.<br/>
Hợp đồng năm chỉ PoC tối đa 1社.
</div>
<p><strong>Starter ~40 nghĩa là:</strong></p>
<ul>
  <li>Mục tiêu triển khai / kiểm chứng khoảng <strong>40 gói XD Starter（gói đầu vào / MVP）</strong></li>
  <li>Mục đích không phải tối đa hóa売上 ngay, mà là học <strong>khách nào / giá trị gì / vì sao chịu mua</strong></li>
  <li>Giá entry khoảng <strong>100万 Yên</strong>; dễ gắn kèm đề xuất WD（renew）</li>
</ul>
<p><strong>Starter ~40 không phải:</strong></p>
<ul>
  <li>40 hợp đồng trả phí WDP</li>
  <li>40 dự án WD（WD vẫn ~500件/năm）</li>
  <li>40 hợp đồng SaaS năm</li>
</ul>
<div class="note">
Ý nghĩa trong phần背景: FY2026 không phải năm “bán XD quy mô lớn”, mà là năm
<strong>dùng ~40 starter để tìm cách thắng</strong>.
Để hỗ trợ vòng検証 đó, WDP cần nền tảng đo After / Before→After.
</div>

<div class="core">
<strong>Một câu chốt phần背景:</strong>
Mục tiêu lớn của Vis là biến XD×WDP thành trụ cột 2 tới 2030.
Hiện WDP đã thành công ở hỗ trợ 受注; FY2026 trước hết là năm検証 với XD starter ~40件 và tận dụng After.
</div>

<h2>【課題】Vì sao giữ nguyên thì không đạt mục tiêu lớn（bottleneck）</h2>
<p>Bottleneck đọc được từ事業計画, chốt thành 5 điểm（cấu trúc trong tài liệu）.</p>

<h4>Bottleneck ① Giữ shot-type thì không 有料 / không SaaS được</h4>
<ul>
  <li>Dùng 1 lần để nắm現状 → không 継続 → 有料 ~2件</li>
  <li>Tài liệu ghi rõ: monetize cần <strong>mở rộng before and after</strong> + <strong>kết hợp XD</strong></li>
</ul>
<p><strong>Ảnh hưởng:</strong> Có hiệu ứng gián tiếp（受注）nhưng doanh thu trực tiếp / trụ SaaS không lớn được.</p>

<h4>Bottleneck ② After（効果検証）còn yếu</h4>
<ul>
  <li>Khó đo hiệu quả sau chuyển/cải tạo</li>
  <li>XD MVP lấy before and after làm lõi</li>
  <li>FY2026: WDP ưu tiên After-spot</li>
</ul>
<p><strong>Ảnh hưởng:</strong> Không vượt “làm xong không gian”; khó chứng minh XD và khó bán 有料.</p>

<h4>Bottleneck ③ Lead time đề xuất khiến WDS không kịp</h4>
<ul>
  <li>Thường chỉ còn <strong>3–4 tuần</strong></li>
  <li>Thu email → chạy survey → đưa vào đề xuất khó kịp</li>
  <li>Hướng trong tài liệu: URL form + nurturing sớm</li>
</ul>
<p><strong>Ảnh hưởng:</strong> Bỏ lỡ hiệu quả hỗ trợ 受注 ở từng案件.</p>

<h4>Bottleneck ④ WDP nặng, khó bắt kịp tốc độ検証 XD</h4>
<ul>
  <li>Khó thêm/sửa chức năng nhanh</li>
  <li>Có hướng app song song → sau đó thay vào WDP</li>
</ul>
<p><strong>Ảnh hưởng:</strong> Vòng学習 của XD starter（~40件）chậm lại.</p>

<h4>Bottleneck ⑤ Thâm dụng lao động thì không scale thành trụ cột 2</h4>
<ul>
  <li>WD phải tăng người mới tăng売上</li>
  <li>XD nếu chỉ dựa XP cũng khó scale</li>
  <li>Cần WDP giúp khách <strong>自走</strong></li>
</ul>
<p><strong>Ảnh hưởng:</strong> Khó đạt mục tiêu XD×WDP ~25億（2030）.</p>

<h3>Hạt nhân bottleneck（chốt）</h3>
<pre class="flow">Đã chứng minh: hỗ trợ 受注（Before）
    ↓ đứt đoạn tại đây
After効果検証 → 継続利用 → 有料化 → SaaS
    ↓
XD starter検証（~40）và trụ cột 2 đều khó tiến</pre>

<div class="core">
<strong>Một câu chốt phần課題:</strong>
Bottleneck cốt lõi là WDP đang dừng ở hỗ trợ 受注.
Muốn đạt mục tiêu lớn phải nối tiếp sang <strong>After / 継続 / 有料</strong>.
</div>
</body></html>
"""


def build() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    HTML(string=HTML_JA, base_url=str(OUT_DIR)).write_pdf(
        str(OUT_DIR / "proposal-haikei-kadai-ja.pdf")
    )
    HTML(string=HTML_VI, base_url=str(OUT_DIR)).write_pdf(
        str(OUT_DIR / "proposal-haikei-kadai-vi.pdf")
    )
    print("Wrote JA/VI 【背景】【課題】PDFs")


if __name__ == "__main__":
    build()
