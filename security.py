from models.user import UserModel




def authenticate(username,password):
    user=UserModel.findByUsername(username)
    return user
def identity(payload):
    
    userId=payload['identity']
    user=UserModel.findById(userId)

    return user

