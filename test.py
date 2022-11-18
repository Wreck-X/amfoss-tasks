inp = input()
lis = [*map(int,input().split())]
finalcount = 0

count4 = lis.count(4)
finalcount = finalcount + count4
for i in range(count4):
    lis.remove(4)

count3 = lis.count(3)
count1 = lis.count(1)
if count3 > count1:
    count3 = count3 - count1
    finalcount = finalcount + count1
    for i in range(count1):
        lis.remove(3)
        lis.remove(1)
    count1 = 0
    oneinlist = False
    threeinlist = True

if count1 > count3:
    count1 = count1 - count3
    finalcount = finalcount + count3
    for i in range(count3):
        lis.remove(1)
        lis.remove(3)
    count3 = 0
    oneinlist = True
    threeinlist = False

if count1 == count3:
    finalcount = finalcount + count1
    for i in range(count1):
        lis.remove(1)
        lis.remove(3)
    count1 = 0
    count3 = 0
    oneinlist = False
    threeinlist = False

count2 = lis.count(2)
ap2 = count2//2
ap2rem = count2%2

for i in range(ap2*2):
    lis.remove(2)

finalcount = finalcount+ap2

count1 = lis.count(1)
count2 = lis.count(2)
dev1 = int(count1/2)
rem1 = count1%2
count1 = lis.count(1)
count2_ = lis.count(2) * 2
count2 = lis.count(2)

count1 = lis.count(1)
count1__ = lis.count(1)//4
count1_ = count1 // 4 * 4

finalcount = finalcount + count1__
if count1 > 4:
    for i in range(count1_):
        lis.remove(1)

if lis == [1]:
    finalcount = finalcount + 1
if lis == [1,1]:
    finalcount = finalcount + 1
if lis == [1,1,1]:
    finalcount = finalcount + 1
if lis == [2]:
    finalcount = finalcount + 1
if lis == [3]:
    finalcount = finalcount + 1
if lis == [2,1,1] or lis == [1,2,1] or lis == [1,1,2]:
    finalcount = finalcount + 1
if lis == [2,1,1,1] or lis == [1,2,1,1] or lis == [1,1,2,1] or lis == [1,1,1,2]:
    finalcount = finalcount + 2
if lis == [1,2] or lis == [2,1]:
    finalcount = finalcount + 1

if len(set(lis)) == 1 and set(lis) == {3} and len(lis) > 1:
    for i in lis:
        finalcount = finalcount + 1

count3 = lis.count(3)
count2 = lis.count(2)
countt = count3 + count2
print(lis)
if count2%2 != 0:
    if len(lis) == countt:
        finalcount = finalcount + len(lis)
print(lis)
print(finalcount)