#!/usr/bin/env python3
"""Static site builder for alchemistmind.pro. Shared header/footer/components, one file per page.
Run: python3 src/build.py  -> writes HTML into dist/
"""
import os, json
OUT = os.path.dirname(os.path.abspath(__file__))
GTM = "GTM-WVP5239R"
SITE = "https://alchemistmind.pro"
EMAIL = "team@alchemistmind.pro"
LINKEDIN = "https://www.linkedin.com/in/tre-forte-9579a4154/"
LINKEDIN_CO = "https://www.linkedin.com/company/108311767/"

# ---------- icons ----------
P = {
 "check":'<path d="M20 6 9 17l-5-5"/>',
 "x":'<path d="M18 6 6 18M6 6l12 12"/>',
 "arrow":'<path d="M5 12h14M13 6l6 6-6 6"/>',
 "chart":'<path d="M3 3v18h18"/><path d="M7 15l4-4 3 3 5-6"/>',
 "target":'<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/>',
 "mic":'<rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3"/>',
 "tablet":'<rect x="5" y="2" width="14" height="20" rx="2"/><path d="M11 18h2"/>',
 "eye-off":'<path d="M3 3l18 18M10.6 10.6a2 2 0 0 0 2.8 2.8M9.9 5.1A10 10 0 0 1 12 5c5 0 9 4.5 10 7a13 13 0 0 1-3 4M6.6 6.6A13 13 0 0 0 2 12c1 2.5 5 7 10 7a10 10 0 0 0 4.2-.9"/>',
 "loop":'<path d="M17 2l4 4-4 4"/><path d="M3 11V9a3 3 0 0 1 3-3h15M7 22l-4-4 4-4"/><path d="M21 13v2a3 3 0 0 1-3 3H3"/>',
 "file":'<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M8 13h8M8 17h5"/>',
 "clock":'<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 "shield":'<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>',
 "users":'<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/>',
 "dollar":'<path d="M12 1v22M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>',
 "zap":'<path d="M13 2 3 14h9l-1 8 10-12h-9z"/>',
 "link":'<path d="M10 13a5 5 0 0 0 7.5.5l3-3a5 5 0 0 0-7-7l-1.7 1.7"/><path d="M14 11a5 5 0 0 0-7.5-.5l-3 3a5 5 0 0 0 7 7l1.7-1.7"/>',
 "search":'<circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/>',
 "phone":'<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/>',
 "layout":'<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/>',
 "bell":'<path d="M18 8a6 6 0 0 0-12 0c0 7-3 9-3 9h18s-3-2-3-9M13.7 21a2 2 0 0 1-3.4 0"/>',
 "trophy":'<path d="M8 21h8M12 17v4M7 4h10v5a5 5 0 0 1-10 0zM17 5h3v2a3 3 0 0 1-3 3M7 5H4v2a3 3 0 0 0 3 3"/>',
 "book":'<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20V2H6.5A2.5 2.5 0 0 0 4 4.5z"/><path d="M4 19.5V22h16"/>',
 "map":'<path d="M1 6v16l7-4 8 4 7-4V2l-7 4-8-4z"/><path d="M8 2v16M16 6v16"/>',
 "flask":'<path d="M9 2h6M10 2v6L4 19a2 2 0 0 0 1.8 3h12.4A2 2 0 0 0 20 19L14 8V2"/><path d="M7 15h10"/>',
 "msg":'<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>',
 "megaphone":'<path d="M3 11v2a1 1 0 0 0 1 1h3l5 4V6L7 10H4a1 1 0 0 0-1 1zM16 8a5 5 0 0 1 0 8M19 5a9 9 0 0 1 0 14"/>',
}
def icon(n, size=22, cls=""):
    return f'<svg class="{cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{P[n]}</svg>'
def chk(): return icon("check",18,"check")
def tick(): return f'<span class="tick">{icon("check",14)}</span>'
ARR = '<span class="arr">&rarr;</span>'

GLOGO = '''<svg class="g" viewBox="0 0 48 48" aria-hidden="true"><path fill="#EA4335" d="M24 9.5c3.5 0 6.6 1.2 9.1 3.6l6.8-6.8C35.8 2.4 30.3 0 24 0 14.6 0 6.6 5.4 2.6 13.3l7.9 6.1C12.4 13.6 17.7 9.5 24 9.5z"/><path fill="#4285F4" d="M46.1 24.6c0-1.6-.1-3.1-.4-4.6H24v9h12.4c-.5 2.9-2.2 5.3-4.6 6.9l7.4 5.8c4.3-4 6.9-9.9 6.9-17.1z"/><path fill="#FBBC05" d="M10.5 28.6A14.5 14.5 0 0 1 9.5 24c0-1.6.3-3.1.8-4.6l-7.9-6.1A24 24 0 0 0 0 24c0 3.9.9 7.5 2.6 10.7l7.9-6.1z"/><path fill="#34A853" d="M24 48c6.5 0 11.9-2.1 15.9-5.8l-7.4-5.8c-2.1 1.4-4.8 2.3-8.5 2.3-6.3 0-11.6-4.1-13.5-9.8l-7.9 6.1C6.6 42.6 14.6 48 24 48z"/></svg>'''
# Official Google Partner badge: paste the HTML snippet from Google Ads > Admin > Partners program >
# Badge status > Badge assets into GP_SNIPPET (Google requires the snippet; imitation badges aren't allowed).
GP_SNIPPET = ""
def gp_badge():
    if GP_SNIPPET:
        return f'<span class="gp-official">{GP_SNIPPET}</span>'
    return f'<span class="gp-badge" title="Alchemist Mind Pros is an official Google Partner">{icon("shield",20,"gp-ico")}<span>Official Google Partner<small>Google Ads agency</small></span></span>'

def book(label="Book a Strategy Call", cls="btn-primary", loc=""):
    return f'<a href="#book" class="btn {cls} js-book" data-loc="{loc}">{label} {ARR}</a>'

# ---------- nav ----------
NAV = [
 ("ClearSignal","clearsignal.html",None),
 ("AI Sales Coach","ai-sales-coach.html",None),
 ("Check-In App","check-in-app.html",None),
 ("PPC Management","ppc-management.html",[
    ("PPC","Google Ads","google-ads.html","Search, LSA and PMax built on signed-case data"),
    ("M","Meta Ads","meta-ads.html","Facebook and Instagram that feed intake, not just forms"),
    ("R","Reddit Ads","reddit-ads.html","Reach people researching their legal problem"),
    ("AI","ChatGPT Ads","chatgpt-ads.html","Show up inside ChatGPT conversations"),
 ]),
 ("HubSpot CRM","hubspot-crm.html",None),
 ("Results","index.html#results",None),
]
def header(active):
    lis=[]
    for label,href,sub in NAV:
        act=' class="active"' if href.split("#")[0]==active and "#" not in href else ''
        if sub:
            items="".join(f'<a href="{h}"><span class="dd-ico">{ic}</span><span><strong>{t}</strong><span>{d}</span></span></a>' for ic,t,h,d in sub)
            items=items.replace('<span class="dd-ico">PPC</span>','<span class="dd-ico">G</span>')
            lis.append(f'<li class="has-dd"><a href="{href}"{act}>{label} <svg class="chev" viewBox="0 0 10 10"><path d="M1 3l4 4 4-4" stroke="currentColor" fill="none" stroke-width="1.6"/></svg></a><div class="dropdown"><a href="{href}"><span class="dd-ico">&#9733;</span><span><strong>PPC Management overview</strong><span>How we run paid media for law firms</span></span></a><div class="dd-foot">{items}</div></div></li>')
        else:
            lis.append(f'<li><a href="{href}"{act}>{label}</a></li>')
    mob=[]
    for label,href,sub in NAV:
        mob.append(f'<a href="{href}">{label}</a>')
        if sub: mob.append('<div class="sub">'+"".join(f'<a href="{h}">{t}</a>' for _,t,h,_ in sub)+'</div>')
    return f'''<header class="site-header"><div class="wrap nav">
<a class="brand" href="index.html" aria-label="Alchemist Mind Pros home"><img src="assets/amp-logo-256.png" alt="Alchemist Mind Pros logo" width="44" height="45"><span class="brand-name">Alchemist Mind Pros<small>Law firm growth</small></span></a>
<ul class="nav-links">{"".join(lis)}</ul>
<div class="nav-cta">{book('<span class="btn-text">Book a Strategy Call</span>','btn-primary','nav').replace(ARR,'')}<button class="burger" aria-label="Menu" aria-expanded="false"><span></span><span></span><span></span></button></div>
</div><nav class="mobile-menu">{"".join(mob)}{book("Book a Strategy Call","btn-primary","mobile")}</nav></header>'''

def footer():
    return f'''<footer class="site-footer"><div class="wrap">
<div class="foot-grid">
<div class="foot-brand"><a class="brand" href="index.html"><img src="assets/amp-logo-256.png" alt="" width="44" height="45"><span class="brand-name">Alchemist Mind Pros</span></a>
<p>Performance marketing and attribution for law firms. We connect ad spend to signed cases so you can make decisions on revenue, not clicks.</p>{gp_badge()}</div>
<div><h4>Platform</h4><ul><li><a href="clearsignal.html">ClearSignal</a></li><li><a href="ai-sales-coach.html">AI Sales Coach</a></li><li><a href="check-in-app.html">Check-In App</a></li><li><a href="hubspot-crm.html">HubSpot CRM</a></li><li><a href="clearsignal.html#pricing">Pricing</a></li></ul></div>
<div><h4>PPC Management</h4><ul><li><a href="ppc-management.html">Overview</a></li><li><a href="google-ads.html">Google Ads</a></li><li><a href="meta-ads.html">Meta Ads</a></li><li><a href="reddit-ads.html">Reddit Ads</a></li><li><a href="chatgpt-ads.html">ChatGPT Ads</a></li><li><a href="ppc-management.html#landing-pages">Landing Pages</a></li></ul></div>
<div><h4>Company</h4><ul><li><a href="index.html#results">Results</a></li><li><a href="index.html#quiz">Free Self-Check</a></li><li><a href="index.html#calculator">Cost Per Signed Case Calculator</a></li><li><a href="index.html#founder">About Tre</a></li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li><a href="{LINKEDIN_CO}" target="_blank" rel="noopener">LinkedIn</a></li></ul></div>
</div>
<div class="foot-bottom"><span>&copy; <span class="yr">2026</span> Alchemist Mind Pros. ClearSignal is a product of Alchemist Mind Pros.</span><span><a href="privacy/">Privacy Policy</a> &nbsp;&middot;&nbsp; <a href="terms-app/">Terms of Service</a></span></div>
</div></footer>'''

def page(fname, title, desc, body, active=None):
    html=f'''<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">
<link rel="canonical" href="{SITE}/{'' if fname=='index.html' else fname.replace('.html','')}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:type" content="website"><meta property="og:image" content="{SITE}/assets/amp-logo.png">
<link rel="icon" href="assets/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&family=Manrope:wght@400;500;600;700;800&family=Sora:wght@500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/styles.css">
<script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);}})(window,document,'script','dataLayer','{GTM}');</script>
</head><body>
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id={GTM}" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
{header(active or fname)}
<main>{body}</main>
{sticky_cta() if "sticky-cta" not in body else ""}
{footer()}
<script src="assets/main.js"></script>
</body></html>'''
    with open(os.path.join(OUT,fname),"w") as f: f.write(html)

