#!usr/bin/python

import numpy as np
import re
rep = {'X':'23', 'Y':'24', 'M':'25', 'chr':''}
rep = dict(rep.iteritems())
pattern = re.compile("|".join(rep.keys()))


outfile = open('Repeats_orga.txt','w')
with open("Annotate_Repeats.txt","r") as repeats:
  for line in repeats:
    line = pattern.sub(lambda m:rep[re.escape(m.group(0))],line)
    line = line.replace('\n','').split('\t')
    filewrite = '\t'.join(line[:3]) + '\n'
    outfile.write(filewrite)
    
outfile.close()
    
    
