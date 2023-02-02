class Person:

    def __init__(self, first_name, second_name, last_name, dict):
        self.first_name = first_name
        self.second_name = second_name
        self.last_name = last_name
        self.dict = dict

    def get_phone(self):
        for i in self.dict:
            if i == "private":
                return self.dict[i]
        return None

    def get_name(self):
        return f'{self.last_name} {self.first_name} {self.second_name}'
    
    def get_work_phone(self):
        for i in self.dict:
            if i == "work":
                return self.dict[i]
        return None

    def get_sms_text(self):
        return f'Уважаемый {self.first_name} {self.second_name}! Примите участие в нашем беспроигрышном конкурсе для физических лиц'

class Company(Person):

    def __init__(self, first_name, second_name, dict, *args):
        self.first_name = first_name
        self.second_name = second_name
        self.dict = dict
        self.args = args

    def get_phone(self):
        for i in self.dict:
            if i == "contact":
                return self.dict[i]
            elif i == "non_contact":
                for i in self.args:
                    return i.get_work_phone()
        return None

    def get_name(self):
        return self.first_name

    def get_sms_text(self):
        return f'Для компании {self.first_name} есть супер предложение! Примите участие в нашем беспроигрышном конкурсе для {self.second_name}'

def send_sms(*args):
    for i in args:
        if i.get_phone() is not None:
            print(f"Отправленно СМС на номер {i.get_phone()} с тестом: {i.get_sms_text()}")
        else:
            print(f"Не удалось отправить сообщение абоненту: {i.get_name()}")

person1 = Person("Степан", "Петрович", "Джобсов", {"private":555})
person2 = Person("Боря", "Иванович", "Гейтсов", {"private":777, "work":888})
person3 = Person("Семен", "Робертович", "Возняцкий", {"work":789})
person4 = Person("Леонид", "Арсенович", "Торвальдсон", {})
company1 = Company("Яблочный комбинат","OOO",{"contact":111},person1, person3)
company2 = Company("ПластОкно","AО",{"non_contact":222},person2)
company3 = Company("Пингвинья ферма","Ltd",{"non_contact":333},person4)
send_sms(person1, person2, person3, person4, company1, company2, company3)