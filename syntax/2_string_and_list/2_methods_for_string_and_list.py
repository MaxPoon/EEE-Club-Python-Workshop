my_string = "this is a string"
my_list = [3,4,1,2]

my_string_2 = my_string*2
my_list_2 = my_list*2

print(my_string_2)
print(my_list_2)
print()

print(3 in my_list)
print('is' in my_string)
print('that' in my_string)
print()

my_list_1 = [1,2,3]
my_list_2 = [1,2,4]
print(my_list_1<my_list_2)
my_string_1 = "abc"
my_string_2 = "xyz"
print(my_string_1>my_string_2)
print()

print(len(my_list))
print(len(my_string))
print()

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
print()

my_string = my_string.strip()
print(my_string.find('is a'))