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

                model_keys = self.getKeys()
                new_dict = {}

                for row in listObj:
                    new_dict = {}
                    for key in row:
                        if key in model_keys:
                            new_dict.update({key: row[key]})
                
                    print(new_dict)

                            

        except FileNotFoundError:
            print('file not found, might need to run a migration')


        print(filename)
    
    def getKeys(self):
        '''Get the key names of the model'''
        getvars = self.modelObj()
        return [*vars(getvars)]