# ---------- shared components ----------
def faq(items):
    return '<div class="faq">'+"".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in items)+'</div>'

def cta_band(h="Stop guessing. Start seeing your cost per signed case.", p="Book a 30-minute strategy call. We'll look at your current ad accounts and reporting, show you where budget is leaking, and tell you honestly whether we're a fit.", bullets=None):
    bullets=bullets or ["Walk through your real numbers, not a canned demo","Month-to-month. No long-term contracts","Works alongside your existing CRM and intake"]
    lis="".join(f"<li>{chk()}{b}</li>" for b in bullets)
    return f'''<section id="book"><div class="wrap"><div class="cta-band reveal">
<div><span class="eyebrow">Next step</span><h2>{h}</h2><p>{p}</p><ul>{lis}</ul></div>
<div class="book-box"><div id="calendly-inline"></div>{book("Book a Strategy Call","btn-primary","cta-band")}<p>Prefer email? <a href="mailto:{EMAIL}" style="color:var(--copper-2)">{EMAIL}</a></p></div>
</div></div></section>'''

def dash_mock(title="Cost per signed case by channel", rows=None):
    rows=rows or [("Google Ads","$1,240","62%"),("Meta Ads","$1,980","88%"),("LSA","$890","44%"),("Organic","$410","22%")]
    bars="".join(f'<div class="bar-row"><span>{n}</span><div class="bar"><i data-w="{w}"></i></div><b>{v}</b></div>' for n,v,w in rows)
    return f'''<div class="dash" role="img" aria-label="Illustrative ClearSignal dashboard">
<div class="dash-top"><div><div class="dash-title">{title}</div><div class="dash-sub">Last 90 days &middot; CRM-verified</div></div><span class="live"><i></i>LIVE</span></div>
<div class="kpis"><div class="kpi"><span>Signed cases</span><b>148<em>+31%</em></b></div><div class="kpi"><span>Blended CPSC</span><b>$1,162</b></div><div class="kpi"><span>CRM match</span><b>94%</b></div></div>
<div class="bars">{bars}</div>
<div class="ticker"><div><span class="ok">&#10003;</span> Case #1084 signed &middot; matched to Google Ads click</div><div><span class="ok">&#10003;</span> Offline conversion sent to Google &amp; Meta</div><div><span class="ok">&#10003;</span> Consult call scored 4.6 / 5 by AI Sales Coach</div></div>
<span class="illus">Illustrative data</span></div>'''

def calculator(h="What is your real cost per signed case?", sub="Move the sliders to match last month. Most firms have never seen this number, and it's the only one that tells you whether your marketing is working."):
    def rng(id_,name,label,mn,mx,step,val,fmt,hint=""):
        return f'<div class="field"><label for="{id_}">{label}<output for="{id_}"></output></label><input type="range" id="{id_}" name="{name}" min="{mn}" max="{mx}" step="{step}" value="{val}" data-fmt="{fmt}">{f"<div class=hint>{hint}</div>" if hint else ""}</div>'
    return f'''<section id="calculator" class="sec-paper"><div class="wrap">
<div class="sec-head center reveal"><span class="eyebrow">Free tool &middot; No email required</span><h2>{h}</h2><p>{sub}</p></div>
<div class="calc reveal"><div class="calc-in">
{rng("c-spend","spend","Monthly ad spend",5000,300000,1000,50000,"$")}
{rng("c-leads","leads","Leads per month",20,2000,5,250,"n","Calls + forms + chats from paid channels")}
{rng("c-show","show","Consult show rate",10,100,1,55,"%","Leads that actually show for a consult")}
{rng("c-close","close","Consult-to-signed rate",5,80,1,30,"%","Consults that sign a retainer")}
</div><div class="calc-out">
<div class="out-main"><span>Your cost per signed case</span><b class="o-cpsc">$0</b></div>
<div class="out-grid"><div><span>Cost per lead</span><b class="o-cpl">$0</b></div><div><span>Signed cases / mo</span><b class="o-signed">0</b></div><div><span>Consults / mo</span><b class="o-consults">0</b></div><div><span>CPSC if 20% waste is cut</span><b class="o-after">$0</b></div></div>
<div class="out-note">Most firms we audit find <b>15 to 30%</b> of spend going to campaigns that never sign a case. At 20%, that's <b class="o-yearly">$0</b> a year you could reinvest in what works.</div>
{book("Get My Real Numbers","btn-primary","calculator")}
<p class="fine">Benchmark: once every cost is attributed, most firms land between $1,500 and $3,000+ per signed case.</p>
</div></div></div></section>'''

QUIZ = [
 ("Do you know your cost per signed case, by channel?",[("Yes, exactly, every month",2),("A rough idea",1),("I only know cost per lead",0)]),
 ("Are signed-case outcomes sent back to Google and Meta?",[("Yes, fully automated",2),("Manually or occasionally",1),("No / not sure",0)]),
 ("Has anyone reviewed your consult calls in the last 30 days?",[("Every call is scored",2),("A handful",1),("No",0)]),
 ("How do clients check in at your office today?",[("Fully digital, synced to our CRM",2),("A mix",1),("Paper clipboard",0)]),
 ("If a lead went cold before the consult, would you know why?",[("Yes, we track every step",2),("Sometimes",1),("No",0)]),
]
def quiz():
    qs=""
    for i,(q,opts) in enumerate(QUIZ):
        o="".join(f'<button class="opt" data-v="{v}"><span class="k">{"ABC"[j]}</span>{t}</button>' for j,(t,v) in enumerate(opts))
        qs+=f'<div class="q" data-i="{i}"><h3>{q}</h3><div class="opts">{o}</div></div>'
    return f'''<section id="quiz" class="sec-dark"><div class="wrap">
<div class="sec-head center reveal"><span class="eyebrow">60-second self-check</span><h2>How clearly can you see your marketing?</h2><p>Five questions. Get a visibility score and the exact gaps costing you signed cases.</p></div>
<div class="quiz reveal" id="quiz-app"><div class="quiz-top"><span class="qcount">Question 1 of 5</span><span>~60 sec</span></div><div class="progress"><i></i></div>
{qs}
<div class="result"><div class="score-ring"><svg width="150" height="150" viewBox="0 0 150 150"><circle cx="75" cy="75" r="64" stroke="rgba(255,255,255,.08)" stroke-width="10" fill="none"/><circle class="ring-fg" cx="75" cy="75" r="64" stroke="url(#cg)" stroke-width="10" fill="none" stroke-linecap="round"/><defs><linearGradient id="cg"><stop offset="0" stop-color="#93622F"/><stop offset="1" stop-color="#DDA76A"/></linearGradient></defs></svg><b><span class="score-num">0</span></b></div>
<h3 class="res-title"></h3><p class="res-desc"></p><div class="gaps"></div>
<div class="btn-row" style="justify-content:center">{book("Fix These Gaps With Us","btn-primary","quiz")}<button class="btn btn-ghost quiz-restart">Retake</button></div></div>
<button class="quiz-back">&larr; Back</button>
</div></div></section>'''

def sub_hero(crumb, eyebrow, h1, lede, visual, ctas=None, rotate=None, trust=None):
    if rotate:
        spans="".join(f"<span>{r}</span>" for r in rotate)
        h=f'<h1><span class="static">{h1}</span><span class="rotator" aria-live="polite">{spans}</span></h1>'
    else:
        h=f"<h1>{h1}</h1>"
    ctas=ctas or book("Book a Strategy Call","btn-primary","hero")
    trust=trust or ""
    return f'''<section class="hero"><div class="wrap hero-grid">
<div><div class="breadcrumb"><a href="index.html">Home</a> / {crumb}</div><span class="eyebrow">{eyebrow}</span>{h}<p class="lede">{lede}</p><div class="btn-row">{ctas}</div>{trust}</div>
<div>{visual}</div></div></section>'''

def feature_cards(items, cols=3, dark=False):
    g={2:"grid-2",3:"grid-3",4:"grid-4"}[cols]
    return f'<div class="{g}">'+"".join(f'<div class="card reveal"><div class="ico">{icon(ic)}</div><h3>{t}</h3><p>{d}</p></div>' for ic,t,d in items)+'</div>'

def feat_list(items):
    return '<ul class="feat-list">'+"".join(f'<li>{tick()}<div><b>{t}</b><p>{d}</p></div></li>' for t,d in items)+'</ul>'

def steps(items, dark=False):
    return '<div class="steps">'+"".join(f'<div class="stepc reveal"><h3>{t}</h3><p>{d}</p></div>' for t,d in items)+'</div>'

def trust_row(items):
    return '<div class="trust-row">'+"".join(f'<span class="trust-item">{icon("check",16)}{t}</span>' for t in items)+'</div>'

CHANNEL_CHIPS = {
 "google":'<span class="logo-chip" style="background:#fff">'+GLOGO.replace('class="g"','width="26" height="26"')+'</span>',
 "meta":'<span class="logo-chip" style="background:#EEF3FF;color:#1D63ED;font-weight:800;font-size:1.3rem">&infin;</span>',
 "reddit":'<span class="logo-chip" style="background:#FFF0EA;color:#FF4500;font-weight:800;font-family:var(--font-h)">r/</span>',
 "chatgpt":'<span class="logo-chip" style="background:#EFF7F3;color:#10A37F;font-weight:800;font-family:var(--font-h);font-size:.85rem">AI</span>',
}
def channel_tiles(exclude=None):
    data=[("google","Google Ads","Our strongest suit","Search, Local Services Ads and Performance Max, optimized on signed cases through offline conversion imports.","google-ads.html"),
          ("meta","Meta Ads","Facebook + Instagram","Creative-led campaigns with Conversions API and CRM feedback so Meta learns what a real client looks like.","meta-ads.html"),
          ("reddit","Reddit Ads","Emerging channel","Reach people researching their exact problem in the communities where they ask for advice.","reddit-ads.html"),
          ("chatgpt","ChatGPT Ads","New in 2026","Appear in front of people asking ChatGPT about legal problems your firm solves.","chatgpt-ads.html")]
    data=[d for d in data if d[0]!=exclude]
    cls="channels" if len(data)==4 else "grid-3"
    return f'<div class="{cls}">'+"".join(f'<a class="channel reveal" href="{h}">{CHANNEL_CHIPS[k]}<span class="pill">{pill}</span><h3>{t}</h3><p>{d}</p><span class="link-arrow">Learn more {ARR}</span></a>' for k,t,pill,d,h in data)+'</div>'

STATS = f'''<div class="wrap stats-wrap"><div class="stats reveal">
<div class="stat"><b>$20M<span class="accent">+</span></b><span>in ad spend managed across Google, Meta and more</span></div>
<div class="stat"><b>$2M<span class="accent">+</span></b><span>monthly budgets managed for our largest accounts</span></div>
<div class="stat"><b>23%<span class="accent">+</span></b><span>average lift in qualified lead rate within 60 days, often faster</span></div>
<div class="stat"><b>95%<span class="accent">+</span></b><span>client retention, on month-to-month agreements</span></div>
</div></div>'''

