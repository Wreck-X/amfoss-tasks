a = [1,0,1,0]
greatestindex = 0
checkindex = 0
solution = None
while solution == None:
    greatest = 0
    for i in a:
        if i > greatest:
            greatest = i
    greatestindex = a.index(greatest)
    if greatestindex == 0:
        if greatest == 1 and 0 not in a:
            solution = "YES"
        if greatest == 1 and 0 in a:
            count = 0
            wofstnum = a[1:]
            for num in a[1:]:
                if num == 0:
                    count = count + 1
            wofstnum.reverse
            count2 = 0
            for num2 in wofstnum:
                if num2 != 0:
                    solution = "NO"
                    break
                if num2 == 0:
                    count2 = count2 + 1
                    if count2 == count:
                        solution = "YES"

        elif greatest != 1:
            solution = "NO"
    if greatestindex != 0:
        if a[greatestindex-1] == 0:
            solution = "NO"
        if a[greatestindex-1] != 0:
            a[greatestindex] = a[greatestindex] - a[greatestindex-1]
        print(a)
    if len(list(set(a))) == 1:
        solution = "YES"
print(solution)