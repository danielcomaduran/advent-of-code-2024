#%% Load data
with open("input.txt") as file:
    data = file.read().splitlines()

#%% Functions
def is_valid_check(data, row, col):
    valid_row = (row >= 0 and row < len(data))
    valid_col = (col >= 0 and col < len(data[0]))
    return valid_col and valid_row

def count_occurrences(data, word, directions):
    data_rows = len(data)
    data_cols = len(data[0])

    word_len = len(word)

    # Look for word from each cell
    count = 0
    for row in range(data_rows):
        for col in range(data_cols):

            # Look for the word in each direction
            for direction in directions:
                dx, dy = direction
                valid = True

                for i in range(word_len):
                    new_row = row + i * dx
                    new_col = col + i * dy

                    # If the word exceeds the boundaries of the data, it's invalid
                    if not is_valid_check(data, new_row, new_col):
                        valid = False
                        break

                    # If the word doesn't match the data, it's invalid
                    if data[new_row][new_col] != word[i]:
                        valid = False
                        break

                if valid:
                    count += 1
    return count

def count_cross_occurrences(data, word, directions):
    data_rows = len(data)
    data_cols = len(data[0])

    count = 0
    for row in range(data_rows):
        for col in range(data_cols):
            if data[row][col] == "A":
                cross_count = 0
            
                for (dx, dy) in directions:
                    valid = True

                    for i in [-1, 1]:
                        new_row = row + i * dx
                        new_col = col + i * dy

                        # If the word exceeds the boundaries of the data, it's invalid
                        if not is_valid_check(data, new_row, new_col):
                            valid = False
                            break

                        # If the word doesn't match the data, it's invalid
                        if (data[new_row][new_col] != word[i+1]):
                            valid = False
                            break

                    if valid:
                        cross_count += 1
                
                    if cross_count == 2:
                        count += 1
                        break
    return count

#%% Part 01
directions = directions = [
    (0, 1),  # right
    (1, 0),  # down
    (0, -1), # left
    (-1, 0), # up
    (1, 1),  # down-right
    (1, -1), # down-left
    (-1, 1), # up-right
    (-1, -1) # up-left
    ]
total_xmas = count_occurrences(data, "XMAS", directions)
print(f"Part 01 total: {total_xmas}")

#%% Part 02
directions = directions = [
    (1, 1),  # down-right
    (1, -1), # down-left
    (-1, 1), # up-right
    (-1, -1) # up-left
    ]
total_x_mas = count_cross_occurrences(data, "MAS", directions)
print(f"Part 02 total: {total_x_mas}")
# %%
