# Task 1: Identifying and Creating Classes Analyze the provided script and identify 
# distinct functionalities that can be encapsulated into classes. Create classes that 
# represent different aspects of the weather forecast application, such as fetching data, 
# parsing data, and user interaction.

# Problem Statement: The existing script for the weather forecast application is written 
# in a procedural style and lacks organization.

# Code Example: Before Refactoring:

# Weather Forecast Application Script

#Expected Outcome:

# Clear definitions of classes such as `WeatherDataFetcher`, `DataParser`, and `UserInterface`,
# each handling specific parts of the application.

class WeatherDataFetcher:
    def __init__(self):
        self.weather_data = {
        "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
        "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
        "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}
    }

    def fetch_weather_data(self, city):
    # Simulated function to fetch weather data for a given city
        print(f"Fetching weather data for {city}...")
        return self.weather_data.get(city, {})

class DataParser:
    def __init__(self):
        pass
        
    def parse_weather_data(self, data):
    # Function to parse weather data
        if not data:
            return "Weather data not available"
        city = data["city"]
        temperature = data["temperature"]
        condition = data["condition"]
        humidity = data["humidity"]
        return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"

class Forecast:
    def __init__(self):
        self.fetch_data = WeatherDataFetcher()
        self.data_parser = DataParser()

    def get_detailed_forecast(self, city):
    # Function to provide a detailed weather forecast for a city
        data = self.fetch_data.fetch_weather_data(city)
        return self.data_parser.parse_weather_data(data)

class UserInterface:
    def __init__(self):
        self.data_parser = DataParser()
        self.fetch_data = WeatherDataFetcher()

    def display_weather(self, city):
    # Function to display the basic weather forecast for a city
        data = self.fetch_data.fetch_weather_data(city)
        if not data:
            print(f"Weather data not available for {city}")
        else:
            weather_report = self.data_parser.parse_weather_data(data)
            print(weather_report)

ui = UserInterface()
def main():
    forecast = Forecast()
    while True:
        city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
        if city.lower() == 'exit':
            break
        detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
        if detailed == 'yes':
            forecast = forecast.get_detailed_forecast(city)
        else:
            forecast = ui.display_weather(city)
        print(forecast)

if __name__ == "__main__":
    main()