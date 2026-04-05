from lesson import Lesson
from pupils import Pupils
from pupil import  Pupil
pupils = Pupils().pupils
import json

class Lessons:
    def __init__(self):
        try:
            with open("for_lessons.json", "r") as file:
                rec = json.load(file)
            self.lessons = []
            for i in rec:
                c = Lesson()
                c.change_from_ldict_to_object(i)
                self.lessons.append(c)


        except Exception as e:
            print(e)
            self.lessons = []

    def __str__(self):
        st = ""
        for i in self.lessons:
            st += str(i)
            st += "\n"

        return st



    def create_lesson(self,lesson_name):
        self.lessons.append(Lesson(lesson_name))
        print(f"the lesson's  name is {lesson_name}")


    def update_lesson(self,pupil_id=None,lesson_name=None):
        for i in self.lessons:
            if lesson_name == i.name :
                for j in range(len(i.pupils_ids)-1,-1,-1):
                    if pupil_id == i.pupils_ids[j]:
                        i.pupils_ids.pop(j)
                        return True

    def delete_lesson(self,lesson_name):
        for i in range(len(self.lessons)-1,-1,-1):
            if lesson_name == self.lessons[i].name:
                self.lessons.pop(i)


    def subscribe_to_lesson(self, given_id,lesson_name):
        for i in pupils:
            if i.pupil_id == given_id:
                for j in self.lessons:
                    if j.name == lesson_name:
                        j.pupils_ids.append(given_id)



    def save_lessons(self):
        lessons = []
        for i in self.lessons:
            lessons.append(i.lto_dict())
        with open("for_lessons.json", "w") as file:
            json.dump(lessons, file)

