import re,html,glob
def inl(s):
    s=html.escape(s,quote=False)
    return re.sub(r'\*(.+?)\*',r'<em>\1</em>',s)
years={1:"Primeiro Ano",2:"Segundo Ano",3:"Terceiro Ano",4:"Quarto Ano"}
def yr(n): return 1 if n<=15 else 2 if n<=30 else 3 if n<=45 else 4
blocks={1:[],2:[],3:[],4:[]}
for f in sorted(glob.glob('episodios/ep*.md')):
    n=int(re.search(r'ep(\d+)',f).group(1))
    lines=open(f,encoding='utf-8').read().strip().split('\n')
    title=lines[0].lstrip('# ').strip()
    paras=[p.strip() for p in '\n'.join(lines[1:]).split('\n\n') if p.strip()]
    pov=''
    if paras and re.fullmatch(r'\*[^*]+\*',paras[0]) and len(paras[0])<30:
        pov=paras[0].strip('*'); paras=paras[1:]
    body=''.join('<hr>' if p=='---' else f'<p>{inl(p)}</p>' for p in paras)
    tag=f'<span>{html.escape(pov)}</span>' if pov else ''
    blocks[yr(n)].append(f'<details class="ep" id="ep{n}"><summary>{html.escape(title)}{tag}</summary><div class="text">{body}</div></details>')
eps=''.join(f'<section class="year"><h2>{years[y]}</h2>{"".join(b)}</section>' for y,b in blocks.items())
page=f'''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Academia de Vésper</title>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Cinzel+Decorative:wght@700&display=swap" rel="stylesheet">
<style>
:root{{--bg:#0d0b0a;--ink:#e8dfcf;--muted:#a89a84;--wine:#6e1f2a;--gold:#c9a45c;--paper:#16120f}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font:19px/1.75 "Cormorant Garamond",Georgia,serif}}
a{{color:var(--gold)}}nav{{position:sticky;top:0;z-index:5;background:#0d0b0aee;border-bottom:1px solid #2a221b;padding:.6rem 1rem;display:flex;gap:1.2rem;flex-wrap:wrap;font-variant:small-caps;letter-spacing:.08em}}
nav a{{text-decoration:none}}
.hero{{min-height:92vh;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:3rem 1rem;position:relative;overflow:hidden;
background:radial-gradient(ellipse at 50% 30%,#3a2a1c55,transparent 60%),radial-gradient(ellipse at 50% 120%,#6e1f2a66,transparent 60%),linear-gradient(#0d0b0a,#120d0b)}}
.hero:before{{content:"";position:absolute;inset:auto 0 0 0;height:45%;background:linear-gradient(transparent,#cfc6b822 40%,#cfc6b833);filter:blur(18px);animation:fog 14s ease-in-out infinite alternate}}
@keyframes fog{{to{{transform:translateX(-6%)}}}}
.star{{width:120px;height:120px;margin-bottom:1.5rem;filter:drop-shadow(0 0 18px #e9dcb6aa);animation:pulse 4s ease-in-out infinite}}
@keyframes pulse{{50%{{filter:drop-shadow(0 0 34px #fff3cc)}}}}
h1{{font-family:"Cinzel Decorative",serif;font-size:clamp(2.2rem,7vw,4.6rem);margin:.2rem 0;color:var(--gold);letter-spacing:.04em}}
.hero p{{max-width:640px;font-size:1.2rem;color:var(--muted);font-style:italic}}
.btn{{margin-top:1.4rem;border:1px solid var(--gold);padding:.6rem 1.6rem;text-decoration:none;font-variant:small-caps;letter-spacing:.15em}}
section{{max-width:820px;margin:0 auto;padding:3rem 1.2rem}}h2{{font-family:"Cinzel Decorative",serif;color:var(--gold);text-align:center;font-size:1.7rem;border-bottom:1px solid #3a2e22;padding-bottom:.6rem}}
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:1rem}}
.card{{background:var(--paper);border:1px solid #2e251d;border-top:3px solid var(--c,var(--wine));padding:1rem 1.2rem}}.card h3{{margin:.2rem 0;color:var(--gold)}}.card p{{margin:.3rem 0;color:var(--muted)}}
.ep{{background:var(--paper);border:1px solid #2a221b;margin:.5rem 0}}.ep summary{{cursor:pointer;padding:.8rem 1rem;font-weight:600;display:flex;justify-content:space-between;gap:1rem}}
.ep summary span{{color:var(--wine);font-style:italic;font-weight:400;filter:brightness(1.8)}}.ep[open] summary{{border-bottom:1px solid #2a221b}}
.text{{padding:.5rem 1.4rem 1.4rem}}.text hr{{border:0;text-align:center}}.text hr:after{{content:"✦";color:var(--gold)}}
footer{{text-align:center;color:var(--muted);padding:3rem 1rem;font-style:italic}}
</style></head><body>
<nav><a href="../">← Reinos de Aço</a><a href="#sobre">A Ilha</a><a href="#eles">Os Três</a><a href="#episodios">Episódios</a></nav>
<header class="hero">
<svg class="star" viewBox="0 0 100 100"><polygon fill="#f3e7c4" points="50,0 58,34 85,15 66,42 100,50 66,58 85,85 58,66 50,100 42,66 15,85 34,58 0,50 34,42 15,15 42,34"/><rect x="47" y="20" width="6" height="60" fill="#6e1f2a"/><circle cx="50" cy="22" r="6" fill="none" stroke="#6e1f2a" stroke-width="3"/></svg>
<h1>Academia de Vésper</h1>
<p>Uma ilha sem mapa, coberta de neblina. Uma escola onde todo poder cobra do corpo ou da memória. E, todo inverno, um aluno que não volta.</p>
<a class="btn" href="#ep1">Ler o Episódio 1</a></header>
<section id="sobre"><h2>A Ilha</h2><p>Robson tem dezoito anos, uma mala pequena e nenhum passado que valha contar, até a carta com o selo da estrela de oito pontas chegar ao orfanato. Na Academia de Vésper, cada feitiço tem um preço, as velas da diretora levam o nome de cada aluno, e a neblina guarda tudo o que se esquece. Quando os olhos do primeiro colega viram vidro, Robson descobre que não chegou à ilha por acaso.</p><p><em>60 episódios em quatro anos letivos. Romance, mistério e magia sombria. Para maiores de 18.</em></p></section>
<section id="eles"><h2>Os Três</h2><div class="grid">
<div class="card" style="--c:#8b1e2d"><h3>Dante Moretti</h3><p>Herdeiro deserdado, magia de sangue, um anel de pedra vermelha que nunca tira. Cruel na escada, outra coisa no escuro.</p></div>
<div class="card" style="--c:#3c6e8f"><h3>Elias Moura</h3><p>Monitor-chefe, cachecol azul, chá de camomila para quem não dorme. Gentil demais para uma ilha como essa.</p></div>
<div class="card" style="--c:#b9b9c6"><h3>Corvin Ashgrave</h3><p>Cabelo branco, olhos prateados, lê memórias com um toque. Sempre por perto. Ninguém sabe de que lado ele está.</p></div>
</div></section>
<section id="episodios"><h2>Episódios</h2></section>
{eps}
<footer>Academia de Vésper · uma história de Robson Victor · <a href="../">voltar a Reinos de Aço</a></footer></body></html>'''
open('index.html','w',encoding='utf-8').write(page)
print(len(page))
