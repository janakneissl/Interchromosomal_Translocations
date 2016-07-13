#!usr/bin/python


##########################################################
# This program reads in the chromosome coverage files 	 #
# and reorganizes it into a coverage file with coverage  # 
# per chromosome in each column	 						 #
#														 #
# The output files are tables with the number of mates	 #
# mapped to each chromosome at each position			 #
##########################################################



import numpy as np

chromosomes = ['1','2','3','4','5','6','7','8','9','10','11', '12', '13', '14', '15', 
				'16', '17', '18', '19', '20', '21', '22', 'X', 'Y', 'M']

for chrn in chromosomes:
	
	#create an outfile for each chromosome and write a header containing the chromosomes to each of them
	out = '/home/jana/j_data/201606_Transloci/01_bam_file/chr_cov/chr' + str(chrn)+'_cov.txt'
	outfile = open(out, 'w')
	outfile.write('Pos\tChr1\tChr2\tChr3\tChr4\tChr5\tChr6\tChr7\tChr8\tChr9\tChr10\tChr11\tChr12\tChr13\tChr14\tChr15\tChr16\tChr17\tChr18\tChr19\tChr20\tChr21\tChr22\tChrX\tChrY\tChrM\n')
	
	#The empty dictionnary and Pos variable will be used to store the number of mates for each chromosome
	dic = {}
	pos = 0 
	
	#infiles are produced by coverage.py; there is a seperate infile for each chromosome
	infile =  '/home/jana/j_data/201606_Transloci/01_bam_file/chr_files/chr' + str(chrn) +'.txt'
	with open(infile, 'r') as file:
		for line in file:
			if line.startswith('Chr'):	#lines with the coverage information
				if pos != 0: #in the first loop round, skip this, because pos = 0
					outstring = str(pos) + '\t' 
					for value in dic.values():	#each dic pos corresponds to chromosome and # of mates
						outstring = outstring + str(value)+ '\t' #the # of mates and pos is printed to the outfile
					outstring = outstring + '\n'
					outfile.write(outstring)
				line = line.strip('\n').split() # current position is saved
				pos = line[3]
				dic = {}
				for x in np.arange(1,26):
					dic[x]=0
			elif line.startswith('\t'): #lines which give the information about the mate reads at current position
				i = line.replace('\t', '').replace('chr','').replace('X','23').replace('Y','24').replace('M', '25')
				dic[int(i)]+=1 #for each occurence of a chromosome for a mate read, the readnumber at this chr is increased
			
	file.close()