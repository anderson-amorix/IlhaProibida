# radia.grace.main.py
# __author__ Finn
from _spy.vitollino.main import Cena, Elemento, STYLE

STYLE["width"] = 800

IMAGEM = "https://i.imgur.com/my9MiVU.jpeg"
PORTAO_BRONZE = "https://i.imgur.com/103Lydz.png"

class IlhaProibida:
    def __init__(self):
        oceano = Cena(IMAGEM).vai()
        portao = Elemento(PORTAO_BRONZE, x=10, y=10, w=100, h=100, cena=oceano)
        
IlhaProibida()