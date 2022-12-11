inputs
the first number is the amount of money in account
second number is the number of men amongst which you must divide the money

if the amount of money is equal to number of men minimum number of notes will be equal to amount of money or men therefore print anyone of the given inputed number

if the amount of money is less than number of men there is no possible way to satisfy the condition print -1

find the quotient of the first number divided by 2 without decimal values
find the remainder when divided by 2

we append the number 2 to the empty list for x times where x is the quotient without decimal
we then append the number 1 if the there is any remainder

for the process of finding out whether or not it is possible to satisfy the condintion
we take an example

10,2

10 when divided by 2 gives 5

2 is appended to list 5 times

[2,2,2,2,2]

to divide the money between two members
the length of list has to be perfectly divisible by the amount of members

5 is not divisible by 2

but the value of 2 can be 1,1

we can modify the list to [2,2,2,2,1,1]

therefore we need to modify the list till the length of the list is divisible by number of men

to do that i use a while loop with condition 

while set(list_) = {1} 
which checks if when duplicates are removed the list is not equal to [1]
as that is the last possible iteration

then i check if the length of list is divisible by number of men inside the loop if yes i print the length of list and break out of the loop
else i remove one 2 from the list and append two 1's into the list and continue the loop

