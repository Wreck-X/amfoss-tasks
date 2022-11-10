t = int(input(""))
for i in range(t):
    n = int(input(""))
    ai = [*map(int,input("").split())]

    count = 0
    while n != 0:
        n = ai[n - 1]
        count = count + 1
        
    if count == 3:
        print("YES")
    else:
        print("NO")
