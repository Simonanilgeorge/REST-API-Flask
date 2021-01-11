from flask import Flask,request
from flask_restful import Resource,Api,reqparse
from flask_jwt import JWT,jwt_required
from security import authenticate,identity

app=Flask(__name__)
app.secret_key="ceejay"
api=Api(app)
jwt=JWT(app,authenticate,identity)
items=[{
"name":"a"
},
{"name":"b"}]

itemNameMapping={i['name']:i for i in items}
print(itemNameMapping)
class Item(Resource):
    @jwt_required()
    def get(self,name):

        item=itemNameMapping.get(name,None)
        if item:
        
            return {"name":name},200
        return {"message":"item with this name does not exist in the database"}
    @jwt_required()
    def post(self,name):
        data=request.get_json()
        item=itemNameMapping.get(name,None)
        if item:
            return {"message":"item with this name already exists in the database"}
        item={
            "name":name,
            "price":data["price"]
        }
        items.append(item)
        itemNameMapping[name]=item
        return {"items":items},201

class ItemList(Resource):
    def get(self):
        return {"items":items}

api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')

if __name__=="__main__":
    app.run(debug=True)