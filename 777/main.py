import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from appliances import Iron, TV, WashingMachine
from calculator import EnergyCalculator
from report import Report


class EnergyWindow(Gtk.Window):

    def __init__(self):
        super().__init__(title="ЛР №7 PyGObject")

        self.set_border_width(10)

        self.appliances = {
            "Утюг": Iron(),
            "Телевизор": TV(),
            "Стиральная машина": WashingMachine()
        }
        self.data = None

        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        self.combo = Gtk.ComboBoxText()
        for name in self.appliances:
            self.combo.append_text(name)
        self.combo.set_active(0)

        self.hours = Gtk.Entry()
        self.hours.set_placeholder_text("Часы")

        self.days = Gtk.Entry()
        self.days.set_placeholder_text("Дни")

        self.tariff = Gtk.Entry()
        self.tariff.set_placeholder_text("Тариф")

        self.label = Gtk.Label(label="Результат")

        btn_calc = Gtk.Button(label="Рассчитать")
        btn_calc.connect("clicked", self.calculate)

        btn_doc = Gtk.Button(label="DOCX")
        btn_doc.connect("clicked", self.save_docx)

        btn_xls = Gtk.Button(label="XLSX")
        btn_xls.connect("clicked", self.save_xlsx)

        self.box.pack_start(self.combo, False, False, 0)
        self.box.pack_start(self.hours, False, False, 0)
        self.box.pack_start(self.days, False, False, 0)
        self.box.pack_start(self.tariff, False, False, 0)
        self.box.pack_start(btn_calc, False, False, 0)
        self.box.pack_start(self.label, False, False, 0)
        self.box.pack_start(btn_doc, False, False, 0)
        self.box.pack_start(btn_xls, False, False, 0)

        self.add(self.box)

    def calculate(self, widget):
        try:
            hours_text = self.hours.get_text().strip()
            days_text = self.days.get_text().strip()
            tariff_text = self.tariff.get_text().strip()

            if not hours_text or not days_text or not tariff_text:
                self.label.set_text("Заполните все поля")
                return

            hours = float(hours_text)
            days = int(days_text)
            tariff = float(tariff_text)

            name = self.combo.get_active_text()

            if not name or name not in self.appliances:
                self.label.set_text("Выберите прибор")
                return

            appliance = self.appliances[name]


            calc = EnergyCalculator(appliance, hours, days, tariff)

            self.label.set_text(
                f"{calc.energy():.2f} кВт·ч / {calc.cost():.2f} руб."
            )

        except ValueError:
            self.label.set_text("Ошибка: введите числа")

    def save_docx(self, widget):

        if self.data is None:
            self.label.set_text("Сначала выполните расчёт")
            return

        Report(self.data).save_docx("report.docx")
        self.label.set_text("DOCX сохранён")


    def save_xlsx(self, widget):

        if self.data is None:
            self.label.set_text("Сначала выполните расчёт")
            return

        Report(self.data).save_xlsx("report.xlsx")
        self.label.set_text("XLSX сохранён")


win = EnergyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()