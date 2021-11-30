# Initar alla layerana

from logic.UserLogic import UserAPI
from logic.PropertyLogic import PropertyAPI

userlogic = UserAPI()
propertyLogic = PropertyAPI()

#userlogic.createEmployee('Kiddi Sales', 'sales@nan.is', 1234567890)
#amenities = ['Klósett', 'Sturta', 'Eldhús']
#propertyLogic.createProperty('Dúfnahólar 10', '85858328jfjfu83', amenities)
all_users = userlogic.findEmployees()
for user in all_users:
    print(user.name, user._id)

if userlogic.deleteEmployee('7449c5bc-217c-42fe-b42d-04cb26fb482e'):
    all_users = userlogic.findEmployees()
    for user in all_users:
        print(user.name, user._id)