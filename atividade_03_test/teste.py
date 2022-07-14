import unittest

from credit_card import CreditCard

class TestCreditCard(unittest.TestCase):

    def test_validar_number(self):
        
        number = '5255901222280001'
        card = CreditCard('', number, '', '', '')
        self.assertTrue(card.validar_number())

        number = '52559012222800011'
        card = CreditCard('', number, '', '', '')
        self.assertFalse(card.validar_number(), 'larger number of characters')

        number = '525590122228000'
        card = CreditCard('', number, '', '', '')
        self.assertFalse(card.validar_number(), 'smaller number of characters')

    def test_validar_cardholder_name(self):

        card = CreditCard('', number, '', '', '')
        self.assertTrue(card.validar_cardholder_name())








if __name__ == '__main__':
    unittest.main()
