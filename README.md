# Interchromosomal_Translocations
Code to find interchromosomal translocations from WGS/WES data (bam-files)

1. Extract discordant reads from bam file using samtools 
    * samtools view -h bamfile.bam | awk '$3 != $7 && $7 != "="' > discordant. sam
    * samtools view -Sb discordant.sam > discordant.bam
    * samtools index discordant.bam 

2. Create a coverage files for each chromosome, for each position find coverage and the chromosomes/positions mate reads are mapped to
    * mkdir chr_files 
    * python scripts/coverage.py

3. Reorganize the chromosome files into a table where for each position the number of mate reads mapped to certain chromosome are        displayed.
  * mkdir chr_cov 
  * python scripts/coverage_per_chr.py

4. Extract the positions that have a significantly high amount of mates mapped to the same chromosome and print those to a file
  * python scripts/scores.py

5. Combine consecutive positions (covered by same reads) from the step before into regions to create an easier overview
  * python scripts/clustering.py
