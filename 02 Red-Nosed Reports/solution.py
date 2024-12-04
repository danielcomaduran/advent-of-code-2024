#%% Load data
# Read code file and store as list of values
with open("input.txt") as file:
    data = file.read().splitlines()

#%% Part 01
safe_reports = [None] * len(data)

def check_step(current_number, next_number):
    if (current_number > next_number) and (current_number <= next_number + 3):
        return 1
    elif (current_number < next_number) and (current_number >= next_number - 3):
        return -1
    else:
        return 0
    
# Check each row
for row in range(len(data)):
    row_of_ints = list(map(int, data[row].split()))
    safe_reports[row] = 1
    
    # Check each list of numbers per row
    for (n,number) in enumerate(row_of_ints):
        
        if (n == 0):
            previous_step = check_step(number, row_of_ints[n+1])

        elif (n < len(row_of_ints)-1):
            current_step = check_step(number, row_of_ints[n+1])

            if (current_step ==0) or (previous_step == 0) or (previous_step != current_step):
                safe_reports[row] = 0
                break
        
total_safe_reports = sum(safe_reports)
print(f'Total safe reports: {total_safe_reports}')

#%% Part 02
