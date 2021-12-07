import json
import uuid
from datetime import datetime
from data.ReadData import ReadData
from data.DBError import DBError

class StoreData:
    def __init__(self, modelObj: object) -> None:
        self.modelObj = modelObj
        self.__readData = ReadData(modelObj)
    

    def store(self, filename, obj):
        ''' Stores the given object in the given file'''
        obj._id = str(uuid.uuid4()) # Creates a "unique" id for the record
        obj.created_at = str(datetime.now()) # Sets the current date and time
        data = self._objToDict(obj) # Converts the object and it's sub-objects(if any) to a dictionary

        try:
            with open(filename) as file: # Open the given file
                listObj = json.load(file) # Convert the records in the file to a list
                listObj.append(data) # Add our new record to the list

                with open(filename, 'w') as json_file: # Open the same file in write mode
                    json.dump(listObj, json_file, indent=4, separators=(',',': ')) # Add our updated list to the file

                return obj # Returns the object we were given to show updated objects(_id and created_at) and indicate success

        except FileNotFoundError:
            return DBError('TABLE_NOT_EXIST') # Return DBError if the file does not exist


    def delete(self, filename, id) -> bool:
        '''Delete record in file by records id'''
        try:
            with open(filename) as file: # Open file
                listObj: list = json.load(file) # Convert file to json list

                for index, row in enumerate(listObj): # Iterare through all records in table
                    if row['_id'] == id:
                        try:
                            listObj.pop(index) # Delete the record if id is found
                        except IndexError:
                            return DBError('DELETION_ERROR') # Return DBError if the deletion failed(index not found)
                        break
                with open(filename, 'w') as json_file:
                    json.dump(listObj, json_file, indent=4, separators=(',',': ')) # Write updated list to the file
                return True
        except FileNotFoundError:
            return DBError('TABLE_NOT_EXIST') # Returns DBError if file doesn't exist

    def update(self, filename, data) -> object:
        _id = data['_id']

        try:
            with open(filename) as file: # Open the given file
                listObj = json.load(file) # Convert the records in the file to a list

                for i, record in enumerate(listObj):
                    if record['_id'] == _id:
                        for key in data:
                            listObj[i][key] = data[key]
                        updated_record = listObj[i]
                        break

                    #print(record)

                with open(filename, 'w') as json_file: # Open the same file in write mode
                    json.dump(listObj, json_file, indent=4, separators=(',',': ')) # Add our updated list to the file

                    return self.__readData._dictToModel(updated_record) # Returns the updated object
        except FileNotFoundError:
            pass
                    

    def _objToDict(self, obj) -> dict:
        ''' Converts a class instance into a dictionary.
        Checks all values in the dictionary if they are a class instance as well
        and converts them.'''
        data = vars(obj)
        for key in data:
            if type(data[key]) is list:
                for i, entry in enumerate(data[key]):
                    try:
                        entry.__dict__
                        data[key][i] = (self._objToDict(entry))
                    except AttributeError:
                        continue
            else:
                try:
                    print(data[key].__dict__)
                    data.update({ key: self._objToDict(data[key]) }) # Update the dictionary with the same method if an class instance is found.
                except AttributeError:
                    continue # If value is not a class instance then it continues.
        return data