CASES = f'''<div class="grid-2">
<div class="case reveal"><span class="case-tag">Estate planning law firm</span><h3>Cost per lead cut in half, with every lead tracked to consult.</h3>
<div class="metric-pair"><span class="lbl">Cost per lead</span><span class="from">$41.62</span><span class="arrow">{icon("arrow")}</span><span class="to">$20.90</span></div>
<div class="metric-pair"><span class="lbl">Lead-to-consult visibility</span><span class="from">Guesswork</span><span class="arrow">{icon("arrow")}</span><span class="to">Live in CRM</span></div>
<p style="margin-top:22px">Rebuilt Google and Meta campaigns, new landing pages and clean conversion tracking. Leadership now sees which campaigns produce consults and retained clients, not just leads.</p></div>
<div class="case reveal"><span class="case-tag">High-volume personal injury firm</span><h3>Every channel tied to signed cases, plus custom lien tracking.</h3>
<div class="metric-pair"><span class="lbl">Marketing reporting</span><span class="from">Spreadsheets</span><span class="arrow">{icon("arrow")}</span><span class="to">Live dashboard</span></div>
<div class="metric-pair"><span class="lbl">Signed cases sent back to Google and Meta</span><span class="from">Never</span><span class="arrow">{icon("arrow")}</span><span class="to">Automated</span></div>
<p style="margin-top:22px">Leadership now reviews cost per signed case by channel every week and moves budget based on cases, not lead volume. Hospital lien tracking was built into the same dashboard.</p></div>
</div>
<p class="note-small" style="text-align:center;margin-top:22px">Client names withheld for confidentiality. Full case studies shared on your strategy call.</p>'''

# ---------- round 2 components ----------
DRIVE_VIDEO = "https://drive.google.com/file/d/1YlGHNzrhW3onscFSIHpI23v8YrKK19gW/preview"

def video_section():
    return f'''<section class="video-sec" id="video"><div class="wrap video-grid">
<div class="reveal"><span class="eyebrow">Watch &middot; 40 seconds</span><h2>What we do, <span class="accent">in under a minute.</span></h2>
<p style="margin-top:16px;font-size:1.08rem">The short version: we run your ads, connect every lead to your CRM, and show you exactly which dollars turn into signed cases. Then we help your team convert more of them.</p>
<ul class="video-points"><li>{chk()}Google &amp; Meta ads built on signed-case data</li><li>{chk()}ClearSignal reporting your whole firm can trust</li><li>{chk()}AI coaching, intake automation and HubSpot cleanup</li></ul>
<div class="btn-row">{book("Book a Strategy Call","btn-primary","video")}</div></div>
<div class="reveal"><div class="video-frame"><span class="vf-corner tl"></span><span class="vf-corner tr"></span><span class="vf-corner bl"></span><span class="vf-corner br"></span>
<div class="vf-bar"><span class="vf-dots"><i></i><i></i><i></i></span><span class="vf-title">Alchemist Mind Pros &middot; What we do</span><span class="vf-rec"><i></i>0:40</span></div>
<div class="vf-screen"><iframe src="{DRIVE_VIDEO}" title="What Alchemist Mind Pros does" loading="lazy" allow="autoplay; fullscreen" allowfullscreen></iframe></div></div>
<p class="vf-caption">Tap play. Sound on recommended.</p></div>
</div></section>'''

def app_mock():
    rows=[("Google Search","$58,400","412","61%","92","$635"),("Google LSA","$21,300","268","72%","51","$418"),("Meta Ads","$39,700","356","38%","44","$902"),("Reddit Ads","$8,900","74","46%","11","$809"),("ChatGPT Ads","$6,200","41","54%","7","$886"),("Referral / Organic","$0","135","70%","38","$0")]
    trs="".join(f'<tr><td><span class="ch-dot ch{i}"></span>{r[0]}</td><td>{r[1]}</td><td>{r[2]}</td><td>{r[3]}</td><td><b>{r[4]}</b></td><td class="cps">{r[5]}</td></tr>' for i,r in enumerate(rows))
    pts=[18,22,21,27,30,29,34,38,36,41,45,49]; spend=[40,42,41,44,43,45,44,46,45,47,46,48]
    W,H=520,150
    def path(v,mx): return " ".join(("M" if i==0 else "L")+f"{i*W/(len(v)-1):.0f},{H-(x/mx)*H*0.9:.0f}" for i,x in enumerate(v))
    area=path(pts,55)+f" L{W},{H} L0,{H} Z"
    return f'''<div class="app reveal" role="img" aria-label="Illustrative ClearSignal dashboard for your firm">
<div class="app-chrome"><span class="vf-dots"><i></i><i></i><i></i></span><span class="app-url">{icon("shield",12)} app.clearsignal.pro/your-firm/overview</span></div>
<div class="app-body"><aside class="app-side"><div class="app-brand"><img src="assets/amp-logo-256.png" alt="" width="22" height="22">ClearSignal</div>
<div class="tenant"><span class="tenant-av">YF</span><span><b>Your Firm</b><small>Personal Injury &middot; 3 offices</small></span><span class="tenant-chev">&#9662;</span></div>
<nav class="app-nav"><a class="on">{icon("layout",15)}Overview</a><a>{icon("chart",15)}Attribution</a><a>{icon("users",15)}Leads</a><a>{icon("mic",15)}Sales Coach</a><a>{icon("tablet",15)}Check-In</a><a>{icon("file",15)}Reports</a></nav></aside>
<div class="app-main"><div class="app-head"><div><b>Good morning, Your Firm</b><small>Here's what your marketing signed this month</small></div><span class="app-range">Last 30 days &#9662;</span></div>
<div class="app-kpis"><div><span>Ad spend</span><b>$134,500</b></div><div><span>Qualified leads</span><b>742</b><em>+23%</em></div><div><span>Signed cases</span><b>243</b><em>+18%</em></div><div class="hl"><span>Cost per signed case</span><b>$553</b><em>-21%</em></div></div>
<div class="app-chart"><div class="app-chart-h"><b>Signed cases vs. spend</b><span><i class="lg c1"></i>Signed <i class="lg c2"></i>Spend</span></div>
<svg viewBox="0 0 {W} {H}" preserveAspectRatio="none"><defs><linearGradient id="ag" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#C08A4F" stop-opacity=".35"/><stop offset="1" stop-color="#C08A4F" stop-opacity="0"/></linearGradient></defs><path d="{area}" fill="url(#ag)"/><path d="{path(pts,55)}" fill="none" stroke="#C08A4F" stroke-width="2.5"/><path d="{path(spend,55)}" fill="none" stroke="#9AA3AE" stroke-width="1.6" stroke-dasharray="4 4"/></svg></div>
<table class="app-table"><thead><tr><th>Channel</th><th>Spend</th><th>Leads</th><th>Qualified</th><th>Signed</th><th>Cost / signed</th></tr></thead><tbody>{trs}</tbody></table>
</div></div><span class="app-tag">Illustrative demo &middot; your data here</span></div>'''

def lp_mock():
    return f'''<div class="lp-mock reveal" aria-hidden="true"><div class="app-chrome"><span class="vf-dots"><i></i><i></i><i></i></span><span class="app-url">yourfirm.com/car-accident-lawyer</span></div>
<div class="lp-body"><div class="lp-hero"><span class="lp-pill">Free case review &middot; No fee unless we win</span><b>Hurt in a car accident? Get a free case review in 2 minutes.</b><div class="lp-stars">&#9733;&#9733;&#9733;&#9733;&#9733; <small>4.9 from 600+ reviews</small></div></div>
<div class="lp-form"><span>Name</span><span>Phone</span><span>What happened?</span><i>Get My Free Review</i></div></div>
<div class="lp-stats"><div><b>1.4s</b><small>load time</small></div><div><b>A/B</b><small>tested headlines</small></div><div><b>100%</b><small>calls + forms tracked</small></div></div></div>'''

INTAKE = f'''<section class="sec-paper" id="intake"><div class="wrap">
<div class="sec-head center reveal"><span class="eyebrow">Convert</span><h2>More signed cases from the leads <span class="accent">you already pay for.</span></h2><p>Two tools that work alongside ClearSignal: one makes every consult better, the other takes the manual work out of intake for your clients and your team.</p></div>
<div class="tool-grid">
<div class="tool-card reveal"><div class="tool-top"><span class="ico">{icon("mic")}</span><div><h3>AI Sales Coach</h3><p>Every consult scored and coached, automatically.</p></div></div>
<ul class="tool-feats">
<li>{tick()}<div><b>Automatic consult scoring</b><p>Rapport, discovery, objection handling and close, on a fixed legal-intake rubric.</p></div></li>
<li>{tick()}<div><b>Timestamped coaching notes</b><p>Exactly what a top closer would have said, at the moment it mattered.</p></div></li>
<li>{tick()}<div><b>Coaching emails after every call</b><p>Reps get their score and next-step tips without a manager in the loop.</p></div></li>
<li>{tick()}<div><b>Objection playbook + leaderboard</b><p>Your best responses, rep rankings and goals in one place.</p></div></li>
<li>{tick()}<div><b>Tied to lead source and outcome</b><p>See whether it's the leads or the intake, by channel, with ClearSignal.</p></div></li></ul>
<a class="link-arrow" href="ai-sales-coach.html">Explore AI Sales Coach {ARR}</a></div>
<div class="tool-card dark reveal"><div class="tool-top"><span class="ico">{icon("zap")}</span><div><h3>Check-In App</h3><p>Less manual work for clients, staff and admins.</p></div></div>
<ul class="tool-feats">
<li>{tick()}<div><b>Digital check-in and intake forms</b><p>Clients finish paperwork on a tablet or phone instead of a clipboard.</p></div></li>
<li>{tick()}<div><b>Automatic CRM data entry</b><p>Every answer lands in your CRM. No re-keying, no typos.</p></div></li>
<li>{tick()}<div><b>Faster document drafting</b><p>Captured details pre-fill intake documents and drafts, so staff start at 80%, not zero.</p></div></li>
<li>{tick()}<div><b>Instant team notifications</b><p>The right person knows the moment a client arrives or submits.</p></div></li>
<li>{tick()}<div><b>Better experience on both sides</b><p>Clients wait less. Staff spend time on people, not data entry.</p></div></li></ul>
<a class="link-arrow" href="check-in-app.html">Explore the Check-In App {ARR}</a></div>
</div></div></section>'''

