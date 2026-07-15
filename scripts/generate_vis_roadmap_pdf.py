#!/usr/bin/env python3
"""Generate Vis roadmap overview PDFs (JA / VI) for WDP team sharing."""

from pathlib import Path

from weasyprint import HTML

OUT_DIR = Path(__file__).resolve().parents[1] / "docs"

CSS = """
  @page {
    size: A4;
    margin: 18mm 16mm 18mm 16mm;
    @bottom-center {
      content: counter(page);
      font-family: "Noto Sans CJK JP", "Noto Sans JP", sans-serif;
      font-size: 9pt;
      color: #999;
    }
  }
  body {
    font-family: "Noto Sans CJK JP", "Noto Sans JP", sans-serif;
    font-size: 10.5pt;
    line-height: 1.7;
    color: #4F4D4D;
  }
  .eyebrow {
    color: #b28e00;
    font-weight: 700;
    font-size: 11pt;
    margin: 0 0 6px;
  }
  h1 {
    font-size: 18pt;
    color: #2f2d2d;
    margin: 0 0 10px;
    line-height: 1.35;
  }
  h2 {
    font-size: 13.5pt;
    color: #2f2d2d;
    margin: 22px 0 10px;
    padding-bottom: 4px;
    border-bottom: 2px solid #f7f1d6;
  }
  h3 {
    font-size: 11.5pt;
    color: #1f4e79;
    margin: 16px 0 6px;
  }
  h4 {
    font-size: 10.5pt;
    color: #2f2d2d;
    margin: 12px 0 4px;
  }
  p { margin: 0 0 8px; }
  ul { margin: 0 0 10px; padding-left: 1.2em; }
  li { margin: 0 0 4px; }
  .note {
    background: #f7f1d6;
    border-radius: 4px;
    padding: 8px 10px;
    margin: 10px 0 14px;
    font-size: 9.5pt;
    color: #6b4a12;
  }
  .meta {
    font-size: 9.5pt;
    color: #7a7777;
    margin-bottom: 8px;
  }
  .formula {
    background: #e8f0f8;
    border-radius: 4px;
    padding: 8px 10px;
    font-weight: 700;
    color: #1f4e79;
    margin: 8px 0 12px;
  }
  .src {
    font-size: 9.5pt;
    color: #7a7777;
  }
"""

