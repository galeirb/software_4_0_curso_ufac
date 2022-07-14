from credit_card import CreditCard
import unittest


class TestCreditCard(unittest.TestCase):

    def test_validate_number(self):

        number = '5255901222280001'
        card = CreditCard('', number, '', '', '')
        self.assertTrue(card.validate_number())

        number = '52559012222800011'
        card = CreditCard('', number, '', '', '')
        self.assertFalse(card.validate_number(),
                         'larger number of characters')

        number = '525590122228000'
        card = CreditCard('', number, '', '', '')
        self.assertFalse(card.validate_number(),
                         'smaller number of characters')

    def test_validate_cardholder_name(self):

        cardholder_name = 'JOAO DA SILVA'
        card = CreditCard(cardholder_name, '', '', '', '')
        self.assertTrue(card.validate_cardholder_name())

        cardholder_name = 'JOAO DA SILVA JOAO DA SILVA JOAO DA SILVA ' \
                          'JOAO DA SILVA JOAO DA SILVA JOAO DA SILVA ' \
                          'JOAO DA SILVA JOAO DA SILVA JOAO DA SILVA ' \
                          'JOAO DA SILVA JOAO DA SI'
        card = CreditCard(cardholder_name, '', '', '', '')
        self.assertTrue(card.validate_cardholder_name(),
                        'not allowed 150 characters')

        cardholder_name = 'JOAO DA SILVA JOAO DA SILVA JOAO DA SILVA ' \
                          'JOAO DA SILVA JOAO DA SILVA JOAO DA SILVA ' \
                          'JOAO DA SILVA JOAO DA SILVA JOAO DA SILVA ' \
                          'JOAO DA SILVA JOAO DA SIL'
        card = CreditCard(cardholder_name, '', '', '', '')
        self.assertFalse(card.validate_cardholder_name(),
                         'allowed 150 characters')

    def test_month(self):

        month = '06'
        card = CreditCard('', '', month, '', '')
        self.assertTrue(card.validate_month())

        month = '13'
        card = CreditCard('', '', month, '', '')
        self.assertFalse(card.validate_month(), 'invalid month allowed')

        month = '123'
        card = CreditCard('', '', month, '', '')
        self.assertFalse(card.validate_month(), 'larger number of characters')

    def test_year(self):

        year = '2020'
        card = CreditCard('', '', '', year, '')
        self.assertTrue(card.validate_year())

        year = '22'
        card = CreditCard('', '', '', year, '')
        self.assertFalse(card.validate_year(), 'smaller number of characters')

        year = '20225'
        card = CreditCard('', '', '', year, '')
        self.assertFalse(card.validate_year(), 'larger number of characters')

    def test_security_code(self):

        security_code = '123'
        card = CreditCard('', '', '', '', security_code)
        self.assertTrue(card.validate_security_code())

        security_code = '12'
        card = CreditCard('', '', '', '', security_code)
        self.assertFalse(card.validate_security_code(),
                         'smaller number of characters')

        security_code = '1234'
        card = CreditCard('', '', '', '', security_code)
        self.assertFalse(card.validate_security_code(),
                         'larger number of characters')

    def test_company(self):

        number = '5255901222280001'
        card = CreditCard('', number, '', '', '')
        self.assertTrue(card.validate_company())

        number = '0055901222280001'
        card = CreditCard('', number, '', '', '')
        self.assertFalse(card.validate_company(), 'company does not accept')

        number = 'xx55901222280001'
        card = CreditCard('', number, '', '', '')
        self.assertFalse(card.validate_company(), 'string to number')


if __name__ == '__main__':
    unittest.main()
