t = int(input(""))
if 1<= t and t <= 100:
    for i in range(t):
        n = int(input(""))
        if 2 <= n and n <=100:
            ai = list(map(int,input('').split()))
            greatestindex = 0
            checkindex = 0
            solution = None
            while solution == None:
                greatest = 0
                for i in ai:
                    if i > greatest:
                        greatest = i
                greatestindex = ai.index(greatest)
                if greatestindex == 0:
                    if greatest == 1:
                        solution = "YES"
                    if greatest != 1:
                        solution = "NO"
                if greatestindex != 0:
                    if ai[greatestindex-1] == 0:
                        solution = "NO"
                    if ai[greatestindex-1] != 0:
                        ai[greatestindex] = ai[greatestindex] - ai[greatestindex-1]
                    

                if len(list(set(ai))) == 1:
                    solution = "YES"
            print(solution)