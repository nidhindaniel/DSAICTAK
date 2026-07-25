
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def get_condition_summary(avg_temp):
    if avg_temp >= 30:
        return "Hot"
    elif avg_temp >= 20:
        return "Warm / Mild"
    else:
        return "Cold"

weather_data = {
    "region": input("Enter region: "),
    "weather_type": input("Enter weather type (e.g., Sunny, Rainy, Cloudy): "),
    "temperatures": [float(input("Enter temperature 1 (°C): ")),float(input("Enter temperature 2 (°C): "))],
    "humidity": [float(input("Enter humidity 1 (%): ")),float(input("Enter humidity 2 (%): "))]}

avg_temp = calculate_average(weather_data["temperatures"])
avg_humidity = calculate_average(weather_data["humidity"])
condition = get_condition_summary(avg_temp)


print("WEATHER RESULTS")
print(f"Region: {weather_data['region']}")
print(f"Type:   {weather_data['weather_type']}")
print(f"Avg Temp:{avg_temp:.1f}°C ({condition})")
print(f"Avg Humidity:{avg_humidity:.1f}%")