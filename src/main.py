# Initar alla layerana

from model.AddressType import Address
from model.userModel import User
from logic.UserLogic import UserAPI
from logic.PropertyLogic import PropertyAPI

userlogic = UserAPI()
propertyLogic = PropertyAPI()

#address = Address(country='Greenland', city='Nuuk', zip=420, address1='Nuukway 1')
#userlogic.createEmployee('Laura', 'laura@nan.is', 1234567890, address)
#amenities = ['Klósett', 'Sturta', 'Eldhús']
#propertyLogic.createProperty('Dúfnahólar 10', '85858328jfjfu83', amenities)
all_users = userlogic.findEmployees()

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

formatTing(all_users)