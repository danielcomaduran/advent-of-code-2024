#%% Load data
with open("input02.txt") as file:
    data = file.read().splitlines()

#%% Functions
def check_step(a, b):
    if a < b:
        return 1 if b - a <= 3 else 0
    elif a > b:
        return -1 if a - b <= 3 else 0
    return 0

def is_safe(row_of_ints):
    for n in range(len(row_of_ints) - 1):
        step = check_step(row_of_ints[n], row_of_ints[n + 1])
        if step == 0 or (n > 0 and step != check_step(row_of_ints[n - 1], row_of_ints[n])):
            return False
    return True
    
#%% Part 01
safe_reports = 0

for row in data:
    row_of_ints = list(map(int, row.split()))
    
    if is_safe(row_of_ints):
        safe_reports += 1

print(f'Total safe reports: {safe_reports}')

#%% Part 02
safe_reports = 0

# Check each row
for row in data:
    row_of_ints = list(map(int, row.split()))
    
    if is_safe(row_of_ints):
        safe_reports += 1
    else:
        for n in range(len(row_of_ints)):
            row_without_bad_number = row_of_ints[:n] + row_of_ints[n+1:]
            if is_safe(row_without_bad_number):
                safe_reports += 1
                break

print(f'Total safe reports: {safe_reports}')