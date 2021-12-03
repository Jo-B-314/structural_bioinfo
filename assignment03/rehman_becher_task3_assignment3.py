from Bio import AlignIO
from Bio.Align import AlignInfo

print()
print('!!!!!!!!!!!!!!CONSENSUS!!!!!!!!!!!!!!')
print()

align = AlignIO.read("seqMsa.fasta", "clustal")
# print(align)
summary_align = AlignInfo.SummaryInfo(align)
print(summary_align.dumb_consensus(require_multiple=1))
