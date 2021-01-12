from werkzeug.security import safe_str_cmp
class User:
    def __init__(self,_id,username,password):
        self.id=_id
        self.username=username
        self.password=password
    def __str__(self):
        return f"username: {self.username} id:{self.id} password:{self.password}"
    def __repr__(self):
        return f"username: {self.username} id:{self.id} password:{self.password}"
    @classmethod
    def validate(cls,usernam,password):
        print(f"username to validate is :{username} ")
        user=usernameMapping.get(username,None)
        if user and safe_str_cmp(user.password,password):
            print(f"Access Granted for {user.username}")
        else:
            print("Invalid credentials")
    @classmethod
    def findById(cls,ID):
        
        user=useridMapping.get(ID,None)
        if user:
            return user
        else:
            return "Invalid"
    @classmethod
    def findByUserName(cls,username):
        
        user=usernameMapping.get(username,None)
        if user:
            return user
        else:
            return "Invalid"



    

users=[
    User(1,'bob','aaa'),
    User(2,'bruce','bbb'),
    User(3,'john','ccc')
]
ID=4
username='john'
password='aaa'
usernameMapping={u.username:u for u in users}
useridMapping={u.id:u for u in users}
User.validate(username,password)
userByID=User.findById(ID)
print(f"user by id is {userByID}")
userByName=User.findByUserName(username)
print(f"user by name is {userByName}")