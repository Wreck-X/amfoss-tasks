import math
input = [*map(int,input().split())]
num1 = input[0]
num2 = input[1]

list_ = []
divid = num2/num1
remainder = num2%num1

if remainder != 0:
    print(-1)
    exit()
else: 
    while divid % 2 == 0:
        list_.append(2)
        divid = divid /2
    for i in range(3,int(math.sqrt(divid))+1,2):
        while divid%i==0:
            list_.append(i)
            divid = divid/i
    if divid > 2:
        list_.append(divid)

count2 = 0
count3 = 0

for i in list_:
    if i not in [2,3]:
        print(-1)
        exit()

for i in list_:
    if i == 2:
        count2 = count2 + 1
    if i == 3:
        count3 = count3 + 1
print(count2 + count3)