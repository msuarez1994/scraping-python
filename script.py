from modules.openWebinars import OpenWebinar
from modules.platzi import Platzi
from modules.styde import Styde
from modules.codigofacilito import CodigoFacilito

# obj = OpenWebinar('javascript-avanzado')
# print(obj.getTitle())
# for caps in obj.getCapitulos():
#     print(caps)

# platzi = Platzi('react-practico')
# print(platzi.getTitle())
# for caps in platzi.getCapitulos():
#     print(caps)

# styde = Styde('tecnicas-de-autorizacion-con-laravel')
# print(styde.getTitle())
# for caps in styde.getCapitulos():
#     print(caps)

codfacilito = CodigoFacilito('rails-profesional')
print(codfacilito.getTitle())
for caps in codfacilito.getCapitulos():
    print(caps)