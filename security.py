from user import User




def authenticate(username,password):
    user=User.findByUsername(username)
    return user
def identity(payload):
    
    userId=payload['identity']
    user=User.findById(userId)

    return user

