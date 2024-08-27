#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main (int argc, char *argv[])
{

    typedef uint8_t BYTE;
    // Create buffer for
    BYTE buffer[512];

    int counter = 0;

    FILE *jpg = NULL;



    // Check that two commands entered
    if (argc != 2)
    {
        printf("UseL ./recover <filename>\n");
        return 1;
    }

    char *pntr_file = argv[1];

    FILE* raw_data = fopen(pntr_file, "r");

    // Check if able to open such file aka exists
    if (raw_data == NULL)
    {
        printf("Failed to open file: '%s'\n", pntr_file);
        return 1;
    }

    // check if we have 512 byte chunk
    while (fread(buffer, sizeof(buffer), 1, raw_data) == 1)
    {
        if (buffer[0] == 0xff &&
            buffer[1] == 0xd8 &&
            buffer[2] == 0xff &&
            (buffer[3] & 0xf0) == 0xe0)

        {
            if (counter > 0)
                fclose(jpg);

            // Create a file name variable
             char jpg_name[8];

            // Name the file
            sprintf(jpg_name, "%03i.jpg", counter);
            jpg = fopen(jpg_name, "a" );
            fwrite(&buffer, sizeof(buffer), 1, jpg);

            counter++;
        }
        else
        {
            if (counter > 0)
            {
                fwrite(&buffer, sizeof(buffer), 1, jpg);
            }
        }
    }

    fclose(raw_data);
    fclose(jpg);
    return 0;

}
