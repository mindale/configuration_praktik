import os
import sys
import subprocess
import json


def read_config(config_path):
    """
    Чтение конфигурационного файла JSON.
    """
    try:
        with open(config_path, 'r') as file:
            config = json.load(file)
            return config
    except Exception as e:
        raise RuntimeError(f"Ошибка чтения конфигурации: {e}")


def get_git_commits(repo_path, before_date):
    """
    Получает список коммитов и их родителей до указанной даты.
    """
    try:
        # Переходим в репозиторий
        os.chdir(repo_path)

        # Выполняем git-команду для получения коммитов
        command = ["git", "rev-list", "--parents", f"--before={before_date}", "HEAD"]
        result = subprocess.check_output(command, text=True)
        return result.strip().split("\n")
    except Exception as e:
        raise RuntimeError(f"Ошибка при получении коммитов из Git: {e}")


def get_git_commits(repo_path, before_date):
    """
    Получает список коммитов и их родителей до указанной даты.
    """
    try:
        # Переходим в репозиторий
        os.chdir(repo_path)

        # Выполняем git-команду для получения коммитов
        command = ["git", "rev-list", "--parents", f"--before={before_date}", "HEAD"]
        result = subprocess.check_output(command, text=True)
        return result.strip().split("\n")
    except Exception as e:
        raise RuntimeError(f"Ошибка при получении коммитов из Git: {e}")




def build_plantuml_code(commits):
    """
    Строит текстовое представление графа зависимостей в формате PlantUML.
    """
    plantuml_lines = ["@startuml", "skinparam linetype ortho"]

    for line in commits:
        parts = line.split()
        commit = parts[0]
        parents = parts[1:]

        # Добавляем узлы и зависимости
        plantuml_lines.append(f'node "{commit}" as {commit}')
        for parent in parents:
            plantuml_lines.append(f'{parent} --> {commit}')

    plantuml_lines.append("@enduml")
    return "\n".join(plantuml_lines)






def save_to_file(output_file, content):
    """
    Сохраняет PlantUML-код в файл.
    """
    try:
        with open(output_file, 'w') as file:
            file.write(content)
    except Exception as e:
        raise RuntimeError(f"Ошибка записи в файл: {e}")


def main(config_path):
    """
    Основная функция программы.
    """
    # Чтение конфигурации
    config = read_config(config_path)
    repo_path = config['repository_path']
    output_file = config['output_file']
    before_date = config['before_date']

    print("Получение коммитов из Git...")
    commits = get_git_commits(repo_path, before_date)
    if not commits:
        print("Нет коммитов до указанной даты.")
        return

    print("Построение PlantUML-кода...")
    plantuml_code = build_plantuml_code(commits)

    # Сохранение кода в файл
    save_to_file(output_file, plantuml_code)

    print("\nГраф зависимостей коммитов в формате PlantUML:")
    print(plantuml_code)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python3 dependency_visualizer.py <config.json>")
        sys.exit(1)

    main(sys.argv[1])
