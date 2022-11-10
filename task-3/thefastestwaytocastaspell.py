num = [*map(int,input().split())]
list1 = []
list2 = []

for i in range(num[1]):
    input_ = input().split()
    for i in input_:
        if input_.index(i) == 0:
            list1.append(i)
        elif input_.index(i) == 1:
            list2.append(i)
spell = input().split()
index_ = 0
final_ = []
for x in spell:
    if x in list1:
        index_ = list1.index(x)
    if len(list1[index_]) == len(list2[index_]):
        final_.append(list1[index_])
    elif len(list1[index_]) < len(list2[index_]):
        final_.append(list1[index_])
    elif len(list1[index_]) > len(list2[index_]):
        final_.append(list2[index_])
    index_ = index_ + 1

for char_ in final_:
    print(char_, end= " ")