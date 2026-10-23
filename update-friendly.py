from pathlib import Path
import re
p=Path(__file__).parent/'dist/index.html'
s=p.read_text(encoding='utf-8')
s,n=re.subn(r'https://fonts.googleapis.com/css2\?[^" ]+', 'https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700;800&display=swap',s);assert n==1
s=s.replace('Qual procedimento<br><em>você procura?</em>','Qual procedimento<br>você procura?')
s=s.replace('Esperamos <em>por você.</em>','Venha nos visitar!')
mapblock='''<div class="map-preview"><iframe title="Localização da Dentista VS10 no Google Maps" src="https://maps.google.com/maps?q=-6.0942001,-49.8917046&amp;z=16&amp;hl=pt-BR&amp;output=embed" width="640" height="260" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div><a class="directions" href="https://www.google.com/maps/search/?api=1&amp;query=-6.0942001%2C-49.8917046" target="_blank" rel="noopener">Abrir rota no Google Maps <span aria-hidden="true">↗</span></a>'''
s=s.replace('<p class="hours">Atendimento das 8h às 18h</p>','<p class="hours">Atendimento das 8h às 18h</p>'+mapblock)
assert s.count('data-procedure=')==6 and s.count('<iframe')==1
p.write_text(s,encoding='utf-8')
print('Friendly typography and map at supplied coordinates added; procedure links preserved.')
