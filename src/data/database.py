from typing import TypeVar
from data.DBError import DBError
from data.ReadData import ReadData
from data.StoreData import StoreData
from data.DBConstants import *
import os.path
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
        filename = DB_DIR + DB_PREFIX+model_name+DB_SUFFIX+'.'+DB_FILETYPE
        if not os.path.isfile(filename):
            self.runMigration(filename)
        return filename

    def save(self, saveObj) -> object:
        '''Use StoreData functions'''
        return self.storeObj.store(self.filename, saveObj)

    def update(self, updateDict: dict) -> object:
        '''Use update() in StoreData'''
        return self.storeObj.update(self.filename, updateDict)

    def find(self, options: dict={}) -> list[object]:
        '''Use StoreData functions'''
        found_data = self.readObj.find(self.filename, options)
        if found_data is not False:
            return found_data
        return False

    def findOne(self, options: dict={}) -> object or bool:
        found_item: dict = self.readObj.findOne(self.filename, options)
        if found_item is not False:
            return found_item
        return False

    def delete(self, id) -> list:
        '''Deletes a record from database using given id'''
        return self.storeObj.delete(self.filename, id)
    
    def runMigration(self, filename: str):
        data = []

        with open(filename, 'w') as file:
            json.dump(data, file, indent=4, separators=(',',': '))