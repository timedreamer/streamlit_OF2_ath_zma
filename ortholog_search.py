# Description: This script is used to find orthologs of a given gene in Arabidopsis or Maize.

# Author: Ji Huang
# Date: 2024-06-26

import re
import argparse

def find_orthologs(query_gene: str) -> list:
    result = []
    with open('of2_file_process/ath__v__zma.tsv', 'r') as f:
        for line in f:
            if query_gene in line:
                result.extend(re.split(r'\t|,', line.strip()))

    result1 = set([item.strip() for item in result])
    result2 = [re.sub("_P...$|\.1$", "", item) for item in result1]
    result_zm = [item for item in result2 if item.startswith("Zm")]
    result_at = [item for item in result2 if item.startswith("AT")]
    return result_zm, result_at

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Find orthologs of a given gene.')
    parser.add_argument('--query_gene', '-q', type=str, help='Gene to find orthologs for', dest = 'query_gene', default = "AT2G37470")
    args = parser.parse_args()

    # Convert query_gene to uppercase if it starts with 'Ath'
    if args.query_gene.lower().startswith("a"):
        args.query_gene = args.query_gene.upper()
    elif args.query_gene.lower().startswith("z"):
        args.query_gene = "Z" + args.query_gene[1:].lower()


    ortholog_zm = ",".join(find_orthologs(args.query_gene)[0])
    ortholog_at = ",".join(find_orthologs(args.query_gene)[1])

    print(f"The query gene is {args.query_gene}.")
    print(f"Here are the maize genes: {ortholog_zm}")
    print(f"Here are the Arabidopsis genes: {ortholog_at}")