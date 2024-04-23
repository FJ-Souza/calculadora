import math

class Calculadora():

    def __init__(self)->None:
        self.ultimo_resultado = 0 

    def error_str(self, x, y = 0):
        if type(x) == str or type(y) == str:
            raise TypeError("Caracter inválido.")
        return True
    
    
    def somar(self, x , y):
        self.error_str(x,y)
        self.ultimo_resultado = x + y
        return self.ultimo_resultado

    def subtrair(self, x, y):
        self.error_str(x,y)
        self.ultimo_resultado = x - y
        return self.ultimo_resultado

    def dividir(self, x, y):
        self.error_str(x,y)
        if y == 0:
            raise ValueError("Divisão por zero não é permitida.")
        self.ultimo_resultado = x / y
        return self.ultimo_resultado

    def multiplicar(self, x, y):
        self.error_str(x,y)
        self.ultimo_resultado = x * y
        return self.ultimo_resultado
    
    def potencializar(self, x, y):
        self.error_str(x,y)
        self.ultimo_resultado = x ** y
        return self.ultimo_resultado
    
    def raiz_quadrada(self, x):
        self.error_str(x,0)
        if x < 0:
            raise ValueError("numeros negativos não são permitdos.")
        self.ultimo_resultado = math.sqrt(x)
        return self.ultimo_resultado
    
    def logaritmo_natural(self, x):
        self.error_str(x,0)
        if x <= 0:
            raise ValueError("Numero 0 e numeros negativos não são permitdos.")
        self.ultimo_resultado = math.log(x)
        return self.ultimo_resultado
    
    def calcular_seno(self, x)->float:
        self.error_str(x,0)
        self.ultimo_resultado = math.radians(x)
        return math.sin(self.ultimo_resultado)
    
    def calcular_cosseno(self, x)->float:
        self.error_str(x,0)
        self.ultimo_resultado = math.radians(x)
        return math.cos(self.ultimo_resultado)
    
    def calcular_tangente(self, x)->float:
        self.error_str(x,0)
        self.ultimo_resultado = math.radians(x)
        if x % 180 == 90:
            raise ValueError("Tangente indefinida")
        return math.tan(self.ultimo_resultado)
    
i = Calculadora()
print(i.somar(0.5,0.5))