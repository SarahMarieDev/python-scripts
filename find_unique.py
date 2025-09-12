def find_unique_items(file1, file2, output_file):
    with open(file1, 'r') as f1:
        lines1 = set(line.strip() for line in f1)

    with open(file2, 'r') as f2:
        lines2 = [line.strip() for line in f2]

    unique_lines = [line for line in lines2 if line not in lines1]

    with open(output_file, 'w') as out:
        for line in unique_lines:
            out.write(line + '\n')

find_unique_items('Compare1.txt', 'Compare2.txt', 'UniqueFromCompare2.txt')
