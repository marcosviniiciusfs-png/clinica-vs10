from pathlib import Path
from urllib.parse import quote
import re
p = Path(__file__).parent / 'dist/index.html'
s = p.read_text(encoding='utf-8')
fixes = {'m?os':'mãos','restaura??o':'restauração','extra??o':'extração','harmoniza??o':'harmonização','SA?DE':'SAÚDE','EST?TICA':'ESTÉTICA','pr?ximo':'próximo','voc?':'você','ortod?ntico':'ortodôntico','Preven??o':'Prevenção','Restaura??o':'Restauração','fun??o':'função','est?tica':'estética','Extra??o':'Extração','Avalia??o':'Avaliação','seguran?a':'segurança','Harmoniza??o':'Harmonização','equil?brio':'equilíbrio','cl?nica':'clínica','Cat?logo':'Catálogo','VOC?':'VOCÊ','respons?vel':'responsável','t?cnico':'técnico','Am?rica':'América','hor?rios':'horários',' ? ':' · ','true">?</span>':'true">↗</span>','equipe ?</a>':'equipe ↗</a>'}
for a,b in fixes.items(): s=s.replace(a,b)
names=['Aparelho ortodôntico','Limpeza','Restauração','Extração','Implante dental','Harmonização facial']
i=iter(names)
def repair(m):
    name=next(i)
    return 'href="https://wa.me/559492046122?text='+quote('Olá! Vim pelo Instagram e gostaria de saber mais sobre '+name+'.')+'" data-procedure='
s=re.sub(r'href="[^"]*" data-procedure=',repair,s)
s=s.replace('Dentista VS10 · Seu','Dentista VS10 — Seu')
p.write_text(s,encoding='utf-8')
