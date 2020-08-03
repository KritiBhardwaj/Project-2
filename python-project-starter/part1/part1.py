import json
from datetime import datetime

with open("data/forecast_5days_a.json") as file:
    data = json.load(file)

numberOfDays = 0
for day in data["DailyForecasts"]:
    numberOfDays +=1
    date = day['Date']
    minTemp = day["Temperature"]["Minimum"]["Value"]
    maxTemp = day["Temperature"]["Maximum"]["Value"]
    dayDesc = day["Day"]["LongPhrase"]
    dayRainProb = day["Day"]["RainProbability"]
    nightDesc = day["Night"]["LongPhrase"]
    nightRainProb = day["Night"]["RainProbability"]
    print(f"Min: {minTemp}F")
    print(f"Max: {maxTemp}F")
    print(f"Day: {dayDesc}")
    print(f"DayRain: {dayRainProb}%")
    print(f"nightDesc: {nightDesc}")
    print(f"nightRain: {nightRainProb}")
    print("-----------------------------")



DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees and celcius symbols.
    
    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"

def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.
    
    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year
    """
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime("%A %d %B %Y")


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius

    Args:
        temp_in_farenheit: integer representing a temperature.
    Returns:
        An integer representing a temperature in degrees celcius.
    """
    temp_in_farenheit = float(temp_in_farenheit)
    temp_in_celcius = round((temp_in_farenheit - 32) * (5/9),1)
    return temp_in_celcius


def calculate_mean(total, num_items):
    """Calculates the mean.
    
    Args:
        total: integer representing the sum of the numbers.
        num_items: integer representing the number of items counted.
    Returns:
        An integer representing the mean of the numbers.
    """
    mean = float(total)/(num_items)
    return mean


def process_weather(forecast_file):
    """Converts raw weather data into meaningful text.

    Args:
        forecast_file: A string representing the file path to a file
            containing raw weather data.
    Returns:
        A string containing the processed and formatted weather data.
    """
    pass


# if __name__ == "__main__":
#     print(process_weather("data/forecast_5days_a.json"))





