import toga
from toga.style import Pack
from toga.style.pack import COLUMN

from appliances import APPLIANCES
from calculator import calculate_energy, calculate_cost
from report import save_doc, save_xls

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
            placeholder="Часы в день",
            style=Pack(padding=5)
        )

        self.days_input = toga.TextInput(
            placeholder="Количество дней",
            style=Pack(padding=5)
        )

        self.tariff_input = toga.TextInput(
            placeholder="Тариф",
            style=Pack(padding=5)
        )

        # Результат
        self.result_label = toga.Label(
            "Результат",
            style=Pack(padding=10)
        )

        # Кнопки
        calculate_button = toga.Button(
            "Рассчитать",
            on_press=self.calculate,
            style=Pack(padding=5)
        )

        doc_button = toga.Button(
            "Сохранить DOCX",
            on_press=self.save_doc_file,
            style=Pack(padding=5)
        )

        xls_button = toga.Button(
            "Сохранить XLSX",
            on_press=self.save_xls_file,
            style=Pack(padding=5)
        )

        # Контейнер
        box = toga.Box(
            children=[
                toga.Label("Прибор"),
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

            power = APPLIANCES[appliance]

            hours = float(self.hours_input.value)
            days = int(self.days_input.value)
            tariff = float(self.tariff_input.value)

            energy = calculate_energy(
                power,
                hours,
                days
            )

            cost = calculate_cost(
                energy,
                tariff
            )

            self.data = {
                "Прибор": appliance,
                "Энергия (кВт·ч)": round(energy, 2),
                "Стоимость": round(cost, 2)
            }

            self.result_label.text = (
                f"Энергия: {energy:.2f} кВт·ч\n"
                f"Стоимость: {cost:.2f}"
            )

        except Exception as e:
            self.result_label.text = f"Ошибка: {e}"

    # Сохранение DOCX
    def save_doc_file(self, widget):

        if self.data:
            save_doc("report.docx", self.data)
            self.result_label.text = "DOCX сохранён"

    # Сохранение XLSX
    def save_xls_file(self, widget):

        if self.data:
            save_xls("report.xlsx", self.data)
            self.result_label.text = "XLSX сохранён"

def main():
    return EnergyApp()
