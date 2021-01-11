class User():
    def __init__(self,_id,username,password):
        self.id=_id
        self.username=username
        self.password=password
    def __str__(self):
        return f"username: {self.username} id:{self.id}"
    def __repr__(self):
        return f"username:{self.username} id:{self.id}"