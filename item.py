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
        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()
        query="SELECT * FROM items WHERE name=?"
        result=cursor.execute(query,(name,))
        row=result.fetchone()
        connection.close()

        if row:
            return {"item":{"name":row[0],"price":row[1]}}
        return {"message":"item does not exist"},404


    # @jwt_required()
    def post(self,name):
        
        if next(filter(lambda x:x['name']==name,items),None):
            return {"message":"an item with this name already exists"}
        data=Item.parser.parse_args()
        item={
            "name":name,
            "price":data["price"]
        }
        items.append(item)
       
        return {"items":items},201
    
    def delete(self,name):
        global items
        items=list(filter(lambda x:x['name']!=name,items))
        return {"message":"item {} deleted".format(name)}

    def put(self,name):

        data=Item.parser.parse_args()
        item=next(filter(lambda x:x['name']==name,items),None)
        if item is None:
            item={"name":name,"price":data["price"]}
            items.append(item)
        else:
            item.update(data)
        return item
        

class ItemList(Resource):
    def get(self):
        return {"items":items}
