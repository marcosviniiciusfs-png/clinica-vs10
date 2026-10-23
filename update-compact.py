from pathlib import Path
from urllib.parse import quote
import re
from PIL import Image

root=Path(__file__).parent/'dist'
old=root.joinpath('index.html').read_text(encoding='utf-8')
cards=re.findall(r'<a class="procedure".*?</a>',old,re.S)
order=['implante-dental','aparelho-ortodontico','harmonizacao-facial','restauracao','limpeza','extracao']
names=['implante dental','aparelho ortodôntico','harmonização facial','restauração','limpeza','extração']
base='https://wa.me/5594992046122?text='
result=[]
for i,(slug,name) in enumerate(zip(order,names),1):
    card=next(c for c in cards if f'data-procedure="{slug}"' in c)
    link=base+quote('Olá! Vim pelo Instagram e quero saber mais sobre '+name+'.',safe='!')
    card=re.sub(r'href="[^"]+"',f'href="{link}"',card,count=1)
    card=re.sub(r'(<span class="number" aria-hidden="true">)\d+',lambda m:m[1]+f'{i:02d}',card)
    result.append(card)
general=base+quote('Olá! Vim pelo Instagram e gostaria de agendar uma avaliação.',safe='!')
maps='https://www.google.com/maps/search/?api=1&query='+quote('Av. Paulo Afonso, Qd. 01, Lt. 04, Jardim América (VS10), Parauapebas, PA')
html='''<!doctype html>
<html lang="pt-BR"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#102c40"><title>Dentista VS10 | Procedimentos e agendamento</title><meta name="description" content="Escolha seu procedimento e agende sua avaliação na Dentista VS10, em Parauapebas. Atendimento das 8h às 18h."><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Allura&family=Cormorant+Garamond:ital,wght@0,400;1,400&family=Manrope:wght@400;600&display=swap" rel="stylesheet"><link rel="stylesheet" href="style.css"></head><body><main>
<section class="logo-section" aria-label="Dentista VS10"><span class="hero-script" aria-hidden="true">Sorria</span><img class="logo" src="assets/logo-vs-transparente.webp" width="360" height="360" alt="Dentista VS10 — símbolo do dente com as letras VS" fetchpriority="high"></section>
<section class="links-section" aria-labelledby="procedures-title"><h1 id="procedures-title">Qual procedimento<br><em>você procura?</em></h1><nav class="procedure-list" aria-label="Procedimentos">'''+''.join(result)+'''</nav></section>
<section class="visit" aria-labelledby="address-title"><h2 id="address-title">Esperamos <em>por você.</em></h2><address>Av. Paulo Afonso, Qd. 01, Lt. 04<br>Jardim América (VS10) · Parauapebas, PA</address><p class="hours">Atendimento das 8h às 18h</p><a class="map-link" href="'''+maps+'''" target="_blank" rel="noopener">Como chegar <span aria-hidden="true">↗</span></a><a class="button primary" href="'''+general+'''" data-contact="agendar" target="_blank" rel="noopener">Vamos agendar? <span aria-hidden="true">↗</span></a></section>
<footer>Responsável técnico: Dr. Lucas Delfino · CRO-PA 8500</footer></main>
<a class="floating-wa" href="'''+general+'''" data-contact="flutuante" target="_blank" rel="noopener" aria-label="Agende sua avaliação pelo WhatsApp"><svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><path d="M20 11.5a8 8 0 0 1-12 7L3 20l1.5-5A8 8 0 1 1 20 11.5Z"/><path d="M8 7c-2 3 3 8 6 8l2-2-3-1-1 1-3-3 1-1Z"/></svg><span>WhatsApp</span></a><script src="tracking.js" defer></script></body></html>'''
root.joinpath('index.html').write_text(html,encoding='utf-8')
im=Image.open(root/'assets/logo-vs-transparente.png')
im.thumbnail((600,600))
im.save(root/'assets/logo-vs-transparente.webp','WEBP',quality=85,method=6)
print('Compact page generated; logo WebP:',(root/'assets/logo-vs-transparente.webp').stat().st_size,'bytes')
