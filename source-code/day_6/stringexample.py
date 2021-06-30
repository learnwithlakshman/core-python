data = " Ramya , Deepa,LIRIL ,amma, dad, Kiran, 12321 , Suresh, Jayesh, Ramesh,Balu"

lst = data.split(",")

for name in lst:
    name = name.strip().upper()
    rname = name[::-1]
    if name == rname:
        print(name)

girlsdata = "Tanvi,Dhatri,Haadya,Deepthi,Deepa,Ramya"
# Name which start with DEE get those name
print("-"*20)
names = girlsdata.split(",")
for name in names:
    name = name.upper()
    if "D" in name:
        print(name)