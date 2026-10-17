weather_data ={}
weather_data["region"]=str(input("Enter the Region Name :"))
weather_data["type_of_weather"] = input("Enter the Weather Type ( Sunny, Rainy, windy etc)")
print("\nEnter 3 Temperature readings (°C):")
weather_data["temperatures"] = [float(input("Reading 1: ")),float(input("Reading 2: ")),float(input("Reading 3: "))]
print("\nEnter 3 Humidity readings (%):")
weather_data["humidity_levels"] = [float(input("Reading 1: ")),float(input("Reading 2: ")),float(input("Reading 3: "))]

def weather_analysis(avg_temp, avg_humidity):
    