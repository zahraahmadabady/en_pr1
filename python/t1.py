class User(): 
    def __init__(self,username,password):
        self.UserName=username
        self.Password=password



class Buyer(User):

    def __init__(self,username,password,address,nationalcode):
        super().__init__(username,password)
        self.Address=address
        self.NationalCode=nationalcode

User_1=Buyer('Zahra',12345,"qom",322222234)
print("UserName:",User_1.UserName)
print("Password:",User_1.Password)
print("Address:",User_1.Address)
print("NationnalCode:",User_1.NationalCode)