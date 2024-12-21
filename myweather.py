import requests


# Step 1: Define the function to fetch weather details from OpenWeather API.
def get_weather(city, api_key):
    """
    Fetches weather details for the given city using OpenWeather API.

    Args:
        city (str): The name of the city to get weather for.
        api_key (str): Your OpenWeather API key.

    Returns:
        dict: A dictionary containing temperature, condition, humidity, and wind speed if successful.
        None: If an error occurs during the API request.
    """
    # TODO: Define the base URL for the OpenWeather API.
base_url = "https://api.openweathermap.org/data/2.5/"
    # TODO: Define the parameters for the API request, including city and API key.

    # TODO: Send a GET request to the OpenWeather API using the defined parameters.

    # TODO: Make the API request and check if the response code is 200.
    if response.status_code == 200:
        # TODO: Parse the JSON response.

        # TODO: Extract relevant weather information from the response.

        return weather
    else:
        return None


# Step 2: Define the function to display weather information.
def display_weather(city, weather):
    """
    Displays weather information for the given city.

    Args:
        city (str): The name of the city.
        weather (dict): A dictionary containing weather details.
    """
    if weather:
        # TODO: Print weather details (temperature, condition, humidity, wind speed).


    else:
        # TODO: Print a message indicating no weather data is available.



# Step 3: Define the main function to interact with the user.
def main():
    """
    Main function to interact with the user.
    """
    # TODO: Replace with your OpenWeather API key.
    api_key = "YOUR_API_KEY"

    while True:
        print("\nWeather Report Application")
        print("1. Get weather information")
        print("2. Exit")

        # TODO: Get user choice.



        if choice == "1":
            # TODO: Get city name from the user.


            # TODO: Fetch weather information using the get_weather function.



            # TODO: Display the fetched weather information.


        elif choice == "2":
            # TODO: Print exiting message and break the loop.


        else:
            # TODO: Handle invalid user choice.



# Step 4: Call the main function to start the application.
main()
