# this is the main file for the project and will be the entry point for the program
# this file will be responsible for running the program and calling the other files
import sys
import requests
import os
from dotenv import load_dotenv


root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__).split("src")[0]))

def main():
    # check for internet connection
    testResponse = requests.get("https://google.com")
    assert testResponse.status_code == 200 , "No internet"
    print("Internet connection found")
    # load environment variables
    load_dotenv(dotenv_path=root_dir + "/.env")
    maps_apikey = load_dotenv('GOOGLE-MAPS-API-KEY')
    api_response = requests.post('https://maps.googleapis.com/maps/api/timezone/json?location=39.6034810%2C-119.6822510&timestamp=1331161200&key={maps_apikey}')
    # assert api_response is status code 200
    assert api_response.status_code == 200, "API request failed"
    print("API key valid")

if __name__ == "__main__":
    main()