def calculate_transportation_footprint(miles_driven, fuel_efficiency):
    # Average CO2 emissions per gallon of gasoline burned
    CO2_per_gallon = 19.6  # in pounds
    gallons_used = miles_driven / fuel_efficiency
    return gallons_used * CO2_per_gallon

def calculate_electricity_footprint(kwh_used):
    # Average CO2 emissions per kWh of electricity consumed
    CO2_per_kWh = 0.92  # in pounds (this can vary by region)
    return kwh_used * CO2_per_kWh

def calculate_waste_footprint(waste_weight):
    # Average CO2 emissions per ton of waste
    CO2_per_ton = 1.2 * 2000  # in pounds (1.2 tons of CO2 per ton of waste)
    return (waste_weight / 2000) * CO2_per_ton

def main():
    print("Welcome to the Carbon Footprint Calculator!")
    
    # Input for transportation
    miles_driven = float(input("Enter the number of miles you drive per week: "))
    fuel_efficiency = float(input("Enter your vehicle's fuel efficiency (miles per gallon): "))
    
    # Input for electricity
    kwh_used = float(input("Enter your monthly electricity usage (in kWh): "))
    
    # Input for waste
    waste_weight = float(input("Enter the amount of waste you produce per week (in pounds): "))
    
    # Calculate footprints
    transportation_footprint = calculate_transportation_footprint(miles_driven, fuel_efficiency) * 52  # annual
    electricity_footprint = calculate_electricity_footprint(kwh_used) * 12  # annual
    waste_footprint = calculate_waste_footprint(waste_weight) * 52  # annual
    
    # Total carbon footprint
    total_footprint = transportation_footprint + electricity_footprint + waste_footprint
    
    print(f"\nYour estimated annual carbon footprint is: {total_footprint:.2f} pounds of CO2.")
    
if __name__ == "__main__":
    main()