HUBSPOT = f'''<section id="hubspot"><div class="wrap split">
<div class="reveal"><span class="eyebrow">Automate</span><h2>HubSpot cleanup and workflows, <span class="accent">done by a certified team.</span></h2>
<p style="margin-top:16px;font-size:1.08rem">Attribution is only as good as the CRM behind it. Our HubSpot-certified team (Reporting and Sales Hub) cleans up messy portals and builds the automations that keep leads from slipping.</p>
{feat_list([("CRM cleanup","Duplicates merged, properties rationalized, lifecycle stages and pipelines that match how your firm actually signs cases."),("Workflows and lead routing","Speed-to-lead alerts, round-robin routing, follow-up sequences and task automation for intake."),("Reporting that matches ClearSignal","Dashboards built on clean data, so marketing, intake and finance finally agree on the numbers.")])}
<div class="btn-row"><a class="btn btn-dark" href="hubspot-crm.html">Explore HubSpot services {ARR}</a></div></div>
<div class="reveal"><div class="flowmock"><div class="fm-h">{icon("zap",16)} Workflow &middot; New PI lead</div>
<div class="fm-step"><span>1</span><div><b>Trigger</b><small>Form or call from Google Ads</small></div></div><div class="fm-line"></div>
<div class="fm-step"><span>2</span><div><b>Route to intake</b><small>Round-robin by office + language</small></div></div><div class="fm-line"></div>
<div class="fm-step"><span>3</span><div><b>Text + task in 60 sec</b><small>Speed-to-lead alert to the rep</small></div></div><div class="fm-line"></div>
<div class="fm-step ok"><span>&#10003;</span><div><b>Signed &rarr; sent to Google &amp; Meta</b><small>Offline conversion via ClearSignal</small></div></div></div></div>
</div></section>'''

def sticky_cta():
    return f'<div class="sticky-cta">{book("Book a Strategy Call","btn-primary","sticky")}</div>'

# =====================================================================
# HOME
# =====================================================================
home_rotate=["see their true cost per signed case.","stop wasting Google Ads spend.","know which channel actually signs clients.","train Google to find clients, not clicks.","turn more consults into signed retainers.","scale past $100K a month without the waste."]
home = f'''
<section class="hero"><div class="wrap hero-grid">
<div>
<span class="eyebrow">Performance marketing for law firms</span>
<h1><span class="static">We help law firms</span><span class="rotator" aria-live="polite">{"".join(f"<span>{r}</span>" for r in home_rotate)}</span></h1>
<p class="lede">Alchemist Mind Pros runs <strong>Google and Meta ads for law firms</strong> and connects every dollar to the cases it signs with <strong>ClearSignal</strong>, our AI-powered reporting dashboard. From $10K a month to $2M+, you make decisions on cost per signed case, not clicks.</p>
<div class="btn-row">{book("Book a Strategy Call","btn-primary","home-hero")}<a href="#calculator" class="btn btn-ghost">Calculate your cost per signed case</a></div>
<div class="trust-row">{gp_badge()}<span class="trust-item">{icon("check",16)}95%+ client retention</span><span class="trust-item">{icon("check",16)}Thousands of signed cases attributed</span><span class="trust-item">{icon("check",16)}Month-to-month</span></div>
</div>
<div style="position:relative">{dash_mock()}</div>
</div></section>
{STATS}
{video_section()}

<section id="problem"><div class="wrap">
<div class="sec-head reveal"><span class="eyebrow">The problem</span><h2>Your ads report leads. <span class="accent">Your partners care about signed cases.</span></h2><p>Most law firms spending serious money on ads can tell you their cost per lead. Almost none can tell you which channel, campaign or keyword produced last month's signed cases. That gap is where budget disappears.</p></div>
<div class="grid-4">
<div class="card reveal"><span class="pain-num">01</span><h3>No cost per signed case</h3><p>You know what a lead costs. You don't know which leads signed, so you can't tell a $300 lead that signs from one that never answers.</p><div class="cost">Budget follows volume, not revenue</div></div>
<div class="card reveal"><span class="pain-num">02</span><h3>Google is optimizing for the wrong thing</h3><p>Smart bidding chases form fills and calls. Without signed-case data flowing back, the algorithm gets better at finding cheap, unqualified leads.</p><div class="cost">More leads, same caseload</div></div>
<div class="card reveal"><span class="pain-num">03</span><h3>A CRM nobody trusts</h3><p>Duplicate contacts, missing sources and agency decks that never match intake. Every meeting starts with whose number is right.</p><div class="cost">Decisions made on gut feel</div></div>
<div class="card reveal"><span class="pain-num">04</span><h3>Intake runs on manual work</h3><p>Clipboards, re-keying and unreviewed calls. Leads go cold and you can't tell if a bad month is marketing or intake.</p><div class="cost">Paid leads leak out the back door</div></div>
</div></div></section>

<section class="sec-paper" id="what-we-do"><div class="wrap">
<div class="sec-head center reveal"><span class="eyebrow">What we do</span><h2>One team for the full path from <span class="accent">click to signed case.</span></h2><p>Think of it like a football program: recruiting, film room, coaching and the playbook all have to work together. We run the ads, measure what signs, automate the CRM and help intake close more of what comes in.</p></div>
<div class="pillars four">
<div class="pillar reveal"><span class="step">01 &middot; Acquire</span><h3>PPC Management</h3><div class="tag">Our strongest suit. Official Google Partner.</div><p>Paid search, paid social and high-converting landing pages, built for intake.</p>
<ul><li><a href="google-ads.html">{chk()}Google Ads + LSA</a></li><li><a href="meta-ads.html">{chk()}Meta Ads</a></li><li><a href="reddit-ads.html">{chk()}Reddit Ads</a></li><li><a href="chatgpt-ads.html">{chk()}ChatGPT Ads</a></li><li><a href="ppc-management.html#landing-pages">{chk()}Landing pages</a></li></ul>
<a class="link-arrow" href="ppc-management.html">PPC Management {ARR}</a></div>
<div class="pillar featured reveal"><span class="badge-core">Core offer</span><span class="step">02 &middot; Measure</span><h3>ClearSignal</h3><div class="tag">AI-powered reporting dashboard</div><p>Cost per qualified lead and cost per signed case by channel, live.</p>
<ul><li>{chk()}Cross-channel attribution</li><li>{chk()}Offline conversion sync</li><li>{chk()}HubSpot, Salesforce, Lead Docket</li></ul>
<a class="link-arrow" href="clearsignal.html">See ClearSignal {ARR}</a></div>
<div class="pillar reveal"><span class="step">03 &middot; Convert</span><h3>Intake Tools</h3><div class="tag">Close more, with less manual work</div><p>Coach every consult and automate intake for clients and staff.</p>
<ul><li><a href="ai-sales-coach.html">{chk()}AI Sales Coach</a></li><li><a href="check-in-app.html">{chk()}Check-In App</a></li></ul>
<a class="link-arrow" href="#intake">Intake tools {ARR}</a></div>
<div class="pillar reveal"><span class="step">04 &middot; Automate</span><h3>HubSpot CRM</h3><div class="tag">Certified cleanup and workflows</div><p>A clean CRM and automations that keep every lead moving.</p>
<ul><li>{chk()}Portal cleanup</li><li>{chk()}Workflows + lead routing</li><li>{chk()}Dashboards</li></ul>
<a class="link-arrow" href="hubspot-crm.html">HubSpot services {ARR}</a></div>
</div></div></section>

<section class="sec-dark" id="clearsignal"><div class="wrap">
<div class="split" style="align-items:end;margin-bottom:48px"><div class="reveal"><span class="eyebrow">Our core offer &middot; ClearSignal</span><h2>Picture your firm's numbers, <span class="accent">all in one place.</span></h2></div>
<div class="reveal"><p style="font-size:1.08rem">Built inside a real law firm's marketing operation, ClearSignal sits on top of the CRM you already use. It matches every signed case to the ad, keyword and call that produced it, then sends that outcome to Google and Meta so they find more clients like your best ones.</p></div></div>
{app_mock()}
<div class="grid-3" style="margin-top:56px">
<div class="mini-feat reveal">{tick()}<div><b>Cost per signed case, by channel</b><p>Updated live, not in a monthly PDF.</p></div></div>
<div class="mini-feat reveal">{tick()}<div><b>Offline conversion sync</b><p>Signed cases flow back to Google and Meta automatically.</p></div></div>
<div class="mini-feat reveal">{tick()}<div><b>One source of truth</b><p>Ads, calls, CRM and intake in one view your CFO trusts.</p></div></div></div>
<div class="btn-row" style="justify-content:center"><a class="btn btn-primary" href="clearsignal.html">Explore ClearSignal {ARR}</a>{book("Book a Live Demo","btn-ghost","home-cs")}</div>
</div></section>

{INTAKE}

<section id="ppc"><div class="wrap">
<div class="split" style="margin-bottom:56px;align-items:end"><div class="reveal"><span class="eyebrow">PPC Management</span><h2>Paid media that's judged on <span class="accent">signed cases.</span></h2></div>
<div class="reveal"><p style="font-size:1.08rem">Google Ads is where most firms spend the most and waste the most. As an official Google Partner, we build on clean conversion tracking, ruthless search term discipline and signed-case feedback, then expand into Meta, Reddit and ChatGPT once the foundation is right.</p><div style="margin-top:18px">{gp_badge()}</div></div></div>
{channel_tiles()}
<div class="lp-callout reveal"><div><span class="eyebrow">Included with PPC</span><h3>High-converting landing pages, built for intake.</h3><p>Ads only get the click. We build fast, practice-area landing pages with the trust signals, call tracking and forms that turn that click into a consult, then A/B test them against cost per signed case.</p>
<ul class="lp-list"><li>{chk()}Practice-area and city pages</li><li>{chk()}Sub-2-second load times</li><li>{chk()}Every call and form tracked</li><li>{chk()}Ongoing A/B testing</li></ul>
<a class="link-arrow" href="ppc-management.html#landing-pages">See how we build them {ARR}</a></div>{lp_mock()}</div>
</div></section>

{HUBSPOT}

<section class="sec-paper" id="who"><div class="wrap">
<div class="sec-head reveal"><span class="eyebrow">Who we help</span><h2>Built for law firms that <span class="accent">take growth seriously.</span></h2><p>We do our best work with consultation-based firms that already invest in advertising, want to know exactly what it's producing, and are ready to scale what works.</p></div>
<div class="fit">
<div class="fit-box reveal"><h3>{icon("check",22)} You're a fit if</h3><ul>
<li>{chk()}You invest at least $10K a month in ads and are comfortable scaling when the numbers prove out</li>
<li>{chk()}You're spending (or heading toward) $100K+ a month. We manage budgets of $2M+ a month</li>
<li>{chk()}Google Ads is a major channel and you suspect it's leaking budget</li>
<li>{chk()}You can't confidently answer &ldquo;what does a signed case cost us, by channel?&rdquo;</li>
<li>{chk()}You use (or are ready to use) a CRM like HubSpot, Salesforce or Lead Docket</li></ul></div>
<div class="fit-box no reveal"><h3>{icon("x",22)} Probably not a fit if</h3><ul>
<li>{icon("x",18,"x")}You're looking for the cheapest possible ad management</li>
<li>{icon("x",18,"x")}You want vanity metrics and monthly PDFs</li>
<li>{icon("x",18,"x")}You aren't willing to share intake and CRM outcomes</li></ul></div>
</div>
<div class="chips reveal"><span class="chip">Personal Injury</span><span class="chip">Estate Planning</span><span class="chip">Elder Law</span><span class="chip">Lemon Law</span><span class="chip">Family Law</span><span class="chip">Criminal Defense</span><span class="chip">Employment Law</span><span class="chip">Mass Tort</span><span class="chip">Any consult-based practice</span></div>
<div class="roles">
<div class="role reveal"><b>Managing Partner / CEO</b><p>Know what growth costs and where the next dollar should go.</p></div>
<div class="role reveal"><b>CFO / Firm Administrator</b><p>Marketing spend tied to signed cases you can reconcile against the books.</p></div>
<div class="role reveal"><b>Marketing Director</b><p>Channel-level proof to defend budget and cut what isn't working.</p></div>
<div class="role reveal"><b>Intake Manager</b><p>Scored consults, automated data entry and fewer leads going cold.</p></div>
</div></div></section>

<section id="results"><div class="wrap">
<div class="sec-head center reveal"><span class="eyebrow">Results</span><h2>Numbers our clients <span class="accent">actually care about.</span></h2><p>We report on cost per lead, cost per qualified lead and cost per signed case, so wins show up where it matters: the caseload.</p></div>
{CASES}
</div></section>

{quiz()}
{calculator()}

<section id="process"><div class="wrap">
<div class="sec-head reveal"><span class="eyebrow">How we work</span><h2>From first call to <span class="accent">fully live.</span></h2><p>No long onboarding. No long-term contract. Most firms see their first cost-per-signed-case report within weeks.</p></div>
{steps([("Strategy call","30 minutes with Tre. We look at your goals, spend and current reporting."),("Audit with your numbers","We review your ad accounts, tracking and CRM and show you where budget leaks."),("Build and connect","Conversion tracking, HubSpot cleanup, offline conversion sync and ClearSignal wired to your stack."),("Launch and optimize","Campaigns and landing pages rebuilt around signed-case data, optimized weekly."),("Monthly case review","A clear review of cost per signed case by channel and where to move budget next.")])}
</div></section>

<section class="sec-paper" id="founder"><div class="wrap founder">
<div class="headshot reveal"><img src="assets/tre-headshot.jpg" width="800" height="1000" loading="lazy" alt="Tre Forte, founder of Alchemist Mind Pros" onerror="this.remove()"><span class="initials">TF</span><div class="headshot-tag"><b>Tre Forte</b>Founder &amp; Fractional CMO</div></div>
<div class="reveal"><span class="eyebrow">Meet the founder</span><h2>Built by a CMO who sat <span class="accent">inside law firms.</span></h2>
<p style="margin-top:18px;font-size:1.06rem">Tre Forte spent years as a fractional CMO inside law firms, accountable for signed cases, not clicks. The reporting he needed didn't exist, so he built it. That system became ClearSignal, and the approach became Alchemist Mind Pros.</p>
<p style="margin-top:14px;font-size:1.06rem">His time playing collegiate football at Ohio State shaped how the team works: watch the film every week, be honest about what the tape shows, and adjust the game plan before the next snap.</p>
<div class="creds"><div class="cred">{icon("dollar",18)}$20M+ in managed ad spend</div><div class="cred">{icon("trophy",18)}Co-founded an Inc. 5000 agency</div><div class="cred">{icon("users",18)}Fractional CMO for law firms</div><div class="cred">{icon("target",18)}Ohio State collegiate football</div></div>
<div class="btn-row">{book("Book a Call With Tre","btn-dark","founder")}<a class="btn btn-outline" href="{LINKEDIN}" target="_blank" rel="noopener">Connect on LinkedIn</a></div></div>
</div></section>

<section id="faq"><div class="wrap">
<div class="sec-head center reveal"><span class="eyebrow">FAQ</span><h2>Questions firms ask us</h2></div>
{faq([
("What does Alchemist Mind Pros actually do?","We're a performance marketing agency for law firms. We manage paid media (Google Ads, Meta, Reddit and ChatGPT ads) and build the landing pages behind it, connect everything to your CRM with ClearSignal so you can see cost per qualified lead and cost per signed case by channel, clean up and automate HubSpot, and offer intake tools (AI Sales Coach and the Check-In App) to help you convert more of the leads you pay for."),
("What budget do you need?","At least $10K a month in ad spend, with the comfort to scale when results prove out. Most of our best results come from firms investing $100K+ a month, and we manage accounts spending more than $2M a month."),
("Do I have to use ClearSignal to work with you on PPC?","No. Many clients start with PPC management and add ClearSignal later. Our PPC is strongest when signed-case data flows back into the ad platforms, which is what ClearSignal does."),
("Do you lock us into a contract?","No. We work month-to-month and keep 95%+ of our clients because the numbers justify it."),
("Can you fix our HubSpot?","Yes. Our HubSpot-certified team handles portal cleanup, lifecycle stages, pipelines, workflows, lead routing and reporting."),
("Will this replace our CRM or intake software?","No. ClearSignal sits on top of the CRM you already use, with native two-way sync for HubSpot, Salesforce and Lead Docket, and custom connections for most tools with API access."),
("Will you share our results with other firms?","Never by name. We highlight anonymized wins only, and we never display client names or logos without written permission."),
])}
</div></section>
{cta_band()}
{sticky_cta()}
'''
page("index.html","Alchemist Mind Pros | Law Firm PPC, Attribution & HubSpot | Cost Per Signed Case","Google Partner agency for law firms investing $10K to $2M+ a month in ads. Google and Meta ads, landing pages, ClearSignal attribution, AI intake tools and HubSpot.",home,"index.html")

