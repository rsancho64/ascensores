#! /usr/bin/python3

class boton:

    number = None
    light = "off"

    def __init__(self, num) -> None:
        self.number = num

    def __str__(self) -> str:
        return f"({str(self.number) + self.light})"

class botonera:
    pass

class botoneraExterior (botonera):
    pass

class botoneraInterior (botonera):
    pass


if __name__ == "__main__":

    b = boton(4)
    print(b)
    
    # d.setWhere(0)
    # print(d)

    # d.setWhereTo("↑")
    # print(d)

