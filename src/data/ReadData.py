import json

class ReadData:
    def __init__(self, modelObj: object) -> None:
        self.modelObj = modelObj
        self.modelKeys = self.getKeys(self.modelObj())

    def find(self, filename: str,  options: dict= {}):
        try:
            where = options['where']
        except KeyError:
            where = None
        try:
            relations = options['relations']
        except KeyError:
            relations = None
        try:
            with open(filename) as file:
                listObj = json.load(file)
                find_list = []
                

                for row in listObj:

                    if self.checkWhereOptions(where):
                        model = self.dictToModel(row)
                        find_list.append(model)

                return find_list

        except FileNotFoundError:
            print('file not found, might need to run a migration')


        print(filename)
    
    def getKeys(self, obj):
        '''Get the key names of the model'''
        return [*vars(obj)]

    def checkWhereOptions(self, row, where: dict=None):
        ''' Check wether row confines with the constraints given in where'''
        if where is not None:
            #if [key for key in where]
            for key in where:
                if row[key] != where[key]:
                    return False
        return True


    def dictToModel(self, dict: dict) -> object:
        model = self.modelObj()
        for key in dict:
            if key in self.modelKeys:
                model.__setattr__(key, dict[key])
        return model


# menuPoss = {
#     "Properties": {
#         "short": "P",
#         "class": PropertyAPI,
#         "accessControl": ""
#     },
#     "Employees": {
#         "short": "E",
#         "class": UserAPI,
#         "accessControl": "manager"
#     }
# }
# 
# propertyMenu = {
#     "Properties": {
#         "short": "P",
#         "class": PropertyAPI,
#         "accessControl": ""
#     },
#     "Employees": {
#         "short": "E",
#         "class": UserAPI,
#         "accessControl": "manager"
#     }
# }