'''
parent je Tabela na katero se nanaša
child je Tabela iz katere se nanaša
stolpec je Stolpec iz child

'''

class Povezava():
    def __init__(self,parent,child,stolpec):
        super().__init__()


        self.setup()
    def setup(self):
        pass

    def izpis(self):
        pass


if __name__ == "__main__":
    Povezava()