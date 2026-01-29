import itertools

my_list = [1, 2, 3, 4]

# Get the permutations as an iterator
perms_iterator = itertools.permutations(my_list)

# Convert the iterator to a list for viewing/processing
permutations_list = list(perms_iterator)

# Print the result
print(len(permutations_list))
print(permutations_list)
