def calculate_energy(power_kw, hours, days):
    return power_kw * hours * days

def calculate_cost(energy, tariff):
    return energy * tariff
