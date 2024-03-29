#!usr/bin/python
# Reorganize the Segment Duplicate File

import numpy as np
import re
import pandas as pd

#Set up re dictionnary to replace chrX|Y|M with numbers 23,24,25
rep = {'X':'23', 'Y':'24', 'M':'25', 'chr':''}
rep = dict(rep.iteritems())
pattern = re.compile("|".join(rep.keys()))


outfile = open('test_File.txt', 'w')

#open original Seg_Dup-File and have each region printed to a new line
with open("Annotate_SegDups.txt", "r") as SegDup:
  for line in SegDup:
    line = pattern.sub(lambda m:rep[re.escape(m.group(0))],line)
    line = re.split('\t|:|-| ', line.replace('\n', ''))
    orig = "\t".join(line[:3]) + '\n'
    outfile.write(orig)
    rest_list = np.array(line[3:]).reshape(-1,3)
    for row in rest_list:
      dups = "te  \t".join(row) +"\n"
      outfile.write(dups)
      
outfile.close()

#Drop duplicate rows and sort by chromosome
dup_df = pd.read_csv('test_File.txt', sep='\t', header=None, index_col =None, dtype = int)
dup_df = pd.dup_df.drop_duplicates()
dup_df.columns = ['chr', 'start', 'end']
dup_df = dup_df.sort_values(['chr', 'start'])

pd.dup_df.to_csv('Seg_Dup_orga.txt',sep='\t', header = False, index=False)
      
