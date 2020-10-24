#import the libraries
import numpy as np

import pandas as pd

#Reading the Core Gene CKSNAP Text File
core_gene = pd.read_csv("core_gene_CKSNAP.txt", sep=" ")
#print(core_gene.head())

# Read the Final Features 
final_features = pd.read_csv("final_features.csv")
#print(final_features.head())

# Read the KP_242 SEQ CKSNAP File
kp_242 = pd.read_csv("KP_242_seq_CKSNAP.txt",sep="\t", header=None)
kp_242 = kp_242.drop([0],axis=1)

# Read the 
kp_amik = pd.read_csv("KP_Amikacin_MIC_242.txt", sep="\t")
kp_amik

population_structure = pd.read_csv("PopulationStructure.csv")
population_structure

snip = pd.read_csv("snp-sites_CKSNAP.txt",sep=" ")
snip

yearinfo = pd.read_csv("year_info_242.txt",sep="\t", header=None)
yearinfo.columns = ["Values","Year"]
yearinfo['Year'].unique()

yearinfo['Year'] = yearinfo['Year'].map({'2012':0,'2013':0.2,'2014':0.4,'2015':0.6,'other':1})
yearinfo

core_gene_extracted = core_gene.iloc[:,6:]
core_gene_extracted.head()

core_gene_extracted = core_gene_extracted.iloc[:,0:192:2]
core_gene_extracted.head()

core_gene_extracted  = core_gene_extracted.replace(r'\d{1,2}:',"",regex=True).astype(float) 
core_gene_extracted.head()

snip_extracted = snip.iloc[:,6:]
snip_extracted.head()

snip_extracted = snip_extracted.iloc[:,0:192:2]
snip_extracted.head()   

snip_extracted  = snip_extracted.replace(r'\d{1,2}:',"",regex=True).astype(float) 
snip_extracted.head()

gene_presence_absence = pd.read_csv("gene_presence_absence.Rtab",sep="\t")
gene_presence_absence.head()

gene_presence_absence_T = gene_presence_absence_T.iloc[1:,:]
gene_presence_absence_T.head()

gene_presence_absence_T.shape

population_structure.head()

population_structure.iloc[:,90:100].columns

population_structure_extracted = population_structure.iloc[:,1:]
population_structure_extracted.head()
