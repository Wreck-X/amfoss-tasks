t = int(input())
if 1<= t<= 10**4:
    for l in range(t):
        n = int(input(""))
        if 2 <= n and n <= 2*10**5:
            a = list(map(float,input("").split()))
            indexes = []
            lastdigit = a.pop()
            zerocount = 0
            for i in a:
                if i == 0:
                    zerocount = zerocount + 1
            if zerocount == len(a):
                print(0)
                continue
            for j in a:
                if j != 0:
                    indexes.append(a.index(j))
            firstnum = indexes[0]
            finallist = a[firstnum:]
            count = 0
            for i in finallist:
                if i == 0:
                    count = count + 1
            sum = 0
            for num in finallist:
                sum = sum + num
            answer = sum + count
            print(int(answer))