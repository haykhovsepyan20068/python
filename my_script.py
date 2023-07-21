my_list = [25, 10, 30, 5, 15]

# Sort the list in descending order using the sorted() function
sorted_list = sorted(my_list, reverse=True)

# Find the smallest value by directly accessing the last element of the sorted list
smallest_value = sorted_list[-1]

print("Original list:", my_list)
print("Sorted list (descending order):", sorted_list)
print("Smallest value in the list:", smallest_value)
