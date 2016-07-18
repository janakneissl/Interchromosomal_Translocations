#!usr/bin/python

###############################################################
# This program will give back the exact read positions of	  #
# mate reads, which were extracted in an earlier step		  #
#															  #
# Infile 1: 												  #
# chr	start	end 	mate_chr	avg_reads				  #
# chr1	8890	8899	chr5		8						  #
#															  #
# Outfile:													  #
# chr1 8890	chr5 	888821									  #
# chr1 8890	chr5	932789									  #
###############################################################

outfile = open('exact_pos_new.txt', 'w')

with open('transloci_fil_annofil.txt', 'r') as realp:
	for region in realp:
		region = region.strip('\n').split('\t')
		file = 'orga/' + region[0] + '_orga.txt'
		with open(file, 'r') as matepos:
			for line in matepos:
				linea = line.strip('\n').split('\t')
				if (linea[0] == region[0]) and (linea[1]>= region[1])and (linea[1]<=region[2]):
					outfile.write(line)
				
		