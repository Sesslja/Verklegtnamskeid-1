import json

class StoreData:
    def __init__(self, modelObj: object) -> None:
        self.modelObj = modelObj
    

    def store(self, filename, obj):
        data = vars(obj)

        try:
            with open(filename) as file:
                listObj = json.load(file)
                print(listObj)

                listObj.append(data)

                print(listObj)

                with open(filename, 'w') as json_file:
                    json.dump(listObj, json_file, indent=4, separators=(',',': '))

                return data

        except FileNotFoundError:
            print('file not found, might need to run a migration')


        print(filename)
