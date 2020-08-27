
"""
    @author = jjr4Programmer

    Resuelve sudokus nivel 1(fácil)

    Logica empleada:
        Se busca los posibles valores de cada casillero, en caso
        se tenga un sólo valor posible, se reemplaza el valor
        y se recalcula los posibles valores de cada casillero
        hasta encontrar la solución total.
        El programa está diseñado para intentar resolverlo en 1 intentos
        caso contrario, terminará indicando que no se logró resolver.

    Cabe recalcar que el programa funciona siempre y cuando encuentre casilleros
    con sólo un valor posible, si no encuentra casilleros con sólo un valor
    posible, el programa no podrá resolverlo.
    Se planea modificar para que pueda resolver en caso se tengan más de una
    posibilidad en cada casillero.
"""


class Casilla:

    def __init__(self, valor):
        self.val = valor
        self.posibles = []

    def getVal(self):
        return self.val

    def setVal(self, newVal):
        self.val = newVal

    def getPosibles(self):
        return self.posibles

    def setPosibles(self, posi):
        self.posibles = posi

    def __str__(self):
        return str(self.getVal())


class Sudoku:

    def __init__(self, sudo):
        self.sudo = Sudoku.armaCasilleros(sudo)

    # Método que intenta resolver el sudoku
    def resolver(self):
        intentos = 0
        while not self.resuelto() and intentos < 10:
            self.posiblesSudoku()
            intentos += 1

        if intentos == 10:
            print("No se logro resolver el sudoku.")
        else:
            print("El sudoku se resolvió en %i intentos." % (intentos))

    # Devuelve True cuando ya no existan '0's en el sudoku
    def resuelto(self):
        for fila in self.sudo:
            for casilla in fila:
                if casilla.getVal() == 0:
                    return False
        return True

    # Crea cada casilla del sudoku con su valor respectivo
    def armaCasilleros(sudoNum):
        sudoku = []
        for fila in sudoNum:
            fil = []
            for valor in fila:
                fil.append(Casilla(valor))
            sudoku.append(fil)
        return sudoku

    # Intenta resolver cada casillero del sudoku

    def posiblesSudoku(self):
        for i in range(9):
            for j in range(9):
                Sudoku.intentar(self.sudo, i, j)

    def intentar(sudo, i, j):
        posi = [n for n in range(1, 10)]
        val = sudo[i][j].getVal()
        if val == 0:
            # Revisa fila
            for casilla in sudo[i]:
                num = casilla.getVal()
                if num in posi:
                    posi.remove(num)

            # Revisa columna
            for fila in sudo:
                num = fila[j].getVal()
                if num in posi:
                    posi.remove(num)

            # Revisa cuadrillas
            # Primeras 3 filas
            if 0 <= i <= 2:
                # Primeras 3 columnas:
                if 0 <= j <= 2:
                    for filas in range(3):
                        for cols in range(3):
                            val = sudo[filas][cols].getVal()
                            if val in posi:
                                posi.remove(val)
                # Segundo grupo de 3 columnas
                elif 3 <= j <= 5:
                    for filas in range(3):
                        for cols in range(3, 6):
                            val = sudo[filas][cols].getVal()
                            if val in posi:
                                posi.remove(val)
                # Últimas 3 columnas
                else:
                    for filas in range(3):
                        for cols in range(6, 9):
                            val = sudo[filas][cols].getVal()
                            if val in posi:
                                posi.remove(val)
            # Segundo grupo de 3 filas
            elif 3 <= i <= 5:
                # Primeras 3 columnas:
                if 0 <= j <= 2:
                    for filas in range(3, 6):
                        for cols in range(3):
                            val = sudo[filas][cols].getVal()
                            if val in posi:
                                posi.remove(val)
                # Segundo grupo de 3 columnas
                elif 3 <= j <= 5:
                    for filas in range(3, 6):
                        for cols in range(3, 6):
                            val = sudo[filas][cols].getVal()
                            if val in posi:
                                posi.remove(val)
                # Últimas 3 columnas
                else:
                    for filas in range(3, 6):
                        for cols in range(6, 9):
                            val = sudo[filas][cols].getVal()
                            if val in posi:
                                posi.remove(val)
            # Últimas 3 filas
            else:
                # Primeras 3 columnas:
                if 0 <= j <= 2:
                    for filas in range(6, 9):
                        for cols in range(3):
                            val = sudo[filas][cols].getVal()
                            if val in posi:
                                posi.remove(val)
                # Segundo grupo de 3 columnas
                elif 3 <= j <= 5:
                    for filas in range(6, 9):
                        for cols in range(3, 6):
                            val = sudo[filas][cols].getVal()
                            if val in posi:
                                posi.remove(val)
                # Últimas 3 columnas
                else:
                    for filas in range(6, 9):
                        for cols in range(6, 9):
                            val = sudo[filas][cols].getVal()
                            if val in posi:
                                posi.remove(val)

            # Si sólo hay un valor posible
            if len(posi) == 1:
                sudo[i][j].setVal(posi[0])
            # En caso se tenga varios valores posibles
            else:
                sudo[i][j].setPosibles(posi)

    def __str__(self):
        st = ""
        for i in range(9):
            fila = self.sudo[i]
            for j in range(9):
                valor = fila[j].getVal()
                if valor == 0:
                    valor = ' '
                if j == 2 or j == 5:
                    st += str(valor) + ' | '
                else:
                    st += str(valor)+' '
            if i == 2 or i == 5:
                st += '\n---------------------\n'
            else:
                st += '\n'
        return st


"""
    Defino la matriz del sudoku, reemplazando por cero '0'
    los casilleros que son vacíos y deben rellenarse.
"""
sudo = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]

# Cargo el sudoku
sudoku = Sudoku(sudo)
# Imprimo el sudoku inicial
print(sudoku)
# Intento resolver el sudoku
sudoku.resolver()
# Imprimo el sudoku luego de intentar resolverlo
print(sudoku)
