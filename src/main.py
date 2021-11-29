# Initar alla layerana

from logic.UserLogic import UserAPI
from logic.PropertyLogic import PropertyAPI

userlogic = UserAPI()
propertyLogic = PropertyAPI()

#userlogic.createEmployee('Kiddi Sales', 'sales@nan.is', 6969690420)
#amenities = ['Klósett', 'Sturta', 'Eldhús']
#propertyLogic.createProperty('Dúfnahólar 10', '85858328jfjfu83', amenities)
userlogic.findEmployees()