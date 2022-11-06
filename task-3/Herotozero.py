t = int(input(""))
if 1 <= t and t <= 1000:
    for i in range(t):
        n = int(input(""))
        if 2 <= n <= 100:
            ai = list(map(int,input('').split()))
            ai.sort()
            flag = 0
            flag = len(set(ai)) == len(ai)
            mana = 0
            if(flag):
                ai[n-1] = ai[0]
                mana = mana + 1
                ai.sort()
            if 0 not in ai:
                mana = mana + len(ai)
            if 0 in ai:
                count = 0
                for j in ai:
                    if j == 0:
                        count=count +1
                mana = (mana + len(ai)) - count
            print(mana)
