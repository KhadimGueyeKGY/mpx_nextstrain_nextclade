# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 15:01:05 2022

@author: khadim
"""

import pandas as pd 



################################   Statistics on countries

df = pd.read_csv("packages/monkeypox/data/metadata.tsv",sep="\t")
df = df.fillna(-1)
head = [i for i in df]
country_total =list(df.country)
#del country_total [country_total.index(" ")]

country_unique = [x for x in list(set(country_total)) if pd.isnull(x) == False]
country_unique.sort()

res = open ("stats/stats_country.tsv","w")
res.write("Country\tNumber\tFrequency\tPercentage\n")
for i in range(len(country_unique)):
    number = country_total.count(country_unique[i])
    freq = country_total.count(country_unique[i])/len(country_total)
    percentage = country_total.count(country_unique[i])/len(country_total)*100
    if country_unique[i] == " ":
        country_unique[i] = "NA"
    res.write(str(country_unique[i])+"\t"+str(number)+"\t"+str(freq)+"\t"+str(percentage)+"\n")
res.close()


################################# Statistics on Clades, on lineages, and evolutions 

df2 = pd.read_csv("output/nextclade.tsv",sep="\t")
#df2 = df2.fillna(-1)
head2 = [i for i in df2]




#----------> Clades

clade=list(df2.clade)
clade_unique = [str(x) for x in list(set(clade)) if pd.isnull(x) == False]
clade_unique.sort()
#del clade_unique [clade_unique.index("-1")]
res1 = open ("stats/stats_clades.tsv","w")
res1.write("Clades\tNumber\tFrequency\tPercentage\n")
for i in range(len(clade_unique)):
    number = clade.count(clade_unique[i])
    freq = clade.count(clade_unique[i])/len(clade)
    percentage = clade.count(clade_unique[i])/len(clade)*100
    if clade_unique[i] == " ":
        clade_unique[i] = "NA"
    res1.write(str(clade_unique[i])+"\t"+str(number)+"\t"+str(freq)+"\t"+str(percentage)+"\n")
res1.close()

#----------> Lineages

lineage=list(df2.lineage)
lineage_unique = [str(x) for x in list(set(lineage)) if pd.isnull(x) == False]
lineage_unique.sort()
#del lineage_unique [lineage_unique.index(" ")]
res2 = open ("stats/stats_lineage.tsv","w")
res2.write("Lineages\tNumber\tFrequency\tPercentage\n")
for i in range(len(lineage_unique)):
    number = lineage.count(lineage_unique[i])
    freq = lineage.count(lineage_unique[i])/len(clade)
    percentage = lineage.count(lineage_unique[i])/len(clade)*100
    if lineage_unique[i] == " ":
        lineage_unique[i] = "NA"
    res2.write(str(lineage_unique[i])+"\t"+str(number)+"\t"+str(freq)+"\t"+str(percentage)+"\n")
res2.close()   
 
#----------> Evolution
id1 = list(df.accession)
id2 = list(df2.seqName)
date= list(df.date)
res3 = open ("stats/stats_evolution.tsv","w")
res3.write("accession\tclade\tlineage\tdate\n")
for i in range(len(id2)):
    if id2[i] != "":
        id = id2[i].split("|")[1]
        res3.write(str(id)+"\t"+str(clade[i])+"\t"+str(lineage[i])+"\t"+str(date[id1.index(id)])+"\n")
res3.close()
    





