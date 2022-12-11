Hero To Zero - 
This code is based on the observation that the number operations is based on whether or not the given 
inputs are distinct or not
 
Given that the demon can target any two heroes in the the city

- if the two heroes are different leveled the higher leveled hero will be debuffed to the lower leveled hero ie. they become equal

- if the two heroes are of the same level one of them gets debuffed to level zero


if the given inputs are distinct the demon is forced to select any two heroes 
resulting in the higher leveled hero being debuffed to the same level as the lower leveled hero

eg: 
1,2,3,4
if the demon selects 3 and 4
the list will become 1,2,3,3
this is 1 operation

then the optimal selections the demon can take would be to select the equal leveled heroes ie 3 and 3
this will result in 1,2,3,0 as they are both equal
now the demon can easily select each hero and the hero that is level 0 to convert all of them to 0
selecting 1 and 0, result = 0,2,3,0
selecting 2 and 0, result = 0,0,3,0
selecting 3 and 0, result = 0,0,0,0 
number of operations = 4

number of operations = 4 + 1

if the inputs are not distinct the demon can directly select the heroes that equal
eg 
list = 1,2,3,3
selecting 3 and 3 result = 1,2,3,0
selecting 1 and 0, result = 0,2,3,0
selecting 2 and 0, result = 0,0,3,0
selecting 3 and 0, result = 0,0,0,0 

number of operations = 4

if the given list contains 0 leveled heroes
1,2,0,0
selecting 1 and 0 result = 1,0,0,0
selecting 2 and 0 result = 0,0,0,0
number of operations = 2

observation - 
if the list is distinct and the elements do not contain zeroes mana required will always be length of list + 1 as there is an extra operation to make one of them equal

if the list is not distinct and the elements do not contain zeroes
the required mana will always be equal to the length of the list

if the list contains zeroes
the required mana will be length of list - number of zeroes






