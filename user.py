import sqlite3
from flask_restful import Resource,reqparse

class User():

    def __init__(self,_id,username,password):
        self.id=_id
        self.username=username
        self.password=password
    
    @classmethod
    def findByUsername(cls,username):
        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()
        query="SELECT * FROM users WHERE username=?"
        # parameter passed must be in the form of a tuple
        result=cursor.execute(query,(username,))
        row=result.fetchone()
        if row:
            user=cls(*row)
        else:
            user=None

        connection.close()
        return user

    @classmethod
    def findById(cls,_id):
        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()
        query="SELECT * FROM users WHERE id=?"
        # parameter passed must be in the form of a tuple
        result=cursor.execute(query,(_id,))
        row=result.fetchone()
        if row:
            user=cls(*row)
        else:
            user=None

        connection.close()
        return user

    
    def __str__(self):
        return f"username: {self.username} id:{self.id}"
    def __repr__(self):
        return f"username:{self.username} id:{self.id}"

class UserRegister(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument("username",
    required=True,
    type=str,
    help="Username is a required field")
    
    parser.add_argument("password",
    required=True,
    type=str,
    help="Password is a required field")
    
    def post(self):

        data=UserRegister.parser.parse_args()

        print(f"New user info send from the client is {data}")

        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()
        query="INSERT INTO users VALUES(null,?,?)"
        cursor.execute(query,(data['username'],data['password']))
        connection.commit()
        connection.close()

        return {"message":"user created successfully"},201