HTML_JA = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8" />
<style>{CSS}</style>
</head>
<body>
  <div class="eyebrow">WDP開発チーム向け / 共有資料</div>
  <h1>Vis社 課題・将来ロードマップ全体像</h1>
  <p class="meta">
    PM、BrSE、メンバー全員で共有するための資料。<br/>
    根拠：『ヴィスの現状と今後について』（WDP XD事業計画 / 2025/12/26）および Vis公式サイト（WDP / XD）。
  </p>
  <div class="note">
    数字は資料時点（2025年12月）のものです。正式利用前にVisへ最新状況を確認してください。
  </div>

  <h2>I. Vis社の大きなゴールと変化</h2>
  <h3>2030年の売上目標</h3>
  <p>会社全体で<strong>250億円</strong>を目指す。</p>
  <ul>
    <li>新しい事業（XD＋WDP）の目標：5年目の2030年に約<strong>25億円</strong>を目指す（詳細な計画書でのFY2030の目標値は<strong>19.45億円</strong>）。</li>
  </ul>

  <h3>ビジネスの変化（リブランディング）</h3>
  <p>
    今までの「オフィスのデザイン（おしゃれな空間を作るだけ）」から、
    働く体験をトータルでデザインする「ワークデザイン」の提供へとシフトする。
  </p>

  <h3>新しい考え方の公式</h3>
  <div class="formula">ワークデザイン ＝ ワークプレイスデザイン × エクスペリエンスデザイン（XD）</div>

  <h2>II. Vis社と今のWDPが抱える「課題」</h2>
  <h3>A. Vis社全体の課題</h3>

  <h4>1. 「新しいオフィス」と「実際の効果」のズレ</h4>
  <p>
    せっかく高いお金を払ってオフィスをきれいにしても、その後うまく使えない顧客
    （ルールが形骸化したり、席が固定化したりする）が多い。
    今までの「空間を作って終わり」の方法では、「作った後にどう使うか」という顧客の問題を解決できていない。
  </p>

  <h4>2. 人手不足とビジネス拡大（スケール）の限界</h4>
  <ul>
    <li>現在の主力である<strong>ワークプレイスデザイン事業</strong>は、売上を増やすためにコンサルタントやクリエイターの人数を増やす必要がある（労働集約型）。</li>
    <li>新しいXD事業も、XP（コンサルタント）の手腕だけに頼っていると、同じようにビジネスを大きくすることが難しい。</li>
  </ul>
  <p>
    <strong>【解決策】</strong>
    顧客が自分たちだけでオフィスを運用できる（自走する）ためのシステム（WDP）を作り、人への依存度を下げる必要がある。
  </p>

  <h3>B. WDPシステムにおける3つのシステム的な問題</h3>
  <p>（開発チームとして解決すべきプロダクトの課題）</p>

  <h4>1. 技術的な課題：開発スピードが遅く、システムが重い</h4>
  <p>
    <strong>【実態】</strong>
    今のWDPはシステムが重いため、新しい機能の追加や小さな修正をクイック（lightweight &amp; quick）に行うことが難しい。
  </p>
  <p>
    <strong>【Vis社の方針】</strong>
    WDPとは別の独立したアプリケーションを並行して開発する。
    これをXPが使う社内ツールとして先に動かし、機能が安定した後にWDPへ統合・置換する。
  </p>
  <div class="note">※注：このアプリを誰が開発するか、いつ作るかはまだ決まっていない。</div>

  <h4>2. マネタイズ課題：1回使って終わり（Shot-type）</h4>
  <p>
    <strong>【実態】</strong>
    サーベイは年間100件ペースでよく使われており、デザイン案件を受注するための営業支援（約1.4億円の効果）にはなっているが、有料の契約はまだ2件しかない。
    理由は、現状把握のための「1回限りのスポット利用」で終わっているから。
  </p>
  <p>
    <strong>【Vis社の方針】</strong>
    サーベイを「Before &amp; After（移転前と移転後）」の2回に増やし、XDサービスとセットにすることで、長く使ってもらう（継続利用）。
    移転から約6ヶ月後にWDSをもう一度行い、前後のスコアを比べる。
  </p>

  <h4>3. 運用上の課題：サーベイ実施までの準備期間（リードタイム）が長すぎる</h4>
  <p>
    <strong>【実態】</strong>
    顧客から提案依頼が来てからコンペ（提案）本番までは通常3〜4週間しかない。
    この短い時間で顧客全員のメールアドレスを集め、サーベイを動かして結果を提案書に載せるのは時間が足りない。
    また、契約前の段階では顧客がメールアドレスを教えたがらない。
  </p>
  <p>
    <strong>【Vis社の方針】</strong>
    メールアドレスの登録がいらない「共通URL形式」の配布方法に変えて、準備期間を短くする。
    さらに、案件の初期段階（ナーチャリングやヒアリング）からサーベイの実施を顧客に促す。
  </p>

  <h2>III. Vis社が描く将来ロードマップ</h2>
  <p>XDサービスの成長と、私たちが関わるシステム（WDP）は、以下のように一緒に進化していく。</p>

  <h3>FY2025 - FY2026（検証と初期テスト）</h3>
  <h4>サービス面</h4>
  <p>
    パッケージ化したお試しサービス「XD MVP」（価格目安：100万円程度）を通常のオフィスリニューアル提案にセットして販売し、価値の検証を行う。
  </p>
  <p>MVPの内容：</p>
  <ul>
    <li>Before &amp; Afterサーベイ</li>
    <li>アブストラクションラダーのワークショップ</li>
    <li>リニューアル後イベント最低2企画</li>
    <li>KPI（WDS目標スコア）の設定</li>
    <li>イベントフォローと最終報告書</li>
  </ul>
  <h4>WDPプロダクト面</h4>
  <p>
    FY2026では、まず顧客にデータ測定の習慣をつけてもらうため、WDPの利用を「After-spot（移転後の測定）」に優先して使う。
    ※サービスMVP自体はBefore &amp; Afterを含む。After-spotはWDP利用の優先方針。
  </p>
  <h4>ツールのサポート</h4>
  <p>
    XPが使いやすいように、WDPとは別の独立したアプリケーションを並行して開発・利用する
    （この段階では、顧客自身がこのアプリを操作する必要はない）。
  </p>

  <h3>FY2027（PMF：プロダクト・マーケット・フィットの達成）</h3>
  <p>
    「Starter → Full XD → 年間契約」という、サービスを段階的に体験できる流れを確立する。
    WDPシステムでも、顧客の「自走」を助ける価値や、年間契約を支える価値を検証していく。
  </p>

  <h3>FY2028（SaaSでお金を稼ぐフェーズ）</h3>
  <p>
    競合他社が同じようなXDサービスを真似し始める時期（2028年頃）に、
    Vis社は低価格で幅広い顧客に届くテクノロジー（システム）で差をつける。
  </p>
  <p>
    並行開発していたアプリケーションの機能を、WDP本体へと完全統合・置換（＝新生WDP）し、
    月額課金（SaaS型）として本格的にスタートする。
  </p>

  <h3>FY2030（ビジネスを大きくして安定させるフェーズ）</h3>
  <p>
    顧客はVis社のコンサルタント（XP）を頼ることなく、提供された「WDP（SaaS）」を使って
    自分たちだけでデータ計測やイベント運用を続け、オフィスを自立して動かす（自走する）。
  </p>
  <p>
    Vis社は「人手（労働）」に頼るビジネスから抜け出し、売上約<strong>25億円</strong>
    （詳細計画のFY2030は<strong>19.45億円</strong>）の「XD×WDP」事業を、会社の第2の柱に育てる。
  </p>

  <h2>出典</h2>
  <ul class="src">
    <li>『ヴィスの現状と今後について』（WDP XD事業計画 / 小川 慧 / 2025/12/26）</li>
    <li>https://vis-produce.com/service/data-solution/wdp</li>
    <li>https://vis-produce.com/lp/experience-design</li>
  </ul>
