def find_unique_in_file2(file1, file2, output_file):
    try:
        # Read lines from both files
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            lines1 = set(line.strip() for line in f1 if line.strip())
            lines2 = set(line.strip() for line in f2 if line.strip())

        # Find lines in file2 that are not in file1
        unique_to_file2 = lines2 - lines1

        # Write unique lines to the output file
        with open(output_file, 'w') as output:
            for line in sorted(unique_to_file2):  # Sort for readability
                output.write(line + '\n')

        print(f"Unique lines written to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Input files
    file1 = 'Compare1.txt'
    file2 = 'Compare2.txt'

    # Output file
    output_file = 'output_list.txt'

    # Find unique lines in Compare2.txt and write to output
    find_unique_in_file2(file1, file2, output_file)
