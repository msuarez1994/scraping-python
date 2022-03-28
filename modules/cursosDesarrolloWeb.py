from interface.curso import Curso

class cursosDesWeb(Curso):
    url = "https://www.cursosdesarrolloweb.es/course/"

    def getTitle(self):
        titles = self.header().find_all('h1', class_="text-white")
        for title in titles:
            return title.text.strip()

    def getCapitulos(self):
        quotes_html = self.header().find_all('a', class_="flex")
        for video in quotes_html:
            super().lista.append(video.get_text().strip())
        return super().lista