# =====================================================================
# CLEARSIGNAL
# =====================================================================
cs = sub_hero("ClearSignal","ClearSignal &middot; AI-powered reporting dashboard","An AI-powered reporting dashboard that",
 "ClearSignal connects your ad platforms, call tracking, CRM and intake into one live dashboard, sends signed-case outcomes back to Google and Meta, and shows your true <strong>cost per signed case</strong> by channel.",
 app_mock().replace(' reveal',''), ctas=book("Book a Live Demo","btn-primary","cs-hero")+'<a href="#calculator" class="btn btn-ghost">See your hidden number</a>',
 rotate=["shows your true cost per signed case.","tells you which channel signs clients.","sends signed cases back to Google and Meta.","replaces the Monday spreadsheet.","gives your CFO numbers they trust."],
 trust=trust_row(["Built inside a real law firm","No rip-and-replace","Typically live in about 2 weeks"])) + f'''
<section><div class="wrap">
<div class="sec-head reveal"><span class="eyebrow">Why firms need it</span><h2>You're flying blind between <span class="accent">ad spend and signed clients.</span></h2></div>
{feature_cards([("eye-off","CPL without context","You know what a lead costs, but not which leads signed or which channel is quietly wasting budget."),("loop","Algorithms learning the wrong lesson","Google and Meta only see form fills and calls, so they get better at finding leads that never retain."),("file","Reports nobody trusts","Agency decks, CRM exports and intake spreadsheets that never reconcile. Every meeting starts with whose number is right.")])}
</div></section>

<section class="sec-paper"><div class="wrap">
<div class="sec-head center reveal"><span class="eyebrow">What's inside</span><h2>Everything between the click and the <span class="accent">signed retainer.</span></h2></div>
{feature_cards([("chart","Multi-channel attribution","Google Ads, LSA, Meta, Reddit, CallRail and organic, matched to CRM outcomes at the lead level."),("zap","Offline conversion sync","Signed-case outcomes sent to Google and Meta conversion APIs automatically, so bidding targets clients."),("link","Native CRM sync","Two-way sync with HubSpot, Salesforce and Lead Docket. Custom connections for most tools with API access."),("layout","Automated reporting","Cost per lead, cost per qualified lead and cost per signed case by channel, campaign and practice area."),("map","Local intelligence","Local rankings, brand monitoring and competitor visibility in the same view as your paid data."),("shield","Practice-specific modules","Hospital lien tracking for PI, consult-to-retainer tracking for estate planning, and custom journey mapping.")])}
</div></section>

<section class="sec-dark"><div class="wrap">
<div class="sec-head center reveal"><span class="eyebrow">The feedback loop</span><h2>Most firms train Google to find more leads. <span class="accent">ClearSignal trains it to find more clients.</span></h2></div>
<div class="flow reveal">
<div class="flow-step"><div class="flow-dot">01</div><h3>A lead or call comes in</h3><p>ClearSignal captures the click ID, source and campaign.</p></div>
<div class="flow-step"><div class="flow-dot">02</div><h3>The case signs (or doesn't)</h3><p>Your CRM records the outcome. ClearSignal matches it automatically.</p></div>
<div class="flow-step"><div class="flow-dot">03</div><h3>Outcomes go back to the platforms</h3><p>Signed cases are sent to Google and Meta via offline conversion APIs.</p></div>
<div class="flow-step"><div class="flow-dot">04</div><h3>The algorithm finds more like them</h3><p>Bidding shifts toward people who look like your best clients. CAC drops over time.</p></div>
</div></div></section>

<section><div class="wrap">
<div class="sec-head reveal"><span class="eyebrow">Compare</span><h2>What are you actually comparing ClearSignal to?</h2><p>Hiring an analyst runs $70K to $100K+ a year before tools, with months to ramp. Spreadsheets break at scale. Legal CRMs track cases, not marketing.</p></div>
<div class="table-wrap reveal"><table>
<tr><th>Capability</th><th class="us">ClearSignal</th><th>Generic legal CRM</th><th>Call tracking only</th><th>Spreadsheets</th></tr>
<tr><td>Multi-channel ad attribution</td><td class="us y">&#10003;</td><td class="n">&ndash;</td><td class="p">Partial</td><td class="p">Manual</td></tr>
<tr><td>Cost per signed case by channel</td><td class="us y">&#10003;</td><td class="n">&ndash;</td><td class="n">&ndash;</td><td class="p">Manual</td></tr>
<tr><td>Offline conversion sync to Google + Meta</td><td class="us y">&#10003;</td><td class="n">&ndash;</td><td class="p">Partial</td><td class="n">&ndash;</td></tr>
<tr><td>AI call scoring and coaching</td><td class="us y">&#10003;</td><td class="n">&ndash;</td><td class="p">Partial</td><td class="n">&ndash;</td></tr>
<tr><td>Native HubSpot, Salesforce, Lead Docket sync</td><td class="us y">&#10003;</td><td class="p">Own data only</td><td class="p">Partial</td><td class="n">&ndash;</td></tr>
<tr><td>Built for legal intake</td><td class="us y">&#10003;</td><td class="y">&#10003;</td><td class="n">&ndash;</td><td class="n">&ndash;</td></tr>
</table></div><p class="note-small">Reflects general category capabilities as of 2026, not specific competitors.</p>
</div></section>

<section class="sec-paper"><div class="wrap"><div class="sec-head center reveal"><span class="eyebrow">Integrations</span><h2>No rip-and-replace.</h2><p>ClearSignal sits on top of what you already use. If an integration isn't feasible, we'll tell you on the first call.</p></div>
<div class="integrations reveal">{"".join(f'<span class="int">{i}</span>' for i in ["Google Ads","Google LSA","Meta Ads","Reddit Ads","CallRail","HubSpot","Salesforce","Lead Docket","GA4","Google Tag Manager","Any tool with an API"])}</div></div></section>

{calculator()}

<section id="pricing"><div class="wrap">
<div class="sec-head center reveal"><span class="eyebrow">Pricing</span><h2>Simple plans. <span class="accent">No long-term contract.</span></h2><p>Final pricing depends on integrations and volume. We'll map it to your stack on the demo.</p></div>
<div class="pricing">
<div class="price reveal"><h3>ClearSignal Core</h3><p>Attribution starter</p><div class="amt"><span class="from">From</span><br>$397<small>/mo</small></div><ul><li>{chk()}Single-channel dashboard</li><li>{chk()}One CRM integration</li><li>{chk()}Weekly automated reporting</li><li>{chk()}Local intelligence</li></ul>{book("Book a Demo","btn-outline","price-core")}</div>
<div class="price hot reveal"><span class="badge-core">Most popular</span><h3>Complete Suite</h3><p>ClearSignal + AI Sales Coach + Check-In App</p><div class="amt"><span class="from">From</span><br>$1,297<small>/mo</small></div><ul><li>{chk()}Full multi-channel attribution</li><li>{chk()}Offline conversion sync</li><li>{chk()}AI coaching on every consult</li><li>{chk()}Digital lobby check-in</li></ul>{book("Book Suite Demo","btn-primary","price-suite")}</div>
<div class="price reveal"><h3>ClearSignal Growth</h3><p>Full attribution</p><div class="amt"><span class="from">From</span><br>$797<small>/mo</small></div><ul><li>{chk()}Multi-channel attribution</li><li>{chk()}Native CRM sync</li><li>{chk()}Offline conversion sync</li><li>{chk()}Custom integrations available</li></ul>{book("Book a Demo","btn-outline","price-growth")}</div>
</div>
<div class="addons"><div class="addon reveal"><div><b>Enterprise</b><br><span>White-label, lien tracking, priority support</span></div><span class="amt2">Custom</span></div><div class="addon reveal"><div><b>AI Sales Coach</b><br><span>150 scored calls/mo, then $3/call</span></div><span class="amt2">$497/mo</span></div><div class="addon reveal"><div><b>Check-In App</b><br><span>14-day free trial</span></div><span class="amt2">$247/mo</span></div></div>
</div></section>

<section class="sec-paper"><div class="wrap"><div class="sec-head center reveal"><span class="eyebrow">FAQ</span><h2>ClearSignal questions</h2></div>
{faq([("Does it replace my CRM?","No. ClearSignal sits on top of your existing CRM and reads outcomes from it."),("How long does setup take?","Most firms are live in about two weeks. Timing depends mainly on how quickly we get account access."),("How is client data secured?","Data is encrypted in transit and at rest, and access is scoped per firm. We'll review security details with your team on the call."),("Can I try it before I commit?","ClearSignal is demo-only because we demo on live accounts, not sandboxes. The Check-In App has a 14-day free trial."),("Is it only for PI and estate planning?","No. It works for any consultation-based practice. We map your terminology and client journey during onboarding."),("Do I need Alchemist Mind Pros to run my ads to use it?","No. ClearSignal works with in-house teams and other agencies too.")])}
</div></section>
{cta_band("See your cost per signed case, live.","Book a demo and we'll walk through ClearSignal on real data, map it to your stack and give you an exact price.")}
'''
page("clearsignal.html","ClearSignal | AI-Powered Reporting Dashboard for Law Firms | Cost Per Signed Case","ClearSignal connects ad spend, intake and CRM to show law firms their true cost per signed case, and sends outcomes back to Google and Meta.",cs)

