from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
def pic(p,a):return f'<img src="assets/{p}" alt="{a}">'
def icon(k):
 p={'memory':'<rect x="10" y="10" width="36" height="36" rx="3"/><path d="M18 10v13h20V10M18 46V33h20v13M32 15v5"/>','yen':'<circle cx="28" cy="28" r="22"/><path d="M18 15l10 14 10-14M28 29v14M18 29h20M18 36h20"/>','repair':'<path d="M35 8a13 13 0 0 0-15 17L7 38a6 6 0 0 0 9 9l13-13A13 13 0 0 0 47 19L37 29l-10-10z"/><circle cx="12" cy="42" r="1"/>','lock':'<rect x="12" y="25" width="32" height="24" rx="3"/><path d="M18 25V16a10 10 0 0 1 20 0v9M28 35v6"/>','leaf':'<path d="M44 8C13 6 8 21 14 35s33 10 30-27zM12 48l24-29M21 37l-1-12M29 29l9 1"/>','drop':'<path d="M28 5C23 15 11 26 11 35a17 17 0 0 0 34 0C45 26 33 15 28 5zM19 34c-1 6 3 10 8 11"/>'}[k]
 return f'<svg class="line-icon" viewBox="0 0 56 56" aria-hidden="true">{p}</svg>'
DATA={
'water':('10ml単位の自動出水','100ml〜1,000mlを10ml刻みで指定。ボタンを押し続けずに、自動で出て自動で止まります。',pic('W06_scenes/icon3.png','水筒')),
'temp':('白湯・40℃も選べる<span class="nowrap">5モード</span>','冷水・温水・常温水・白湯（<span class="nowrap">55〜60℃</span>）・40℃に対応。40℃モードは温水と冷水を順に出し、指定量に仕上げます。',pic('W08_temps/mug.png','湯気の立つカップ')),
'uv':('出水口のUV殺菌','浮遊・付着段階で殺菌。バイオフィルムを形成する前に殺菌し、水が出てくる直前まで清潔にこだわります。',icon('drop')),
'memory':('前回の量を覚えるメモリ','ボタンごとに前回の量を記憶。いつもの量をすぐに選べます。冷水と常温水のメモリは共通です。',icon('memory')),
'care':('毎日使いやすい細かな配慮','水はねしにくい出水口と外せる受け皿。2Lボトルや鍋も置けます。チャイルドロック・エコモードも搭載。',pic('W06_scenes/icon1.png','出水口とグラス')),
'color':('暮らしになじむ2色','ホワイトはクラウドダンサー。ブラックは光沢をおさえたマット仕上げです。','<span class="swatches"><i></i><i></i></span>'),
'price':('月額3,300円〈税抜〉','税込3,630円。契約条件と設置スペースは製品ガイドの「製品仕様」をご覧ください。',icon('yen')),
'mall':('YASUNEモール','ご契約者は日用品・食料品・美容品などを安い価格で購入できます。',pic('W19_yasune/icon_daily.png','日用品の洗剤ボトル')),
'repair':('レンタル中の修理サポート','自然故障は無料修理。任意の安心保証オプション（月額税抜550円）で、お客様側の原因による故障も無料修理になります。',icon('repair')),
'app':('専用アプリでまとめて管理','必要水分量の算出、飲水記録、トラブル時の確認、フィルターの注文・交換時期の確認ができます。',pic('W20_app/phone_l.png','飲水記録アプリ画面（開発中）'))}
PROOF='第三者機関の試験で、緑膿菌をはじめとする一般細菌に対する99.9%の殺菌効果を確認。'
COLOR='クラウドダンサーは、Pantoneが2026年のカラー・オブ・ザ・イヤーに選んだ白です。'
def card(k,extra=''):
 t,b,v=DATA[k]
 return f'<article class="feature {extra}" data-feature="{k}"><div class="feature-visual">{v}</div><div><h3>{t}</h3><p>{b}</p></div></article>'
def footer():return f'<footer class="notes"><p>{PROOF}</p><p>{COLOR}</p><p>詳しい仕様・条件は<a href="index.html#spec">製品ガイド</a>をご確認ください。アプリ画像は開発中のものです。</p></footer>'
def page(letter,intro,body):return f'''<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="robots" content="noindex"><meta name="viewport" content="width=device-width,initial-scale=1"><title>PureNext 強みまとめ｜案{letter}</title><link rel="stylesheet" href="css/v2/base_v2.css"><link rel="stylesheet" href="css/v2/summary-options.css?v=20260908-3"></head><body class="summary-page"><main class="summary-shell"><nav aria-label="比較ページ"><a href="summary-options.html">3案の比較へ</a><a href="index.html">製品ガイド</a><span>案{letter}</span></nav><header class="summary-head"><h1>PureNextの<span>強みまとめ</span></h1><p>{intro}</p></header>{body}{footer()}</main></body></html>'''
major=''
for k,n,u in [('water','10','ml'),('temp','5','モード'),('uv','99.9','%')]:
 t,b,v=DATA[k]
 if k=='uv':v=pic('W12_uv_place/uv_render.png','出水口に向けたUV照射の図')
 extra='<span class="metric-label">第三者機関の試験での殺菌効果</span>' if k=='uv' else ''
 major+=f'<article class="major-card" data-feature="{k}"><div class="major-visual">{v}</div><div class="metric">{n}<small>{u}</small></div>{extra}<h2>{t}</h2><p>{b}</p></article>'
