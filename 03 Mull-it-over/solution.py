#%% Load data
with open("input.txt") as file:
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
       
#%% Part 01
total = 0
for row in data:
    valid_muls = find_muls(row)

    total_per_row = sum_mul_valid_muls(valid_muls)
    total += total_per_row

    print(f"Total mul per row: {total_per_row}")

print(f"Total mul: {total}")