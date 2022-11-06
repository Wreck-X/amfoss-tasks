n = int(input(""))
a = list(map(int,input("").split()))
majlist = []
for i in a:
    if i == 4:
        majlist.append([a.pop(a.index(i))])
for j in a:
    ap1 = []
    if j == 1:
        ap1.append(a.pop(a.index(j)))
        for k in a:
            if k == 3:
                ap1.append(a.pop(a.index(k)))
                break
    if ap1!= []:
        majlist.append(ap1)

for k in a:
    ap2= []
    if k == 3:
        ap2.append(a.pop(a.index(k)))
        for l in a:
            if l == 1:
                ap2.append(a.pop(a.index(l)))
                break
    if ap2!= []:
        majlist.append(ap2)

for m in a:
    ap3 = []
    if m == 2:
        ap3.append(a.pop(a.index(m)))
        for n in a:
            if n == 2:
                ap3.append(a.pop(a.index(n)))
                break
    if ap3 != []:
        majlist.append(ap3)

count1 = a.count(1)
numcar1 = int(count1/4)
rem = count1%4
for i in range(numcar1):
    majlist.append([1,1,1,1])
    for i in range(4):
        a.pop(1)
if a != []:
    majlist.append(a)
print(len(majlist))          