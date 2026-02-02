from core import find_tallest

print("Запуск диагностики...")

allerrors = 0 #Счетчик проблем
overallerr = 0

print("(smoke) Проверка базовой функциональности")
for gender in ["Male", "Female"]:
    for job in [True, False, 1, 0]:
        target = find_tallest(gender, job)
        if target == None:
            print(f"Внимание: некорректно обрабатывается значение {job} для пары {gender}, {job}")
            continue
        if job != (target['work']['occupation'] != "-"):
            print(f"Внимание: некорректно обрабатывается значение {job} для пары {gender}, {job}")
            allerrors += 1
        if gender != target['appearance']['gender']:
            print(f"Внимание: некорректно обрабатывается значение {gender} для пары {gender}, {job}")
            allerrors += 1
print(f"(smoke) Пройдены позитивные тесты. Всего ошибок при прохождении тестов: {allerrors}")
input("\n Нажмите Enter чтобы продолжить диагностику (если дальнейшие тесты необходимы) \n")
overallerr += allerrors
allerrors = 0

for gender in [None]:
    for job in [True, False]:
        target = find_tallest(gender, job)
        if target != None:
            print(f"Внимание: некорректно обрабатывается значение {gender} для пары {gender}, {job}")
            allerrors += 1
for job in [None]:
    for gender in ["Male", "Female"]:
        target = find_tallest(gender, job)
        if target != None:
            print(f"Внимание: некорректно обрабатывается значение {job} для пары {gender}, {job}")
            allerrors += 1
print("Пройдены тесты при отсутствии вводных (None вводные) в back-end")

for gender in ["bruh", "", " ", "!", "'", '"']:
    for job in [True, False]:
        target = find_tallest(gender, job)
        if target != None:
            print(f"Внимание: некорректно обрабатывается значение {gender} для пары {gender}, {job}")
            allerrors += 1
for job in ["bruh", "", " ", "!", "'", '"', "+", -1]:
    for gender in ["Male", "Female"]:
        target = find_tallest(gender, job)
        if target != None:
            print(f"Внимание: некорректно обрабатывается значение {job} для пары {gender}, {job}")
            allerrors += 1
print("Пройдены тесты на некорректные вводные в back-end")

print(f"Диагностика завершена. Всего ошибок при прохождении тестов: {overallerr}")
input("\n Нажмите Enter чтобы завершить работу")
    