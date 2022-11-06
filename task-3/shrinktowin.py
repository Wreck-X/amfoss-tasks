n = input("")
numlist = []
for i in n:
    numlist.append(int(i))

sum = 0
count = 0

if len(numlist) ==1:
    print(0)
    exit()
while True:
    for i in numlist:
        sum = i + sum
    numlist = []
    for i in str(sum):
        numlist.append(int(i))
    sum = 0
    count = count+1
    if len(numlist) ==1:
        break
print(count)