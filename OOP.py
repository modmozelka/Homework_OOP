class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_le(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def calc_average(self):
        average = round(sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), [])), 2)
        return average

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.calc_average()}\nКурсы в процессе обучения: {", ".join(self.courses_in_progress)}\nЗавершённые курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.calc_average() < other.calc_average()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def calc_average(self):
        average = round(sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), [])), 2)
        return average

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.calc_average()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.calc_average() < other.calc_average()


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

    # Создание экземпляров студентов


student_1 = Student('Ruoy', 'Eman', 'male')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']
student_1.finished_courses += ['Введение в программирование']
student_2 = Student('Mila', 'Kunis', 'female')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Git']
student_2.finished_courses += ['Введение в программирование']
student_2.finished_courses += ['Английский для программиста']

# Создание экземпляров лекторов
lecturer_1 = Lecturer('Forest', 'Gump')
lecturer_1.courses_attached += ['Python']
lecturer_2 = Lecturer('Mel', 'Gibson')
lecturer_2.courses_attached += ['Git']

# Создание экземпляров проверяющих
reviewer_1 = Reviewer('Ben', 'Goon')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Git']
reviewer_2 = Reviewer('Tom', 'Cat')
reviewer_2.courses_attached += ['Python']
reviewer_2.courses_attached += ['Git']

# Проверка ДЗ проверяющими
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_2, 'Python', 10)
reviewer_2.rate_hw(student_1, 'Python', 8)
reviewer_2.rate_hw(student_2, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_2, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Git', 7)
reviewer_1.rate_hw(student_2, 'Git', 9)
reviewer_2.rate_hw(student_1, 'Git', 8)
reviewer_2.rate_hw(student_2, 'Git', 10)
reviewer_1.rate_hw(student_1, 'Git', 8)
reviewer_1.rate_hw(student_2, 'Git', 10)

# Оцека лекторов студентами
student_1.rate_le(lecturer_1, 'Python', 9)
student_1.rate_le(lecturer_2, 'Git', 9)
student_1.rate_le(lecturer_1, 'Python', 8)
student_1.rate_le(lecturer_2, 'Git', 9)
student_2.rate_le(lecturer_1, 'Python', 9)
student_2.rate_le(lecturer_2, 'Git', 10)

list_1 = [student_1, student_2]
list_2 = [lecturer_1, lecturer_2]


def av_grade_st(course, list=list_1):
    su = 0
    length = 0
    for st in list:
        if course in st.grades:
            su += sum(st.grades[course])
            length += len(st.grades[course])
        else:
            return 'По этому курсу оценок нет'
    return f'Средний балл студентов за курс {course}: {round(su / length, 2)}'


def av_grade_lec(course, list=list_2):
    su = 0
    length = 0
    for lec in list:
        if course in lec.grades:
            su += sum(lec.grades[course])
            length += len(lec.grades[course])
        else:
            return 'По этому курсу оценок нет'
    return f'Средний балл лекторов за курс {course}: {round(su / length, 2)}'


print()
print(reviewer_1)
print(reviewer_2)
print()
print(lecturer_1)
print(lecturer_2)
print()
print(student_1)
print(student_2)
print()
print(student_1 < student_2)
print(lecturer_2 < lecturer_1)
print()
print(av_grade_st('Python'))
print()
print(av_grade_lec('Python'))
print()
print(lecturer_1.grades)