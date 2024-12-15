# import json
# with open("information.json", "r", encoding="utf-8") as file:
#     data = json.load(file)
#
# # Парсим JSON-строку в словарь
# print(data["rep"])  #2
#
# # Преобразуем словарь обратно в JSON
# json_output = json.dumps(data)
# print(json_output)  # {"name": "Вова", "age": 19}


import subprocess
import sys
import datetime


def get_commits(before_date):
    """
    Получает список коммитов и их родителей до указанной даты.
    """
    try:
        # Выполнение команды git для получения коммитов и их родителей
        result = subprocess.check_output(
            ["git", "rev-list", "--parents", f"--before={before_date}", "HEAD"],
            text=True
        )
        return result.strip().split("\n")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при выполнении git: {e}")
        sys.exit(1)


def build_dependency_graph(commits):
    """
    Строит граф зависимостей из списка коммитов.
    Возвращает текст PlantUML.
    """
    plantuml_lines = ["@startuml", "skinparam linetype ortho"]

    # Узлы и связи
    for line in commits:
        parts = line.split()
        commit = parts[0]
        parents = parts[1:]

        # Добавляем узел для коммита
        plantuml_lines.append(f'node "{commit}" as {commit}')

        # Добавляем связи с родительскими коммитами
        for parent in parents:
            plantuml_lines.append(f'{parent} --> {commit}')

    plantuml_lines.append("@enduml")
    return "\n".join(plantuml_lines)


def main():
    if len(sys.argv) != 2:
        print("Использование: python3 git_dependency_visualizer.py <YYYY-MM-DD>")
        sys.exit(1)

    before_date = sys.argv[1]

    # Проверка формата даты
    try:
        datetime.datetime.strptime(before_date, "%Y-%m-%d")
    except ValueError:
        print("Ошибка: дата должна быть в формате YYYY-MM-DD")
        sys.exit(1)

    # Получаем коммиты и строим граф
    print("Получение коммитов из репозитория...")
    commits = get_commits(before_date)

    if not commits:
        print("Нет коммитов до указанной даты.")
        sys.exit(0)

    print("Построение графа зависимостей...")
    plantuml_code = build_dependency_graph(commits)

    # Вывод результата
    print("\nСгенерированный PlantUML-код:")
    print(plantuml_code)



