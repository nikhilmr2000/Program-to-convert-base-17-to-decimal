#23GF
n=str(input())
l=[]
p=0

f=len(n)


for i in n:
    l.append(i)

for i in l:
    if(i=="A" or i=="a"):
        m=0
        k=1
        c=l.index(i)
        m=f-(c+1)
        if(m>0):
            for j in range(m):
                k*=17
        else:
            k=1
        p=p+(10*k)
    elif(i=="B" or i=="b"):
        m=0
        k=1
        c=l.index(i)
        m=f-(c+1)
        if(m>0):
            for j in range(m):
                k*=17
        else:
            k=1
        p=p+(11*k)
    elif(i=="C" or i=="c"):
        m=0
        k=1
        c=l.index(i)
        m=f-(c+1)
        if(m>0):
            for j in range(m):
                k*=17
        else:
            k=1
        p=p+(12*k)
    elif(i=="D" or i=="d"):
        m=0
        k=1
        c=l.index(i)
        m=f-(c+1)
        if(m>0):
            for j in range(m):
                k*=17
        else:
            k=1
        p=p+(13*k)
    elif(i=="E" or i=="e"):
        m=0
        k=1
        c=l.index(i)
        m=f-(c+1)
        if(m>0):
            for j in range(m):
                k*=17
        else:
            k=1
        p=p+(14*k)
    elif(i=="F" or i=="f"):
        m=0
        k=1
        c=l.index(i)
        m=f-(c+1)
        if(m>0):
            for j in range(m):
                k*=17
        else:
            k=1
        p=p+(15*k)
    elif(i=="G" or i=="g"):
        m=0
        k=1
        c=l.index(i)
        m=f-(c+1)
        if(m>0):
            for j in range(m):
                k*=17
        else:
            k=1
        p=p+(16*k)
    else:
        m=0
        k=1
        c=l.index(i)
        m=f-(c+1)
        if(m>0):
            for j in range(m):
                k*=17
        else:
            k=1
        p=p+(k*int(i))

print(p)
        
