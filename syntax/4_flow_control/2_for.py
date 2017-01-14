total = 0
for i in range(1,100,2):
	total += i
print(total)

l = [1,2,3,4,5]
for x in l:
	print(x)

s = set(l)
for x in s:
	print(x)

d = {'Name': 'Jack', 'Age': 20}
for k,v in d.items():
	print(k,'is',v)