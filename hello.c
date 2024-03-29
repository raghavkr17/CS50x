#include <stdio.h>
#include <cs50.h>

int main(void)
{
    printf("hello, world\n");
    string answer = get_string("What's your name? : ");
    printf("Hello, " + answer);
}
