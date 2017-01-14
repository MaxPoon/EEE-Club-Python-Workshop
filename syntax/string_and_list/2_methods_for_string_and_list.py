my_string = "this is a string"
my_list = [3,4,1,2]

my_string_2 = my_string*2
my_list_2 = my_list*2

print(my_string_2)
print(my_list_2)

print(len(my_list))
print(len(my_string))

my_list.append(0)
my_list.append(5)
print(my_list)
my_list.sort()
print(my_list)
print()

print(my_list.pop())
print(my_list.pop(0))
print(my_list)
print()

my_string = "  this is a string  "
my_string.strip()
print(my_string)
my_string = my_string.strip()
print(my_string)
print()

my_string = "---this is a string---"
print(my_string.strip('-'))