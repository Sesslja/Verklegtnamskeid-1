import json

class ReadData:
    def __init__(self, modelObj: object) -> None:
        self.modelObj = modelObj

    def find(self, filename: str,  options: dict= {}):
        try:
            with open(filename) as file:
                listObj = json.load(file)
                find_list = []
                
                modelKeys = self.getKeys(self.modelObj())

                for row in listObj:
                    model = self.modelObj()
                    for key in row:
                        if key in modelKeys:
                            model.__setattr__(key, row[key])
                    find_list.append(model)

                return find_list

                            

        except FileNotFoundError:
            print('file not found, might need to run a migration')


        print(filename)
    
    def getKeys(self, obj):
        '''Get the key names of the model'''
        return [*vars(obj)]
