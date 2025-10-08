import unittest
import numeroromano as nr




class numeroRomanoTest(unittest.TestCase):
    def tearDown(self):
        print('Teste', self._testMethodName, 'finalizado.')

    def testUm(self):
        self.assertEqual(nr.converte('I'), 1)

    def testDois(self):
        self.assertEqual(nr.converte('II'), 2)

    def testCinco(self):
        self.assertEqual(nr.converte('V'), 5)

    def testNove(self):
        self.assertEqual(nr.converte('IX'), 9)

    def testVinteDois(self):
        self.assertEqual(nr.converte('XXII'), 22)

    def testVinteQuatro(self):
        self.assertEqual(nr.converte('XXIV'), 24)


if __name__ == "__main__":
  unittest.main()