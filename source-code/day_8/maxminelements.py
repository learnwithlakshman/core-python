import random
def max_min(lst):
    min = max = lst[0]
    for i in range(1,len(lst)):
        if min > lst[i]:
            min = lst[i]
        if max < lst[i]:
            max = lst[i]
    return max, min



 

input_lst = [random.randint(100,500) for i in range(1,11)]
print(input_lst)
max_r,min_r = max_min(input_lst)
max , min = max(input_lst),min(input_lst)

input_lst.sort(reverse=True)
print(input_lst)