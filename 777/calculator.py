class EnergyCalculator:

    def __init__(self, appliance, hours, days, tariff):
        self.appliance = appliance
        self.hours = max(0, hours)
        self.days = max(0, days)
        self.tariff = max(0, tariff)

    def energy(self):
        return self.appliance.power * self.hours * self.days

    def cost(self):
        return self.energy() * self.tariff