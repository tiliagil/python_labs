
class Student:
    def __init__(self, student_id, full_name, specialty):
        self.student_id = student_id
        self.full_name = full_name
        self.specialty = specialty
        self.disciplines = {}
        self.semester = 1

    def add_discipline(self, discipline):
        if discipline in self.disciplines:
            raise ValueError(f"Студент уже записан на {discipline}")
        self.disciplines[discipline] = None

    def remove_discipline(self, discipline):
        if discipline not in self.disciplines:
            raise ValueError(f"Студент не записан на {discipline}")
        del self.disciplines[discipline]

    def set_grade(self, discipline, grade):
        if discipline not in self.disciplines:
            raise ValueError(f"Студент не записан на {discipline}")
        if not (1 <= grade <= 10):
            raise ValueError("Оценка должна быть от 1 до 10")
        self.disciplines[discipline] = grade

    def go_to_next_semester(self):
        for discipline, grade in self.disciplines.items():
            if grade is None or grade < 5:
                raise ValueError(f"Не сдана дисциплина: {discipline} (оценка {grade})")
        self.semester += 1

    def average_grade(self):
        grades = [g for g in self.disciplines.values() if g is not None]
        if not grades:
            return 0
        return sum(grades) / len(grades)



class Discipline:
    def __init__(self, name, department):
        self.name = name
        self.department = department
        self.specialties = []


class Department:
    def __init__(self, name):
        self.name = name
        self.disciplines = []

    def add_discipline(self, discipline):
        self.disciplines.append(discipline)



class Faculty:
    def __init__(self, name):
        self.name = name
        self.departments = []
        self.students = []
        self.disciplines = []

    def add_department(self, department):
        self.departments.append(department)

    def add_discipline(self, discipline):
        self.disciplines.append(discipline)

    def enroll_student(self, student):
        self.students.append(student)

    def expel_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                return f"Студент {student.full_name} отчислен"
        raise ValueError("Студент не найден")

    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        raise ValueError("Студент не найден")

    def find_discipline(self, name):
        for discipline in self.disciplines:
            if discipline.name.lower() == name.lower():
                return discipline
        raise ValueError("Дисциплина не найдена")

    def check_discipline_for_student(self, student, discipline_name):
        discipline = self.find_discipline(discipline_name)
        if student.specialty not in discipline.specialties:
            raise ValueError(
                f"Дисциплина '{discipline_name}' не ведётся для специальности '{student.specialty}'"
            )
        return True



faculty = Faculty("РФиКТ")

department_it = Department("Информационные технологии")
department_sec = Department("Кибербезопасность")
faculty.add_department(department_it)
faculty.add_department(department_sec)


discipline_python = Discipline("Python", department_it)
discipline_python.specialties = ["прикладная информатика"]


discipline_crypto = Discipline("Криптография", department_sec)
discipline_crypto.specialties = ["кибербезопасность"]

department_it.add_discipline(discipline_python)
department_sec.add_discipline(discipline_crypto)

faculty.add_discipline(discipline_python)
faculty.add_discipline(discipline_crypto)



def menu():
    while True:
        print("\n=== МЕНЮ (Факультет РФиКТ) ===")
        print("1. Зачислить студента")
        print("2. Отчислить студента")
        print("3. Записать на дисциплину")
        print("4. Удалить с дисциплины")
        print("5. Выставить оценку")
        print("6. Перевести на следующий семестр")
        print("7. Ведомость по студенту")
        print("8. Ведомость по дисциплине")
        print("0. Выход")

        choice = input("Выберите действие: ").strip()

        try:
            if choice == "1":
                student_id = input("ID: ").strip()
                full_name = input("ФИО: ").strip()
                specialty = input("Специальность: ").strip()
                faculty.enroll_student(Student(student_id, full_name, specialty))
                print(f"Студент {full_name} зачислен")

            elif choice == "2":
                student_id = input("ID: ").strip()
                print(faculty.expel_student(student_id))

            elif choice == "3":
                student_id = input("ID: ").strip()
                discipline_name = input("Дисциплина: ").strip()
                student = faculty.find_student(student_id)
                faculty.check_discipline_for_student(student, discipline_name)
                real_discipline = faculty.find_discipline(discipline_name).name
                student.add_discipline(real_discipline)
                print(f"{student.full_name} записан на {real_discipline}")

            elif choice == "4":
                student_id = input("ID: ").strip()
                discipline_name = input("Дисциплина: ").strip()
                student = faculty.find_student(student_id)
                real_discipline = faculty.find_discipline(discipline_name).name
                student.remove_discipline(real_discipline)
                print(f"{student.full_name} удалён с {real_discipline}")

            elif choice == "5":
                student_id = input("ID: ").strip()
                discipline_name = input("Дисциплина: ").strip()
                grade = int(input("Оценка (1-10): ").strip())
                student = faculty.find_student(student_id)
                real_discipline = faculty.find_discipline(discipline_name).name
                student.set_grade(real_discipline, grade)
                print("Оценка выставлена")

            elif choice == "6":
                student_id = input("ID: ").strip()
                student = faculty.find_student(student_id)
                student.go_to_next_semester()
                print(f"{student.full_name} переведён на семестр {student.semester}")

            elif choice == "7":
                student_id = input("ID: ").strip()
                student = faculty.find_student(student_id)
                with open("student_report.txt", "w", encoding="utf-8") as file:
                    file.write(f"Факультет: {faculty.name}\n")
                    file.write(f"Студент: {student.full_name}\n")
                    file.write(f"Специальность: {student.specialty}\n")
                    file.write(f"Семестр: {student.semester}\n")
                    file.write("Дисциплины:\n")
                    for discipline, grade in student.disciplines.items():
                        file.write(f"  {discipline}: {grade if grade else 'не сдано'}\n")
                    file.write(f"Средний балл: {student.average_grade():.2f}\n")
                print("Ведомость сохранена в student_report.txt")

            elif choice == "8":
                discipline_name = input("Дисциплина: ").strip()
                discipline_obj = faculty.find_discipline(discipline_name)
                real_name = discipline_obj.name
                students = [s for s in faculty.students if real_name in s.disciplines]
                grades = [s.disciplines[real_name] for s in students if s.disciplines[real_name] is not None]
                average = sum(grades) / len(grades) if grades else 0

                with open("discipline_report.txt", "w", encoding="utf-8") as file:
                    file.write(f"Факультет: {faculty.name}\n")
                    file.write(f"Дисциплина: {real_name}\n")
                    file.write(f"Кафедра: {discipline_obj.department.name}\n")
                    file.write(f"Средний балл: {average:.2f}\n")
                    file.write("Студенты:\n")
                    for student in students:
                        file.write(f"  {student.full_name}: {student.disciplines[real_name]}\n")
                print("Ведомость сохранена в discipline_report.txt")

            elif choice == "0":
                break
            else:
                print("Такого пункта нет. Попробуйте снова.")
        except ValueError as error:
            print(f"Ошибка: {error}")
        except Exception as error:
            print(f"Непредвиденная ошибка: {error}")


if __name__ == "__main__":
    menu()