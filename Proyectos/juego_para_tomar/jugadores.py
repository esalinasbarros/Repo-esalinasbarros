class Jugador:
    def __init__(self, nombre):
        super.__init__()
        self.nombre = nombre
        self._tragos = 0
        self.piscolas = 0
    def tragos(self, num):
        if (self._tragos + num) > 15:
            self._tragos = (self._tragos + num) - 15
            self.piscolas += 1
        else:
            self._tragos += num
