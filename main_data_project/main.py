from pupil import Pupil
from pupils import Pupils
from teachers import Teachers
from teacher import Teacher
from lessons import Lessons
from lesson import Lesson

pupils = Pupils()
pupil = Pupil()
teachers = Teachers()
teacher = Teacher()
lessons = Lessons()
lesson = Lesson()

# ---------------------------------

def choose():
    print("\n===============")
    print("     MENU ")
    print("1 - Create Pupil")
    print("2 - Print pupils")
    print("3 - Update Pupil")
    print("4 - Delete Pupil")
    print("5 - Create teacher")
    print("6 - Print teacher")
    print("7 - Update teacher")
    print("8 - Delete teacher")
    print("9 - Create lesson")
    print("10 -Subscribe to lesson")
    print("11 -Print Lessons")
    print("12 -Update Lesson")
    print("13 -Delete lesson")
    print("14 -Exit")
    choice = input("Pick one: ")
    choice.isdigit()
    if choice.isdigit():
        choice = int(choice)
        return choice
    else:
        print("enter valid input (number) "
              "")
    return None


def main():
    # sthn main tha vazw pou tha etrexe olo to programma xwris synarthshseis
    while True:
        x = choose()

        if x == 1:
            pupils.create_pupil()

        elif x == 2:
            pupils.print_pupil()


        elif x == 3:
            id_or_surname = input("if you want to search by surname press 0 "
                                  "if you want to search by id press 1 "
                                  "if you want update type 2 ")
            if id_or_surname == "0":
                print(pupils.search_pupil_by_surname(input("search pupil by surname! type surname: ")))

            elif id_or_surname == "1":
                pupils.search_pupil_by_id(input("search pupil by id! type id: "))

            elif id_or_surname == "2":
                for pupil in pupils:
                    print(pupil)
                    print("-" * 30)
                print()
                print("(KEY) type surname or father's_name or age or class and ENTER !")
                pupils.update(input("enter the name of the player who want to change:  "),
                       input("enter what you want to change "),
                       input("type the new value :"))

                for pupil in pupils:
                    print(pupil)
                    print("-" * 30)

        elif x == 4:
            search_method = input("enter the method you want to search by surname or id: ")

            if search_method == "surname":
                pupils.delete_pupil(input("enter the surname of the pupil to delete: "))


            elif search_method == "id":
                pupils.delete_pupil(int(input("enter the id of the pupil to delete: ")))

        elif x == 5:
            teachers.create_teacher(input("Name : "), input("Surname : "))
            print("-" * 60)


        elif x == 6:
            teacher_id = int(input("enter the id of the teacher to print  : "))
            t = teachers.read_teacher(teacher_id)
            if t is None:
                print("not exist")
            else :
                print(t)
            print("-" * 60)


        elif x == 7:
            teacher_id = int(input("enter the id of the teacher to update: "))
            teachers.update_teacher(teacher_id)
            print("-" * 60)


        elif x == 8:
            teacher_id = int(input("enter the id of the teacher to delete  : "))
            teachers.delete_teacher(teacher_id)

        elif x == 9:
            lesson_name = input("enter the name of the lesson to create:")
            lessons.create_lesson(lesson_name)

        elif x == 10:

            given_id = int(input("enter the pupil's  id to subscribe: "))
            give_lesson_name = input("enter the name of the lesson to subscribe: ")
            print(lessons)
            print("--"*10)
            lessons.subscribe_to_lesson(given_id = given_id,lesson_name=give_lesson_name)
            print(lessons)


        elif x == 11:
            print(lessons)


        elif x == 12:
            name_lesson = input("enter the name of the lesson to update : ")
            pupil_id = int(input("enter the id of the pupil to delete : "))
            x=lessons.update_lesson(lesson_name=name_lesson,pupil_id= pupil_id)
            if not x:
                print("not exist")
            else:
                print("the pupil's id is deleted",x)

        elif x == 13:
            lesson_name = input("enter the name of the lesson to delete: ")
            lessons.delete_lesson(lesson_name)
            print(lessons)


        elif x == 14:
            print("exit , bye bye ")
            return

        pupils.save_pupils_data() # grafoume
        teachers.save_teachers_data()
        lessons.save_lessons()

main()