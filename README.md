# README

Author: Ji Huang

Date: 2024-06-26

This is a streamlit app to search the orthoFinder2 results between Arabidopsis and maize. 

The app `of2_ath_zma_streamlit.py` is deployed at Streamlit Community Cloud.

Here is the details about how the orthology table was generated.

> To infer the orthology between maize and Arabidopsis, we ran OrthoFinder2 (Emms and Kelly 2015) with the following command `orthofinder -a 8 -t 16 -M msa -A mafft`. Protein sequences of the longest transcripts were downloaded from Phytozome 12 (Goodstein et al. 2012) for eight species, including A.thaliana, B.distachyon, M.sinensis, O.sativa, P.virgatum, S.bicolor, S.italica and Z.mays. The protein sequences were used in OrthoFinder2 and the output ortholog table between maize and Arabidopsis were retrieved.


The `ortholog_search.py` is a command line python script.

I also have a similar Shiny app at https://github.com/timedreamer/ShinyOrtholog.