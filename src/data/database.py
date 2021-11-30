from data.ReadData import ReadData
from data.StoreData import StoreData
from data.DBConstants import *
import json

class DB:
    '''DB is a shortcut to ReadData and StoreData'''
    def __init__(self, model) -> None:
        '''Initialise the DB object using the model class'''
        self.storeObj = StoreData(model)
        self.readObj = ReadData(model)
        self.filename = self.getFileName(model)

    def getFileName(self, model):
        '''Filename is PREFIX constant + name of the model + SUFFIX constant'''
        model_name = model.__name__
        return DB_PREFIX+model_name+DB_SUFFIX+'.'+DB_FILETYPE

    def save(self, saveObj) -> object:
        '''Use StoreData functions'''
        return self.storeObj.store(self.filename, saveObj)

    def find(self, options: dict={}) -> list:
        '''Use StoreData functions'''
        return self.readObj.find(self.filename, options)

    def delete(self, id) -> list:
        '''Deletes a record from database using given id'''
        return self.storeObj.delete(self.filename, id)
    
    def runMigration(self):
        data = []

        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4, separators=(',',': '))