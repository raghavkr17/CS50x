import csv
import sys


def main():
    # Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        return

    # Read database file into a variable
    with open(sys.argv[1]) as database_file:
        reader = csv.DictReader(database_file)
        database = list(reader)

    # Read DNA sequence file into a variable
    with open(sys.argv[2]) as sequence_file:
        dna_sequence = sequence_file.read()

    # Find longest match of each STR in DNA sequence
    str_counts = {}
    str_keys = reader.fieldnames[1:]  # Get the list of STRs (excluding 'name')

    for str_key in str_keys:
        str_counts[str_key] = longest_match(dna_sequence, str_key)

    # Check database for matching profiles
    for person in database:
        match = all(int(person[str_key]) == str_counts[str_key] for str_key in str_keys)
        if match:
            print(person['name'])
            return

    print("No match")
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    for i in range(sequence_length):
        count = 0
        while True:
            start = i + count * subsequence_length
            end = start + subsequence_length
            if sequence[start:end] == subsequence:
                count += 1
            else:
                break
        longest_run = max(longest_run, count)

    return longest_run


main()
