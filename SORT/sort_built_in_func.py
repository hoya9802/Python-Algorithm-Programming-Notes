array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

b = sorted(array)

# When using sorted()
print(b)
print(array)

# When using .sort()
array.sort()
print(array)

"""
output:
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""