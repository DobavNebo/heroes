from core import find_tallest

gend = input("Введите пол(гендер) искомого героя (Male / Female): ")
user_inp = input("Имеет ли работу? (True / False): ")
if user_inp == "True":
    target = find_tallest(gend, True)
    if target:
        print(target)
    else:
        print(f"Не удалось получить героя по запросу {gend} {user_inp}")
elif user_inp == "False":
    target = find_tallest(gend, False)
    if target:
        print(target)
    else:
        print(f"Не удалось получить героя по запросу {gend} {user_inp}")
else:
    print("Некорректный ввод. В следующий раз используйте True/False")

input("Нажмите Enter для завершения работы")