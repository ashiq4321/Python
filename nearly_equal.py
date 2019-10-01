def nearly_equal(a="",b=""):
    if len(a)== len(b):
        i=0
        s=b
        while(i<len(b)):
            s=s.replace(b[i],a[i])
            if a==s:
                return print("nearly equal")
            i=i+1
            s=b
    return print("not nearly equal")    
nearly_equal("ashiq","ashiq")
nearly_equal("aghiq","ashiq")
nearly_equal("sahiq","ashiq")
nearly_equal("ashiq","sakib")
    
