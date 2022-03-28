from interface.curso import Curso

class edTeam(Curso):
    url = "https://ed.team/cursos/"

    def getTitle(self):
        titles = self.header().find_all('h1', class_="title s-mb-1 s-cross-start s-nowrap")
        for title in titles:
            return title.text.strip()

    def getCapitulos(self):
        quotes_html = self.header().find_all('p', class_="s-mb-0 s-color-text s-mr-2")
        for video in quotes_html:
            super().lista.append(video.get_text().strip())
        return super().lista