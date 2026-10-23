from pathlib import Path
import re
from xml.etree import ElementTree

p=Path(__file__).parent/'dist/index.html'
s=p.read_text(encoding='utf-8')
tooth='<path d="M15 10C9 7 6 11 8 18l3 11c1 4 4 5 5 1l2-6c.7-2 3.3-2 4 0l2 6c1 4 4 3 5-1l3-11c2-7-1-11-7-8-4 2-6 2-10 0Z"/>'
icons=[
 '<path d="M12 16v-5c0-5 3-8 8-8s8 3 8 8v5H12ZM15 16v5h10v-5M15 21l2 13 3 3 3-3 2-13M15.5 25h9M16 29h8M17 33h6"/>',
 '<path d="M5 12v16M35 12v16M14 9v22M26 9v22M5 20h30"/><rect x="8" y="15" width="10" height="10" rx="2"/><rect x="22" y="15" width="10" height="10" rx="2"/><path d="M11 18h4v4h-4M25 18h4v4h-4"/>',
 '<path d="M23 6c-8-2-14 4-14 13 0 9 5 15 11 17 5-2 8-6 9-12M15 17h2M15 23l5 1M18 29c2 1 4 1 6-1M30 5v10M25 10h10M34 19v6M31 22h6"/>',
 tooth+'<path d="m17 14 5-1 3 4-2 4-6-1-2-3Z"/>',
 '<path d="M14 12c-5-2-8 2-6 8l3 10c1 4 4 4 5 1l2-6c.7-2 3.3-2 4 0l2 6c1 3 4 3 5-1l3-10M14 12c4 2 7 2 11 0M29 4v12M23 10h12M35 20v6M32 23h6"/>',
 '<path d="M11 19c-4-2-6 1-5 5l2 8c.6 3 2.5 3 3.5.5l1.5-4 1.5 4c1 2.5 2.9 2.5 3.5-.5l2-8c1-4-1-7-5-5-1.5.7-2.5.7-4 0Z"/><path d="m23 4-2 10 5 7 7 14M32 6l-3 10-3 5-3 14M25 8l4 1M24 25l5 1"/>',
]
it=iter(icons)
def replace(m):
 svg='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40" width="40" height="40" fill="none" stroke="currentColor" stroke-width="1.65" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'+next(it)+'</svg>'
 ElementTree.fromstring(svg)
 return '<span class="procedure-icon" aria-hidden="true">'+svg+'</span>'
s,n=re.subn(r'<span class="procedure-icon".*?</span>',replace,s,flags=re.S)
assert n==6 and s.count('data-procedure=')==6
p.write_text(s,encoding='utf-8')
print('Six refined SVG icons validated. WhatsApp links preserved.')
