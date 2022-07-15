from datetime import datetime, date


class Person:
    def __init__(self, first_name, last_name, birth_date):
        self.data_format = '%d/%m/%Y'
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = datetime.strptime(birth_date, self.data_format)
        self.age = self.age_calculator()

    def birth_date_view(self):
        return self.birth_date.strftime(self.data_format)

    def age_calculator(self):
        today = date.today()
        return today.year - self.birth_date.year - ((today.month, today.day) <
                                                    (self.birth_date.month,
                                                     self.birth_date.day))


def read_and_storage_csv():
    # read data for csv file
    file = open('dados_candidatos.csv', 'rb')
    text_file = file.read().decode('utf-8')
    file.close()
    raw_data = text_file.splitlines()
    # insert data on processed_data
    for i in raw_data[1:]:
        data = i.split(',')
        first_name = data[10].split(' ')[0]
        last_name = data[10].split(' ')[-1]
        birth_data = data[8]

        person = Person(first_name, last_name, birth_data)
        processed_data.append(person)


def classify_persons_by_age():
    per_age = {
        '21-30': [],
        '31-40': [],
        '41-50': [],
        '51-60': [],
        '61-70': [],
        '71+': []
    }

    # classify persons by age
    for i in processed_data:
        if i.age in range(21, 31):
            per_age['21-30'].append(i)
        elif i.age in range(31, 41):
            per_age['31-40'].append(i)
        elif i.age in range(41, 51):
            per_age['41-50'].append(i)
        elif i.age in range(51, 61):
            per_age['51-60'].append(i)
        elif i.age in range(61, 71):
            per_age['61-70'].append(i)
        elif i.age >= 71:
            per_age['71+'].append(i)

    # print first 10 persons
    print_first = 10
    print('First ' + str(print_first) + ' rows')
    for i in processed_data[:print_first]:
        print('Birthdate: %s Age: %s - %s %s' % (i.birth_date_view(), i.age,
                                                 i.first_name, i.last_name))

    # print total per age
    print('Total per age')
    for i in per_age:
        print(i + ' ' + str(len(per_age[i])))


if __name__ == '__main__':
    processed_data = []
    read_and_storage_csv()
    classify_persons_by_age()

