x = int(input("enter an integer: "))
if x<10 and x%2==1:
	print("it's an odd number less than 10\n")
elif x<10 and x%2==0:
	print("it's an even number less than 10\n")
else:
	print("it's larger than or equal to 10\n")

x = int(input("enter an integer: "))
if not x==10:
	print("it's not equal to 10")
else:
	print("it's equal to 10")