n = int(input())
for i in range(n):
    meh = input()
    values = input().split()
    values.pop()
    firstnum = None
    for i in values:
        if i != '0':
            firstnum = values.index(i)
            break
    finallist = [*map(int,values[firstnum:])]
    count0 = finallist.count(0)
    if count0 == len(finallist):
        print(0)
        exit()
    sum_ = sum(finallist)
    print(count0 + sum_)