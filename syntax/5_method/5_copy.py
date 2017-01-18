import copy

l1 = [1,2,3,4]
l2 = l1
l2[0] = 10
print(l1)
print(l2)
print()

l1 = [1,2,3,4]
l2 = copy.copy(l1)
l2[0] = 10
print(l1)
print(l2)
print()

l1 = [1,2,3,4]
l2 = l1[:]
l2[0] = 10
print(l1)
print(l2)
print()

l1 = [[1,2,3,4], [1,2,3,4], [1,2,3,4]]
l2 = copy.copy(l1)
l2[0][0] = 10
print(l1)
print(l2)
print()

l1 = [[1,2,3,4], [1,2,3,4], [1,2,3,4]]
l2 = copy.deepcopy(l1)
l2[0][0] = 10
print(l1)
print(l2)
print()