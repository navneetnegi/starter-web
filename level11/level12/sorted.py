

numbers = [6,9,3,1]

numbers_sorted_rev = sorted(numbers, reverse = True)

print(sorted(numbers))

print(numbers_sorted_rev)

help(sorted)

numbers_tuple = (7,10,3,2,6,8,1,16,90,45,37,65,21,16)

numbers_set = {2,1,3,8,7,5,11,15,10,99,101,45,56,32,17,90}

numbers_tuple_sorted = sorted(numbers_tuple)

numbers_set_sorted = sorted(numbers_set)

print(numbers_tuple_sorted)
print(numbers_set_sorted)

print(tuple(numbers_tuple_sorted))
print(set(numbers_set_sorted))

# How split works

test = 'Lets go to the Newyork'

test_try = test.split()

print(test_try)

print(' '.join(test_try))


# Sorted strings

string_numbers_value = '34521'

string_value = 'I love to sort'

sorted_string_numbers = sorted(string_numbers_value)

sorted_string = sorted(string_value.split())


print(sorted_string_numbers)
print(' '.join(sorted_string))