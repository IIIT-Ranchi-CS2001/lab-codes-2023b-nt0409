from statistics import mean, median, mode

# Input multiple integers from the keyboard using list comprehension
input_list = [int(x) for x in input("Enter numbers separated by space: ").split()]

# Calculate mean, median, and mode
mean_value = mean(input_list)
median_value = median(input_list)
mode_value = mode(input_list)

# Display the results
print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Mode: {mode_value}")
