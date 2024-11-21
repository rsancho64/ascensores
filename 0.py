#! /usr/bin/python3

from display import display
from Buttons import boton

class boton:
    pass

class botonera:
    pass

class botoneraExterior (botonera):
    pass

class botoneraInterior (botonera):
    pass

class elevator:
    pass

class bigCotrolElevators:
    pass

if __name__ == "__main__":

    d = display()
    print(d)
    
    d.setWhere(0)
    print(d)

    d.setWhereTo("↑")
    print(d)

