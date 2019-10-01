def dups(a=[]):
    b=[]
    c=[]
    for i in a:
        if i not in b:
            b.append(i)
        else:
            c.append(i)
    if len(c)==0:
        return print("no duplicate value in the list")
    else:
        return print("duplicate values in the list : ",c)
dups([2,6,1,3])
dups([2,6,1,1,3,2,3])
dups(['a',6,1,3])
    
