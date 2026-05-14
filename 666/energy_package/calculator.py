def calculate_energy(power_kw, hours_per_day, days):
    return power_kw * hours_per_day * days

def calculate_cost(energy_kwh, tariff):
    return energy_kwh * tariff
