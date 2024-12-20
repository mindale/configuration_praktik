# Визуализатор графа зависимостей Git-коммитов

## **Описание задачи**

Разработан инструмент командной строки для визуализации графа зависимостей коммитов в Git-репозитории.  
- Зависимости включают как **прямые**, так и **транзитивные связи**.  
- Визуализация представлена в формате **PlantUML**.  
- Граф строится только для коммитов, созданных **до указанной даты**.  
- Результат выводится на экран и сохраняется в файл.

---

## **Функциональные возможности**

- **Получение зависимостей** коммитов из Git-репозитория.
- **Формирование графа** зависимостей на основе хеш-значений коммитов.
- **Генерация кода PlantUML** для визуализации графа.
- **Конфигурация через JSON-файл**.
- **Покрытие функций тестами** для проверки корректности работы.

---

## **Алгоритм работы**

1. **Чтение конфигурации** из файла `config.json`:
   - Путь к программе для визуализации.
   - Путь к анализируемому Git-репозиторию.
   - Путь к файлу для сохранения результата.
   - Заданная дата для фильтрации коммитов.

2. **Сбор коммитов** из репозитория:
   - Чтение коммитов с их хеш-значениями.
   - Фильтрация коммитов по дате.

3. **Анализ зависимостей**:
   - Построение графа коммитов на основе их связей.
   - Учёт транзитивных зависимостей.

4. **Генерация кода PlantUML**:
   - Формирование узлов и связей графа.
   - Вывод PlantUML-кода на экран и сохранение в файл.

5. **Результат**:
   - Код графа в формате PlantUML сохраняется в указанный файл.

---

## **Пример конфигурационного файла (`config.json`)**

```json
{
  "visualizer_path": "/usr/local/bin/plantuml",
  "repository_path": "/path/to/git-repo",
  "output_file": "output_graph.puml",
  "commit_date": "2024-06-01"
}
```

---

## **Пример использования**

1. Запустите скрипт, передав конфигурацию:

   ```bash
   python graph_visualizer.py config.json
   ```

2. **Вывод на экран** кода графа:

   ```plaintext
   @startuml
   node "Коммит A" as A
   node "Коммит B" as B
   node "Коммит C" as C
   A --> B
   B --> C
   @enduml
   ```

3. Откройте результат в программе для визуализации PlantUML или в онлайн-сервисах.

---

## **Описание решения**

1. **Git-коммиты** получаются через вызов команд Git из Python (`subprocess`):
   - `git log` с фильтрацией по дате.
   - `git rev-list` для анализа зависимостей.

2. Для **построения графа** используется словарь, где:
   - Ключ: хеш коммита.
   - Значения: родительские коммиты.

3. Результат конвертируется в формат **PlantUML** с узлами и связями.

4. Скрипт сохраняет результат в файл и выводит на экран.

5. **Тестирование** покрывает:
   - Чтение конфигурации.
   - Получение коммитов и зависимостей.
   - Генерацию PlantUML.

---

## **Тестирование**

Для запуска тестов используйте **unittest**:

```bash
python -m unittest test_graph_visualizer.py
```

---

## **Требования**

- Python 3.8+
- Git
- PlantUML

---

## **Установка**

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/username/graph-visualizer.git
   cd graph-visualizer
   ```

2. Установите зависимости:

   ```bash
   pip install -r requirements.txt
   ```

3. Настройте `config.json` и запустите программу.

---

## **Пример результата**

После обработки репозитория с коммитами:

```plaintext
@startuml
node "Коммит 123abc" as A
node "Коммит 456def" as B
node "Коммит 789ghi" as C
A --> B
B --> C
@enduml
```

Этот код можно визуализировать в **PlantUML** для наглядного графа зависимостей.

---

.