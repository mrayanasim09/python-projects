# This code is made by MRayan Asim
# Packages needed:
# pip install requests
import time

import requests

# Default timeout for HTTP requests (seconds)
DEFAULT_TIMEOUT = 10


def check_website_connectivity(url, timeout=DEFAULT_TIMEOUT):
    """
    Check if a website is reachable and measure response time.

    Args:
        url: The website URL to check
        timeout: Request timeout in seconds (default: 10)
    """
    try:
        start_time = time.time()
        # Always use timeout to prevent hanging requests
        response = requests.get(url, timeout=timeout)
        end_time = time.time()

        if response.status_code == 200:
            speed = end_time - start_time
            print(f"The website {url} is reachable.")
            print(f"Response time: {speed:.2f} seconds")
        else:
            print(f"Error: The website {url} returned a status code {response.status_code}.")
    except requests.Timeout:
        print(f"Error: Connection to {url} timed out after {timeout} seconds.")
    except requests.ConnectionError:
        print(f"Error: Unable to connect to the website {url}.")
    except requests.RequestException as e:
        print(f"Error: Unable to connect to the website {url}.")
        print(f"Exception: {e}")


if __name__ == "__main__":
    user_url = input("Enter the website URL: ")
    check_website_connectivity(user_url)
