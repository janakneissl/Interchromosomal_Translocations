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

6. Annotate the result files to check whether the regions cover Segment Duplicates or simple repeats. This might be a reason for mismapping the reads (and therefore, there might not be a real translocation)
   * move the simple_repeats.txt and segDups.txt to the correct folder
   * python scripts/transloci_anno.py

7. Reorganize the output file from step 2: chr pos mate_chr mate_pos

8.
