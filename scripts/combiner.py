import argparse

parser = argparse.ArgumentParser(description='Combine the contents of two files.')
parser.add_argument('--file_1', type=str, help='the first input file')
parser.add_argument('--file_2', type=str, help='the second input file')
parser.add_argument('--out', type=str, help='the output file')

args = parser.parse_args()

with open(args.file_1, 'r') as f:
    file_1_contents = f.read().splitlines()

with open(args.file_2, 'r') as f:
    file_2_contents = f.read().splitlines()

result = []
for letter in file_1_contents:
    for number in file_2_contents:
        result.append(letter + number)

with open(args.out, 'w') as f:
    for line in result:
        f.write(line + '\n')
