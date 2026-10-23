from pathlib import Path
import json,re
from xml.etree import ElementTree
root=Path(__file__).parent
def load(name):
 data=json.loads((root/name).read_text(encoding='utf-8-sig'))
 return json.loads(data) if isinstance(data,str) else data
health=load('healthicons-source.json')
tabler=load('tabler-source.json')
choices=[(health,'odontology-implant-outline'),(health,'mouth-outline'),(health,'syringe-outline'),(health,'tooth-outline'),(health,'dental-hygiene-outline'),(tabler,'dental-broken')]
items=[]
for pack,name in choices:
 icon=pack['icons'][name]
 w=icon.get('width',pack.get('width',24));h=icon.get('height',pack.get('height',24))
 svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="36" height="36" aria-hidden="true">'+icon['body']+'</svg>'
 ElementTree.fromstring(svg)
 items.append('<span class="procedure-icon" aria-hidden="true">'+svg+'</span>')
s=(root/'dist/index.html').read_text(encoding='utf-8')
it=iter(items)
s,n=re.subn(r'<span class="procedure-icon".*?</span>',lambda m:next(it),s,flags=re.S)
assert n==6 and s.count('data-procedure=')==6
(root/'dist/index.html').write_text(s,encoding='utf-8')
(root/'dist/ICON-SOURCES.txt').write_text('Ready-made icons. Original vector geometry retained.\nHealth Icons (MIT): https://github.com/resolvetosavelives/healthicons\n'+ '\n'.join(name for pack,name in choices if pack is health)+'\nTabler Icons (MIT): https://github.com/tabler/tabler-icons\ndental-broken\nDistributed through https://github.com/iconify/icon-sets\n',encoding='utf-8')
print('Installed six original library icons; XML and procedure links verified.')
