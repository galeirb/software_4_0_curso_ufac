from creditcard import CreditCard
import pandas as pd

cards = pd.read_json('cards.json')
cards_qtd = len(cards)

for i in range(cards_qtd):
    number = str(cards.number[i])
    cardholder_name = cards.cardholder_name[i]
    security_code = str(cards.security_code[i])
    expiration_month = str(cards.expiration_month[i])
    expiration_year = str(cards.expiration_year[i])
    print('------------------')
    print('Cartão número ' + str(i) + ':')
    credit_card_1 = CreditCard(cardholder_name, number, expiration_month, 
                               expiration_year, security_code)
    credit_card_1.validar_credit_card()
    print('------------------')