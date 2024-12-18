#%% Import libraries
import numpy as np

#%% Part 01
# - Read data
data = np.genfromtxt('input-01.csv', delimiter="", dtype=int)

# - Sort data and find distances
sorted_data = np.sort(data, axis=0)
distance_data = np.abs(np.diff(sorted_data, axis=1))

# - Calculate total distance
total_distance = np.sum(distance_data)
print(f"Total distance: {total_distance}")

#%% Part 02
similarity_score = 0
for i in range(data.shape[0]):
    number_mask = np.array(data[:,1] == data[i,0], dtype=int)
    similarity_score += data[i,0] * np.sum(number_mask)

print(f"Similarity score {similarity_score}")