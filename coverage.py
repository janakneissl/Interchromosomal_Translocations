#!usr/bin/python

##########################################################
# This program takes in a bam file with discordant reads # 
# and outputs a file with the coverage at each position  #
# and the chromosome and position of the mate read		 #
#														 #
# format of the output file:							 #
#		Chr chr1 Pos 9999 Cov 9999						 #
#				chr5 87670								 #
##########################################################


import pysam

#the discordant read bam file is read in 
samfile = pysam.AlignmentFile("/home/jana/j_data/201606_Transloci/01_bam_file/discordant.bam", "rb")

chromosomes = ['1','2','3','4','5','6','7','8','9','10','11', '12', '13', '14', '15', 
				'16', '17', '18', '19', '20', '21', '22', 'X', 'Y', 'M']


for i in chromosomes: #for each chromosome the coverage information is saved in its own file
	chr = "chr" + i
    filename = '/home/jana/j_data/201606_Transloci/01_bam_file/new_chr_files/'+ chr + '.txt'
    f = open(filename,'w')
	for column in samfile.pileup(chr): #Loops through every position of the current chromosome
		#then get the information for all the reads at this position and their mate reads
		for read in column.pileups:
			seq =(str(chr), str(column.pos), read.alignment.next_reference_name, read.alignment.next_reference_start)
			f.write('\t'.join(seq))
			f.write('\n')
	f.close()
