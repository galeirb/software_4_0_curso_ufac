from datetime import date
from datetime import datetime


class CreditCard:
    def __init__(self, cardholder_name, number, expiration_month, 
                 expiration_year, security_code):
        self.cardholder_name = cardholder_name
        self.number = number
        self.expiration_month = expiration_month
        self.expiration_year = expiration_year
        self.security_code = security_code
        self.cardholder_name_max_size = 150
        self.number_size = 16
        self.expiration_month_size = 2
        self.expiration_year_size = 4
        self.security_code_size = 3
        self.company_an_number = ['4']
        self.company_two_number = ['51', '52', '53', '54', '55']

    def validar_credit_card(self):
        a = self.validar_cardholder_name()
        b = self.validar_number()
        c = self.validar_expiration()
        d = self.validar_security_code()
        e = self.validar_company()
        if ((a and b and c and d and e) == True):
            print('Informações inseridas corretamente!')  

    def validar_cardholder_name(self):
        #print('Processo de validar o nome!')
        if len(self.cardholder_name) <= self.cardholder_name_max_size:
            return True
        else:
            print('Nome do titular do cartão possui mais de ' + 
                  str(self.cardholder_name_max_size) + ' caracteres!')
            return False

    def validar_number(self):
        #print('Processo de validar o número!')
        if len(self.number) == self.number_size:
            return True
        else:
            print('O número do cartão não possui ' + 
                  str(self.number_size) + ' caracteres!')
            return False

    def validar_month(self):
        if len(self.expiration_month) == self.expiration_month_size:
            if int(self.expiration_month) in range(1, 13, 1):
                return True
            else:
                print ('Mês de expiração incorreto!')
                return False
        else:
            print('O mês não possui ' + 
                  str(self.expiration_month_size) + ' caracteres!')
            return False

    def validar_year(self):
        if len(self.expiration_year) == self.expiration_year_size:
            #print('processo de validação do ano realizado!')
            return True
        else:
            print('O ano não possui ' + 
                  str(self.expiration_year_size) + ' caracteres!')
            return False

    def validar_expiration(self):
        if (self.validar_year() == True) and (self.validar_month() == True):
            data_today = date.today()
            data_today = datetime.strptime(str(data_today.month) + '/' 
                                           + str(data_today.year), 
                                           '%m/%Y')
            data_expiration = datetime.strptime(str(self.expiration_month)+ '/'
                                                + str(self.expiration_year), 
                                                '%m/%Y')
            if data_expiration >= data_today:
                return True
            else:
                print('Cartão vencido!')
                return False
        else:
            return False      

    def validar_security_code(self):
        #print('Processo de validar o código de seguraça!')
        if len(self.security_code) == self.security_code_size:
            return True
        else:
            print('O código de segurança não possui ' + 
                  str(self.security_code_size) + ' caracteres!')
            return False

    def validar_company(self):
        len_number_company_an_number = len(str(self.company_an_number[0]))
        len_number_company_two_number = len(str(self.company_two_number[0]))
        if (self.number[:len_number_company_an_number] in 
            self.company_an_number):
            return True
        elif (self.number[:len_number_company_two_number] in 
              self.company_two_number):
            return True
        else:
            print('Bandeira do cartão não aceita!')
            return False