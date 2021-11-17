import re
import sys
# from pylab import *
import matplotlib.pyplot as plt

kd = ['ALA', "1.8", 'ARG', "-4.5", 'ASN', "-3.5", 'ASP', "-3.5", 'CYS', '2.5',
      'GLN', '-3.5', 'GLU', '-3.5', 'GLY', '-0.4', 'HIS', '-3.2', 'ILE', '4.5',
      'LEU', '3.8', 'LYS', '-3.9', 'MET', '1.9', 'PHE', '2.8', 'PRO', '-1.6',
      'SER', '-0.8', 'THR', '-0.7', 'TRP', '-0.9', 'TYR', '-1.3', 'VAL', '4.2']

obj = open(sys.argv[1], 'r')
# obj = open("1hda.pdb", "r")
dataString = obj.read()
dataList = dataString.split('\n')

aaRawData = []

for i in dataList:
    if re.findall('.*SEQRES.*', i):
        aaRawData.append(i)
# print(aaRawData)

aaRawString = ''.join(aaRawData)
list = aaRawString.split(' ')
# print(list)

aaExtracted = []
for i in list:
    if re.findall('.*ALA.*', i):
        aaExtracted.append(i)
    if re.findall('.*ARG.*', i):
        aaExtracted.append(i)
    if re.findall('.*ASN.*', i):
        aaExtracted.append(i)
    if re.findall('.*ASP.*', i):
        aaExtracted.append(i)
    if re.findall('.*CYS.*', i):
        aaExtracted.append(i)
    if re.findall('.*GLN.*', i):
        aaExtracted.append(i)
    if re.findall('.*GLU.*', i):
        aaExtracted.append(i)
    if re.findall('.*GLY.*', i):
        aaExtracted.append(i)
    if re.findall('.*HIS.*', i):
        aaExtracted.append(i)
    if re.findall('.*ILE.*', i):
        aaExtracted.append(i)
    if re.findall('.*LEU.*', i):
        aaExtracted.append(i)
    if re.findall('.*LYS.*', i):
        aaExtracted.append(i)
    if re.findall('.*MET.*', i):
        aaExtracted.append(i)
    if re.findall('.*PHE.*', i):
        aaExtracted.append(i)
    if re.findall('.*PRO.*', i):
        aaExtracted.append(i)
    if re.findall('.*SER.*', i):
        aaExtracted.append(i)
    if re.findall('.*THR.*', i):
        aaExtracted.append(i)
    if re.findall('.*TRP.*', i):
        aaExtracted.append(i)
    if re.findall('.*TYR.*', i):
        aaExtracted.append(i)
    if re.findall('.*VAL.*', i):
        aaExtracted.append(i)

# print(aaExtracted)


kdValues = []

for i in range(0, len(aaExtracted)):
    for j in range(0, len(kd)):
        if aaExtracted[i] == kd[j]:
            kdValues.append(kd[j+1])
# print(kdValues)
totalaa = []
for i in range(1, len(kdValues)+1):
    totalaa.append(i)
plt.axis(xmin=1, xmax=len(totalaa))

# window size of 3 for smoothing/averaging
average_3_kdvalues = []
for i in range(1, len(kdValues)-1):
    # print(type(kdValues[i]))
    leftRes = kdValues[i-1]
    center = kdValues[i]
    rightRes = kdValues[i+1]
    average_3_kdvalues.append((float(leftRes) + float(center) + float(rightRes)) / 3)
print(average_3_kdvalues)

# print((len(totalaa)), totalaa)
totalaa = range(1, len(totalaa)-1)
# for i in range(0, len(totalaa)):
#     print(totalaa[i])
print(len(totalaa))
print(len(average_3_kdvalues))


plt.plot(totalaa, average_3_kdvalues, linewidth=1.0)

# plt.plot(totalaa, kdValues, linewidth=1.0)

plt.xlabel("Residue number")
plt.ylabel("Hydrophobicity")
plt.title("Hydrophobicity according to Kyte&Doolittle")
plt.show()
