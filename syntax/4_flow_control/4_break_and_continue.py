total = 0
for i in range(1,101):
	if i%5==0:
		continue
	total += i
print(total)

total = 0
for i in range(1,101):
	if i==50: 
		break
	total += i
print(total)