# Description: Streamlit app to find orthologs of a gene in Arabidopsis and Maize.

# Author: Ji Huang
# Date: 2024-06-25

import streamlit as st
import re
import os

# Check if '__file__' is defined, otherwise use a default directory
if '__file__' in globals():
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, 'ath__v__zma.tsv')
else:
    # If '__file__' is not defined, specify a default path or directory
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, 'ath__v__zma.tsv')

def find_orthologs(query_gene: str) -> list:
    result = []
    with open(file_path, 'r') as f:
        for line in f:
            if query_gene in line:
                result.extend(re.split(r'\t|,', line.strip()))

    result1 = set([item.strip() for item in result])
    result2 = [re.sub("_P...$|\\.1$", "", item) for item in result1]
    result_zm = [item for item in result2 if item.startswith("Zm")]
    result_at = [item for item in result2 if item.startswith("AT")]
    return result_zm, result_at

# Streamlit app
st.title('Arabidopsis-Maize Ortholog Finder')
st.write('This app helps you find orthologous genes between Arabidopsis and Maize based on the OrthoFinder2 results from Ji Huang.')

query_gene = st.text_input('Enter a gene to find its orthologs (One gene only):', 'AT2G36380')

# Convert query_gene to uppercase if it starts with 'Ath'
if query_gene.lower().startswith("a"):
    query_gene = query_gene.upper()
elif query_gene.lower().startswith("z"):
    query_gene = "Z" + query_gene[1:].lower()

if st.button('Find Orthologs'):
    ortholog_zm, ortholog_at = find_orthologs(query_gene)
    if ortholog_zm or ortholog_at:
        st.write(f"The query gene is {query_gene}.")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("Maize Genes")
            st.table([gene] for gene in ortholog_zm)
        
        with col2:
            st.write("Arabidopsis Genes")
            st.table([gene] for gene in ortholog_at)
    else:
        st.write("No orthologs found.")