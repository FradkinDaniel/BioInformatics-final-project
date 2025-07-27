import re
oct4="ATTTGCAT"
genes={}
sox2="ATTTGCAT"
klf4="CACCC"
myc="CAC[GA]TC"
e2f1="TTTC[CG]CGC"
nanog="TTTC[CG]CGC"
nanog1="[CG][GA][CG]C[GC]ATTAN[GC]"
trascription=[oct4,sox2,klf4,myc,e2f1,nanog,nanog1]
f=open('data','r')
line=f.readline()
name=""
seq=""
while True:
    line=line.rstrip('\n')
    if len(line)==0:
        break
    if line.startswith('>'):
        for i in range(len(trascription)):
            if re.search(trascription[i],seq)!= "None":
                genes={trascription[i]: name}
            a,n,b=line.partition('_')
            name,c,d=n.partition(' ')
        seq=""
    else:
        seq+=line
for i in range(len(trascription)):
    if re.search(trascription[i],seq)!= "None":
        genes={trascription[i]: name}
