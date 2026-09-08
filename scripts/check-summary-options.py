from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit
from collections import Counter

root=Path(__file__).resolve().parent.parent
expected={'water','temp','uv','memory','care','color','price','mall','repair','app'}
class Scan(HTMLParser):
    def __init__(self):
        super().__init__(); self.features=[]; self.refs=[]; self.ids=[]
    def handle_starttag(self,tag,attrs):
        d=dict(attrs)
        if d.get('data-feature'): self.features.append(d['data-feature'])
        if d.get('id'): self.ids.append(d['id'])
        for key in ('src','href'):
            if d.get(key): self.refs.append(d[key])

for name in ['index.html','summary-a.html','summary-b.html','summary-c.html','summary-options.html']:
    scan=Scan(); content=(root/name).read_text(encoding='utf-8'); scan.feed(content)
    missing=[]
    for ref in scan.refs:
        url=urlsplit(ref)
        if not url.scheme and url.path and not (root/url.path).is_file(): missing.append(ref)
    assert not missing,(name,missing)
    assert len(scan.ids)==len(set(scan.ids)),(name,'duplicate ids')
    if name in ['summary-a.html','summary-b.html','summary-c.html']:
        assert set(scan.features)==expected and len(scan.features)==10,(name,Counter(scan.features))
        for required in ['3,630','550','55〜60℃','99.9%','常温水のメモリは共通','浮遊・付着段階']:
            assert required in content,(name,required)
    if name=='index.html':
        for required in ['重要なことは、浮遊・付着段階で殺菌すること。','バイオフィルムを形成する前に殺菌し、水が出てくる直前まで清潔にこだわります。','unit01_larger_20260908.png','unit02_smaller_20260908.png']:
            assert required in content,required
    print(name,': links OK, IDs unique, features',len(scan.features))
