# radia.grace.main.py
# __author__ Finn
from _spy.vitollino.main import Cena, Elemento, STYLE

STYLE["width"] = 800
STYLE["height"] = "600px"

IMAGEM = "https://i.imgur.com/my9MiVU.jpeg"

PORTAO_BRONZE = "https://i.imgur.com/103Lydz.png"
PALACIO_CORAL = "https://i.imgur.com/3Ywu4pe.jpg"
PALACIO_CORAL2 = "https://i.imgur.com/3Ywu4pe.jpg"

PAWN = "https://static.vecteezy.com/system/resources/previews/021/975/110/original/pawn-3d-render-icon-illustration-with-transparent-background-chess-game-png.png"

class IlhaProibida:
    def __init__(self):
        oceano = Cena(IMAGEM).vai()
        info_terrenos = [PORTAO_BRONZE, PALACIO_CORAL, PALACIO_CORAL2]
        
        self.terrenos = [Terreno(l, i * 110, 10, oceano) for i, l in enumerate(info_terrenos)]
        
        self.pawn = Peao(oceano)
        
class Terreno:
    def __init__(self, local, posx, posy, cena):
        self.local = Elemento(local, x=posx, y=posy, w=100, h=100, cena=oceano)
        
class Peao:
    def __init__(self, cena):
        self.pawn = Elemento(PAWN, x=10, y=10, w=100, h=100, cena=oceano, vai=self.move)
        
    def move(self, ev=None):
        self.pawn.x = 120
        
        
IlhaProibida()