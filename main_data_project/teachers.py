import json
from teacher import Teacher

class Teachers:
    def __init__(self):

        try:
            with open('for_teachers.json',"r") as json_file:
                teachers_list = json.load(json_file)

            self.teachers = []
            for teacher_dict in teachers_list:
                t = Teacher()
                t.from_dict(teacher_dict)
                self.teachers.append(t)

        except FileNotFoundError:
            self.teachers = []


    def save_teachers_data(self):
        teachers_list = []
        for teacher in self.teachers:
            teachers_list.append(teacher.to_dict())

        with open("for_teachers.json", "w") as f:
            json.dump(teachers_list, f)


    def create_teacher(self,first_name,last_name):
        for teacher in self.teachers:
            if teacher.first_name ==  first_name and teacher.last_name == last_name:
                return None
        x = Teacher(first_name,last_name,self.next_id())
        self.teachers.append(x)
        return x


    def read_teacher(self,teacher_id):
        for teacher in self.teachers:
            if teacher_id == teacher.teacher_id:
                return teacher
        return None

    def next_id(self):
        if not self.teachers:
            return 1000
        else:
            ids = []
            for teacher in self.teachers:
                ids.append(teacher.teacher_id)
            return max(ids)+1

    def update_teacher(self,id_t):
        if  id_t != int(id_t):
            return "invalid input"
        else:
            for t in self.teachers:
                if id_t == t.teacher_id:
                    print(t)
                    choose = input("choose what you want to update:|first_name | last_name | :")
                    if choose == "first_name":
                        x = input("give the new first name:")
                        t.first_name = x
                    elif choose == "last_name":
                        y = input("give the new first name:")
                        t.last_name = y
                    return None

    def delete_teacher(self,id_t):
        id_t = int(id_t)
        for i in range(len(self.teachers)-1,-1,-1):
            if  self.teachers[i].teacher_id == id_t:
                self.teachers.pop(i)
                return
        else:
            print("invalid input")
