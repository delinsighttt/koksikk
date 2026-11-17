

class Hero:
    def __init__(self, name, level, hp):
        self.name = name
        self.level = level
        self.hp = hp

    def to_line(self):
        """Превращает объект в строку формата 'имя;уровень;здоровье'."""
        return f"{self.name};{self.level};{self.hp}"


def hero_from_line(line):
    """Создаёт объект Hero из строки 'имя;уровень;здоровье'."""
    name, level, hp = line.strip().split(";")
    return Hero(name, int(level), int(hp))


def save_to_file(objects, filename):
    """Сохраняет список объектов в файл: одна строка — один объект."""
    with open(filename, "w", encoding="utf-8") as f:
        for obj in objects:
            f.write(obj.to_line() + "\n")


def load_from_file(filename):
    """Загружает объекты из файла. Возвращает список даже при ошибках."""
    objects = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                try:
                    objects.append(hero_from_line(line))
                except ValueError:
                    print(f"Ошибка в формате строки, пропущено: {line.strip()}")
    except FileNotFoundError:
        print("Файл не найден, начинаем с пустого списка.")
    return objects


# задангие 1
def task1():
    print("\n--- Задание 1: деление с обработкой ошибок ---")
    try:
        a = int(input("Введи первое число: "))
        b = int(input("Введи второе число: "))
        result = a / b
        print("Результат:", result)
    except ValueError:
        print("Введено не число!")
    except ZeroDivisionError:
        print("На ноль делить нельзя!")


# задание 2
def task2():
    print("\n--- Задание 2: несколько except и finally ---")
    try:
        x = int(input("Введи число: "))
        result = 10 / x
    except ValueError:
        print("Это не число!")
    except ZeroDivisionError:
        print("На ноль делить нельзя!")
    else:
        print("Результат:", result)
    finally:
        print("Программа завершена.")


# задание 3
def task3():
    print("\n--- Задание 3: запись и чтение файла ---")
    with open("hello.txt", "w", encoding="utf-8") as f:
        f.write("Привет\n")
        f.write("Как дела?\n")
        f.write("Пока\n")

    with open("hello.txt", "r", encoding="utf-8") as f:
        lines = f.read().split("\n")

    print(lines)
    real_lines = [x for x in lines if x != ""]
    print("Строк в файле:", len(real_lines))


#задание 4
def task4():
    print("\n--- Задание 4: дозапись в файл ---")
    with open("hello.txt", "a", encoding="utf-8") as f:
        f.write("Ещё одна строка\n")

    with open("hello.txt", "r", encoding="utf-8") as f:
        print(f.read())


# задание 5
def task5():
    print("\n--- Задание 5: класс + сохранение в файл (круговой тест) ---")
    hero = Hero("Артас", 80, 2500)
    line = hero.to_line()
    print("Строка объекта:", line)

    hero2 = hero_from_line(line)
    print("Новый объект:", hero2.name, hero2.level, hero2.hp)
    print("Атрибуты совпадают:",
          hero.name == hero2.name and
          hero.level == hero2.level and
          hero.hp == hero2.hp)

#заданеи 6
def task6():
    print("\n--- Задание 6: сохранение списка объектов в файл ---")
    objects = [
        Hero("Артас", 80, 2500),
        Hero("Сильвана", 65, 1800)
    ]
    save_to_file(objects, "test_data.txt")
    print("Сохранено в test_data.txt")

    loaded = load_from_file("test_data.txt")
    print("Загружено:")
    for obj in loaded:
        print(f"Герой: {obj.name}, уровень {obj.level}, здоровье {obj.hp}")

    print("\nПопытка загрузить несуществующий файл:")
    missing = load_from_file("no_such_file.txt")
    print("Результат (пустой список):", missing)


# задание 7
def task7():
    print("\n--- Задание 7: полная программа ---")
    heroes = [
        Hero("Артас", 80, 2500),
        Hero("Сильвана", 65, 1800),
        Hero("Иллидан", 70, 2100)
    ]
    save_to_file(heroes, "data.txt")
    print("Сохранено 3 героя в data.txt")

    heroes = []
    print("Список очищен")

    loaded_heroes = load_from_file("data.txt")
    print("Загружено из файла:")
    for h in loaded_heroes:
        print(f"Герой: {h.name}, уровень {h.level}, здоровье {h.hp}")


def test_missing_file():
    print("\n--- Тест: загрузка несуществующего файла ---")
    result = load_from_file("data_missing.txt")
    print("Программа не упала. Список:", result)


def main():
    while True:
        print("\n" + "=" * 40)
        print("Выберите задание:")
        print("1 - Задание 1")
        print("2 - Задание 2")
        print("3 - Задание 3")
        print("4 - Задание 4")
        print("5 - Задание 5")
        print("6 - Задание 6")
        print("7 - Задание 7")
        print("8 - Тест: загрузка несуществующего файла")
        print("0 - Выход")
        choice = input("Ваш выбор: ")

        if choice == "1":
            task1()
        elif choice == "2":
            task2()
        elif choice == "3":
            task3()
        elif choice == "4":
            task4()
        elif choice == "5":
            task5()
        elif choice == "6":
            task6()
        elif choice == "7":
            task7()
        elif choice == "8":
            test_missing_file()
        elif choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор, попробуйте снова.")


if __name__ == "__main__":
    main()