import json
from typing import Type
from data.ModelListConstants import SUBMODELS
from data.DBError import DBError, RecordNotFoundError

class ReadData:
    def __init__(self, modelObj: object) -> None:
        self.modelObj = modelObj
        self.modelKeys = self._getKeys(self.modelObj())

    def find(self, filename: str,  options: dict= {}) -> list[object]:
        try:
            where = options['where']
        except KeyError:
            where = None
        try:
            relations = options['relations']
        except KeyError:
            relations = None
        try:
            limit: int = options['limit']['limit']
            page: int = options['limit']['page']
        except KeyError:
            limit: int = 0
            page: int = 0
        try:
            with open(filename) as file:
                listObj = json.load(file)
                find_list = []
                
                record_start = limit * page
                record_end = (record_start + limit) if limit>0 else len(listObj)
                for row in listObj[record_start:record_end]:
                    if self._checkWhereOptions(row, where):
                        model = self._dictToModel(row)
                        find_list.append(model)

                return find_list
        except FileNotFoundError:
            print('file not found, might need to run a migration')

    def findOne(self, filename: str, options: dict = {}) -> object:
        '''Returns the first record found matching given options'''
        try:
            options.pop('limit')
        except KeyError:
            pass
        # options.update({'limit': {'limit':1, 'page':0}})
        try:
            return self.find(filename, options)[0]
        except IndexError:
            print('didnt find')
            raise RecordNotFoundError

    
    def _getKeys(self, obj):
        '''Get the key names of the model'''
        return [*vars(obj)]

    def _checkWhereOptions(self, row, where: dict=None):
        ''' Check wether row confines with the constraints given in where'''
        if where is not None:
            #if [key for key in where]
            for key in where:
                if type(row[key]) is dict:
                    if not self._checkWhereOptions(row[key], where[key]):
                        return False
                elif type(row[key]) is list:
                    try:
                        row[key].index(where[key])
                    except ValueError:
                        return False
                elif row[key] != where[key]:
                    return False
        return True


    def _dictToModel(self, foundDict: dict, customModel=None) -> object:
        if customModel is None:
            model = self.modelObj()
        else:
            model = customModel()
        model_attr = vars(model)
        model_keys = self._getKeys(model)
        attr_types = {k: type(v) for k, v in iter(model_attr.items())}

        for key in model_keys:
            try:
                if key in foundDict and not None:
                    if attr_types[key] is type and key in SUBMODELS:
                        foundDict[key] = self._dictToModel(dict(foundDict[key]), SUBMODELS[key])
                    elif type(attr_types[key]) is list:
                        sub_list = []
                        for col in attr_types[key]:
                            if col is type and key in SUBMODELS:
                                print('er i dotinu')
                                sub_list.append(self._dictToModel(dict(foundDict[key]), SUBMODELS[key]))
                        print(sub_list)
                        foundDict[key] = sub_list
                    model.__setattr__(key, foundDict[key])
            except TypeError:
                print('typu err')
                raise RecordNotFoundError
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