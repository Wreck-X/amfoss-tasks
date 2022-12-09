#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

int main (int argc, string argv[]){
    if (argc > 1){
        int loop;
        int key = atoi(argv[1]);
        string string_ = get_string("enter string- ");
        int length = strlen(string_);
        int count;
        for (count = 0;count < length;count++){
            char letter = string_[count] + key;
            printf("%c",letter);
        }
    }
    else{
        printf("Fail");
    }
    
}
