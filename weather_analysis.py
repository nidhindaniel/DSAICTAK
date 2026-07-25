# --- FUNCTIONS ---

def calculate_average(data_list):
    """Calculates average from a list of numbers."""
    return sum(data_list) / len(data_list) if data_list else 0.0


def determine_weather_summary(avg_temp, avg_humidity, weather_type):
    """Uses conditional statements to assess overall severity/conditions."""
    if "rain" in weather_type.lower() and avg_humidity > 80:
        return f"{weather_type} (Heavy Downpour Risk ⛈️)"
    elif avg_temp >= 30.0:
        return f"{weather_type} (Hot Weather Alert 🥵)"
    elif avg_temp <= 0.0:
        return f"{weather_type} (Freezing Conditions 🥶)"
    else:
        return f"{weather_type} (Moderate Conditions 🌤️)"


def print_weather_report(weather_dict):
    """Calculates statistics from the weather dictionary and displays results."""
    # Calculating averages using functions
    avg_temp = calculate_average(weather_dict["temperatures"])
    avg_humidity = calculate_average(weather_dict["humidity_levels"])
    
    # Determining condition note using conditional logic
    condition_summary = determine_weather_summary(
        avg_temp, avg_humidity, weather_dict["weather_type"]
    )
    
    # Displaying results
    print("\n" + "=" * 45)
    print(f"  WEATHER REPORT: {weather_dict['region'].upper()}")
    print("=" * 45)
    print(f"• Custom Weather Type: {weather_dict['weather_type']}")
    print(f"• Average Temperature: {avg_temp:.1f}°C")
    print(f"• Average Humidity:    {avg_humidity:.1f}%")
    print(f"• Analysis Summary:    {condition_summary}")
    print("=" * 45)


# --- MAIN PROGRAM / USER INPUT ---

# 1. Initialize empty dictionary to hold weather data
weather_data = {}

# 2. Get custom inputs from the user
weather_data["region"] = input("Enter the Region Name: ").strip()
weather_data["weather_type"] = input("Enter Custom Weather Type (e.g., Rainy, Hazy, Stormy): ").strip()

# 3. Collect temperature readings (List of floats)
print("\nEnter 3 Temperature readings (°C):")
weather_data["temperatures"] = [
    float(input("  Reading 1: ")),
    float(input("  Reading 2: ")),
    float(input("  Reading 3: "))
]

# 4. Collect humidity readings (List of floats)
print("\nEnter 3 Humidity readings (%):")
weather_data["humidity_levels"] = [
    float(input("  Reading 1: ")),
    float(input("  Reading 2: ")),
    float(input("  Reading 3: "))
]

# 5. Run the analyzer function passing the dictionary
print_weather_report(weather_data)