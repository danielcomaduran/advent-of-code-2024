#%% Load data
with open("input.txt") as file:
    data = file.read()

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
            numbers = [num for num in mul.split(",")]

            if len(numbers) == 2:
                num1 = int(numbers[0])
                num2 = int(numbers[1])
                total += num1 * num2
        except ValueError:
            continue

    return total

def remove_dont_segments(row):
    result = 0
    segments = row.split("don't()")
    for segment in segments:
        subsegments = segment.split("do()")
        for sub, subsegment in enumerate(subsegments):
            # Skip the first subsegment if it's not the first segment (after a don't())
            if (sub == 0) and (segment != segments[0]):                
                continue

            print(f"Evaluated Subsegment: {subsegment}")
            muls = find_muls(subsegment)
            print(f"Muls: {muls}")
            result += sum_mul_valid_muls(muls)
    return result
       
#%% Part 01
total = sum_mul_valid_muls(find_muls(data))
print(f"Part 01 total: {total}")

# %% Part 02
total = remove_dont_segments(data)
print(f"Part 02 total: {total}")