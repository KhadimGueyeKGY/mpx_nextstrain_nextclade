#!/bin/bash 

cd packages/aupice_res/aupice

sed -i -e "s/Genomic epidemiology of monkeypox virus/Genomic epidemiology of monkeypox virus on data from ENA/g" monkeypox_mpxv.json 
sed -i -e "s/Nextstrain team/EMBL-EBI ENA team/g" monkeypox_mpxv.json 
sed -i -e "s/GenBank/INSDC/g" monkeypox_mpxv.json 
sed -i -e "s/http:\/\/nextstrain.org/https:\/\/www.insdc.org\//g" monkeypox_mpxv.json 
sed -i -e "s/https:\/\/www.ncbi.nlm.nih.gov\/genbank\//https:\/\/www.ebi.ac.uk\/ena\/pathogens\/v2\/monkeypox?db=embl-mpox/g" monkeypox_mpxv.json 
sed -i -e "s/https:\/\/github.com\/nextstrain\/monkeypox/https:\/\/github.com\/KhadimGueyeKGY\/ena_mpx_phylogeny/g" monkeypox_mpxv.json
