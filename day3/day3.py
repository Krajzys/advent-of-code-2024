import argparse
import regex

parser = argparse.ArgumentParser()
parser.add_argument('filename')

args = parser.parse_args()

result = 0
with open(args.filename, 'r') as file:
    raw_file = file.read().replace('\n', '')
    valid_muls = regex.findall(r'mul\(\d{1,3},\d{1,3}\)', raw_file)
    for mul in valid_muls:
        [num1, num2] = regex.findall(r'\d+', mul)
        result += int(num1) * int(num2)
    # print(valid_muls)
    print(f'3-1: {result}')

result = 0
with open(args.filename, 'r') as file:
    raw_file = file.read().replace('\n', '')
    valid_muls = regex.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", raw_file)
    do_muls = True
    for mul in valid_muls:
        if mul.startswith('mul'):
            if do_muls:
                [num1, num2] = regex.findall(r'\d+', mul)
                result += int(num1) * int(num2)
        else:
            do_muls = mul == 'do()'
    # print(valid_muls)
    print(f'3-2: {result}')
