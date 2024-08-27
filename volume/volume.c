// Modifies the volume of an audio file

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// Number of bytes in .wav header
const int HEADER_SIZE = 44;

int main(int argc, char *argv[])
{
    // Check command-line arguments
    if (argc != 4)
    {
        printf("Usage: ./volume input.wav output.wav factor\n");
        return 1;
    }

    // Open files and determine scaling factor
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open input file.\n");
        return 1;
    }

    FILE *output = fopen(argv[2], "w");
    if (output == NULL)
    {
        printf("Could not open output file.\n");
        fclose(input); // Close input file before exiting
        return 1;
    }

    float factor = atof(argv[3]);

    // Buffer for header
    unsigned char header[HEADER_SIZE];

    // Copy header from input file to output file
    if (fread(header, sizeof(unsigned char), HEADER_SIZE, input) != HEADER_SIZE)
    {
        printf("Could not read header from input file.\n");
        fclose(input);
        fclose(output);
        return 1;
    }

    if (fwrite(header, sizeof(unsigned char), HEADER_SIZE, output) != HEADER_SIZE)
    {
        printf("Could not write header to output file.\n");
        fclose(input);
        fclose(output);
        return 1;
    }

    // Buffer for samples
    int16_t sample;

    // Read samples from input file, adjust volume, and write to output file
    while (fread(&sample, sizeof(int16_t), 1, input) == 1)
    {
        // Scale sample value
        sample = (int16_t) (sample * factor);

        // Write modified sample to output file
        if (fwrite(&sample, sizeof(int16_t), 1, output) != 1)
        {
            printf("Could not write sample to output file.\n");
            fclose(input);
            fclose(output);
            return 1;
        }
    }

    // Close files
    fclose(input);
    fclose(output);

    return 0;
}
