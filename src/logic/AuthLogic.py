from data.DBError import RecordNotFoundError
from data.database import DB
from model.userModel import User

class AuthAPI:
    '''Logic for log in authentication'''
    def __init__(self) -> None:
        self.userRepo = DB(User)

    def userLogin(self, userSsn):
        try:
            return self.userRepo.findOne({
                'where': {
                    'ssn': userSsn
                }
            })
        except RecordNotFoundError:
            return False
