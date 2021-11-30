import json
import uuid
from datetime import datetime
from data.DBError import DBError
import inspect

class StoreData:
    def __init__(self, modelObj: object) -> None:
        self.modelObj = modelObj
    

    def store(self, filename, obj):
        obj._id = str(uuid.uuid4())
        obj.created_at = str(datetime.now())
        data = vars(obj)
        #for key in data:
        #    print(inspect.isclass(data[key]))
        #    if inspect.isclass(data[key]):
        #        print('is object')
        #        data.update({ key: vars(data[key]) })

        try:
            with open(filename) as file:
                listObj = json.load(file)
                listObj.append(data)

                with open(filename, 'w') as json_file:
                    json.dump(listObj, json_file, indent=4, separators=(',',': '))

                return data

        except FileNotFoundError:
            return DBError('TABLE_NOT_EXIST')


    def delete(self, filename, id) -> bool:
        try:
            with open(filename) as file:
                listObj: list = json.load(file)

                for index, row in enumerate(listObj):
                    if row['_id'] == id:
                        try:
                            listObj.pop(index)
                        except IndexError:
                            return DBError('DELETION_ERROR')
                        break
                with open(filename, 'w') as json_file:
                    json.dump(listObj, json_file, indent=4, separators=(',',': '))
                return True
        except FileNotFoundError:
            return DBError('TABLE_NOT_EXIST')
                    

