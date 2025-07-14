Scripts for Final Year Project

Python (3.13.5)
<br>
|Script |Function|
| --- | --- |
|copy_rename.py | Copy files to another directory and rename copied files using a csv|
|count_msadepth.py | Retrieves MSA depth from AlphaFold2 a3m files |
|cut_SP.py | Trims signal peptide (SP) from protein seq using SignalP 6.0 output|
|extract_cds_orf.py | Extract coding sequence (CDS) containing ORF in header|
|extract_header.py | Extract headers from FASTA file |
|extract_prop.py | Extract prediction scores from ProP 1.0 output |
|extract_score.py | Retrieves pLDDT and pTM score from AlphaFold2 JSON files |
|fasta_rename.py | Renames header in FASTA file using a csv file |
|gc_counter.py | Counts GC content of a coding sequence |
|heatmap.py | Plots heatmap using pairwise FATCAT p-value | 
|pp_scraper.py | Extracts pLDDT and pTM score from ColabFold JSON files |
|remove_stop_codon.py | Remove stop codon from all sequence in a FASTA file|
|removefasta.py | Remove .fasta from file name|
|rename_blocks.py | Rename segmented protein sequence blocks using a csv file|
|segment_fasta.py | Segments FASTA file preset blocks |
|subunit_split.py| Split S protein seq into S1 and S2 using ProP output|


R (4.4.2)

Requires ggplot2, which can be installed using the following:
```
install.packages("ggplot2")
```
<br>
|Script |Function|
| --- | --- |
|gcdnds.R | Plots GC content against dN/dS ratio|
|plddt_msa_splot.R | Plots pLDDT score against log MSA depth|
|ptm_msa_splot.R | Plots pTM score against log MSA depth|
