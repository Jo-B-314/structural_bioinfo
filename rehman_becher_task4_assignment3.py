from Bio import AlignIO
from Bio.Align import AlignInfo
from Bio import motifs


# alignment = AlignIO.read("seqMsa.fasta", "clustal")
# summary_align = AlignInfo.SummaryInfo(alignment)
# consensus = summary_align.dumb_consensus()
# my_pssm = summary_align.pos_specific_score_matrix()

# print(my_pssm)

# with open("seqMsa.fasta") as handle:
#     motif = motifs.read(handle, "sites")
# print(motif.counts)


from Bio import motifs
with open("Arnt.sites") as handle:
    motif = motifs.read(handle, "sites")
print(motif.counts)
