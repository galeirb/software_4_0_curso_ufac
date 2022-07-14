import unittest

from my_sum import Card

class TestCard(unittest.TestCase):

    def test_card_number(self):
        card = Card("5155901222280001")
        self.assertTrue(card.validate_number())

        card = Card("51559012222800012")
        self.assertFalse(card.validate_number(), 'larger number of characters')

        card = Card("5155901222280001")
        self.assertFalse(card.validate_number(), 'smaller amount of characters')



if __name__ == '__main__':
    unittest.main()