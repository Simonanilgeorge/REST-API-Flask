from flask import Flask,request
from flask_restful import Resource,Api,reqparse
from flask_jwt import JWT,jwt_required
from security import authenticate,identity
from user import UserRegister

app=Flask(__name__)
app.secret_key="ceejay" 
api=Api(app)
jwt=JWT(app,authenticate,identity)
items=[]



class Item(Resource):

    parser=reqparse.RequestParser()
    parser.add_argument('price',
    type=float,
    required=True,
    help="This field cannot be left blank")
    
    @jwt_required()
    def get(self,name):
        item=next(filter(lambda x:x['name']==name,items),None)
        if item:
            return {"item":item}
        return {"message":"item does not exist"}


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

api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(UserRegister,'/register')

if __name__=="__main__":
    app.run(debug=True)