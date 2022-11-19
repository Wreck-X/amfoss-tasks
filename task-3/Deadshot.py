inp = int(input())
pairs = []

for i in range(inp):
    pairs.append([*map(int,input().split())])


n = 0
list_ = []
vantagelist = []
right = None
left = None
lower = None
top = None
final = []
for i in pairs:
    for k in range(len(pairs)):
        pair = pairs[k]
        if i == pair:
            pass
        if pair[0] > i[0] and pair[1] == i[1]:
            right = True
        if pair[0] < i[0] and pair[1] == i[1]:
            left = True
        if pair[1] < i[1] and pair[0] == i[0]:
            lower = True
        if pair[1] > i[1] and pair[0] == i[0]:
            top = True
    if right == True and left == True and lower == True and top == True:
        final.append(i)
    right = None
    left = None
    lower = None
    top = None
print(len(final))