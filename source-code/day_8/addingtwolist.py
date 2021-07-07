even_list = [i for i in range(2,25) if i % 2 == 0]
odd_list = [i for i in range(5,35) if i % 2 != 0]

num_list = []
num_list.extend(even_list)
num_list.extend(odd_list)
print(num_list)