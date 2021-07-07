lst1 = [1001,1002,1003,1005,1006]
lst2 = [1005,1008,1010,1015]
lst3 = [2010,1020,1015,1010,1002]

num_set = set()
num_set.update(lst1,lst2,lst3)
num_set=sorted(num_set,reverse=True)
print(num_set)