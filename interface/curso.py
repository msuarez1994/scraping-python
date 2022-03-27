import requests
from bs4 import BeautifulSoup


class Curso:
    url = ''
    def __init__(self, partial):
        self.partial = partial
    
    def getUrl(self):
        return self.url + self.partial

    def header(self):
        response = requests.get(self.getUrl())
        html = BeautifulSoup(response.text, 'html.parser')
        return html
    
