import math

# Sizes in acres
sizes = [23, 21, 23, 23, 48, 26, 34, 27]

# Calculate the maximum diagonal length
diagonal_max = math.sqrt(sum(size**2 for size in sizes[:4]) + sum(size**2 for size in sizes[4:]))
print(diagonal_max)
