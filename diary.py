# Инициализация пустых списков для хранения оценок и предметов

list_estim = []
list_items = []


# Цикл для получения кол-ва предметов от пользователя
while True:
    try:
        items_quantity = int(input("Введите количество предметов: "))
        break
    except ValueError:
        print("Ошибка! Введите ЦИФРУ!")


# Основной цикл для ввода предметов и оценок
for i in range(items_quantity):
    # Ввод названия предмета
    while True:
        items = input(f"Введите название {i + 1} предмета: ")
        # Проверка на уникальность предмета
        if items in list_items:
            print("Этот предмет уже есть. Введите другой.")
            continue
        else:
            list_items.append(items)
            break
    # ввод оценки по предмету
    while True:
            try:
                estim = int(input("Введите оценку по этому предмету: "))
               # Проверка корректности оценки (от 2 до 5)
                if 2 > estim or 5 < estim:
                    print("Оценка должна быть от 2 до 5.")
                    continue
                break
            except ValueError:
                print("Введите ЦИФРУ от 2 до 5!")
    list_estim.append(estim)

# Вывод результатов
print()
print("Предметы и оценки:")
# Вывод списка предметов с соответствующими оценками
for subject, grade in zip(list_items, list_estim):
    print(f"|{subject}: {grade}")

# Статистика по оценкам
print()
for mark in range(2, 6):
    print(f"Оценок '{mark}': {list_estim.count(mark)}")

# Расчет среднего балла
sum_mark = sum(list_estim)
average = round((sum_mark / items_quantity), 2)
print(f"Ваш средний балл составляет: {average}")

# Оценка успеваемости в зависимости от среднего балла
if average <= 2.5:
    print("Нужно срочно подтянуть учёбу!")
elif 2.6 < average < 3.4:
    print("Ты справляешься, но есть куда расти!")
elif 3.5 < average < 4.4:
    print("Хорошо! Продалжай в томже духе.")
elif average >= 4.5:
    print("Отлично! Ты большая умница!")