from interface.curso import Curso

def ceros(valor):
    return f"{valor:02d}"

class Platzi(Curso):
    url = "https://platzi.com/cursos/"

    def getTitle(self):
        titles = self.header().find_all('h1')
        for title in titles:
            return title.text.strip()

    def getCapitulos(self):
        quotes_html = self.header().find_all('span', class_="ContentClass-content-title")
        for cons, video in enumerate(quotes_html):
            super().lista.append(ceros(cons+1) + ' - ' + video.get_text().strip())
        return super().lista