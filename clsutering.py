#!usr/bin/python

###################################################
# This program reorganizes the translocation file #
# by summarizing regions, which most likely share #
# the same reads, that cover them				  #
###################################################

outfile = open('transloci_fil.txt','w')

with open('translocations.txt', 'r') as infile:
	next(infile) #skip headerline
	first_row = next(infile) #use first row to set all the variables
	first_row = first_row.strip('\n').split('\t')
	fst_chr = first_row[0] 
	pos = first_row[1]
	start_pos = first_row [1]
	sec_chr = first_row[2]
	total = int(first_row[4])
	reads =1 #number of reads for this region
	
	for line in infile:
		line = line.strip('\n').split('\t')
		
		#check whether the two reads have consecutive positions (are in one region)
		if (line[0] == fst_chr) and (int(line[1]) == int(pos)+1) and (line[2]== sec_chr):
			pos = line[1]
			total += int(line[4])
			reads +=1
		
		#if they are not in one region, then the current region is printed and the variables reset
		else: 
			outstring = fst_chr +'\t'+ str(start_pos)+'\t'+str(pos)+'\t'+sec_chr+'\t' +str(total/reads)+'\n'
			outfile.write(outstring)
			
			start_pos = line[1]
			pos = line[1]
			fst_chr = line[0]
			sec_chr = line[2]
			total = int(line[4])
			reads =1
			
			
			
		
			
		