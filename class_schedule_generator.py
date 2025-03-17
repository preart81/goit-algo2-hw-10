# Визначення класу Teacher
class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = set(can_teach_subjects)
        self.assigned_subjects = set()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return (
            f"Teacher('{self.first_name}', '{self.last_name}', {self.age}, '{self.email}', {self.can_teach_subjects})"
        )



def create_schedule(subjects, teachers):
    # Використання жадібного алгоритму для призначення викладачів на предмети
    remaining_subjects = set(subjects)
    schedule = []

    while remaining_subjects:
        best_teacher = None
        best_subjects = set()

        for teacher in teachers:
            if teacher.assigned_subjects:
                continue

            can_teach = teacher.can_teach_subjects & remaining_subjects
            if len(can_teach) > len(best_subjects) or (
                len(can_teach) == len(best_subjects) and (best_teacher is None or teacher.age < best_teacher.age)
            ):
                best_teacher = teacher
                best_subjects = can_teach

        if not best_teacher:
            return None

        best_teacher.assigned_subjects = best_subjects
        remaining_subjects -= best_subjects
        schedule.append(best_teacher)

    return schedule


if __name__ == "__main__":
    # Множина предметів
    subjects = {"Математика", "Фізика", "Хімія", "Інформатика", "Біологія"}
    # Створення списку викладачів
    teachers = [
        Teacher("Олександр", "Іваненко", 45, "o.ivanenko@example.com", {"Математика", "Фізика"}),
        Teacher("Марія", "Петренко", 38, "m.petrenko@example.com", {"Хімія"}),
        Teacher("Сергій", "Коваленко", 50, "s.kovalenko@example.com", {"Інформатика", "Математика"}),
        Teacher("Наталія", "Шевченко", 29, "n.shevchenko@example.com", {"Біологія", "Хімія"}),
        Teacher("Дмитро", "Бондаренко", 35, "d.bondarenko@example.com", {"Фізика", "Інформатика"}),
        Teacher("Олена", "Гриценко", 42, "o.grytsenko@example.com", {"Біологія"}),
    ]

    # Виклик функції створення розкладу
    schedule = create_schedule(subjects, teachers)

    # Виведення розкладу
    if schedule:
        print("Розклад занять:")
        for teacher in schedule:
            print(f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}")
            print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")
