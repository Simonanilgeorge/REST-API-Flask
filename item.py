from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
import sqlite3

class Item(Resource):

    parser=reqparse.RequestParser()
    parser.add_argument('price',
    type=float,
    required=True,
    help="This field cannot be left blank")
    
    @jwt_required()
    def get(self,name):
        try:
            item=self.findByName(name)
        except:
            return {"message":"An error occured"}
        if item:
            return item
        else:
            return {"message":"Item not found"},404

    def post(self,name):
        
        if self.findByName(name):
            return {"message":"An item with name: {} already exists".format(name)}
       
        data=Item.parser.parse_args()       
        item={"name":name,"price":data["price"]}

        try:
            self.insert(item)
        except:
            return {"message":"an error occured"},500
        return {"message":"Item {} added".format(item.get("name"))},201
    
    def delete(self,name):
        
        if self.findByName(name) is None:
            return {"message":"Item does not exist"}

        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()
        query="DELETE FROM items WHERE name=?"
        cursor.execute(query,(name,))
        connection.commit()
        connection.close()

        return {"message":"item {} deleted".format(name)}

    def put(self,name):

        data=Item.parser.parse_args()
        item=self.findByName(name)
        updatedItem={"name":name,"price":data["price"]}



        if item is None:
            try:
                self.insert(updatedItem)
            except:
                {"message":"An error occured when updating the item"},500
        else:
            try:
                self.update(updatedItem)
            except:
                {"message":"An error occured when updating the item"},500
        return updatedItem


  



    @classmethod
    def update(cls,item):
        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()
        query="UPDATE items SET price=? WHERE name=?"
        cursor.execute(query,(item["price"],item["name"]))
        connection.commit()
        connection.close()

    @classmethod
    def insert(cls,item):
        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()
        query="INSERT INTO items VALUES(?,?)"
        cursor.execute(query,(item['name'],item['price']))
        connection.commit()
        connection.close()



    @classmethod
    def findByName(cls,name):
        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()
        query="SELECT * FROM items WHERE name=?"
        result=cursor.execute(query,(name,))
        row=result.fetchone()
        connection.close()
        if row:
            return {"item":{"name":row[0],"price":row[1]}}
        

class ItemList(Resource):
    def get(self):
        return {"items":"items"}
