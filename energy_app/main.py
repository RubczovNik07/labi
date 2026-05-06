import tkinter as tk
from tkinter import messagebox

from energy_package.appliances import APPLIANCES
from energy_package.calculator import calculate_energy, calculate_cost
from energy_package.report import save_doc, save_xls

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор энергии")

        # --- выбор прибора ---
        tk.Label(root, text="Прибор").pack()
        self.appliance = tk.StringVar(value="Утюг")
        tk.OptionMenu(root, self.appliance, *APPLIANCES.keys()).pack()

        # --- ввод ---
        tk.Label(root, text="Часы в день").pack()
        self.hours = tk.Entry(root)
        self.hours.pack()

        tk.Label(root, text="Дни").pack()
        self.days = tk.Entry(root)
        self.days.pack()

        tk.Label(root, text="Тариф (за кВт⋅ч)").pack()
        self.tariff = tk.Entry(root)
        self.tariff.pack()

        # --- результат ---
        self.result = tk.Label(root, text="Результат появится здесь")
        self.result.pack()

        # --- кнопки ---
        tk.Button(root, text="Рассчитать", command=self.calculate).pack()
        tk.Button(root, text="Сохранить DOC", command=self.save_doc).pack()
        tk.Button(root, text="Сохранить XLS", command=self.save_xls).pack()

        self.data = {}

    def calculate(self):
        try:
            appliance = self.appliance.get()
            power = APPLIANCES[appliance]

            hours = float(self.hours.get())
            days = int(self.days.get())
            tariff = float(self.tariff.get())

            energy = calculate_energy(power, hours, days)
            cost = calculate_cost(energy, tariff)

            self.data = {
                "Прибор": appliance,
                "Энергия (кВт⋅ч)": energy,
                "Стоимость": cost
            }

            self.result.config(text=f"Энергия: {energy:.2f}, Стоимость: {cost:.2f}")

        except ValueError:
            messagebox.showerror("Ошибка", "Введите числа правильно")

    def save_doc(self):
        save_doc("report.docx", self.data)

    def save_xls(self):
        save_xls("report.xlsx", self.data)

root = tk.Tk()
app = App(root)
root.mainloop()
