INPUT_FILE = "input.txt"

with open(INPUT_FILE, 'r') as file:
    lines = file.readlines()

first_list_of_lists = [[12, 45, 2], [3, 7, 3, 1], [23, 89, 10, 9]]

for i, line in enumerate(lines):
    if line[-1] == '\n':
        lines[i] = line[:-1]

def find_number(line: str, index: int, row: int) -> tuple[int, int, int] | None:

    if line[index] not in numbers:
        return None
    
    l = r = index
    while True:
        changed = False
        if l != 0 and line[l-1] in numbers:
            l -= 1
            changed = True
        if r != len(line) - 1 and line[r+1] in numbers:
            r += 1
            changed = True

        if not changed:
            return (row, l, r)

    

part_numbers = set()
numbers = {str(x) for x in range(10)}
for r, row in enumerate(lines):
    for c, char in enumerate(row):
        if char != "." and char not in numbers:
            for x_offset in (-1, 0, 1):
                for y_offset in (-1, 0, 1):
                    try:
                        num_indices = find_number(lines[r + y_offset], c + x_offset, r+y_offset)
                        if num_indices is not None:
                            part_numbers.add(num_indices)
                    except IndexError:
                        pass

nums = []
for x in part_numbers:
    print(x)
    nums.append(int(lines[x[0]][x[1]:x[2]+1]))
print(nums)
print(sum(nums))