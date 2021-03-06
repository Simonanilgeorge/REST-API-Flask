
from db import db

class ItemModel(db.Model):

    __tablename__="items"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80))
    price=(db.Column(db.Float(precision=2)))

    def __init__(self,name,price):
        self.name=name
        self.price=price
    def json(self):
        return {"name":self.name,"price":self.price}



    
    def deleteFromDb(self):
        db.session.delete(self)
        db.session.commit()


    
    def saveToDb(self):
        db.session.add(self)
        db.session.commit()



    @classmethod
    def findByName(cls,name):
        return ItemModel.query.filter_by(name=name).first()
        