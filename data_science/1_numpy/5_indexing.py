import numpy as np

r = np.arange(36)
r.resize((6, 6))
print("r:\n")
print(r)
print()

print("r[2,2]:\n")
print(r[2,2])
print()

print("r[3, 3:6]:\n")
print(r[3, 3:6])
print()

print("r[3:4, 3:6]:\n")
print(r[3:4, 3:6])
print()

print("r[:,3:6]:\n")
print(r[:,3:6])
print()

print("r[r>20]:\n")
print(r[r>20])
print()

print("r[r[:,2]>10]:\n")
print(r[r[:,2]>10])