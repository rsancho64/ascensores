#! /usr/bin/python3

class display:

    where = None
    whereTo = "-" # ["-","↑","↓"]
    
    def __str__(self) -> str:
        return f"<{str(self.where) + self.whereTo}>"

    def setWhere(self, planta = 0):
        self.where = planta

    def setWhereTo(self, to = "-"):
        self.whereTo = to

if __name__ == "__main__":

    d = display()
    print(d)
    
    d.setWhere(0)
    print(d)

    d.setWhereTo("↑")
    print(d)

