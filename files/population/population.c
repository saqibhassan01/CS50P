#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Declare variables
    int x, y;

    // Prompt for start size
    do
    {
        x = get_int("Starting size: ");
    }
    while (x < 9);

    // Prompt for end size
    do
    {
        y = get_int("End size: ");
    }
    while (y < x);

    // Calculate number of years until we reach threshold
    int total = x;
    int years = 0;

    while (total < y)
    {
        total = total + (total / 3) - (total / 4);
        years++;
    }

    // Print number of years
    printf("Years: %d\n", years);

    return 0;
}

