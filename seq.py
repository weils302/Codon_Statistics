import os
import re

f = open("")
lines = f.read().splitlines(keepends=0)

F = ['TTT', 'TTC']
L = ['TTA', 'CTT', 'CTC', 'CTA', 'CTG']
I = ['ATT', 'ATC', 'ATA']
M = ['ATG', 'TTG', 'GTG']
V = ['GTT', 'GTC', 'GTA']
S = ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC']
P = ['CCT', 'CCC', 'CCA', 'CCG']
T = ['ACT', 'ACC', 'ACA', 'ACG']
A = ['GCT', 'GCC', 'GCA', 'GCG']
Y = ['TAT', 'TAC']
star = ['TAA', 'TAG', 'TGA']
H = ['CAT', 'CAC']
Q = ['CAA', 'CAG']
N = ['AAT', 'AAC']
K = ['AAA', 'AAG']
D = ['GAT', 'GAC']
E = ['GAA', 'GAG']
C = ['TGT', 'TGC']
W = ['TGG']
R = ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG']
G = ['GGT', 'GGC', 'GGA', 'GGG']
specs = {'F': F, 'L': L, 'I': I, 'M': M, 'V': V, 'S': S, 'P': P, 'T': T, 'A': A, 'Y': Y, 'star': star, 'H': H, 'Q': Q,
         'N': N, 'K': K, 'D': D, 'E': E, 'C': C, 'W': W, 'R': R, 'G': G}
specsNo = {}

cnt = 0
s = ''
codeNo = {}
for line in lines:
    if '>' in line:  # 跳过描述行
        splt = re.findall(r'\w{3}', s)  # 以3个字符串长度分割
        print(s)
        print(splt)
        for code in splt:
            codeNo[code] = codeNo.get(code, 0) + 1  # 统计密码子数量
        print(codeNo)
        line = ''
        s = ''
        cnt = cnt + 1
        print(cnt)
    else:
        s = s + line
        cnt = cnt + 1
        print(cnt)

splt = re.findall(r'\w{3}', s)  # 以3个字符串长度分割
print(s)
print(splt)
for code in splt:
    codeNo[code] = codeNo.get(code, 0) + 1  # 统计密码子数量
print(codeNo)

for dictcode in codeNo:  # 统计每种氨基酸数量
    for AmiName in specs:
        for i in range(len(specs[AmiName])):
            #    print(AmiName)
            #   print(len(specs[AmiName]))
            #  print(specs[AmiName])
            # print(dictcode)
            # print(specs[AmiName][i])
            if specs[AmiName][i] == dictcode:
                #        print(i)
                #       print(specs[AmiName][i])
                specsNo[AmiName] = specsNo.get(AmiName, 0) + codeNo[dictcode]
                print(specsNo[AmiName])
                break
        else:
            continue
        break
    else:
        continue

print(specsNo)
print(codeNo)

rate = 0
for dictcode in codeNo:  # 统计比例
    for AmiName in specsNo:
        if dictcode in specs[AmiName]:
            rate = codeNo[dictcode] / specsNo[AmiName]
            #            print(dictcode)
            #            print(codeNo[dictcode])
            #            print(specsNo[AmiName])
            #            print(rate)
            print('rate of %s in %s is %.2f' % (dictcode, AmiName, rate))  # 指定保留小数点位数
            break

f.close()