# =====================================================================
# AI SALES COACH
# =====================================================================
coach_mock=f'''<div class="mock reveal"><div class="dash-top"><div><div class="dash-title" style="color:var(--text)">Consult scorecard</div><div class="dash-sub">Intake call &middot; 14 min &middot; PI auto accident</div></div><span class="live" style="background:var(--copper-soft);color:var(--copper-deep)">4.2 / 5</span></div>
<div class="score-row"><span>Rapport</span><div class="bar"><i data-w="90%"></i></div><b>4.5</b></div>
<div class="score-row"><span>Discovery</span><div class="bar"><i data-w="80%"></i></div><b>4.0</b></div>
<div class="score-row"><span>Objection handling</span><div class="bar"><i data-w="60%"></i></div><b>3.0</b></div>
<div class="score-row"><span>Close</span><div class="bar"><i data-w="90%"></i></div><b>4.5</b></div>
<div class="coach-note"><b>COACHING NOTE &middot; 08:42</b>When the caller said &ldquo;I need to talk to my wife first,&rdquo; a top closer would acknowledge it, then offer to schedule a three-way call today so the case doesn't go cold.</div></div>'''
coach = sub_hero("AI Sales Coach","AI Sales Coach","Every consult scored. <span class='accent'>Every rep coached.</span>",
 "Submit a call recording or transcript and AI Sales Coach scores it on rapport, discovery, objection handling and close, then tells your rep exactly what a top closer would have said at the moment it mattered.",
 coach_mock, trust=trust_row(["Fixed rubric + human review loop","Works with your call recording tool","Pairs with ClearSignal"])) + f'''
<section><div class="wrap"><div class="sec-head reveal"><span class="eyebrow">The problem</span><h2>You're paying for leads that <span class="accent">die on the intake call.</span></h2><p>A bad marketing month and a bad intake month look identical in the numbers. Without call review, you can't tell which one you have, and nobody has time to listen to every call.</p></div>
{feature_cards([("mic","Calls nobody reviews","Managers spot-check a handful of calls a month, if that. Patterns go unnoticed for quarters."),("users","Inconsistent reps","Your best closer signs half her consults. Your newest rep signs one in five. Nobody knows exactly why."),("dollar","Expensive leads, cheap follow-through","At $300+ per lead, every fumbled objection is real money walking out the door.")])}</div></section>
<section class="sec-paper"><div class="wrap split"><div class="reveal"><span class="eyebrow">How it helps</span><h2>Like game film for <span class="accent">your intake team.</span></h2><p style="margin-top:14px">Great teams review film after every game. AI Sales Coach does that for every consult, automatically, so coaching is based on what actually happened on the call.</p>
{feat_list([("Automatic scoring","Each call scored on rapport, discovery, objection handling and close using a fixed legal-intake rubric."),("Plain-language coaching notes","Specific, timestamped feedback reps can apply on the next call."),("Objection playbook","The objections your callers raise most, with the responses that are working for your best closers."),("Coaching emails after every call","Reps get their score and specific next-step tips automatically, no manager required."),("Leaderboard and goals","Rep rankings and goal tracking so managers know who needs help and who to learn from.")])}</div>
<div class="reveal">{coach_mock.replace(' reveal','')}</div></div></section>
<section class="sec-dark"><div class="wrap split rev"><div class="reveal">{dash_mock("Sign rate by rep vs. channel",[("Rep A","48%","48%"),("Rep B","36%","36%"),("Rep C","22%","22%"),("Rep D","19%","19%")])}</div>
<div class="reveal"><span class="eyebrow">Better together</span><h2>Pair it with ClearSignal to see <span class="accent">marketing and intake in one view.</span></h2><p style="margin-top:14px">Tie call scores to the channel and campaign that produced the lead. Finally answer the question every partner asks: is it the leads, or is it intake?</p><div class="btn-row"><a class="btn btn-primary" href="clearsignal.html">Explore ClearSignal {ARR}</a></div></div></div></section>
<section><div class="wrap"><div class="mini-cta reveal" style="margin-top:0"><div><b>AI Sales Coach: $497/mo</b><p>Includes 150 scored calls per month, then $3 per call. Included in the Complete Suite.</p></div>{book("Book a Demo","btn-dark","coach-price")}</div>
<div style="margin-top:56px">{faq([("What do I need to submit?","A call recording or transcript. It works with most call recording and tracking tools you already use."),("Is this a generic AI wrapper?","No. Scoring uses a fixed rubric built for legal intake, with a human review loop to keep feedback accurate."),("Can I customize the rubric?","Yes. We map scoring to your intake process and terminology during onboarding."),("Will my reps feel micromanaged?","The best teams use it as coaching, not surveillance. Reps get specific notes they can use on the next call, and wins are celebrated on the leaderboard.")])}</div></div></section>
{cta_band("Turn more consults into signed retainers.","See AI Sales Coach score one of your own calls on a live demo.")}
'''
page("ai-sales-coach.html","AI Sales Coach for Law Firm Intake | Score & Coach Every Consult | Alchemist Mind Pros","AI Sales Coach scores every law firm intake call on rapport, discovery, objection handling and close, with coaching notes for each rep.",coach)

# =====================================================================
# CHECK-IN APP
# =====================================================================
tab=f'''<div class="tablet reveal"><div class="tablet-screen"><div class="tlogo"><i></i>Welcome to Your Law Firm</div>
<div class="tfield filled">Maria Gonzalez</div><div class="tfield filled">(305) 555-0142</div><div class="tfield">Reason for visit</div><div class="tfield">How did you hear about us?</div><div class="tbtn">Check In</div></div>
<div class="notif"><i></i><span><b>Front desk:</b> Maria Gonzalez checked in for her 2:00 consult. CRM updated.</span></div></div>'''
chk_page = sub_hero("Check-In App","Check-In App &middot; Intake automation","Less paperwork. Faster intake. <span class='accent'>Happier clients and staff.</span>",
 "The Check-In App takes manual work off your clients, your front desk and your admins. Clients complete check-in and intake on a tablet or phone, and every answer flows straight into your CRM and pre-fills your documents, so your team spends time on people, not data entry.",
 tab, ctas=book("Start a 14-Day Free Trial","btn-primary","checkin-hero")+'<a href="#how" class="btn btn-ghost">See how it works</a>',
 trust=trust_row(["No re-keying","Pre-fills CRM records and documents","14-day free trial"])) + f'''
<section><div class="wrap"><div class="sec-head reveal"><span class="eyebrow">The manual-work problem</span><h2>Your team is retyping what <span class="accent">clients already told you.</span></h2><p>Every clipboard, PDF form and sticky note becomes a data entry task. It slows intake, introduces errors and burns hours your staff could spend with clients.</p></div>
{feature_cards([("file","Re-keying everything","Staff copy intake answers into the CRM, then again into documents. Hours a week, plus typos."),("clock","Slow, clunky client experience","Clients wait on paperwork and repeat the same details to three different people."),("eye-off","Data that never connects","Sources, notes and intake details stay on paper, so reporting and attribution break.")])}</div></section>
<section class="sec-paper" id="how"><div class="wrap"><div class="sec-head center reveal"><span class="eyebrow">How it works</span><h2>Capture once. <span class="accent">Use everywhere.</span></h2></div>
{feature_cards([("tablet","1. Clients check in and complete intake","On a lobby tablet or their own phone. Branded to your firm, with the questions your practice needs."),("link","2. Data lands in your CRM automatically","Contact details, case facts and lead source sync to HubSpot, Salesforce or Lead Docket instantly."),("file","3. Documents start pre-filled","Captured details populate intake documents and drafts, so staff review and finish instead of starting from scratch."),("bell","4. The right person is notified","Front desk, attorney or intake rep gets an alert the moment a client arrives or submits."),("chart","5. Admins see everything","Check-in volume, wait times and completion rates in one view, connected to ClearSignal."),("shield","6. Consistent, secure records","Every client follows the same process, with the same fields, every time.")])}
</div></section>
<section><div class="wrap"><div class="sec-head center reveal"><span class="eyebrow">Who it helps</span><h2>Better for everyone who touches intake.</h2></div>
<div class="grid-3">
<div class="card reveal"><div class="ico">{icon("users")}</div><h3>Your clients</h3><p>Less waiting, no clipboards, and no repeating their story. A modern first impression that matches the firm they hired.</p></div>
<div class="card reveal"><div class="ico">{icon("zap")}</div><h3>Your team</h3><p>No more data entry or retyping. Faster drafting, fewer errors and more time for the work that actually needs a person.</p></div>
<div class="card reveal"><div class="ico">{icon("layout")}</div><h3>Admins and partners</h3><p>Streamlined processes, consistent data and visibility into intake, without chasing paperwork.</p></div></div>
<div class="mini-cta reveal"><div><b>Check-In App: $247/mo</b><p>Try it free for 14 days. Included in the Complete Suite with ClearSignal and AI Sales Coach.</p></div>{book("Start Free Trial","btn-dark","checkin-price")}</div></div></section>
<section class="sec-paper"><div class="wrap">{faq([("What hardware do I need?","Any modern tablet for the lobby, and clients can also complete intake on their own phone."),("Can we customize the intake questions and documents?","Yes. Questions, branding, the fields that sync to your CRM and the documents they pre-fill are configured for your firm."),("Which CRMs does it sync with?","HubSpot, Salesforce and Lead Docket natively, plus custom connections for most tools with an API."),("Is there a contract?","No. Month-to-month after your 14-day free trial.")])}</div></section>
{cta_band("Take the manual work out of intake.","Start a free 14-day trial or see the Check-In App alongside ClearSignal on a demo.",["14-day free trial","Pre-fills your CRM and documents","Month-to-month"])}
'''
page("check-in-app.html","Law Firm Check-In & Intake Automation App | Alchemist Mind Pros","Digital check-in and intake that syncs to your CRM and pre-fills documents. Less manual work for clients, staff and admins. 14-day free trial.",chk_page)

