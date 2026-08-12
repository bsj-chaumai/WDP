import re, markdown, html as htmlmod

SRC = 'docs/context/82-kadai-teian-map.md'
OUT = 'docs/context/82-kadai-teian-map.html'

md_text = open(SRC, encoding='utf-8').read()

# Build TOC from h1 headings (the 課題 blocks) and h2
def slug(t):
    s = re.sub(r'[^\w\u3040-\u30ff\u4e00-\u9fff\- ]', '', t).strip()
    s = re.sub(r'\s+', '-', s)
    return s or 'sec'

toc = []
for line in md_text.splitlines():
    m = re.match(r'^(#{1,2})\s+(.*)$', line)
    if m:
        level = len(m.group(1))
        title = m.group(2).strip()
        toc.append((level, title, slug(title)))

body = markdown.markdown(
    md_text,
    extensions=['tables', 'fenced_code', 'toc', 'sane_lists', 'attr_list'],
    extension_configs={'toc': {'slugify': lambda value, sep: slug(value)}},
)

toc_html = ['<nav class="toc"><div class="toc-title">目次</div><ol>']
for level, title, sid in toc:
    cls = 'lv1' if level == 1 else 'lv2'
    toc_html.append(f'<li class="{cls}"><a href="#{sid}">{htmlmod.escape(title)}</a></li>')
toc_html.append('</ol></nav>')
toc_html = '\n'.join(toc_html)

