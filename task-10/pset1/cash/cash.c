#include <stdio.h>
#include <cs50.h>
#include <math.h>
int main(void) {
int count = 0;
int cash = round(get_float("enter cash- ")*100);
while(cash!= 0){
    if(cash>=25){
        cash = cash - 25;
        count++;

    }
    else if(cash>=10){
        cash = cash - 10;
        count++;
    }
    else if(cash>=5){
        cash = cash - 5;
        count++;
    }
    else if(cash>=1){
        cash = cash - 1;
        count++;
    }
}
printf("%i",count);
}