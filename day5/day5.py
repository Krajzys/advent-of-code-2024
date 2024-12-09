import argparse

def fix_line(line: str, successors: dict) -> list:
    fixed_line = []
    for num in line.split(","):

        min_index = len(fixed_line)
        for succesor in successors.get(num, []):
            try:
                min_index = min(fixed_line.index(succesor), min_index)
            except ValueError:
                pass
        fixed_line.insert(min_index, num)
    return ",".join(fixed_line)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')

    args = parser.parse_args()

    result = 0
    with open(args.filename, 'r') as file:
        successors = {}
        read_rules = True
        for line in file.readlines():
            line = line.strip()
            if read_rules and line != '':
                key, val = line.split('|')
                successors[key] = successors.get(key, []) + [val]
            elif read_rules:
                read_rules = False
                continue
            else:
                for i, num in enumerate(line.split(',')[1:]):
                    if set(successors.get(num, [])).intersection(line.split(',')[:i+1]):
                        break
                else:
                    result += int(line.split(',')[len(line.split(','))//2])

    # part 2
    result2 = 0
    with open(args.filename, 'r') as file:
        successors = {}
        read_rules = True
        for line in file.readlines():
            line = line.strip()
            if read_rules and line != '':
                key, val = line.split('|')
                successors[key] = successors.get(key, []) + [val]
            elif read_rules:
                read_rules = False
                continue
            else:
                for i, num in enumerate(line.split(',')[1:]):
                    if set(successors.get(num, [])).intersection(line.split(',')[:i+1]):
                        fixed_line = fix_line(line, successors)
                        result2 += int(fixed_line.split(',')[len(fixed_line.split(','))//2])
                        break
                

    print(f'5-1: {result}')
    print(f'5-2: {result2}')
