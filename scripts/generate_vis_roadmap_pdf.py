#!/usr/bin/env python3
"""Generate Japanese Vis roadmap overview PDF for WDP team sharing."""

from pathlib import Path

from weasyprint import HTML

OUT_DIR = Path(__file__).resolve().parents[1] / "docs"
OUT_PDF = OUT_DIR / "vis-wdp-roadmap-overview-ja.pdf"
MD_SRC = OUT_DIR / "vis-wdp-roadmap-overview-ja.md"


HTML_DOC = """<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8" />
<style>
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
</style>
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


def build() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    if not MD_SRC.exists():
        raise SystemExit(f"Missing markdown source: {MD_SRC}")
    HTML(string=HTML_DOC, base_url=str(OUT_DIR)).write_pdf(str(OUT_PDF))
    print(f"Wrote {OUT_PDF}")


if __name__ == "__main__":
    build()
