from sys import modules
from modules.openWebinars import OpenWebinar
from modules.platzi import Platzi
from modules.styde import Styde
from modules.codigofacilito import CodigoFacilito
from modules.edTeam import edTeam
from modules.cursosDesarrolloWeb import cursosDesWeb

# obj = OpenWebinar('javascript-avanzado')
# print(obj.getTitle())
# for caps in obj.getCapitulos():
#     print(caps)

# platzi = Platzi('react-practico')
# print(platzi.getTitle())
# for caps in platzi.getCapitulos():
#     print(caps)

styde = Styde('manejo-de-colecciones-en-laravel')
print(styde.getTitle())
for caps in styde.getCapitulos():
    print(caps)

# codfacilito = CodigoFacilito('rails-profesional')
# print(codfacilito.getTitle())
# for caps in codfacilito.getCapitulos():
#     print(caps)

# edteam = edTeam('javascript')
# print(edteam.getUrl())
# print(edteam.getTitle())
# for caps in edteam.getCapitulos():
#     print(caps)

# desWeb = cursosDesWeb('desarrollar-formulario-con-subida-de-archivos-laravel-livewire')
# print(desWeb.getTitle())

# for caps in desWeb.getCapitulos():
#     print(caps)