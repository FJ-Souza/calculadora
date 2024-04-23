from calculadora import Calculadora
import unittest
import math

class TesteCalculadora(unittest.TestCase):
    def setUp(self) -> None:
        self.calc = Calculadora()

    def teste_str(self):
        self.assertTrue(self.calc.error_str("a", "b")) #Erro
        with self.assertRaises(TypeError):
            self.calc.error_str(1,'a')

    
    def teste_soma(self):
        self.assertEqual(self.calc.somar(-1,-1), -2)
        self.assertEqual(self.calc.somar(300,400), 700)
        self.assertNotEqual(self.calc.somar(30,20), 70)
        with self.assertRaises(TypeError):
            self.calc.somar(1,'a')

    def teste_subtracao(self):
        self.assertEqual(self.calc.subtrair(3,3), 0)
        self.assertEqual(self.calc.subtrair(500,300), 200)
        with self.assertRaises(TypeError):
            self.calc.subtrair(1,'a')


    def teste_divisao(self):
        self.assertEqual(self.calc.dividir(4,2), 2)
        self.assertNotEqual(self.calc.dividir(500,300), 0)
        with self.assertRaises(TypeError):
            self.calc.dividir(1,'a')


    def teste_multiplicacao(self):
        self.assertEqual(self.calc.multiplicar(4,2), 8)
        self.assertNotEqual(self.calc.multiplicar(28,300), 4)
        with self.assertRaises(TypeError):
            self.calc.multiplicar(1,'a')


    def teste_ponteciacao(self):
        self.assertEqual(self.calc.potencializar(2,2), 4)
        self.assertNotEqual(self.calc.potencializar(3,5), 4)
        with self.assertRaises(TypeError):
            self.calc.potencializar(1,'a')


    def teste_raiz_quadrada(self):
        self.assertEqual(self.calc.raiz_quadrada(25), 5)
        self.assertEqual(self.calc.raiz_quadrada(0), 0)
        with self.assertRaises(ValueError):
            self.calc.raiz_quadrada(-1)
            self.calc.raiz_quadrada(1,'a')

    def teste_log_natural(self):
        self.assertEqual(self.calc.logaritmo_natural(10), 2.302585092994046)
        with self.assertRaises(ValueError):
            self.calc.logaritmo_natural(-1)
            self.calc.logaritmo_natural(1,'a')

    def teste_seno(self):
        self.assertEqual(self.calc.calcular_seno(45), 0.7071067811865476)
        self.assertEqual(self.calc.calcular_seno(math.pi/2), 0.027412133592044294)
        with self.assertRaises(TypeError):
            self.calc.calcular_seno(1,'a')

    def teste_cosseno(self):
        self.assertEqual(self.calc.calcular_cosseno(45), 0.7071067811865476)
        with self.assertRaises(TypeError):
            self.calc.calcular_cosseno(1,'a')


    def teste_tangente(self):
        self.assertEqual(self.calc.calcular_tangente(45), 0.9999999999999999)
        with self.assertRaises(ValueError):
            self.calc.calcular_tangente(90)
            self.calc.calcular_tangente(1,'a')

if __name__ == '__main__':
    unittest.main()