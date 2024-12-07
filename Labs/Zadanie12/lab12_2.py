def f(m=0):    
    z = int(input())
    if z == 0: return m
    else:       
         m = max(m, z)
    return f(m) 
print(f(0))