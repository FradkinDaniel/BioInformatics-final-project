def writing(dic):
    t=open('gene.txt','r')
    z=open('finaly.txt','w')
    while True:
        line1=t.readline()
        line1=line1.rstrip('\n')
        if len(line1)==0:
            break
        (c,d,name)=line1.partition('\t')
        if dic[name]>1:
            z.write(line1+'\n')
    z.close()
    t.close()
f=open('gene.txt','r')
dic={}
while True:
    line=f.readline()
    line=line.rstrip('\n')
    if len(line)==0:
        break
    (a,b,name)=line.partition('\t')
    if name not in dic:
        dic[name]=1
    else:
        dic[name]=dic[name]+1
writing(dic)
f.close()
