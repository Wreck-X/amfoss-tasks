n = int(input())
for i in range(n):
    num = input()
    list_ = [*map(int,input().split())]
    flag = True
    firstelement = list_[0]
    for i in list_:
        if i%firstelement != 0:
            flag = False

    if flag == True:
        print("YES")
    elif flag == False:
        print("NO")