from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource):

    parser=reqparse.RequestParser()
    parser.add_argument('price',
    type=float,
    required=True,
    help="This field cannot be left blank")
    
    @jwt_required()
    def get(self,name):
        try:
            item=ItemModel.findByName(name)
        except:
            return {"message":"An error occured"}
        if item:
            return item.json()
        else:
            return {"message":"Item not found"},404

    def post(self,name):
        
        if ItemModel.findByName(name):
            return {"message":"An item with name: {} already exists".format(name)}
       
        
        data=Item.parser.parse_args()   
        print(data)    
        item=ItemModel(name,data["price"])
        print(item)

        try:
            item.saveToDb()
        except:
            return {"message":"an error occured"},500
        return {"message":"Item {} added".format(item.name)},201
    
    def delete(self,name):
        item=ItemModel.findByName(name)
        if item:
            item.deleteFromDb()
            return {"message":"Item deleted"}
        else:
            return {"message":"Item does not exist"}

    def put(self,name):

        data=Item.parser.parse_args()
        
        item=ItemModel.findByName(name)
        



        if item is None:
            item=ItemModel(name,data["price"])
        else:
            item.price=data["price"]

        item.saveToDb()
        return item.json()


  


        

class ItemList(Resource):


    def get(self):
        return {"items":[item.json() for item in ItemModel.query.all()]}
        # alternate method to return all items
        # return {"items":list(map(lambda x:x.json,ItemModel.query.all()))}
