# Initar alla layerana

from model.AddressType import Address
from model.userModel import User
from test.UserLogic import UserAPI
from test.PropertyLogic import PropertyAPI

userlogic = UserAPI()
propertyLogic = PropertyAPI()

#address = Address(country='Greenland', city='Nuuk', zip=420, address1='Nuukway 1')
#userlogic.createEmployee('Laura', 'laura@nan.is', 1234567890, address)

#for i in range(20):
#    country = 'Greenland' if i%2 else 'Iceland'
#    address = Address(country=country, city='Eih', zip=420, address1='Nuukway 1')
#    userlogic.createEmployee(i, f'{i}@nan.is', i*10^7, address)

#amenities = ['Klósett', 'Sturta', 'Eldhús']
#propertyLogic.createProperty('Dúfnahólar 10', '85858328jfjfu83', amenities)
all_users = userlogic.findEmployees(limit=3, page=1)
#all_properties = propertyLogic.findPropertyByAmenity('bleh')

# for user in all_users:
#     print(user.name, user._id)

# if userlogic.deleteEmployee('7449c5bc-217c-42fe-b42d-04cb26fb482e'):
#     all_users = userlogic.findEmployees()
#     for user in all_users:
#         print(user.name, user._id)

def formatTing(many:list):
    header = [*vars(many[0])]
    if 'Address' in header:
        header.remove('Address')
    format_row = "{:>20}" * (len(header))
    print(format_row.format("", *header))
    for user in many:
        user_vals = []
        for key in header:
            user_vals.append(user.__getattribute__(key))
        print(format_row.format(*user_vals))

for user in all_users:
    print(user.Address.country, user.name, user.ssn)
    #for amenity in prop.amenities:
    #    print(amenity)