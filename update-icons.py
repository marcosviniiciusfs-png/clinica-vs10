from pathlib import Path
import re

p=Path(__file__).parent/'dist/index.html'
s=p.read_text(encoding='utf-8')
tooth='<path d="M10 5c-4-2-6 0-5 5l2 9c.4 2 2 2 2.5 0l1-4c.3-1.3 1.7-1.3 2 0l1 4c.5 2 2.1 2 2.5 0l2-9c1-5-1-7-5-5-1 .5-2 .5-3 0Z"/>'
icons=[
 '<path d="M7 7V5c0-2 2-3 5-3s5 1 5 3v2H7ZM9 7v4h6V7M9 11l1 9 2 2 2-2 1-9M9 13h6M10 16h4M10 19h4"/>',
 '<path d="M3 6v12M21 6v12M8 5v14M16 5v14M3 12h18"/><rect x="5" y="9" width="6" height="6" rx="1"/><rect x="13" y="9" width="6" height="6" rx="1"/>',
 '<path d="M9 3C6 4 5 7 5 11c0 5 3 9 7 10 3-1 5-4 6-7M9 8h1M8 13l3 1M10 17h3M17 3v6M14 6h6M20 10v4M18 12h4"/>',
 tooth+'<path d="m10 8 2-1 2 2-1 3-3-1Z"/>',
 tooth+'<path d="M20 2v5M17.5 4.5h5M2 14v4M0 16h4"/>',
 '<path d="M7 5c-3-1-4 1-3 4l1.5 6c.4 1.5 1.5 1.5 2 0L9 12l1.5 3c.5 1.5 1.6 1.5 2 0L14 9c1-3 0-5-3-4-1.5.5-2.5.5-4 0ZM17 3l-2 7 3 3M21 4l-2 7-1 2 3 8M18 13l-4 8"/>',
]
counter=iter(icons)
def replace(match):
 return '<span class="procedure-icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="30" height="30" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">'+next(counter)+'</svg></span>'
s,n=re.subn(r'<span class="number" aria-hidden="true">\d+</span>',replace,s)
assert n==6 and s.count('data-procedure=')==6
p.write_text(s,encoding='utf-8')
print('Six custom SVG icons installed; procedure links preserved.')
