#include <stdio.h>
#include <cs50.h>
#include <math.h>


int main(void)
{

int count = 0;

while(true)
{
    float cash = get_float("enter cash- ");
if (cash < 1){
    cash = round(cash*100);
}

    if (cash > 0)
    {

        while(cash!= 0)
        {
            if(cash>=25){
                cash = cash - 25;
                count++;
                continue;
            }
            else if(cash>=10){
                cash = cash - 10;
                count++;
                continue;
            }
            else if(cash>=5){
                cash = cash - 5;
                count++;
                continue;
            }
            else if(cash>=1){
                cash = cash - 1;
                count++;
                continue;
            }
        }
    }

    else
    {
        continue;
    }
    break;
}
printf("%i\n",count);
}
