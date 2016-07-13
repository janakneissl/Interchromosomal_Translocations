#!usr/bin/python

###################################################
# This program reads in chromosome coverage files #
# and calculates scores for each of the positions #
# The possible translocation candidates are then  #
# printed to the outfile						  #
###################################################


import numpy as np

outfile = open('/home/jana/j_data/201606_Transloci/01_bam_file/translocations.txt', 'w')
outfile.write('Chr1\tPos\tChr2\tScore\tTotal\n')


for chrn in range(1,26): #open the input file for current chromosome
	chr = 'chr' + str(chrn)
	infstr =  '/home/jana/j_data/201606_Transloci/01_bam_file/chr_cov/'+ chr + '_cov.txt'
	with open(infstr, 'r') as infile:
		for line in infile:
			if line[0].isdigit(): #skip header line
				line = line.strip('\n').split('\t')[:-1]
				tab = np.array(line, dtype = int)
				total = np.sum(tab[1:]) #calculate total coverage at that position
				for i in range(1, 26): #loop through each chromosome for each line
					if (tab[i] != 0) and (total > 5): #check whether there are more than 5 reads at the position and that cov is not 0
						perc = tab[i]/total
						if perc > 0.9: #if 90% of discordant reads are from the same chromosome print the information to the file
							outstr = chr + '\t' + str(tab[0]) + '\t' + 'chr'+str(i) + '\t' + str(perc)+ '\t' +str(total)+'\n'
							outfile.write(outstr)
	infile.close()
outfile.close()