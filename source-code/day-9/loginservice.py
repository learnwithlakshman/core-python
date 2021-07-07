users = [
       
        {"username":"krish","email":"krish.t@gmail.com","password":"krish@123","fullname":"Krish T"},
        {"username":"manoj","email":"manoj.pvn@gmail.com","password":"manoj@123","fullname":"Manoj PVN"},
        {"username":"sujith","email":"sujith.s@gmail.com","password":"sujith@123","fullname":"Sujith S"},
        {"username":"naresh","email":"naresh.n@gmail.com","password":"krish@123","fullname":"naresh M"}
        #1000000
]

def login(username,password):
    pass


fullName = login("abc","manoj@123")
if fullName:
    print("Welcome ",fullName)
else:
    print("Sorry you have given bad credentials")