from Bio import AlignIO
from Bio.Align import AlignInfo
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline
plt.ion()
import logomaker as lm
import re

file = open('seqMsa.fasta', 'r')
# file = open('sample.txt', 'r')
# file = open('newSampleMSA.txt', 'r')

fasta = file.read()
fastaList = fasta.split(' ')
# print(fastaList)
str1 = ','.join(fastaList)
# print(str1)
fastaList = str1.split('\n')
# print(fastaList)
str1 = '\t'.join(fastaList)
# print(str1)
fastaList = str1.split(',')
# print(fastaList)
str1 = ' '.join(fastaList)
# print(str1)
fastaList = str1.split('\t')
# print(fastaList)

res = []
id = []
count = 0

for i in fastaList:
    if re.findall('.*_.*', i):
        count += 1
        res.append(i[12:])
        id.append(i[:12])

dict = {i: id.count(i) for i in id}
totalRes = len(dict.keys())

x= []
for i in res:
    x.append(i[:60])

counts_mat = lm.alignment_to_matrix(x)
print(counts_mat.head())
lm.Logo(counts_mat)