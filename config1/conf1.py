import os
import sys
import datetime
import getpass

def ls():#Список файлов и папок в текущей директории.
    try:
        for file in os.listdir(os.getcwd()):
            print(file)
    except Exception as e:
        print(f"Ошибка: {e}")

def cd(path):#Переход в указанную директорию.
    try:
        os.chdir(path)
        print(f"Текущая директория: {os.getcwd()}")
    except Exception as e:
        print(f"Ошибка: {e}")

def date():#Вывод текущей даты и времени
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))

def who():#Вывод имени текущего пользователя.
    print(f"Пользователь: {getpass.getuser()}")

def shell():#Главная функция.
    print("Добро пожаловать в эмулятор оболочки! Введите 'exit' для выхода.")
    while True:
        try:
            # Печатаем приглашение
            user_input = input(f"{os.getcwd()} $ ").strip()
            if not user_input:
                continue

            # Разбиваем команду и аргументы
            parts = user_input.split()
            command = parts[0]
            args = parts[1:]

            # Обработка команд
            if command == "ls":
                ls()
            elif command == "cd":
                if args:
                    cd(args[0])
                else:
                    print("Ошибка: укажите путь для перехода.")
            elif command == "date":
                date()
            elif command == "who":
                who()
            elif command == "exit":
                print("Выход из оболочки...")
                sys.exit(0)
            else:
                print(f"Команда '{command}' не найдена.")

        except KeyboardInterrupt:
            print("\nНажмите 'exit' для выхода.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

shell()
