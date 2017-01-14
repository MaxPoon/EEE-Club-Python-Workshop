s = set([1,2,3])
print(s)
print(2 in s)
print(5 in s)
print()

s.add(5)
s.remove(2)
print(2 in s)
print(5 in s)
print()

l = [1,1,1,2,2,3,4,0]
s = set(l)
print(s)
l = list(s)
print(l)