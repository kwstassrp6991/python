import json
from pupil import Pupil

class Pupils:
    def __init__(self):
        self.pupils = []
        with open('for_pupils.json') as f:
            json_dict = json.load(f)
            for diction in json_dict:
                pupil = Pupil()
                pupil.pfrom_dict(diction)
                self.pupils.append(pupil)

    def __str__(self):
        st = ""
        for pupil in self.pupils:
            st += str(pupil)
            st += "\n"
        return st

    def __getitem__(self,key):
        return self.pupils[key]


    def next_id(self):
        ids = [999]
        for pupil in self.pupils:
            ids.append(pupil.pupil_id)

        return max(ids) + 1


    def create_pupil(self):
        print("NEW PUPIL")
        print("===========")
        name = input("Give name: ")
        surname = input("Give surname: ")
        fathers_name = input("Give father's name: ")

        stop = False
        for pupil in self.pupils:
            if name == pupil.first_name and surname == pupil.last_name and fathers_name == pupil.fathers_name:
                print("This pupil already exists.")
                ch = input("Do you want to continue? (y-yes, n-no): ")
                if ch == "n":
                    stop = True
                    break
        if stop:
            return

        id_number = 0
        age = int(input("Give age: "))
        pupil_class = int(input("Give class: "))
        id_card = input("Does he/she has an id card: (y-true, n-false): ")
        if id_card == "y":
            id_number = input("Give id card number: ")


        next_id = self.next_id()
        if not name.isdigit() and not surname.isdigit() and not fathers_name.isdigit():
            bot  = Pupil(first_name=name,last_name=surname,fathers_name=fathers_name,age=age,
              class_name=pupil_class,id_number=id_number,pupil_id=next_id)
            if id_number != 0:
                print(f"ID card number: {Pupil().id_number}")
            print("NEW PUPIL")
            print(bot)

            self.pupils.append(bot)
        else:
            print(f"invalid input set strings not digits ! 😡")


    def search_pupil_by_id(self,id_number):
        id_number.isdigit()
        id_number = int(id_number)
        z = []
        for pupil in self.pupils:
            if pupil.pupil_id == id_number:
                z.append(pupil)
                return z
        if id_number not in z:
            return "not valid id"
        return id_number


    def search_pupil_by_surname(self,surname=None):
        y = []
        for pupil in self.pupils:
            if pupil.last_name == surname:
                y.append(pupil)

        if len(y) == 1:
            return y

        elif len(y) > 0:
            print(y)
            print()
            x = input("enter the id of the pupil: ")
            x.isdigit()
            x = int(x)
            for i in y:
                for k, v in i.items():
                    if k == "pupil_id":
                        if v == x:
                            return i

        y.clear()
        return "not valid surname"


    def update(self,x,new_value,y):
        if not x.isalpha():
            return "invalid input"
        else:
            for pupil in self.pupils:
                if x == pupil.first_name:
                    if new_value == "first_name":
                        pupil.first_name = y
                    elif new_value == "last_name":
                        pupil.last_name = y
                    elif new_value == "fathers_name":
                        pupil.fathers_name = y
                    elif new_value =="age":
                        pupil.age = y
                    elif new_value == "class_name":
                        pupil.class_name = y
                    elif new_value == "id_number":
                        pupil.id_number = y


        return None


    def print_pupil(self):
        z = int(input("if you want to see one pupil, enter 1\n"
                  "if you want to see the  pupils(Analytical), enter 2\n"
                  "if you want to see only the names, enter 3\n "))
        if z == 1:
            x = input("Give the id of the pupil: ")
            x.isdigit()
            x = int(x)
            for pupil in self.pupils:
                if pupil.pupil_id == x:
                    print(pupil)
            return z

        elif z == 2:
            for i in self.pupils:
                self.prints(i)


            return z

        elif z == 3:
            for pupil in self.pupils:
                print(f"pupil_id: {pupil.pupil_id}")
                print(f"Name: {pupil.first_name}")
                print(f"Surname: {pupil.last_name}")
                print(f"Father's Name: {pupil.fathers_name}")
                print("-"*15)
            return z
        return None


    def prints(self,arg):
        print(f"Name: {arg.first_name}")
        print(f"Surname: {arg.last_name}")
        print(f"Father's Name: {arg.fathers_name}")
        print(f"Age: {arg.age}")
        print(f"Class: {arg.class_name}")
        print(f"Ids: {arg.pupil_id}")
        if arg.id_number and arg.id_number != 0:
            print(f"ID card number: {arg.id_number}")
        print("-" * 15)

    def test_print(self):
        for pupil in self.pupils:
            print(pupil.first_name)



    def delete_pupil(self,id_num):
        for pupil in self.pupils:
            if pupil.pupil_id == id_num:
                self.pupils.remove(pupil)
                return id_num

            if pupil.last_name == id_num:
                self.pupils.remove(pupil)
                return id_num
        return None


    def save_pupils_data(self):
        pupil_list = []
        for pupil in self.pupils:
            pupil_list.append(pupil.pto_dict())
        with open("for_pupils.json", "w") as file:
            json.dump(pupil_list,file)
