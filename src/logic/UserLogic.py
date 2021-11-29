from model.userModel import User
from data.database import DB

class UserAPI:
    def __init__(self) -> None:
        self.userRepo = DB(User)

    def createEmployee(self, name: str, email: str, ssn: int):
        new_user = User(name, email, ssn, False)
        return self.userRepo.save(new_user)

    def findEmployees(self):
        return self.userRepo.find()