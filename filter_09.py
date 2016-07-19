#!usr/bin/python

import re
import numpy as np

chromosomes = ['1','2','3','4','5','6','7','8','9','10','11', '12', '13', '14', '15', 
				'16', '17', '18', '19', '20', '21', '22', 'X', 'Y', 'M']
				
for chromosome in chromosomes:
    filename = 'new_chr_files/chr'+chromosome+'.txt'
    with open(filename, 'r') as coverage_file:
        outfilename = 'new_filtered_chr/chr'+chromosome+'.txt'
        outfile = open(outfilename, 'w')
        coverage = 0
        cur_pos = 0
    
        for line in coverage_file:
            line_split = line.replace('\n','').split('\t')
      
   	        if line_split[1] != cur_pos: 
                if cur_pos != 0:
                    score = np.max(chroms) / coverage
                    if score >= 0.9:
                        outfile.write(''.join(lines))
   			
                cur_pos = line_split[1]
                coverage = 0
                chroms = np.zeros(25)
                lines = []
	
            coverage += 1
            chroms[int(line_split[2])-1] +=1
            lines.append(line)
    outfile.close()
      
        	chroms = np.zeros(25)
        	lines = []
	
	coverage += 1
      	chroms[int(line_split[2])-1] +=1
      	lines.append(line)
    outfile.close()
      
       	
   
