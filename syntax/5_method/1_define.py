def add(a,b):
	return a+b

x = add(2,5)
print(x)
print()

s = add("Hi", " Jack")
print(s)
print()

# x = sub(1,2)
# print(x)
# def sub(a,b):
# 	return a-b

def add(a, b=1):
	return a+b

x = add(2)
print(x)
x = add(2,2)
print(x)
print()