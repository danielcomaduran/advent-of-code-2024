#%% Load data
with open("example.txt") as file:
    data = file.read().splitlines()

#%% Functions
def find_muls(row):
    segments = row.split('mul')
    valid_muls = []
    for segment in segments[1:]:
        if segment.startswith('('):
            end_idx = segment.find(')')
            if end_idx != -1:
                valid_muls.append(segment[1:end_idx])
    return valid_muls

def sum_mul_valid_muls(valid_mul):
    total = 0

    for mul in valid_mul:
        try:
            numbers = [int(num) for num in mul.split(",")]

            if len(numbers) == 2:
                total += int(numbers[0]) * int(numbers[1])
        except ValueError:
            continue

    return total

def remove_donts(row):
    while "don't()" in row and "do()" in row:
        start_idx = row.find("don't(")
        end_idx = row.find("do(", start_idx)
        if end_idx != -1:
            end_idx = row.find(")", end_idx) + 1
            row = row[:start_idx] + row[end_idx:]
            print(f"removed {row[start_idx:end_idx]}")
        else:
            break
    return row
       
#%% Part 01
total = 0
for row in data:
    valid_muls = find_muls(row)

    total_per_row = sum_mul_valid_muls(valid_muls)
    total += total_per_row

    print(f"Total mul per row: {total_per_row}")

print(f"Total mul: {total}")

#%% Part 02
total = 0
for row in data:
    removed_donts = remove_donts(row)
    valid_muls = find_muls(removed_donts)

    total_per_row = sum_mul_valid_muls(valid_muls)
    total += total_per_row

    print(f"Total mul per row: {total_per_row}")

print(f"Total mul: {total}")