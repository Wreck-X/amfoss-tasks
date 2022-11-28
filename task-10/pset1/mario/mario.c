#include <stdio.h>
#include <cs50.h>

int main (void){
    while (true){
        int num = get_int("enter number- ");
        if (num > 0 && num <= 8){
            int i;
            int nums = num;
            for (i = 0 ;i < num; i++){
                int k;
                int c;
                for(k = nums - 1; k!= 0 ;k--){
                    printf(" ");
                }
                for(c = 0; c <= i; c++){
                    printf("#");
                }
            printf("\n");
            nums = nums - 1;}
        }
        else{
            continue;
        }
    };
}