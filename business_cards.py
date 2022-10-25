from faker import Faker
import sys

fake = Faker(["pl_PL"])

class BaseContact:
    """przedstawia podstawowe dane osoby"""
    def __init__(self, first_name, last_name, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = first_name + "_" + last_name + "@mail.com"


    def __str__(self):
        return f"{self.first_name} {self.last_name}"


    def contact():
        return f"Wybieram numer {self.phone_number} i dzwonie do {self.first_name} {self.last_name}"


    @property
    def label_lenght(self):
        """zwraca dlugosc imienia i nazwiska, wykorzystywany w dwoch klasach"""
        return len(self.first_name + " " + self.last_name)

    
class BusinessContact(BaseContact):
    """przedstawia informacje biznesowe danej osoby"""
    def __init__(self, job_position, company, business_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.job_position = job_position
        self.company = company
        self.business_phone = business_phone


    def contact(self):
        return f"Wybieram numer {self.business_phone} i dzwonie do {self.first_name} {self.last_name}"


def create_contacts(kind, quantity):
    """tworzy nowe wizytowki"""
    if kind == 'podstawowe':
        for i in range(quantity):
            i = BaseContact(first_name=fake.first_name(), last_name=fake.last_name(), phone_number = fake.phone_number())
            list_of_bc.append(i)
        for i in list_of_bc:
            print(i.first_name, i.last_name, i.phone_number)
    elif kind == 'biznesowe':
        for i in range(quantity):
            i = BusinessContact(first_name= fake.first_name(), last_name=fake.last_name(), phone_number = fake.phone_number(), company=fake.company(), job_position=fake.job(), business_phone= fake.phone_number())
            list_of_bc.append(i)
        for i in list_of_bc[2:]:
            print(i.first_name, i.last_name, i.company, i.job_position, i.business_phone)
    else:
        print("Podano zła wartość.")
        sys.exit(1)

#wizytowki podstawowe
w_1 = BaseContact(first_name= fake.first_name(), last_name=fake.last_name(), phone_number = fake.phone_number())
w_2 = BaseContact(first_name= fake.first_name(), last_name=fake.last_name(), phone_number = fake.phone_number())
w_3 = BusinessContact(first_name= fake.first_name(), last_name=fake.last_name(), phone_number = fake.phone_number(), company=fake.company(), job_position=fake.job(), business_phone= fake.phone_number())
w_4 = BusinessContact(first_name= fake.first_name(), last_name=fake.last_name(), phone_number = fake.phone_number(), company=fake.company(), job_position=fake.job(), business_phone= fake.phone_number())
w_5 = BusinessContact(first_name= fake.first_name(), last_name=fake.last_name(), phone_number = fake.phone_number(), company=fake.company(), job_position=fake.job(), business_phone= fake.phone_number())

#lista wizytowek
list_of_bc = [w_1, w_2, w_3, w_4, w_5]

new_bc = input("Chcesz stworzyć nowe wizytówki? [t/n]")
if new_bc == "t":
    kind = input("Jakie dane ma zawierać wizytowka? [podstawowe/biznesowe]")
    quantity = int(input("Ile wizytówek stworzyc? podaj liczbe."))
    create_contacts(kind, quantity)
elif new_bc == 'n':
    sys.exit(0)
else:
    print("Została podana zla wartosc!")


