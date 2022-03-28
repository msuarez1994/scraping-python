from interface.curso import Curso

def ceros(valor):
    return f"{valor:02d}"
class OpenWebinar(Curso):
    url = "https://openwebinars.net/cursos/"

    def getTitle(self):
        titles = self.header().find_all('h1', class_="title text-left")
        for title in titles:
            return title.text.strip()

    def getCapitulos(self):
        quotes_html = self.header().find_all('h4', class_="col-8")
        for cons, video in enumerate(quotes_html):
            super().lista.append(ceros(cons+1) + ' - ' + video.get_text().strip())
        return super().lista