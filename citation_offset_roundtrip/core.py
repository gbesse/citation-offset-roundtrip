from .common import integer,unique_ids

def run(data):
 text=data['text'];encoding=data.get('offset_encoding','codepoints');rows=data['annotations'];unique_ids(rows)
 if not isinstance(text,str)or len(text)>100000 or len(rows)>2000 or encoding not in ('codepoints','utf8','utf16'):raise ValueError('bounds')
 maps={k:{0:0}for k in ('codepoints','utf8','utf16')};positions={k:0 for k in maps}
 for i,char in enumerate(text):
  widths={'codepoints':1,'utf8':len(char.encode('utf-8')),'utf16':len(char.encode('utf-16-le'))//2}
  for k in maps:positions[k]+=widths[k];maps[k][positions[k]]=i+1
 out=[]
 for row in rows:
  lo=integer(row['start'],0,1000000);hi=integer(row['end'],lo,1000000);a=maps[encoding].get(lo);b=maps[encoding].get(hi)
  if a is None or b is None:out.append({'id':row['id'],'status':'invalid_boundary','span':None});continue
  quote=text[a:b];spans={k:[next(pos for pos,cp in maps[k].items()if cp==a),next(pos for pos,cp in maps[k].items()if cp==b)]for k in maps}
  expected=row.get('quote');status='matched'if expected==quote else'quote_mismatch'if'quote'in row else'extracted'
  out.append({'id':row['id'],'status':status,'span':spans,'text':quote})
 return {'annotations':out,'text_lengths':positions,'model':'exact_unicode_boundary_roundtrip_no_normalization_or_fact_check'}
