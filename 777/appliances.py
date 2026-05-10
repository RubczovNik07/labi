class Appliance:

    def __init__(self, power_kw):
        self._power_kw = power_kw

    @property
    def power(self):
        return self._power_kw


class Iron(Appliance):

    def __init__(self):
        super().__init__(2.0)

    def __str__(self):
        return "Утюг"


class TV(Appliance):

    def __init__(self):
        super().__init__(0.15)

    def __str__(self):
        return "Телевизор"


class WashingMachine(Appliance):

    def __init__(self):
        super().__init__(1.5)

    def __str__(self):
        return "Стиральная машина"
