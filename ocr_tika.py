import tika
tika.initVM()
from tika import parser

parsed = parser.from_file('sample.pdf', xmlContent=True)
f = open('sample.html','w') # w if you want to write override or a if you want to create or write and append
f.write(parsed["content"])
f.close()
