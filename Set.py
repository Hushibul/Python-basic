setOne = {1, 4, 6, 22, 9, 9, 6, 9}
setTwo = {0, 9, 6, 22, 8}

# Checks the difference between two sets
differenceSet = setOne.difference(setTwo)

# Union Between Two Sets
unifiedSet = setOne.union(setTwo)

# Intersection Between Sets
intersectSet = setTwo.intersection(setOne)

# Removing Element in set
setOne.pop()

print(setOne)
print(setTwo)
print(differenceSet)
print('Unified Set', unifiedSet)
print('Intersect Set', intersectSet)

listItem = [1, 1, 5, 1, 8, 12, 15, 1, 9, 0, 9]
listToSet = set(listItem)
print('List to Set', listToSet)

setToTuple = tuple(setOne)
print(setToTuple)

listToTuple = tuple(listItem)
print(listToTuple)