TEMPLATE = """<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>課題 → 提案 マップ（memo の整理版）</title>
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700&display=swap" rel="stylesheet" />
<style>
  :root {
    --text: #4F4D4D;
    --text-strong: #2f2d2d;
    --muted: #7a7777;
    --line: #e6e4e0;
    --bg: #f6f5f2;
    --paper: #fff;
    --gold: #b28e00;
    --gold-soft: #f7f1d6;
    --k1: #1f4e79;
    --k1-soft: #e8f0f8;
    --k2: #8b5a2b;
    --k2-soft: #f5ebe0;
    --k3: #2f6f6a;
    --k3-soft: #e7f3f1;
    --warn: #9a3412;
    --warn-soft: #fff1eb;
    --max: 1000px;
  }
  * { box-sizing: border-box; }
  body {
    margin: 0;
    font-family: "Noto Sans JP", sans-serif;
    font-size: 15px;
    line-height: 1.8;
    letter-spacing: 0.02em;
    color: var(--text);
    background: var(--bg);
    -webkit-font-smoothing: antialiased;
  }
  .layout { max-width: var(--max); margin: 0 auto; padding: 28px 16px 80px; }

  /* TOC */
  .toc {
    background: var(--paper);
    border: 1px solid var(--line);
    border-radius: 8px;
    padding: 18px 22px;
    margin: 0 0 24px;
  }
  .toc-title {
    color: var(--gold);
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.08em;
    margin-bottom: 10px;
  }
  .toc ol { list-style: none; margin: 0; padding: 0; }
  .toc li { margin: 3px 0; font-size: 14px; }
  .toc li.lv2 { padding-left: 18px; font-size: 13px; color: var(--muted); }
  .toc a { color: var(--text); text-decoration: none; border-bottom: 1px solid transparent; }
  .toc a:hover { color: var(--gold); border-bottom-color: var(--gold); }
  .toc li.lv1 > a { font-weight: 700; color: var(--text-strong); }

  /* Content card */
  .doc {
    background: var(--paper);
    border: 1px solid var(--line);
    border-radius: 8px;
    padding: 34px 34px 44px;
  }

  h1 {
    font-size: 22px;
    font-weight: 700;
    color: var(--text-strong);
    margin: 46px 0 6px;
    padding: 12px 0 12px 16px;
    border-left: 5px solid var(--gold);
    background: var(--gold-soft);
    border-radius: 0 6px 6px 0;
    line-height: 1.5;
  }
  h1:first-of-type { margin-top: 0; }
  h2 {
    font-size: 17px;
    font-weight: 700;
    color: var(--text-strong);
    margin: 34px 0 10px;
    padding-bottom: 7px;
    border-bottom: 2px solid var(--line);
  }
  h3 {
    font-size: 15px;
    font-weight: 700;
    color: var(--k1);
    margin: 26px 0 8px;
  }
  h4 {
    font-size: 14px;
    font-weight: 700;
    color: var(--muted);
    margin: 20px 0 6px;
  }

  p { margin: 10px 0; }
  strong { color: var(--text-strong); font-weight: 700; }
  hr { border: 0; border-top: 1px solid var(--line); margin: 36px 0; }

  ul, ol { margin: 10px 0; padding-left: 22px; }
  li { margin: 5px 0; }

  blockquote {
    margin: 14px 0;
    padding: 12px 18px;
    background: var(--k3-soft);
    border-left: 4px solid var(--k3);
    border-radius: 0 6px 6px 0;
    color: var(--text-strong);
  }
  blockquote p { margin: 5px 0; }

  pre {
    background: #2f2d2d;
    color: #f2efe9;
    padding: 16px 18px;
    border-radius: 6px;
    overflow-x: auto;
    font-size: 13.5px;
    line-height: 1.75;
    margin: 14px 0;
  }
  pre code { font-family: "SFMono-Regular", Menlo, Consolas, monospace; }
  :not(pre) > code {
    background: var(--gold-soft);
    color: #6b5500;
    padding: 2px 6px;
    border-radius: 4px;
    font-size: 13px;
    font-family: "SFMono-Regular", Menlo, Consolas, monospace;
  }

  table {
    width: 100%;
    border-collapse: collapse;
    margin: 16px 0 20px;
    font-size: 14px;
    background: var(--paper);
  }
  th, td {
    border: 1px solid var(--line);
    padding: 9px 12px;
    text-align: left;
    vertical-align: top;
    line-height: 1.7;
  }
  th {
    background: #faf9f6;
    color: var(--text-strong);
    font-weight: 700;
    white-space: nowrap;
  }
  tbody tr:nth-child(even) td { background: #fcfbf9; }
  td strong { color: var(--k1); }

  /* 課題ごとの色分け */
  h1[id^="課題-1"] { border-left-color: var(--k1); background: var(--k1-soft); }
  h1[id^="課題-2"] { border-left-color: var(--k2); background: var(--k2-soft); }
  h1[id^="課題-3"] { border-left-color: var(--k3); background: var(--k3-soft); }
  h1[id^="補足"]   { border-left-color: var(--warn); background: var(--warn-soft); }

  /* TOC: 課題行を色分け */
  .toc a[href^="#課題-1"] { color: var(--k1); font-weight: 700; }
  .toc a[href^="#課題-2"] { color: var(--k2); font-weight: 700; }
  .toc a[href^="#課題-3"] { color: var(--k3); font-weight: 700; }
  .toc a[href^="#補足"]   { color: var(--warn); font-weight: 700; }

  .foot {
    margin-top: 18px;
    color: var(--muted);
    font-size: 12px;
    text-align: center;
  }

  @media (max-width: 720px) {
    .doc { padding: 22px 18px 30px; }
    table { font-size: 13px; }
    th { white-space: normal; }
  }
  @media print {
    body { background: #fff; }
    .toc { display: none; }
    .doc { border: 0; padding: 0; }
    h1 { break-after: avoid; }
    table { break-inside: avoid; }
  }
</style>
</head>
<body>
<div class="layout">
__TOC__
<article class="doc">
__BODY__
</article>
<div class="foot">docs/context/82-kadai-teian-map.md をそのままHTML化したものです（内容の変更はありません）</div>
</div>
</body>
</html>
"""

out = TEMPLATE.replace('__TOC__', toc_html).replace('__BODY__', body)
open(OUT, 'w', encoding='utf-8').write(out)
print('wrote', OUT, len(out), 'bytes')