# =====================================================================
# PPC OVERVIEW
# =====================================================================
ppc_vis=f'''<div class="dash reveal"><div class="dash-top"><div><div class="dash-title">Account audit snapshot</div><div class="dash-sub">Google Ads &middot; PI firm &middot; $85K/mo</div></div><span class="live" style="color:#E8A07E;background:rgba(194,85,63,.14)"><i style="background:#E8A07E"></i>4 ISSUES</span></div>
<div class="bars">
<div class="bar-row"><span>Wasted terms</span><div class="bar"><i data-w="72%"></i></div><b>$14.2K</b></div>
<div class="bar-row"><span>Bad conv. goals</span><div class="bar"><i data-w="55%"></i></div><b>3 of 5</b></div>
<div class="bar-row"><span>No offline sync</span><div class="bar"><i data-w="100%"></i></div><b>0%</b></div>
<div class="bar-row"><span>Overlap</span><div class="bar"><i data-w="38%"></i></div><b>18%</b></div></div>
<div class="ticker"><div><span class="ok">&rarr;</span> Recommendation: import signed cases as primary conversion</div><div><span class="ok">&rarr;</span> Recommendation: 212 negatives across 9 campaigns</div></div><span class="illus">Illustrative data</span></div>'''
ppc = sub_hero("PPC Management","PPC Management &middot; Official Google Partner","Law firm PPC that's judged on",
 "We manage Google, Meta, Reddit and ChatGPT ads for law firms spending $10K to $100K+ a month. Every campaign is built on clean tracking and optimized on what matters: <strong>cost per signed case</strong>.",
 ppc_vis, ctas=book("Get Your Account Audited","btn-primary","ppc-hero")+'<a href="#channels" class="btn btn-ghost">See channels</a>',
 rotate=["signed cases, not clicks.","cost per qualified lead.","revenue your CFO can verify.","what actually hits the caseload."],
 trust='<div class="trust-row">'+gp_badge()+f'<span class="trust-item">{icon("check",16)}$20M+ managed</span><span class="trust-item">{icon("check",16)}Month-to-month</span></div>') + f'''
<section><div class="wrap"><div class="sec-head reveal"><span class="eyebrow">Why most law firm PPC underperforms</span><h2>The ads aren't the problem. <span class="accent">The scoreboard is.</span></h2><p>If your campaigns optimize for form fills, the platform will happily deliver cheap, unqualified ones. We fix the scoreboard first, then the campaigns.</p></div>
{feature_cards([("target","Wrong conversion goals","Page views, button clicks and 10-second calls counted as conversions, teaching Google to chase junk."),("search","Search term leakage","Broad match and loose PMax spending on job seekers, free-advice hunters and the wrong practice areas."),("eye-off","No outcome feedback","Signed cases never make it back to the ad platforms, so bidding never improves where it counts.")])}</div></section>
<section class="sec-paper" id="channels"><div class="wrap"><div class="sec-head center reveal"><span class="eyebrow">Channels</span><h2>Google first. <span class="accent">Then everywhere your clients are.</span></h2></div>{channel_tiles()}</div></section>
<section class="sec-dark"><div class="wrap split"><div class="reveal"><span class="eyebrow">What's included</span><h2>Everything it takes to run paid media <span class="accent">like a CFO is watching.</span></h2>
{feat_list([("Full account audit","Tracking, structure, search terms, budgets and landing pages, with a prioritized fix list."),("Conversion tracking and offline conversion imports","GTM, GA4, call tracking and CRM outcomes wired so platforms learn from signed cases."),("Campaign build and management","Search, LSA, PMax, Meta, Reddit and ChatGPT campaigns managed weekly by specialists."),("Landing pages that convert","Practice-area pages built for speed, trust and intake, with A/B testing."),("Reporting on cases, not clicks","Cost per lead, cost per qualified lead and cost per signed case, by channel, in ClearSignal.")])}</div>
<div class="reveal">{dash_mock()}</div></div></section>
<section class="sec-paper" id="landing-pages"><div class="wrap split"><div class="reveal"><span class="eyebrow">Landing pages</span><h2>High-converting pages that <span class="accent">turn clicks into consults.</span></h2>
<p style="margin-top:14px">Sending paid traffic to a generic homepage is the fastest way to waste budget. We build dedicated pages for each practice area, market and campaign, designed for one job: getting the right person to call or submit.</p>
{feat_list([("Message match","The headline repeats what they searched or clicked, so visitors know they're in the right place."),("Trust above the fold","Reviews, results, credentials and a clear no-fee or free-review offer where your bar rules allow."),("Built for speed and mobile","Sub-2-second loads and thumb-friendly forms, because most legal searches happen on a phone."),("Tracked and tested","Every call and form tracked to the keyword, and headlines and offers A/B tested against cost per signed case.")])}
<div class="btn-row">{book("Get Your Pages Audited","btn-dark","lp")}</div></div>
<div>{lp_mock()}</div></div></section>
<section><div class="wrap"><div class="sec-head reveal"><span class="eyebrow">Our process</span><h2>How we take over an account</h2></div>
{steps([("Audit","Full review of your accounts, tracking and CRM data, with findings in plain English."),("Fix tracking","Conversion goals cleaned up and signed-case data connected."),("Restructure","Campaigns rebuilt around practice areas, intent and profitability."),("Optimize weekly","Search terms, bids, budgets and creative reviewed every week."),("Scale what signs","Budget moved toward the channels and campaigns with the best cost per signed case.")])}
<div style="margin-top:56px">{faq([("How much do you charge for PPC management?","Pricing is based on spend and scope. We'll give you an exact number after the audit call, with no long-term contract."),("Do you need access to our CRM?","To optimize on signed cases, yes. We connect read access to outcomes through ClearSignal. Without it, we're limited to lead-level optimization like everyone else."),("Do you follow legal advertising rules?","Yes. We build ads and landing pages with state bar advertising rules in mind and work with your team on any required disclaimers."),("Can you work alongside our in-house team?","Yes. Some firms hand us everything; others keep a channel in-house and use us for Google Ads and ClearSignal.")])}</div></div></section>
{cta_band("Find out where your ad budget is leaking.","Book an audit call. We'll review your Google Ads account and tracking and show you exactly what we'd fix first.",["Plain-English findings","No long-term contract","Official Google Partner"])}
'''
page("ppc-management.html","Law Firm PPC Management | Google Partner Agency | Alchemist Mind Pros","PPC management for law firms spending $10K+/mo. Google, Meta, Reddit and ChatGPT ads optimized on cost per signed case by an official Google Partner.",ppc)

# =====================================================================
# CHANNEL PAGES
# =====================================================================
def channel_page(fname, key, name, title, desc, eyebrow, h1, lede, rotate, problems, includes, why_h, why_p, faqs, extra_trust):
    vis=dash_mock(f"{name}: cost per signed case",[("Campaign A","$980","45%"),("Campaign B","$1,420","66%"),("Campaign C","$2,310","96%"),("Campaign D","$760","34%")])
    body = sub_hero(f'<a href="ppc-management.html">PPC Management</a> / {name}', eyebrow, h1, lede, vis,
        ctas=book(f"Get Your {name} Audited","btn-primary",key+"-hero")+'<a href="#calculator" class="btn btn-ghost">Calculate cost per signed case</a>',
        rotate=rotate, trust=extra_trust) + f'''
<section><div class="wrap"><div class="sec-head reveal"><span class="eyebrow">Common problems we fix</span><h2>Where law firms lose money on <span class="accent">{name}.</span></h2></div>{feature_cards(problems)}</div></section>
<section class="sec-paper"><div class="wrap split"><div class="reveal"><span class="eyebrow">What we do</span><h2>{why_h}</h2><p style="margin-top:14px">{why_p}</p>{feat_list(includes)}<div class="btn-row">{book("Book a Strategy Call","btn-dark",key+"-mid")}</div></div>
<div class="reveal">{dash_mock("Signed-case feedback loop",[("Leads","412","100%"),("Qualified","196","48%"),("Consults","121","29%"),("Signed","38","9%")])}</div></div></section>
{calculator()}
<section><div class="wrap"><div class="sec-head reveal"><span class="eyebrow">Other channels</span><h2>Part of a full-funnel paid media program</h2></div>{channel_tiles(exclude=key)}
<div style="margin-top:64px">{faq(faqs)}</div></div></section>
{cta_band(f"See what {name} should be producing for your firm.","Book a strategy call. We'll review your account and tracking and show you the first three things we'd change.")}
'''
    page(fname,title,desc,body)

