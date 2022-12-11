input is an array of numbers

we can select 2 elements and subtract 1st element by the element next to it 2,3 will become 3,1 but it should never result in negative number

-> this means that the given array should be in ascending order for it to work

if given the array is in ascending order
1,2,3
1,2,1
1,1,1
1,1,0 
1,0,0
we can select 1 element and reduce it to zero with the insta kill sword
which in turn makes the list 0,0,0
resulting in "YES" as the output

in certain cases the resulting list will have more than 1 element left over
3,4,5
3,4,1
3,1,1
3,1,0
which should result in "NO" as we can't use the instakill sword more than once

for an element to be zero after all the subtraction
the preceding element and the element that is preceding the preceding element and so on should be divisible by the first element

this iteration should be done for all elements till only 1 element is left over - (1)
recall that the given array should be ascending also - (2)

so the two conditions to satisfied are (1) and (2)

for that all we have to do is
-> get the first element
-> iterate over the array and check if the first element divides all the elements in the array using elementinlist%firstelement != 0 if True output is "NO" else output is "YES"
-> modulus also in turn checks if array is ascending as modulus will always return the value element if element in list is greater than first element
ie 5 % 10 will return 5 !=0 check will be true
10 % 5 will return  !=0 check will be false

