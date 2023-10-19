def tpl_sort(tpl):
    if all(isinstance(x, int) for x in tpl):
        return tuple(sorted(tpl))
    else:
        return tpl
def slicer(tpl, element):
    if element in tpl:
        start_index = tpl.index(element)
        end_index = tpl.index(element, start_index + 1)
        return tpl[start_index:end_index+1]
    else:
        return ()
def sieve(lst):
    unique_elements = list(set(lst))
    unique_elements.reverse()
    return tuple(unique_elements)
def del_from_tuple(tpl, element):
    if element in tpl:
        return tuple(filter(lambda x: x != element, tpl))
    else:
        return tpl
from collections import namedtuple

Student = namedtuple('Student', ['name', 'age', 'city'])

def good_students(students):
    avg_grade = sum(student.grade for student in students) / len(students)
    good_students = [student.name for student in students if student.grade >= avg_grade]
    print("Ученики", ", ".join(good_students), "в этом семестре хорошо учатся!")

students
    Student('Рамиль'17,81,Баку),
    Student('Кирилл'17,76,Новосибирск ),
    Student('Рудольф'17,75,Гамбург ),
    Student('Владимир'17,79,Санкт-Петербург ),
    Student('Дмитрий'17,90,Чик ),
    Student('Марк'18,77, )Новосибирск,
    Student('Александр'17,75,НЬЮ-ЙОРК)
]