A=f'<div class="major-grid">{major}</div><div class="support-grid">'+''.join(card(k) for k in ['memory','care','color','price','mall','repair','app'])+'</div>'
left=''.join(card(k,'map-point') for k in ['water','temp','memory'])
right=''.join(card(k,'map-point') for k in ['uv','care','color'])
B=f'<section class="product-map"><div class="map-side map-left">{left}</div><figure class="map-product">'+pic('W04_strengths/body_balanced_dry_20260908.png','受け皿が乾いた状態の細身のPureNextホワイト本体')+f'<figcaption>PureNext</figcaption></figure><div class="map-side map-right">{right}</div></section><div class="service-band">'+''.join(card(k) for k in ['price','mall','repair','app'])+'</div>'
def step(v,l):return f'<div class="step">{v}<span>{l}</span></div>'
flow1=step('<b>250<small>ml</small></b>','量を決める')+'<span class="arrow">→</span>'+step(pic('W06_scenes/icon3.png','水筒'),'自動で出水')+'<span class="arrow">→</span>'+step(icon('memory'),'量を記憶')
flow2=step('<span class="germs">· ·<br> · ·</span>','浮遊・付着')+'<span class="arrow">→</span>'+step('<b>UV</b>','形成前に<br>殺菌')+'<span class="arrow">→</span>'+step(pic('W08_temps/glasses.png','水の入ったグラス'),'出水直前も<br>清潔')
scene1=f'<section class="scene"><header><span>01</span><h2>飲みたい量・温度で</h2></header><div class="steps">{flow1}</div><div class="scene-copy">'+''.join(card(k) for k in ['water','temp','memory'])+'</div></section>'
scene2=f'<section class="scene"><header><span>02</span><h2>清潔に、使いやすく</h2></header><div class="steps">{flow2}</div><div class="scene-copy">'+''.join(card(k) for k in ['uv','care'])+'</div><div class="mini-benefits">'+icon('lock')+'<span>チャイルドロック</span>'+icon('leaf')+'<span>エコモード</span></div></section>'
scene3='<section class="scene"><header><span>03</span><h2>暮らしになじむ</h2></header><div class="lifestyle-visual">'+pic('W16_color/unit_white_t.png','ホワイト本体')+pic('W16_color/unit_black_t.png','ブラック本体')+'<div><b>3,300<small>円／月・税抜</small></b><span>税込3,630円</span></div></div><div class="scene-copy">'+''.join(card(k) for k in ['color','price','mall'])+'</div></section>'
scene4='<section class="scene"><header><span>04</span><h2>使い始めてからも</h2></header><div class="after-visual">'+pic('W20_app/phone_l.png','飲水記録アプリ画面（開発中）')+'<div>'+icon('repair')+'<b>記録・確認・修理</b><span>毎日の管理をサポート</span></div></div><div class="scene-copy">'+''.join(card(k) for k in ['repair','app'])+'</div></section>'
C=f'<div class="scene-grid">{scene1}{scene2}{scene3}{scene4}</div>'
for l,i,b in [('A','量・温度・清潔さ。特徴を数字とイラストで確認できます。',A),('B','本体を中心に、機能と暮らしを支えるサービスをまとめました。',B),('C','飲むときから使い続ける毎日まで、4つの場面でご紹介します。',C)]:
 (ROOT/f'summary-{l.lower()}.html').write_text(page(l,i,b),encoding='utf-8')
choices=''
for l,t,d in [('A','数字とイラストで一覧','10ml・5モード・UV殺菌を大きく見せ、特徴を一覧できます。'),('B','本体を中心に機能を図解','本体の左右に機能を配置。製品の全体像をつかめます。'),('C','使う場面に沿って紹介','出水・清潔・暮らし・サポートを、図の流れで理解できます。')]:
 choices+=f'<a class="option" href="summary-{l.lower()}.html"><div class="option-title"><b>案{l}</b><h2>{t}</h2></div><div class="mini-preview"><iframe src="summary-{l.lower()}.html" title="案{l}の縮小プレビュー" tabindex="-1" loading="lazy" aria-hidden="true"></iframe></div><p>{d}</p><span class="open-option">案{l}を大きく見る →</span></a>'
(ROOT/'summary-options.html').write_text(f'<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="robots" content="noindex"><meta name="viewport" content="width=device-width,initial-scale=1"><title>PureNext 強みまとめ｜3案比較</title><link rel="stylesheet" href="css/v2/base_v2.css"><link rel="stylesheet" href="css/v2/summary-options.css?v=20260908-3"></head><body class="summary-page"><main class="summary-shell"><nav><a href="index.html">製品ガイドへ</a></nav><header class="summary-head"><h1>強みまとめの3パターン</h1><p>同じ10項目を、今のテイストに合わせた3つの構成でご覧いただけます。</p></header><div class="options-grid">{choices}</div></main></body></html>',encoding='utf-8')
print('Built 3 variants and comparison page')
