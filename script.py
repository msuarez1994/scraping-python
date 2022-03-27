from modules.openWebinars import OpenWebinar
from modules.platzi import Platzi
from modules.styde import Styde

# obj = OpenWebinar('crear-plugins-para-wordpress')
# print(obj.getTitle())
# print(obj.getCapitulos())


p = Platzi('react-practico')
print(p.getTitle())
print(p.getCapitulos())

# styde = Styde('tecnicas-de-autorizacion-con-laravel')
# print(styde.getTitle())
# print(styde.getCapitulos())