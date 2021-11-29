import json

from model.userModel import User

class ReadData:
    def __init__(self, modelObj: object) -> None:
        self.modelObj = modelObj

    def find(self, filename: str,  options: dict= {}):
        try:
            with open(filename) as file:
                listObj = json.load(file)
                print(listObj)

                getvars = self.modelObj()
                print(vars(getvars).keys())

                user = User()

                for row in listObj:
                    for key in row:
                        #print(key)
                        pass

        except FileNotFoundError:
            print('file not found, might need to run a migration')


        print(filename)
    
    def getKeys(self):
        getvars = self.modelObj()
        print(vars(getvars).keys())