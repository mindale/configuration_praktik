import os
import sys
import zipfile
import shutil
import tempfile
import datetime
import getpass
import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox

class VirtualShell:
    def __init__(self, zip_path):
        # Проверяем ZIP-файл
        if not os.path.exists(zip_path) or not zipfile.is_zipfile(zip_path):
            raise FileNotFoundError("Указанный файл не является ZIP-архивом или не существует.")

        # Создаем временную директорию для распаковки
        self.temp_dir = tempfile.mkdtemp()
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(self.temp_dir)

        # Устанавливаем рабочую директорию
        os.chdir(self.temp_dir)
        self.root_dir = os.getcwd()

    def ls(self):
        return "\n".join(os.listdir(os.getcwd()))

    def cd(self, path):
        try:
            os.chdir(os.path.abspath(path))
            return f"Текущая директория: {os.getcwd()}"
        except Exception as e:
            return f"Ошибка: {e}"

    def date(self):
        now = datetime.datetime.now()
        return now.strftime("%Y-%m-%d %H:%M:%S")

    def who(self):
        return f"Пользователь: {getpass.getuser()}"

    def cleanup(self):
        shutil.rmtree(self.temp_dir)

# GUI для оболочки
class ShellGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Выбор ZIP-архива для эмулятора оболочки")

        # Поле выбора файла
        self.label = tk.Label(root, text="Выберите ZIP-файл для виртуальной файловой системы:")
        self.label.pack(pady=10)

        self.browse_button = tk.Button(root, text="Выбрать ZIP-файл", command=self.select_zip_file)
        self.browse_button.pack(pady=10)

        # Поле вывода
        self.output_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=20, width=80)
        self.output_area.pack(pady=10)

        # Поле ввода команд
        self.command_entry = tk.Entry(root, width=50)
        self.command_entry.pack(pady=5)
        self.command_entry.bind("<Return>", self.run_command)

        # Кнопка выполнения
        self.run_button = tk.Button(root, text="Выполнить команду", command=self.run_command)
        self.run_button.pack(pady=5)

        self.exit_button = tk.Button(root, text="Выход", command=self.cleanup_and_exit)
        self.exit_button.pack(pady=5)

        self.virtual_shell = None

    def select_zip_file(self):
        """Открывает диалоговое окно для выбора ZIP-файла."""
        zip_path = filedialog.askopenfilename(filetypes=[("ZIP Files", "*.zip")])
        if zip_path:
            try:
                self.virtual_shell = VirtualShell(zip_path)
                self.output_area.insert(tk.END, f"ZIP-файл успешно загружен: {zip_path}\n")
                self.output_area.insert(tk.END, f"Текущая директория: {os.getcwd()}\n")
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось загрузить ZIP-файл: {e}")
                sys.exit(1)

    def run_command(self, event=None):
        if not self.virtual_shell:
            messagebox.showwarning("Предупреждение", "Сначала выберите ZIP-файл.")
            return

        command_input = self.command_entry.get().strip()
        if not command_input:
            return

        if command_input == "exit":
            self.cleanup_and_exit()

        parts = command_input.split()
        command = parts[0]
        args = parts[1:]

        # Обработка команд
        if command == "ls":
            result = self.virtual_shell.ls()
        elif command == "cd":
            if args:
                result = self.virtual_shell.cd(args[0])
            else:
                result = "Ошибка: укажите путь для перехода."
        elif command == "date":
            result = self.virtual_shell.date()
        elif command == "who":
            result = self.virtual_shell.who()
        else:
            result = f"Команда '{command}' не найдена."

        # Вывод результата
        self.output_area.insert(tk.END, f"$ {command_input}\n{result}\n")
        self.output_area.see(tk.END)
        self.command_entry.delete(0, tk.END)

    def cleanup_and_exit(self):
        if self.virtual_shell:
            self.virtual_shell.cleanup()
        else:
            exit(0)
        self.root.quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = ShellGUI(root)
    root.mainloop()
