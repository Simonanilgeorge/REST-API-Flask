import sqlite3
from flask_restful import Resource,reqparse
from models.user import UserModel


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
        user=UserModel.findByUsername(data['username'])
        if user:
            return {"message":"A user with that username already exists "},400
        print(f"New user info send from the client is {data}")

        user=UserModel(data["username"],data["password"])
        # alternate method to execute the above line
        # user=UserModel(**data)
        user.saveToDb()

        return {"message":"user added successfully"},201