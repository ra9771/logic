def calculate_transportation_footprint(km_driven, fuel_efficiency):
    # Conversion factors
    liters_per_gallon = 3.78541
    kg_per_pound = 0.453592
    
    # Average CO2 emissions per liter of gasoline burned (converted from pounds per gallon)
    CO2_per_liter = (19.6 / liters_per_gallon) * kg_per_pound  # in kg
    liters_used = km_driven / fuel_efficiency
    return liters_used * CO2_per_liter

def calculate_electricity_footprint(kwh_used):
    # Average CO2 emissions per kWh of electricity consumed
    CO2_per_kWh = 0.92 * 0.453592  # in kg (converted from pounds)
    return kwh_used * CO2_per_kWh

def calculate_waste_footprint(waste_weight):
    # Conversion factors
    kg_per_pound = 0.453592
    
    # Average CO2 emissions per ton of waste (converted from pounds per ton)
    CO2_per_ton = 1.2 * 2000 * kg_per_pound  # in kg
    return (waste_weight * kg_per_pound) / 1000 * CO2_per_ton

def main():
    print("Welcome to the Carbon Footprint Calculator!")
    
    # Input for transportation
    km_driven = float(input("Enter the number of kilometers you drive per week: "))
    fuel_efficiency = float(input("Enter your vehicle's fuel efficiency (km per liter): "))
    
    # Input for electricity
    kwh_used = float(input("Enter your monthly electricity usage (in kWh): "))
    
    # Input for waste
    waste_weight = float(input("Enter the amount of waste you produce per week (in kg): "))
    
    # Calculate footprints
    transportation_footprint = calculate_transportation_footprint(km_driven, fuel_efficiency) * 52  # annual
    electricity_footprint = calculate_electricity_footprint(kwh_used) * 12  # annual
    waste_footprint = calculate_waste_footprint(waste_weight) * 52  # annual
    
    # Total carbon footprint
    total_footprint = transportation_footprint + electricity_footprint + waste_footprint
    
    print(f"\nYour estimated annual carbon footprint is: {total_footprint:.2f} kg of CO2.")
    
if __name__ == "__main__":
    main()
