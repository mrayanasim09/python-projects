# This code is made by MRayan Asim
# Packages needed:
# pip install requests
import requests
import time


def check_website_connectivity(url):
    try:
        start_time = time.time()
        response = requests.get(url)
        end_time = time.time()

        if response.status_code == 200:
            speed = end_time - start_time
            print(f"The website {url} is reachable.")
            print(f"Response time: {speed:.2f} seconds")
        else:
            print(
                f"Error: The website {url} returned a status code {response.status_code}."
            )
    except requests.RequestException as e:
        print(f"Error: Unable to connect to the website {url}.")
        print(f"Exception: {e}")


if __name__ == "__main__":
    user_url = input("Enter the website URL: ")
    check_website_connectivity(user_url)
