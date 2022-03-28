import requests
from bs4 import BeautifulSoup
class Curso:
    url = ''
    lista = []
    def __init__(self, partial):
        self.partial = partial
    
    def getUrl(self):
        return self.url + self.partial

    def header(self):
        response = requests.get(self.getUrl(), headers={'User-Agent': 'Mozilla/5.0'})
        html = BeautifulSoup(response.text, 'html.parser')
        return html
    
