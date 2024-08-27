#include <cs50.h> // This includes the CS50 library for get_int function
#include <stdio.h>

int main(void)
{
    int cents;

    // Prompt user for the amount of change owed
    do
    {
        cents = get_int("Change owed: ");
    }
    while (cents < 0);

    int coins = 0;

    // Calculate the number of quarters (25 cents)
    coins += cents / 25;
    cents %= 25;

    // Calculate the number of dimes (10 cents)
    coins += cents / 10;
    cents %= 10;

    // Calculate the number of nickels (5 cents)
    coins += cents / 5;
    cents %= 5;

    // Calculate the number of pennies (1 cent)
    coins += cents / 1;

    // Print the total number of coins
    printf("%d\n", coins);
}
