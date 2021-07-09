users = [
       
        {"username":"krish","email":"krish.t@gmail.com","password":"krish@123","fullname":"Krish T"},
        {"username":"manoj","email":"manoj.pvn@gmail.com","password":"manoj@123","fullname":"Manoj PVN"},
        {"username":"sujith","email":"sujith.s@gmail.com","password":"sujith@123","fullname":"Sujith S"},
        {"username":"naresh","email":"naresh.n@gmail.com","password":"krish@123","fullname":"naresh M"}
        #1000000
]

user_map = {}

for user in users:
    user_map[user['username']] = user

def find_by_user_name(username):
    return user_map.get(username)

def login(username,password):
    user = find_by_user_name(username)
    if user and user["password"] == password:
        return user["fullname"]
    
  
fullName = login("krish","krish@123")
if fullName:
    print("Welcome ",fullName)
else:
    print("Sorry you have entered bad credentials")


