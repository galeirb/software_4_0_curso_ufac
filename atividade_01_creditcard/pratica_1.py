# -*- coding: utf-8 -*-
"""pratica_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hhdVy2bJH9ZML9YUQJLKevUWHtrEilSI
"""

# Utilizado para importar a classe CreditCard no Google Colab
from google.colab import drive
import sys
drive.mount('/content/gdrive')
sys.path.insert(0, '/content/gdrive/MyDrive/ColabNotebooks')
from creditcard import CreditCard

# Utilizado para importar os dados do cartão
import pandas as pd
cards=pd.read_json('/content/gdrive/MyDrive/ColabNotebooks/cards.json')

#Código utilizado para validar todos os dados
cards_qtd=len(cards)

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