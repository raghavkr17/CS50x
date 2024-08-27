#include <cs50.h>
#include <stdio.h>

// Function to get a valid height from the user
int get_valid_height(void)
{
    int height;
    do
    {
        height = get_int("Height: ");
    }
    while (height <= 0);
    return height;
}

int main(void)
{
    // Get the height from the user
    int height = get_valid_height();

    // Loop through each row of the pyramid
    for (int i = 1; i <= height; i++)
    {
        // Print leading spaces
        for (int j = 0; j < height - i; j++)
        {
            printf(" ");
        }

        // Print hashes
        for (int k = 0; k < i; k++)
        {
            printf("#");
        }

        // Move to the next line
        printf("\n");
    }
}
