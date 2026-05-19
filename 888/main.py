import json
import os
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


# =========================
# Пользовательские исключения
# =========================
class PasswordManagerError(Exception):
    pass


class EntryNotFoundError(PasswordManagerError):
    pass


class DuplicateEntryError(PasswordManagerError):
    pass


class StorageError(PasswordManagerError):
    pass


# =========================
# Модель данных
# =========================
class PasswordEntry:
    def __init__(self, service: str, username: str, password: str):
        self.service = service
        self.username = username
        self.password = password

    def to_dict(self):
        return {
            "service": self.service,
            "username": self.username,
            "password": self.password
        }

    @staticmethod
    def from_dict(data):
        return PasswordEntry(
            data["service"],
            data["username"],
            data["password"]
        )


# =========================
# Хранилище
# =========================
class PasswordStorage:
    def __init__(self, filename="passwords.json"):
        self.filename = filename
        self.entries = {}
        self.load()

    def load(self):
        if not os.path.exists(self.filename):
            self.entries = {}
            return

        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.entries = {
                    k: PasswordEntry.from_dict(v)
                    for k, v in data.items()
                }
        except Exception as e:
            raise StorageError(f"Ошибка загрузки: {e}")

    def save(self):
        try:
            with open(self.filename, "w", encoding="utf-8") as f:
                json.dump(
                    {k: v.to_dict() for k, v in self.entries.items()},
                    f,
                    indent=4,
                    ensure_ascii=False
                )
        except Exception as e:
            raise StorageError(f"Ошибка сохранения: {e}")

    def add_entry(self, entry: PasswordEntry):
        if entry.service in self.entries:
            raise DuplicateEntryError("Сервис уже существует")

        self.entries[entry.service] = entry
        self.save()

    def delete_entry(self, service: str):
        if service not in self.entries:
            raise EntryNotFoundError("Сервис не найден")

        del self.entries[service]
        self.save()

    def get_entry(self, service: str):
        if service not in self.entries:
            raise EntryNotFoundError("Сервис не найден")

        return self.entries[service]

    def get_all(self):
        return list(self.entries.values())


# =========================
# GUI (Toga)
# =========================
class PasswordManagerApp(toga.App):

    def startup(self):
        self.storage = PasswordStorage()

        # Поля ввода
        self.service_input = toga.TextInput(placeholder="Сервис")
        self.username_input = toga.TextInput(placeholder="Логин")
        self.password_input = toga.TextInput(placeholder="Пароль")

        # Список сервисов
        self.list_selection = toga.Selection(
            items=self.get_services()
        )

        # Кнопки
        add_btn = toga.Button("Добавить", on_press=self.add_entry)
        view_btn = toga.Button("Просмотр", on_press=self.view_entry)
        delete_btn = toga.Button("Удалить", on_press=self.delete_entry)

        # Разметка
        input_box = toga.Box(
            children=[
                self.service_input,
                self.username_input,
                self.password_input
            ],
            style=Pack(direction=COLUMN, margin=5)
        )

        button_box = toga.Box(
            children=[add_btn, view_btn, delete_btn],
            style=Pack(direction=ROW, margin=5)
        )

        main_box = toga.Box(
            children=[input_box, button_box, self.list_selection],
            style=Pack(direction=COLUMN, margin=10)
        )
        
        self.main_window = toga.MainWindow(title="Менеджер паролей")
        self.main_window.content = main_box
        self.main_window.show()

    # =========================
    # Логика
    # =========================
    def get_services(self):
        return [e.service for e in self.storage.get_all()]

    def refresh_list(self):
        self.list_selection.items = self.get_services()

    def add_entry(self, widget):
        try:
            entry = PasswordEntry(
                self.service_input.value,
                self.username_input.value,
                self.password_input.value
            )
            self.storage.add_entry(entry)
            self.refresh_list()

        except PasswordManagerError as e:
            self.main_window.error_dialog("Ошибка", str(e))

    def view_entry(self, widget):
        try:
            service = self.list_selection.value
            entry = self.storage.get_entry(service)

            self.main_window.info_dialog(
                "Запись",
                f"Сервис: {entry.service}\n"
                f"Логин: {entry.username}\n"
                f"Пароль: {entry.password}"
            )

        except PasswordManagerError as e:
            self.main_window.error_dialog("Ошибка", str(e))

    def delete_entry(self, widget):
        try:
            service = self.list_selection.value
            self.storage.delete_entry(service)
            self.refresh_list()

        except PasswordManagerError as e:
            self.main_window.error_dialog("Ошибка", str(e))


# =========================
# Точка входа (ВАЖНО ДЛЯ TOGA)
# =========================
if __name__ == "__main__":
    app = PasswordManagerApp(
        "Менеджер паролей",
        "org.example.passwordmanager"
    )
    app.main_loop()