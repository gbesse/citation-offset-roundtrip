import unittest
from citation_offset_roundtrip import run
class Tests(unittest.TestCase):
 def test_astral_symbol_roundtrips_three_encodings(self):
  for encoding,a,b in [('codepoints',1,2),('utf8',1,5),('utf16',1,3)]:
   r=run({'text':'A🚀B','offset_encoding':encoding,'annotations':[{'id':'r','start':a,'end':b,'quote':'🚀'}]})['annotations'][0];self.assertEqual(r['status'],'matched');self.assertEqual(r['span'],{'codepoints':[1,2],'utf8':[1,5],'utf16':[1,3]})
 def test_split_surrogate_or_multibyte_rejected(self):
  for enc,lo in [('utf8',2),('utf16',2)]:self.assertEqual(run({'text':'A🚀B','offset_encoding':enc,'annotations':[{'id':'a','start':lo,'end':3}]})['annotations'][0]['status'],'invalid_boundary')
 def test_combining_characters_not_normalized(self):
  r=run({'text':'e\u0301','annotations':[{'id':'a','start':0,'end':2,'quote':'é'}]})['annotations'][0];self.assertEqual(r['status'],'quote_mismatch');self.assertEqual(r['text'],'e\u0301')
 def test_empty_span_and_outside(self):
  r=run({'text':'abc','annotations':[{'id':'empty','start':3,'end':3},{'id':'outside','start':4,'end':4}]});self.assertEqual(r['annotations'][0]['text'],'');self.assertEqual(r['annotations'][1]['status'],'invalid_boundary')