</body>
</html>
"""

HTML_VI = f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8" />
<style>{CSS}</style>
</head>
<body>
  <div class="eyebrow">Tài liệu cho đội WDP / Dùng để share nội bộ</div>
  <h1>Bức tranh tổng thể về chiến lược, 課題 và định hướng của Vis</h1>
  <p class="meta">
    Tài liệu chuẩn hóa dành cho PM, BrSE và toàn bộ thành viên.<br/>
    Nguồn：『ヴィスの現状と今後について』（WDP XD事業計画 / 2025/12/26）và website chính thức Vis（WDP / XD）.
  </p>
  <div class="note">
    Số liệu lấy tại thời điểm tài liệu（2025/12）. Trước khi dùng chính thức, hãy xác nhận lại với Vis.
  </div>

  <h2>I. Mục tiêu lớn và sự dịch chuyển của Vis</h2>
  <h3>Mục tiêu doanh thu năm 2030</h3>
  <p>Toàn công ty Vis hướng tới <strong>250億 Yên</strong>.</p>
  <ul>
    <li>Mảng mới（XD＋WDP）hướng tới khoảng <strong>25億 Yên</strong> vào năm thứ 5（2030）（trong bảng kế hoạch chi tiết, mục tiêu FY2030 là <strong>19.45億 Yên</strong>）.</li>
  </ul>

  <h3>Sự dịch chuyển định vị（Rebranding）</h3>
  <p>
    Chuyển từ 「thiết kế văn phòng（chỉ làm không gian đẹp）」sang cung cấp
    <strong>Work Design</strong> — thiết kế toàn diện trải nghiệm làm việc.
  </p>

  <h3>Công thức cốt lõi mới</h3>
  <div class="formula">Work Design ＝ Workplace Design × Experience Design（XD）</div>

  <h2>II. Các vấn đề cốt lõi（課題）của Vis và hệ thống WDP hiện tại</h2>
  <h3>A. Vấn đề vĩ mô phía Vis</h3>

  <h4>1. Khoảng cách giữa 「văn phòng mới」và 「hiệu quả thực tế」</h4>
  <p>
    Khách hàng bỏ nhiều tiền để làm mới văn phòng, nhưng sau đó thường không dùng được đúng kỳ vọng
    （quy tắc mới bị hình thức hóa, chỗ ngồi lại cố định）.
    Cách làm cũ 「làm xong không gian là hết」chưa giải quyết được bài toán 「sau khi làm xong thì vận hành thế nào」.
  </p>

  <h4>2. Phụ thuộc sức người và giới hạn mở rộng quy mô（Scalability）</h4>
  <ul>
    <li>Mảng chủ lực hiện tại là <strong>Workplace Design</strong> đang ở trạng thái thâm dụng lao động（労働集約型）: muốn tăng doanh thu thì phải tăng thêm Consultant / Creator.</li>
    <li>Mảng XD mới nếu chỉ dựa vào năng lực của chuyên viên tư vấn（XP）cũng sẽ rất khó scale.</li>
  </ul>
  <p>
    <strong>【Hướng giải quyết】</strong>
    Cần có hệ thống（WDP）giúp khách hàng tự vận hành văn phòng（自走）, giảm phụ thuộc vào tư vấn viên.
  </p>

  <h3>B. 3 rào cản kỹ thuật &amp; vận hành trên hệ thống WDP</h3>
  <p>（Các vấn đề sản phẩm mà đội phát triển cần xử lý）</p>

  <h4>1. Rào cản công nghệ: chu kỳ phát triển chậm, hệ thống nặng</h4>
  <p>
    <strong>【Thực trạng】</strong>
    WDP hiện tại nặng, khó thêm tính năng mới hoặc chỉnh sửa nhỏ một cách nhanh（lightweight &amp; quick）.
  </p>
  <p>
    <strong>【Định hướng của Vis】</strong>
    Phát triển song song một ứng dụng độc lập ngoài WDP, dùng trước như công cụ nội bộ cho XP;
    khi tính năng ổn định sẽ tích hợp / thay thế ngược vào WDP.
  </p>
  <div class="note">※Lưu ý: Vis chưa chỉ định bên nào làm app này và chưa có timeline chi tiết.</div>

  <h4>2. Rào cản thương mại hóa: khách hàng chỉ 「dùng 1 lần」（Shot-type）</h4>
  <p>
    <strong>【Thực trạng】</strong>
    Survey dùng khoảng <strong>100案件/năm</strong>, hỗ trợ bán hàng cho mảng thiết kế với hiệu ứng gián tiếp khoảng
    <strong>1.4億 Yên</strong>, nhưng hợp đồng trả phí trực tiếp mới khoảng <strong>2件</strong>.
    Lý do: chủ yếu dùng để nắm現状 rồi dừng（spot 1 lần）.
  </p>
  <p>
    <strong>【Định hướng của Vis】</strong>
    Mở rộng mô hình survey <strong>Before &amp; After</strong>（trước và sau chuyển VP）, kết hợp với dịch vụ XD để chuyển sang dùng liên tục（継続利用）.
    Khoảng <strong>6 tháng</strong> sau chuyển VP sẽ chạy lại WDS để so điểm trước–sau.
  </p>

  <h4>3. Rào cản vận hành: lead time triển khai survey quá dài</h4>
  <p>
    <strong>【Thực trạng】</strong>
    Từ lúc khách gửi yêu cầu đề xuất đến buổi đề xuất / コンペ thường chỉ còn <strong>3–4 tuần</strong>.
    Trong thời gian ngắn này, việc thu thập email toàn bộ nhân viên rồi chạy survey và đưa kết quả vào đề xuất thường không kịp.
    Ngoài ra, trước khi ký HĐ khách cũng ngại cung cấp email sớm.
  </p>
  <p>
    <strong>【Định hướng của Vis】</strong>
    Chuyển sang phát survey bằng <strong>URL dùng chung</strong>（không bắt buộc đăng ký email）để rút ngắn chuẩn bị.
    Đồng thời thúc đẩy chạy survey sớm từ giai đoạn nuôi dưỡng KH（ナーチャリング）hoặc hearing ban đầu.
  </p>

  <h2>III. Lộ trình dịch chuyển chiến lược của Vis</h2>
  <p>Sự phát triển dịch vụ XD và hệ thống WDP（phần đội mình tham gia）sẽ tiến hóa cùng nhau như sau.</p>

  <h3>FY2025 - FY2026（Thử nghiệm / MVP）</h3>
  <h4>Về dịch vụ</h4>
  <p>
    Vis kiểm chứng giá trị bằng gói dùng thử 「XD MVP」（giá khoảng <strong>100万 Yên</strong>）,
    gắn kèm vào đề xuất renew văn phòng thông thường.
  </p>
  <p>Nội dung MVP tối thiểu:</p>
  <ul>
    <li>Survey Before &amp; After</li>
    <li>Workshop Abstraction Ladder</li>
    <li>Event sau renew tối thiểu <strong>2企画</strong></li>
    <li>Thiết lập KPI（điểm mục tiêu WDS）</li>
    <li>Follow event và báo cáo cuối</li>
  </ul>
  <h4>Về sản phẩm WDP</h4>
  <p>
    FY2026 ưu tiên dùng WDP theo hướng <strong>After-spot</strong>（đo sau chuyển VP）để tạo thói quen đo lường dữ liệu cho khách.
    ※Bản thân gói dịch vụ MVP vẫn gồm Before &amp; After. After-spot là ưu tiên cách dùng WDP trong năm này.
  </p>
  <h4>Về công cụ hỗ trợ</h4>
  <p>
    Định hướng phát triển / dùng song song một ứng dụng độc lập ngoài WDP để XP dùng nội bộ
    （giai đoạn này khách chưa nhất thiết phải tự thao tác app）.
  </p>

  <h3>FY2027（PMF）</h3>
  <p>
    Thiết lập được đường trải nghiệm dịch vụ theo bậc: <strong>Starter → Full XD → hợp đồng năm</strong>.
    Phía WDP cũng kiểm chứng giá trị hỗ trợ 「自走」của khách và giá trị gắn với hợp đồng năm.
  </p>

  <h3>FY2028（Thương mại hóa SaaS）</h3>
  <p>
    Khoảng năm 2028, khi đối thủ bắt đầu sao chép dịch vụ kiểu XD,
    Vis tạo khác biệt bằng công nghệ giá thấp, tiếp cận được tệp khách rộng.
  </p>
  <p>
    Các tính năng đã chạy ổn trên ứng dụng song song sẽ được tích hợp / thay thế hoàn toàn vào WDP chính（<strong>新生WDP</strong>）,
    và chính thức chạy mô hình <strong>SaaS</strong>（thu phí định kỳ）.
  </p>

  <h3>FY2030（Quy mô lớn / trở thành trụ cột thứ 2）</h3>
  <p>
    Khách hàng giảm phụ thuộc consultant（XP）, dùng 「WDP（SaaS）」để tự đo dữ liệu,
    tự chạy hoạt động nội bộ và tự vận hành văn phòng（自走）.
  </p>
  <p>
    Vis thoát dần mô hình phụ thuộc sức người, đưa mảng 「XD × WDP」đạt quy mô khoảng
    <strong>25億 Yên</strong>（theo bảng chi tiết FY2030 là <strong>19.45億 Yên</strong>）,
    trở thành trụ cột vững chắc thứ 2 bên cạnh Workplace Design.
  </p>

  <h2>Nguồn</h2>
  <ul class="src">
    <li>『ヴィスの現状と今後について』（WDP XD事業計画 / 小川 慧 / 2025/12/26）</li>
    <li>https://vis-produce.com/service/data-solution/wdp</li>
    <li>https://vis-produce.com/lp/experience-design</li>
  </ul>
</body>
</html>
"""


def write_pdf(html: str, out_path: Path) -> None:
    HTML(string=html, base_url=str(OUT_DIR)).write_pdf(str(out_path))
    print(f"Wrote {out_path}")


def build() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    write_pdf(HTML_JA, OUT_DIR / "vis-wdp-roadmap-overview-ja.pdf")
    write_pdf(HTML_VI, OUT_DIR / "vis-wdp-roadmap-overview-vi.pdf")


if __name__ == "__main__":
    build()
