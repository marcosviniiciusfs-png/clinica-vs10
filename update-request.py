from pathlib import Path
import re
p=Path(__file__).parent/'dist/index.html'
s=p.read_text(encoding='utf-8')
s=s.replace('<main>', '<main><header class="brand-header"><a class="wordmark" href="./" aria-label="Dentista VS10, início">DENTISTA <b>VS<span>10</span></b></a><span class="location">PARAUAPEBAS · PA</span></header>',1)
s=s.replace('<h1 id="procedures-title">','<div class="seal" aria-hidden="true">VS<span>✦</span></div><p class="welcome">BEM-VINDO À DENTISTA VS10</p><h1 id="procedures-title">',1)
s,n=re.subn(r'<a class="map-link".*?</a>','',s,flags=re.S); assert n==1
s,n=re.subn(r'<a class="button primary".*?</a>','',s,flags=re.S); assert n==1
s,n=re.subn(r'<footer>.*?</footer>','',s,flags=re.S); assert n==1
s,n=re.subn(r'<a class="floating-wa".*?</a>','',s,flags=re.S); assert n==1
assert s.count('data-procedure=')==6
p.write_text(s,encoding='utf-8')
print('Header and welcome seal restored; requested bottom elements removed.')
