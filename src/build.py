import json,glob,base64,sys
sys.path.insert(0,'.')
from content import *
import os
B=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..')+'/'
EV=[]
for f in sorted([B+'data/events.jsonl']):
    for l in open(f):
        if l.strip():
            e=json.loads(l); e['t_']=e.pop('t'); EV.append(e)
PL=json.load(open(B+'data/places.json'))
RG=json.load(open(B+'data/regions.json'))
osm=json.load(open(B+'data/water.json')); C=json.load(open(B+'data/contours.json'))
shade='data:image/png;base64,'+base64.b64encode(open(B+'data/shade.png','rb').read()).decode()
J=lambda o: json.dumps(o,ensure_ascii=False,separators=(',',':'))
s=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'template.html')).read()
rep={'{{C100}}':C['c100'],'{{C300}}':C['c300'],'{{C600}}':C['c600'],'{{C1000}}':C['c1000'],'{{C1500}}':C['c1500'],'{{C2000}}':C['c2000'],
 '{{WATER}}':osm['water'],'{{RIVERS}}':osm['rivers'],'{{SEA}}':osm['sea'],'{{SHADE}}':shade,
 '{{EVENTS}}':J(EV),'{{PLACES}}':J(PL),'{{REGIONS}}':J({k:{'d':v['d'],'c':v['c']} for k,v in RG.items()}),'{{REGSTATUS}}':J(REGIONS),
 '{{ERAS}}':J(ERAS),'{{POSTS}}':J(POSTS),'{{LINES}}':J(LINES),'{{ROUTES}}':J(ROUTES),'{{PEOPLE}}':J(PEOPLE),'{{TERMS}}':J(CONCEPTS),'{{CMP}}':J(CMP),'{{SLIPS}}':J(SLIPS)}
for k,v in rep.items():
    assert k in s,k
    s=s.replace(k,v)
open(B+'index.html','w').write(s)
print(len(s))
