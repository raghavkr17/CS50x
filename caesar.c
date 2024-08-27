#include <cs50.h> // This includes the CS50 library for get_string and get_int functions
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Function prototype
bool is_valid_key(string s);

int main(int argc, string argv[])
{
    // Check if a single command-line argument is provided
    if (argc != 2 || !is_valid_key(argv[1]))
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    // Convert the key from string to an integer
    int key = atoi(argv[1]);

    // Get the plaintext from the user
    string plaintext = get_string("plaintext: ");

    // Encrypt the plaintext
    printf("ciphertext: ");
    for (int i = 0, n = strlen(plaintext); i < n; i++)
    {
        char c = plaintext[i];

        // Check if the character is an uppercase letter
        if (isupper(c))
        {
            printf("%c", (c - 'A' + key) % 26 + 'A');
        }
        // Check if the character is a lowercase letter
        else if (islower(c))
        {
            printf("%c", (c - 'a' + key) % 26 + 'a');
        }
        // If it's not an alphabetic character, print it as it is
        else
        {
            printf("%c", c);
        }
    }

    // Print a newline at the end
    printf("\n");

    return 0;
}

// Function to check if the provided key is valid (only digits)
bool is_valid_key(string s)
{
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        if (!isdigit(s[i]))
        {
            return false;
        }
    }
    return true;
}
