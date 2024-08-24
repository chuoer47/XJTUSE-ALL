
n=5
lst = [11,33,55,22,9]
s = sum(lst)
p = []
d = 0
for i in range(n):
    p.append(lst[i]/s)
for i in range(n):
    for j in range(i,n):
        d = d + p[i]*p[j]*(j-i)
print(d)
