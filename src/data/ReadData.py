import json
from typing import Type
from data.ModelListConstants import SUBMODELS
from data.DBError import DBError

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


    def dictToModel(self, foundDict: dict, customModel=None) -> object:
        if customModel is None:
            model = self.modelObj()
        else:
            model = customModel()
        model_attr = vars(model)
        model_keys = self.getKeys(model)
        attr_types = {k: type(v) for k, v in iter(model_attr.items())}

        for key in model_keys:
            try:
                if key in foundDict and not None:
                    if attr_types[key] is type and key in SUBMODELS:
                        foundDict[key] = self.dictToModel(dict(foundDict[key]), SUBMODELS[key])
                    model.__setattr__(key, foundDict[key])
            except TypeError:
                return DBError('TYPE_NOT_AVAILABLE')
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