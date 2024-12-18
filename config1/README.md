# Эмулятор Shell для UNIX-подобной ОС с GUI

## **Описание задачи**

Разработан **эмулятор языка оболочки** для UNIX-подобных операционных систем. Эмулятор запускается из реальной командной строки и работает в режиме **GUI**. Образ виртуальной файловой системы передаётся в виде **ZIP-архива**, который распаковывается и обрабатывается в памяти, не затрагивая файловую систему пользователя.

---

## **Основные возможности**

- **Интерфейс командной строки**, приближенный к UNIX shell.
- **Виртуальная файловая система**, работающая с образа `zip`.
- **Режим GUI** для удобного взаимодействия.
- Поддержка **стандартных команд**:
  - `ls` — просмотр содержимого текущей директории.
  - `cd` — смена текущей директории.
  - `exit` — завершение работы эмулятора.
  - `date` — отображение текущей даты и времени.
  - `who` — отображение имени пользователя.

---

## **Алгоритм работы**

1. **Запуск эмулятора**:
   - Из командной строки передаются параметры:
     - **Имя пользователя** (для shell-приглашения).
     - **Путь к ZIP-архиву** с виртуальной файловой системой.

2. **Инициализация виртуальной ФС**:
   - ZIP-архив распаковывается **в оперативной памяти** с помощью Python-модуля `zipfile`.
   - Структура файлов и папок эмулируется в виде **виртуальной файловой системы**.

3. **Реализация команд оболочки**:
   - **`ls`**: Выводит список файлов и папок в текущей директории.
   - **`cd`**: Переход в указанную директорию (проверка на существование).
   - **`date`**: Вывод текущей системной даты и времени.
   - **`who`**: Вывод имени пользователя.
   - **`exit`**: Завершает работу эмулятора.

4. **Интерфейс GUI**:
   - Отображается окно с приглашением пользователя.
   - Команды вводятся через поле ввода, результат выводится в текстовое окно.

5. **Тестирование**:
   - Для каждой команды (`ls`, `cd`, `date`, `who`, `exit`) написано **2 теста**.
   - Тесты проверяют корректность выполнения команд и их взаимодействие с виртуальной файловой системой.

---

## **Формат запуска**

```bash
python emulator.py --user username --fs /path/to/filesystem.zip
```

- **`--user`**: Имя пользователя для приглашения (`username`).
- **`--fs`**: Путь к архиву виртуальной файловой системы.

---

## **Пример использования**

### **Запуск эмулятора**

```bash
python emulator.py --user vova --fs vfs.zip
```

### **Работа с командной оболочкой**

```plaintext
vova@shell:~$ ls
folder1 file1.txt file2.log

vova@shell:~$ cd folder1

vova@shell:~$ ls
nested.txt script.sh

vova@shell:~$ date
2024-06-05 15:23:01

vova@shell:~$ who
vova

vova@shell:~$ exit
Goodbye!
```

---

## **Описание решения**

1. **Аргументы командной строки** обрабатываются с помощью модуля `argparse`.
2. **ZIP-архив**:
   - Открывается в памяти с помощью `zipfile.ZipFile`.
   - Эмулируется файловая система с виртуальными путями и папками.
3. **Командный обработчик**:
   - Читает ввод пользователя.
   - Парсит команды и вызывает соответствующие функции.
4. **GUI** реализован с использованием **Tkinter**:
   - Поле ввода команд.
   - Поле для вывода результата выполнения команд.
5. **Тестирование**:
   - Используется модуль `unittest`.
   - Тесты охватывают выполнение всех команд и работу с виртуальной файловой системой.

---

## **Тестирование**

Запуск тестов:

```bash
python -m unittest test_emulator.py
```

---

## **Требования**

- **Python** 3.8+
- Модули:
  - `zipfile` — для работы с архивами.
  - `tkinter` — для GUI.
  - `argparse` — для парсинга аргументов командной строки.

---

## **Структура проекта**

```
shell_emulator/
│
├── emulator.py          # Основной скрипт эмулятора
├── test_emulator.py     # Тесты для эмулятора
├── config.json          # Конфигурация для тестов и примеров
├── vfs.zip              # Пример виртуальной файловой системы
└── README.md            # Документация
```

---

## **Как запустить**

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/username/shell-emulator.git
   cd shell-emulator
   ```

2. Запустите эмулятор:

   ```bash
   python emulator.py --user vova --fs vfs.zip
   ```

3. Взаимодействуйте с виртуальной оболочкой через GUI.

---

## **Пример виртуальной файловой системы**

Содержимое `vfs.zip`:

```
vfs/
│
├── folder1/
│   └── nested.txt
├── file1.txt
└── file2.log
```

---
