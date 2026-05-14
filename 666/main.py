import toga
from toga.style import Pack
from toga.style.pack import COLUMN

from energy_package.appliances import APPLIANCES
from energy_package.calculator import (calculate_energy, calculate_cost)
from energy_package.report import (save_doc, save_xls)

class EnergyApp(toga.App):

    def startup(self):

        self.data = {}

        # Главное окно
        self.main_window = toga.MainWindow(
            title="Расчёт электроэнергии"
        )

        # Выбор прибора
        self.appliance_selection = toga.Selection(
            items=list(APPLIANCES.keys()),
            style=Pack(padding=5)
        )

        # Поля ввода
        self.hours_input = toga.TextInput(
            placeholder="Часы работы в день",
            style=Pack(padding=5)
        )

        self.days_input = toga.TextInput(
            placeholder="Количество дней",
            style=Pack(padding=5)
        )

        self.tariff_input = toga.TextInput(
            placeholder="Тариф (руб/кВт·ч)",
            style=Pack(padding=5)
        )

        # Результат
        self.result_label = toga.Label(
            "Введите данные и нажмите Рассчитать",
            style=Pack(padding=10)
        )

        # Кнопка расчёта
        calculate_button = toga.Button(
            "Рассчитать",
            on_press=self.calculate,
            style=Pack(padding=5)
        )

        # Кнопка DOCX
        doc_button = toga.Button(
            "Сохранить DOCX",
            on_press=self.save_doc_file,
            style=Pack(padding=5)
        )

        # Кнопка XLSX
        xls_button = toga.Button(
            "Сохранить XLSX",
            on_press=self.save_xls_file,
            style=Pack(padding=5)
        )

        # Контейнер
        box = toga.Box(
            children=[
                toga.Label("Выберите прибор:"),

                self.appliance_selection,

                self.hours_input,
                self.days_input,
                self.tariff_input,

                calculate_button,

                self.result_label,

                doc_button,
                xls_button
            ],

            style=Pack(
                direction=COLUMN,
                padding=10
            )
        )

        self.main_window.content = box
        self.main_window.show()

    # Расчёт
    def calculate(self, widget):

        try:
            appliance = self.appliance_selection.value

            if appliance is None:
                self.result_label.text = "Выберите прибор"
                return

            power = APPLIANCES[appliance]

            hours = float(self.hours_input.value)
            days = int(self.days_input.value)
            tariff = float(self.tariff_input.value)

            # Расчёт энергии
            energy = calculate_energy(
                power,
                hours,
                days
            )

            # Расчёт стоимости
            cost = calculate_cost(
                energy,
                tariff
            )

            # Сохранение данных
            self.data = {
                "Прибор": appliance,
                "Мощность (кВт)": power,
                "Часы в день": hours,
                "Количество дней": days,
                "Тариф": tariff,
                "Энергия (кВт·ч)": round(energy, 2),
                "Стоимость": round(cost, 2)
            }

            # Вывод результата
            self.result_label.text = (
                f"Энергия: {energy:.2f} кВт·ч\n"
                f"Стоимость: {cost:.2f} руб."
            )

        except ValueError:
            self.result_label.text = (
                "Введите корректные числа"
            )

        except Exception as e:
            self.result_label.text = f"Ошибка: {e}"

    # Сохранение DOCX
    def save_doc_file(self, widget):

        if self.data:
            save_doc("report.docx", self.data)

            self.result_label.text += (
                "\nDOCX файл сохранён"
            )

    # Сохранение XLSX
    def save_xls_file(self, widget):

        if self.data:
            save_xls("report.xlsx", self.data)

            self.result_label.text += (
                "\nXLSX файл сохранён"
            )

def main():
    return EnergyApp(
        formal_name="Энергопотребление",
        app_id="org.example.energy"
    )

if __name__ == "__main__":
    app = main()
    app.main_loop()