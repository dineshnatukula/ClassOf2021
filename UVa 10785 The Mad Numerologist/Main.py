t = int(input())
d = {}
s = "AJS,BKT,CLU,DMV,ENW,FOX,GPY,HOZ,IR"
freq = {}
l = s.split(",")
for i in range(0, len(l)):
    d[i + 1] = l[i]
print(d)
for i in range(t):
    n = int(input())
    
        
