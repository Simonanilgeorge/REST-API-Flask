
from db import db

class StoreModel(db.Model):

    __tablename__="stores"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80))
   

    def __init__(self,name):
        self.name=name
        
    def json(self):
        return {"name":self.name,"items":self.items}



    
    def deleteFromDb(self):
        db.session.delete(self)
        db.session.commit()


    
    def saveToDb(self):
        db.session.add(self)
        db.session.commit()



    @classmethod
    def findByName(cls,name):
        return ItemModel.query.filter_by(name=name).first()
        