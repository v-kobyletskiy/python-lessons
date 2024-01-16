from datetime import datetime

class Student:
    def __init__(self, name: str, date_of_birt):
        self.name = name
        self.date_of_birt = date_of_birt

    @property
    def date_of_birt(self):
        return self.__date_of_birt

    @date_of_birt.setter
    def date_of_birt(self, value):
        birth_date = datetime.strptime(value, '%d-%m-%Y')
        now = datetime.now()
        age = now.year - birth_date.year - ((now.month, now.day) < (birth_date.month, birth_date.day))
        if not 18 <= age <= 100:
            raise ValueError('Invalid age')
        self.__date_of_birt = value

    @property
    def name(self):
        return f'{self.__first_name} {self.__last_name}'

    @name.setter
    def name(self, value):
        is_valid_name = all(map(lambda name: name.istitle(), value.split()))
        if not is_valid_name:
            raise ValueError("Invalid name")
        name = value.split()
        self.__first_name = name[0]
        self.__last_name = name[0]

    @name.deleter
    def name(self):
        pass

    def __eq__(self, other: str):
        return self.name == other

    # def __str__(self):
    #     return f"Product: {self.name}, Price: {self.price}"





if __name__ == '__main__':
   st_1 = Student('Ivan Ivanov', datetime(2000, 1, 1))
