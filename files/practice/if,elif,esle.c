#include <stdio.h>
#include <cs50.h>

int main(void)

{
    int age = get_int("So What's your age? ");
    if (age >= 18)
    {
        printf("Your an Adult\n");
    }
    else if (age < 18)
    {
        printf("Your just a Kiddo\n");
    }
    else
    {
        printf("Your Input Is Wrong\n");
    }
}