#%% Import data
with open("input_order.txt") as f:
    orders = f.read().splitlines()
    orders = [tuple(map(int, order.split("|"))) for order in orders]

with open("input_section.txt") as f:
    sections = f.read().splitlines()
    sections = [list(map(int, section.split(","))) for section in sections]

#%% Functions
def mask_valid_sections(orders, sections):
    valid_sections = []
    
    for (s,section) in enumerate(sections):
        is_valid = True

        for (n, number) in enumerate(section):
            for (preceding, succeding) in orders:
                if (number == succeding) and (preceding in section[n:]):
                    # print(f"Section {s} invalid because {preceding} is after {succeding}")
                    is_valid = False
                    break

            if not is_valid:
                break

        valid_sections.append(is_valid)

    return valid_sections

def sum_middle_number(sections):
    middle_numbers = []
    
    for section in sections:
        len_section = len(section)

        middle_numbers.append(section[(len_section // 2)])
    
    return sum(middle_numbers)

def fix_wrong_sections(orders, invalid_sections):
    fixed_sections = []

    for section in invalid_sections:
        fixed_section = section.copy()

        while not mask_valid_sections(orders, [fixed_section])[0]:           
            for (n, number) in enumerate(fixed_section):
                for (preceding, succeding) in orders:
                    if (number == succeding) and (preceding in fixed_section[n:]):
                        fixed_section = fixed_section[:n] + [preceding] + [num for num in fixed_section[n:] if num != preceding]
        
        fixed_sections.append(fixed_section)

    return fixed_sections

#%% Part 01
masked_valid_sections = mask_valid_sections(orders, sections)
valid_sections = [section for (s,section) in enumerate(sections) if masked_valid_sections[s]]
sum_middle = sum_middle_number(valid_sections)
print(f"Total sum: {sum_middle}")

# %% Part 02
masked_fixed_sections = mask_valid_sections(orders, sections)
invalid_sections = [section for (s,section) in enumerate(sections) if not masked_fixed_sections[s]]
fixed_sections = fix_wrong_sections(orders, invalid_sections)
sum_fixed_middle = sum_middle_number(fixed_sections)
print(f"Fixed sections total sum: {sum_fixed_middle}")


