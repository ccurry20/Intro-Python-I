# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE

x.append(4)
print(x)  # [1, 2, 3, 4]

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
mergedlist = list(set(x + y))
print(mergedlist)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
# x.append(y)
mergedlist = list(set(x + y))
mergedlist.remove(8)
print(mergedlist)


# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
x.insert(5, 99)
print(x)

# Print the length of list x
# YOUR CODE HERE
print(len(x))

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
my_new_list = [i * 1000 for i in x]
print(my_new_list)
