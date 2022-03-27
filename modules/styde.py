from interface.curso import Curso

class Styde(Curso):
    url = "https://styde.net/"

    def getTitle(self):
        titles = self.header().find_all('h1')
        for title in titles:
            return title.text.strip()

    def getCapitulos(self):
        quotes_html = self.header().find_all('ul', class_="lesson-list")
        for video in quotes_html:
            for lista in video.find_all('li'):
                print(lista.text.strip())
