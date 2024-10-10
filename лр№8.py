# Словник для зберігання інформації про студентів
students = {
    "Іванов Іван Іванович": {
        "Група": "КН-21",
        "Курс": "2",
        "Предмети": {
            "Математика": "85",
            "Програмування": "92",
            "Фізика": "78"
        }
    },
    "Петренко Марія Олександрівна": {
        "Група": "КН-21",
        "Курс": "2",
        "Предмети": {
            "Математика": "91",
            "Програмування": "88",
            "Фізика": "82"
        }
    },
    "Сидоренко Олексій Петрович": {
        "Група": "КН-22",
        "Курс": "2",
        "Предмети": {
            "Математика": "76",
            "Програмування": "95",
            "Фізика": "70"
        }
    },
    "Коваленко Анна Василівна": {
        "Група": "КН-22",
        "Курс": "2",
        "Предмети": {
            "Математика": "88",
            "Програмування": "84",
            "Фізика": "79"
        }
    },
    "Бондаренко Дмитро Сергійович": {
        "Група": "КН-23",
        "Курс": "2",
        "Предмети": {
            "Математика": "93",
            "Програмування": "89",
            "Фізика": "85"
        }
    }
}

def add_student():
    group_number = input("Введіть номер групи: ")
    full_name = input("Введіть ПІБ студента: ")
    course = input("Введіть курс: ")
    subjects = {}
    while True:
        subject = input("Введіть назву предмету (або 'готово' для завершення): ")
        if subject.lower() == 'готово':
            break
        grade = input(f"Введіть оцінку за {subject}: ")
        subjects[subject] = grade
    
    students[full_name] = {
        "Група": group_number,
        "Курс": course,
        "Предмети": subjects
    }
    print(f"Студент {full_name} доданий успішно.")

def remove_student():
    full_name = input("Введіть ПІБ студента для видалення: ")
    if full_name in students:
        del students[full_name]
        print(f"Студент {full_name} видалений успішно.")
    else:
        print("Студент не знайдений.")

def edit_student():
    full_name = input("Введіть ПІБ студента для редагування: ")
    if full_name in students:
        print("Що ви хочете відредагувати?")
        print("1. Номер групи")
        print("2. Курс")
        print("3. Предмети та оцінки")
        choice = input("Ваш вибір (1/2/3): ")
        
        if choice == '1':
            new_group = input("Введіть новий номер групи: ")
            students[full_name]["Група"] = new_group
        elif choice == '2':
            new_course = input("Введіть новий курс: ")
            students[full_name]["Курс"] = new_course
        elif choice == '3':
            subject = input("Введіть назву предмету для редагування: ")
            if subject in students[full_name]["Предмети"]:
                new_grade = input(f"Введіть нову оцінку за {subject}: ")
                students[full_name]["Предмети"][subject] = new_grade
            else:
                print("Предмет не знайдений.")
        print("Інформація оновлена успішно.")
    else:
        print("Студент не знайдений.")

def display_students():
    if not students:
        print("Словник порожній.")
    else:
        for full_name, info in students.items():
            print(f"\nСтудент: {full_name}")
            print(f"Група: {info['Група']}")
            print(f"Курс: {info['Курс']}")
            print("Предмети та оцінки:")
            for subject, grade in info['Предмети'].items():
                print(f"  {subject}: {grade}")

def main():
    while True:
        print("\nМеню:")
        print("1. Додати студента")
        print("2. Видалити студента")
        print("3. Редагувати інформацію про студента")
        print("4. Показати всіх студентів")
        print("5. Вийти")
        
        choice = input("Виберіть опцію (1-5): ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            remove_student()
        elif choice == '3':
            edit_student()
        elif choice == '4':
            display_students()
        elif choice == '5':
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()