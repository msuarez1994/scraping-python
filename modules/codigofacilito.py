from interface.curso import Curso

def ceros(valor):
        return f"{valor:02d}"

class CodigoFacilito(Curso):
    url = "https://codigofacilito.com/cursos/"

    def getTitle(self):
        titles = self.header().find_all('h1', class_="no-margin normal-line-height h1 f-text-36")
        for title in titles:
            return title.text.strip()

    def getCapitulos(self):
        quotes_html = self.header().find_all('li', class_="f-grey-text green-alpha-hover topic-item")
        for cons, video in enumerate(quotes_html):
            print(ceros(cons+1),'-',video.get_text().strip(), end="\n")

    def secciones(self):
        seccions = self.header().find_all('div', class_="right-space col-xs no-padding")
        for sec in seccions:    
            print(sec.text.strip(), end="\n")