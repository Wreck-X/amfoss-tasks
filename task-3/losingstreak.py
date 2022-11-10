import math
ai = [*map(int,input('').split())]
firstnum = ai[0]
secondnum = ai[1]


divi = int(secondnum/firstnum)

list_ = []
while divi % 2 == 0:
    list_.append(2)
    divi = divi/2

for i in range(3,int(math.sqrt(divi))+1,2):
    while(divi % i == 0):
        list_.append(i)
        divi = divi/i
if divi > 2:
    list_.append(divi)

if list_ == []:
    print(-1)
    exit()


for j in list_:
    if j not in [2,3]:
        print(-1)
        exit()

count2 = list_.count(2)
count3 = list_.count(3)

final = count2 + count3

print(final)