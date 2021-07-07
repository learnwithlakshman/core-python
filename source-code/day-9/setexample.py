CS = "Krish,Manoj,Charan,Kiran,Naresh"
IS = "Krish,Balu,Srinu,Jayesh"
EC = "Balu,Ramesh,Rohit,Charan,Krish,Kiran"
names = set()
names.update(CS.split(","),IS.split(","),EC.split(","))
print(names)
print(len(names))
# Count of faculty in the college

cs_list = CS.split(",")
is_list = IS.split(",")
ec_list = EC.split(",")

# if len(cs_list) < len(is_list) and len(cs_list) < len(ec_list):
#     min_list = cs_list
# elif len(is_list) < len(ec_list):
#     min_list = is_list    
# else:
#     min_list = ec_list

# for name in min_list:
#     if name in is_list and name in cs_list and name in ec_list:
#         print(f"=====> {name}")

u_name_set = set(cs_list).intersection(set(is_list)).intersection(set(ec_list))
print(u_name_set)
