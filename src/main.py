# this is the main file for the project and will be the entry point for the program
# this file will be responsible for running the program and calling the other files
import sys
import requests
import os
from dotenv import load_dotenv


root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__).split("src")[0]))

def main():
    # check for internet connection
    try:
        testResponse = requests.get("https://google.com")
        assert testResponse.status_code == 200
        print("Internet connection found")
    except:
        print("No internet connection")
        sys.exit(1)
    # load environment variables
    load_dotenv(dotenv_path=root_dir + "/.env")
    # check for api keys
    

if __name__ == "__main__":
    main()