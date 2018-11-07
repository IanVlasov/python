# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class SchoolDB:
    def __init__(self):
        self._students = []
        self._teachers = []

    @property
    def students(self):
        return self._students

    @property
    def teachers(self):
        return self._teachers

    def add_person(self, person):
            if person.type_ == 'Student':
                self.students.append(person)
            else:
                for class_room in person.classes:
                    list_of_subjects = self.get_all_teachers_in_class(class_room).keys()
                    if person.subject in list_of_subjects:
                        raise ValueError
                    else:
                        self.teachers.append(person)
                        break

    # Проверяем только лист с учениками, так как, если в классе нет учеников, значит, класса тоже нет
    def get_all_classes(self):
        classes = {student.class_ for student in self.students}
        return classes

    def get_all_studs_in_class(self, class_):
        studs = [
            get_fio(student.full_name)
            for student in self.students
            if student.class_ == class_
        ]
        return studs

    def get_all_teachers_in_class(self, class_):
        teachers_in_class = {
            teacher.subject: get_fio(teacher.full_name)
            for teacher in self.teachers
            if class_ in teacher.classes
        }
        return teachers_in_class

    # В этой функции и функции поиска родителей предусмотрена возможность поиска как непосредственно
    # По экземпляру класса так и по части имени, либо имени в формате Фамилия И.О.
    def get_all_teachers_of_student(self, student):
        try:
            teachers_of_student = {
                teacher.subject: get_fio(teacher.full_name)
                for teacher in self.teachers
                if student.class_ in teacher.classes
            }
        except AttributeError:
            student = self.find_student(student)
            teachers_of_student = {
                teacher.subject: get_fio(teacher.full_name)
                for teacher in self.teachers
                if student.class_ in teacher.classes
            }
        return teachers_of_student

    def get_mother_and_father(self, student_to_find):
        try:
            father = get_fio(student_to_find.father)
            mother = get_fio(student_to_find.mother)
        except AttributeError:
            student = self.find_student(student_to_find)
            father = get_fio(student.father) if student else 'Unknown'
            mother = get_fio(student.mother) if student else 'Unknown'
        return father, mother

    def find_student(self, student):
        for person in self.students:
            if student in person.full_name or student == get_fio(person.full_name):
                return person
        print('Такого студента нет в списке')


class Student:
    def __init__(self, school, full_name, class_, father=None, mother=None):
        try:
            self._type_ = 'Student'
            self.full_name = str(full_name)
            self._class_ = convert_class(class_)
            self.father = str(father) if father is not None else None
            self.mother = str(mother) if mother is not None else None
            school.add_person(self)
        except AttributeError:
            print("Не существует базы данных указанной школы\n"
                  "Пожалуйста, сначала создайте базу")

    @property
    def type_(self):
        return self._type_

    @property
    def class_(self):
        return "{} {}".format(self._class_['class_num'],
                              self._class_['class_char'])


class Teacher:
    def __init__(self, school, full_name, subject, classes):
        try:
            self._type_ = 'Teacher'
            self.full_name = str(full_name)
            self.subject = str(subject)
            self.classes = classes.split(', ')
            school.add_person(self)
        except AttributeError:
            print("Не существует базы данных указанной школы\n"
                  "Пожалуйста, сначала создайте базу")

        except ValueError:
            print(
                "Извините, {}\n"
                "Преподаватель предмета {} уже есть в одном из классов,\n"
                "который вы собираетесь вести".format(self.full_name, self.subject)
            )

    @property
    def type_(self):
        return self._type_


def get_fio(full_name):
    splitted_full_name = full_name.split(' ')
    fio = '{} {}.{}.'.format(splitted_full_name[0],
                             splitted_full_name[1][0],
                             splitted_full_name[2][0])
    return fio


def convert_class(class_room):
    class_room = {'class_num': int(class_room.split()[0]),
                  'class_char': class_room.split()[1]}
    return class_room


if __name__ == "__main__":
    school1 = SchoolDB()

    stud1 = Student(school1, 'Власов Ян Эдуардович', '10 Б', "Власов Эдуард Юрьевич", "Власова Роза Рафаильевна")
    stud2 = Student(school1, "Кузьмин Никита Сергеевич", "10 Б")
    stud3 = Student(school1, "Системник Валентин Графенович", "11 А")

    teacher1 = Teacher(school1, "Фалафель Константин Занудович", "Математика", "10 Б, 11 А")
    teacher2 = Teacher(school1, "Властелин Виктор Цезаревич", "История", "8 А, 11 Б")
    teacher3 = Teacher(school1, "Вездеход Федук Васильевич", "Труд", "10 Б")
    teacher_fake = Teacher(school1, "Вольный Жулик Олегович", "Математика", "10 Б")

    print(school1.get_all_classes())
    print(school1.get_all_studs_in_class("10 Б"))
    print(school1.get_all_teachers_in_class("10 Б"))
    print(school1.get_mother_and_father('Власов'))
    print(school1.get_all_teachers_of_student(stud3))
