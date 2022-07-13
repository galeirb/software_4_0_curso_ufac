from datetime import datetime, date


class Person:
    def __init__(self, first_name, last_name, birth_date, age=None):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.age = age

def readcsv():
    # read data for csv file
    file = open('dados_candidatos.csv', 'rb')
    text_file = file.read().decode('utf-8')
    file.close()
    list = text_file.splitlines()
    list2 = []
    # insert data on list2
    for i in list[1:]:
        data = i.split(',')
        person = Person(data[10].split(' ')[0], data[10].split(' ')[len(data[10].split(' '))-1], datetime.strptime(data[8], '%d/%m/%Y').date())
        list2.append(person)

    per_age = {
        '21-30': [], '31-40': [], '41-50': [], '51-60': [], '61-70': [], '71+': []
    }

    # age calculator
    for i in list2:
        today = date.today()
        age = today.year - i.birth_date.year - ((today.month, today.day) < (i.birth_date.month, i.birth_date.day))
        i.age = age
    # classify persons by age
    for i in list2:
        if i.age >= 20 and i.age <= 30:
            per_age['21-30'].append(i)
        if i.age >= 31 and i.age <= 40:
            per_age['31-40'].append(i)
        if i.age >= 41 and i.age <= 50:
            per_age['41-50'].append(i)
        if i.age >= 51 and i.age <= 60:
            per_age['51-60'].append(i)
        if i.age >= 61 and i.age <= 70:
            per_age['61-70'].append(i)
        if i.age >= 71:
            per_age['71+'].append(i)
    # print first 10 persons
    print('First 10 rows')
    for i in list2[:10]:
        print('Birthdate: %s Age: %s - %s %s' %(i.birth_date.strftime("%d/%m/%Y"), i.age, i.first_name, i.last_name))
    # print total per age
    print('Total per age')
    for i in per_age:
        print(i +' '+ str(len(per_age[i])))


if __name__ == '__main__':
    readcsv()