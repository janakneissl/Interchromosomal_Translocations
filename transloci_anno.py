#!usr/bin/python
#coding: utf-8
import numpy as np
import re

#create empty dictionnaries with the chromosomes as keys 
chros =  ["chr1", "chr2", "chr3", "chr4", "chr5", "chr6", "chr7", "chr8", "chr9", "chr10", "chr11", "chr12", "chr13", "chr14", 
          "chr15", "chr16", "chr17", "chr18", "chr19", "chr20", "chr21", "chr22", "chr23", "chr24","chr25"]

#dictionnary for Duplicate regions and Repeat Regions
dupdic = {key:[] for key in chros}
repdic = {key:[] for key in chros}

#Open the segment duplicate file and safe all the duplication positions in the dup dict
for line in open("Annotate_SegDups.txt", 'r'):
	
	line = line.replace('chrX', 'chr23').replace('chrY', 'chr24')
        line = re.split('\t|:|-| ', line.replace('\n', ''))

        for i in range(len(line)):
                if line[i] in dupdic:
                        dupdic[line[i]].append((line[i+1], line[i+2]))
                        i = i+2

#open the Simple repeat file and safe the repeat positions in the repeat dic
for line in open("Annotate_SimpleRepeats_parsed.txt", 'r'):
	line = line.replace('chrX', 'chr23').replace('chrY', 'chr24')
        line = re.split('\t', line)
        if line[0] in repdic:
                repdic[line[0]].append((line[1], line[2]))

#Open output file
f = open('transloci_fil_anno.txt', 'w')



#write all the lines to a file and annotated them if the positions lay in a duplicated segment
for line in open('transloci_fil.txt', 'r'):
	linel = np.array(line.split('\t'))
        chr = linel[0]
	start = linel[1]
	end = linel[2]
        #lines has now 4 columns: chr1 pos1 chr2 pos2
        if any(lower <= start <= upper for (lower, upper) in dupdic[chr]) or any(lower <= end <= upper for (lower, upper) in dupdic[chr]):
		f.write(str.join('\t', (line.strip('\n'), 'SegDup\n')))  
        elif any(lower <= start <= upper for (lower, upper) in repdic[chr]) or any(lower <= end <= upper for (lower, upper) in repdic[chr]):
                f.write(str.join('\t', (line.strip('\n'), 'Repeat\n')))  
        else:
                f.write(line)
                

f.close()



