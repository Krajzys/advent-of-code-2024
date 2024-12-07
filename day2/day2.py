import argparse
from functools import reduce

parser = argparse.ArgumentParser()
parser.add_argument('filename')

args = parser.parse_args()

lines = []

safe_reports = 0

with open(args.filename, 'r') as file:
    for line in file.readlines():
        values = [int(value) for value in line.strip().split()]
        values_range = range(len(values) - 1)

        is_sorted_asc = all(values[i] < values[i+1] for i in values_range)
        is_sorted_des = all(values[i] > values[i+1] for i in values_range)
        is_diff_in_range = all(abs(values[i] - values[i+1]) in range(1, 4) for i in values_range)
        if (is_sorted_asc or is_sorted_des) and is_diff_in_range:
            safe_reports += 1

safe_reports2 = 0
with open(args.filename, 'r') as file:
    for line in file.readlines():
        values = [int(value) for value in line.strip().split()]
        values_range = range(len(values) - 1)

        is_sorted_asc = all(values[i] < values[i+1] for i in values_range)
        is_sorted_des = all(values[i] > values[i+1] for i in values_range)
        is_diff_in_range = all(abs(values[i] - values[i+1]) in range(1, 4) for i in values_range)
        if (is_sorted_asc or is_sorted_des) and is_diff_in_range:
            safe_reports2 += 1
        else:
            for i in range(len(values)): # Remove elements and see if the array is okay without it
                value_alt = values[:]
                value_alt.pop(i)
                values_range = range(len(value_alt) - 1)
                
                is_sorted_asc = all(value_alt[i] < value_alt[i+1] for i in values_range)
                is_sorted_des = all(value_alt[i] > value_alt[i+1] for i in values_range)
                is_diff_in_range = all(abs(value_alt[i] - value_alt[i+1]) in range(1, 4) for i in values_range)
                if (is_sorted_asc or is_sorted_des) and is_diff_in_range:
                    safe_reports2 += 1
                    break


print(f'2-1: {safe_reports}')
print(f'2-2: {safe_reports2}')