gp_trust='<div class="trust-row">'+gp_badge()+f'<span class="trust-item">{icon("check",16)}Signed-case bidding</span><span class="trust-item">{icon("check",16)}Month-to-month</span></div>'
channel_page("google-ads.html","google","Google Ads","Google Ads for Law Firms | Google Partner Agency | Alchemist Mind Pros","Google Ads management for law firms by an official Google Partner. Search, LSA and PMax optimized on signed cases with offline conversion imports.",
 "Google Ads &middot; Our strongest suit","Google Ads for law firms that",
 "As an official Google Partner, we run Search, Local Services Ads and Performance Max for law firms, and feed signed-case outcomes back to Google so smart bidding chases clients, not clicks.",
 ["finally tracks signed cases.","stops paying for junk searches.","trains smart bidding on real clients.","scales without spiking cost per case."],
 [("search","Search terms bleeding budget","Job seekers, free-advice searches and other practice areas eating 10 to 30% of spend."),("target","Conversions that aren't conversions","Short calls and page events counted as leads, so tCPA and tROAS optimize for noise."),("map","LSA left on autopilot","Local Services Ads with no lead disputes, no review strategy and no tie to signed cases.")],
 [("Offline conversion imports (GCLID)","Signed cases and qualified leads imported as primary conversions so bidding targets value."),("Search, LSA and Performance Max","Built by practice area and intent, with tight negative keyword and placement control."),("Weekly search term and bid reviews","A specialist in your account every week, not a quarterly check-in."),("Landing pages and call tracking","Fast practice-area pages, call tracking and clean GA4 and GTM setup.")],
 "Built on <span class='accent'>signed-case data.</span>","Most law firm Google Ads accounts are optimized for the cheapest lead. We tell Google which leads became clients, so it can go find more people like them.",
 [("Are you really a Google Partner?","Yes. Alchemist Mind Pros is an official Google Partner, which recognizes ad performance, spend and certification standards."),("Do you manage Local Services Ads?","Yes, including lead disputes, review strategy and tying LSA leads to signed cases."),("How long until we see results?","Tracking fixes and waste cuts usually show up in the first 30 days. Signed-case bidding typically improves over 60 to 90 days as the algorithm learns."),("What spend do you need?","$10K+ a month. Our best results come with firms spending $50K to $100K+ on Google.")],gp_trust)

channel_page("meta-ads.html","meta","Meta Ads","Facebook & Instagram Ads for Law Firms | Meta Ads Management | Alchemist Mind Pros","Meta ads for law firms on Facebook and Instagram, with Conversions API and CRM feedback so campaigns optimize on signed cases.",
 "Meta Ads &middot; Facebook + Instagram","Facebook and Instagram ads that",
 "Meta can be a law firm's most efficient channel or its most expensive. The difference is creative, compliance and whether Meta knows which leads actually became clients.",
 ["fill your intake calendar.","feed signed cases back to Meta.","turn scrollers into consults.","stop flooding intake with junk forms."],
 [("file","Instant forms full of junk","Low-friction lead forms producing fake numbers and people who never answer."),("loop","No Conversions API","Browser pixels alone miss conversions, so Meta's optimization runs on partial data."),("megaphone","Creative fatigue","The same few ads running for months while frequency climbs and cost per case drifts up.")],
 [("Conversions API + CRM feedback","Server-side tracking and signed-case events sent back so Meta optimizes on quality."),("Creative testing system","Video, static and testimonial-style creative tested on a regular cadence."),("Lead quality filters","Form design and qualifying questions that trade a little volume for far better leads."),("Landing pages built for Meta traffic","Mobile-first pages and forms designed for scrollers, not searchers, and tested against cost per signed case.")],
 "Optimized on quality, <span class='accent'>not volume.</span>","We set up Meta to learn from signed cases, then build creative that earns attention in the feed without crossing bar advertising lines.",
 [("Do Meta ads work for law firms?","Yes, especially for estate planning, PI awareness and mass tort. They work best when Meta receives signed-case data via Conversions API."),("Lead forms or landing pages?","Both have a place. We test them and judge by cost per signed case, not cost per lead."),("Do you produce creative?","Yes. We plan, script and produce ad creative, or work with your existing assets and team."),("What about special ad category rules?","We handle Meta's policies and your state's advertising rules when building campaigns.")],
 trust_row(["Conversions API setup","Creative testing","Signed-case optimization"]))

channel_page("reddit-ads.html","reddit","Reddit Ads","Reddit Ads for Law Firms | Reach People Researching Legal Problems | Alchemist Mind Pros","Reddit ads for law firms. Reach people in the communities where they ask about injuries, estates, lemon cars and legal problems.",
 "Reddit Ads &middot; Emerging channel","Reddit ads that reach people",
 "People turn to Reddit when they're trying to figure out whether they have a case. We put your firm in front of them, in the right communities, with tracking that ties results to signed cases.",
 ["researching their exact legal problem.","asking strangers for legal advice.","comparing firms before they call.","your competitors aren't reaching yet."],
 [("users","Wrong communities","Broad targeting that spends on entertainment subreddits instead of high-intent ones."),("msg","Ads that feel like ads","Reddit users punish salesy creative. Generic legal ads get ignored or roasted."),("eye-off","No measurement","Without the Reddit pixel and Conversions API, nobody can tell if it's working.")],
 [("Community and keyword targeting","Subreddits and conversation topics matched to your practice areas and markets."),("Native-feeling creative","Helpful, plain-spoken ads written for how Reddit users actually talk."),("Pixel + Conversions API","Clean tracking so Reddit leads can be matched to signed cases in ClearSignal."),("Controlled testing budgets","Start small, prove cost per signed case, then scale."),("Dedicated landing pages","Pages written for how Reddit users research, with tracking that ties visits to cases.")],
 "Test it the <span class='accent'>disciplined way.</span>","Reddit isn't a replacement for Google. It's an emerging channel that can produce efficient cases when it's targeted tightly and measured honestly.",
 [("Is Reddit right for my firm?","It works best for practices where people research before calling: lemon law, PI, employment, consumer and mass tort. We'll tell you honestly if it isn't."),("How much should we test with?","Usually a modest test budget for 60 to 90 days, judged on cost per qualified lead and signed case."),("Can it hurt our brand?","Not with the right creative and community choices. We avoid controversial placements and write ads that are genuinely useful.")],
 trust_row(["High-intent communities","Pixel + CAPI tracking","Test, then scale"]))

channel_page("chatgpt-ads.html","chatgpt","ChatGPT Ads","ChatGPT Ads for Law Firms | OpenAI Ads Management | Alchemist Mind Pros","ChatGPT ads management for law firms. Reach people asking ChatGPT about legal problems, with conversion tracking tied to signed cases.",
 "ChatGPT Ads &middot; New in 2026","ChatGPT ads that put your firm",
 "People now ask ChatGPT what to do after an accident, how to set up a trust or whether their car qualifies under lemon law. OpenAI's Ads Manager lets firms show up in those moments. We help you test it early and measure it properly.",
 ["in front of people asking legal questions.","ahead of competitors still waiting.","into the AI search conversation.","on the scoreboard with signed cases."],
 [("clock","Waiting too long","Early advertisers on new channels usually get cheaper clicks and less competition."),("eye-off","Testing without tracking","Spending on a new channel with no pixel or conversion data, then guessing if it worked."),("target","Copying Google ads","Search-style ads don't fit conversational placements. Messaging needs to match the question.")],
 [("Ads Manager setup","Account, campaigns, budgets and CPC bidding set up in OpenAI's Ads Manager."),("Pixel and Conversions API","Conversion tracking connected so ChatGPT leads can be matched to signed cases."),("Conversation-fit messaging","Ad copy and landing pages written for the questions people actually ask."),("Eligibility and compliance review","We confirm what your practice area can run before you spend a dollar.")],
 "Early, but <span class='accent'>measured.</span>","ChatGPT ads are new, and policies around legal services can change. We treat it as a disciplined test with a clear scorecard, not a shiny object.",
 [("Can law firms advertise in ChatGPT?","OpenAI's self-serve Ads Manager is open to U.S. advertisers, with some category restrictions. We'll confirm eligibility for your practice area before launching."),("How is it priced?","ChatGPT ads support cost-per-click bidding. We recommend a defined test budget measured on qualified leads and signed cases."),("Will this replace Google Ads?","No. For most firms Google remains the core channel. ChatGPT ads are an incremental test to capture AI-assisted research.")],
 trust_row(["Early-mover advantage","Pixel + CAPI tracking","Measured on signed cases"]))

# =====================================================================
# HUBSPOT
# =====================================================================
hub_vis = HUBSPOT[HUBSPOT.index('<div class="flowmock">'):HUBSPOT.rindex('</div></div>\n</div></section>')] + '</div>'
hub = sub_hero("HubSpot CRM","HubSpot CRM &middot; Certified team","A HubSpot portal your whole firm <span class='accent'>can actually trust.</span>",
 "Our HubSpot-certified team (Reporting and Sales Hub) cleans up messy portals and builds the workflows that route, follow up and report on every lead, so intake moves faster and your attribution holds up.",
 hub_vis, trust=trust_row(["HubSpot Reporting + Sales Hub certified","Built for law firm intake","Works with ClearSignal"])) + f'''
<section><div class="wrap"><div class="sec-head reveal"><span class="eyebrow">Sound familiar?</span><h2>A CRM full of data <span class="accent">nobody believes.</span></h2></div>
{feature_cards([("users","Duplicates and junk contacts","The same lead three times, missing sources and fields nobody fills in."),("clock","Leads waiting on a human","No routing, no alerts, no follow-up. Hot leads cool off while they sit unassigned."),("chart","Reports that don't add up","Marketing, intake and finance each pull a different number from the same portal.")])}</div></section>
<section class="sec-paper"><div class="wrap"><div class="sec-head center reveal"><span class="eyebrow">What we do</span><h2>Cleanup, automation and reporting.</h2></div>
{feature_cards([("search","Portal audit and cleanup","Duplicates merged, properties rationalized, imports fixed and junk archived."),("layout","Lifecycle stages and pipelines","Stages that match how your firm qualifies, consults and signs cases."),("zap","Workflows and lead routing","Round-robin and rules-based routing, speed-to-lead alerts, tasks and follow-up sequences."),("msg","Nurture and follow-up","Automated emails and texts for no-shows, unsigned consults and referrals."),("chart","Dashboards and reporting","Reports built on clean data that finally match ClearSignal and your books."),("link","Integrations","Call tracking, forms, intake tools and ClearSignal connected so nothing is entered twice.")])}
</div></section>
<section><div class="wrap">{steps([("Audit","We review your portal and show you what's broken, in plain English."),("Clean","Data, properties, stages and pipelines fixed without losing history."),("Automate","Routing, alerts and follow-up workflows built and tested."),("Report","Dashboards for partners, marketing and intake."),("Support","Ongoing changes as your firm and campaigns grow.")])}
<div style="margin-top:56px">{faq([("Do you only work with HubSpot?","HubSpot is where our certified team goes deepest. ClearSignal also syncs with Salesforce and Lead Docket, and we can advise on those."),("Will cleanup break our existing data?","No. We back up first, merge carefully and keep history intact."),("Can you do this without running our ads?","Yes. HubSpot work is available on its own, though it pairs best with ClearSignal and PPC.")])}</div></div></section>
{cta_band("Get a CRM your team actually trusts.","Book a call and we'll walk through your HubSpot portal and show you the first fixes we'd make.",["Certified HubSpot team","Built for law firm intake","Month-to-month"])}
'''
page("hubspot-crm.html","HubSpot CRM Cleanup & Workflows for Law Firms | Alchemist Mind Pros","HubSpot-certified cleanup, lifecycle stages, workflows, lead routing and reporting for law firms. Built to work with ClearSignal attribution.",hub)

# vercel config + sitemap
pages=["","clearsignal","ai-sales-coach","check-in-app","ppc-management","google-ads","meta-ads","reddit-ads","chatgpt-ads","hubspot-crm"]
with open(os.path.join(OUT,"sitemap.xml"),"w") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+"".join(f"<url><loc>{SITE}/{p}</loc></url>" for p in pages)+"</urlset>")
print("built", len(pages), "pages")
