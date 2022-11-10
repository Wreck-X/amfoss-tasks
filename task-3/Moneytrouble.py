nums = [*map(int,input("").split())]
if nums[0] == nums[1]:
    print(nums[0])

if nums[0] < nums[1]:
    print(-1)
    exit()
quotient = int(nums[0]/2) 
remainder = nums[0]%2

list_ = []

for i in range(quotient):
    list_.append(2)

for i in range(remainder):
    list_.append(1)

while set(list_) != {1}:
    if len(list_)%nums[1] == 0:

        print(len(list_))
        break
    elif len(list_)%nums[1] != 0:
        list_.pop(0)
        for i in range(2):
            list_.append(1)
