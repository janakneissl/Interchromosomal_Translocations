#!usr/bin/python

import numpy as np

for chrn in range(1,23):
	
	chr = 'chr' + str(chrn)
	infstr =  '/home/jana/j_data/201606_Transloci/01_bam_file/chr_cov/'+ chr + '_cov.txt'
	
	outfstr = '/home/jana/j_data/201606_Transloci/01_bam_file/cov_pos/pos_in_' + chr + '.txt'
	outfile = open(outfstr, 'w')
	
	outfile.write('Chr1\tPos\tChr2\tScore\tTotal\n')

	with open(infstr, 'r') as infile:
		for line in infile:
			if line[0].isdigit():
				line = line.strip('\n').split('\t')[:-1]
				tab = np.array(line, dtype = int)
				total = np.sum(tab[1:])
				for i in range(1, len(tab)):
					if tab[i] != 0 & total > 10:
						perc = tab[i]/total
						if perc > 0.9:
							outstr = chr + '\t' + str(tab[0]) + '\t' + 'chr'+str(i) + '\t' + str(perc)+ '\t' +str(total)+'\n'
							outfile.write(outstr)