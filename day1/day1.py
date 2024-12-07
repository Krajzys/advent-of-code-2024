import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename')

args = parser.parse_args()

lines = []

with open(args.filename, 'r') as file:
    left = []
    right = []
    for line in file.readlines():
        l, r = line.strip().split()
        left.append(int(l))
        right.append(int(r))
    left.sort()
    right.sort()

total = 0
for [l, r] in zip(left, right):
    total += abs(l - r)

total2 = 0
for l in left:
    total2 += l * right.count(l)

print(f'1-1: {total}')
print(f'1-2: {total2}')