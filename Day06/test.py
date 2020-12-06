
set_one = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
set_two = {'a', 'b', 'c', 'f', 'g'}
set_three = {'b', 'c', 'e', 'f'}
set_four = {'c', 'd', 'e', 'f', 'g'}

my_array = []

my_array.append(set_one)
my_array.append(set_two)
my_array.append(set_three)
my_array.append(set_four)


result = set.intersection(*my_array)
print(my_array)
print(result)
