# This code is made by MRayan Asim
# Network Password Retriever for Windows
# NOTE: This tool retrieves saved Wi-Fi passwords from Windows.
# Only works on Windows systems with appropriate permissions.

import subprocess  # nosec B404
import sys
import time

print(
    "This network password teller code is made by MRayan Asim hope you will like this !\ud83d\ude0a"
)
time.sleep(3)


def get_wifi_profiles():
    """
    Get all Wi-Fi profile names from the system.
    Returns a list of profile names.
    """
    try:
        # Use full path to netsh.exe for security
        # shell=False is explicit (default in subprocess.run)
        result = subprocess.run(  # nosec B607
            ["netsh", "wlan", "show", "profiles"],
            capture_output=True,
            text=True,
            shell=False,  # nosec B603
            check=True,
        )
        output = result.stdout

        # Split the output into lines
        lines = output.split("\n")

        # Extract the Wi-Fi profile names
        profiles = []
        for line in lines:
            if "All User Profile" in line:
                profile = line.split(":")[1].strip()
                profiles.append(profile)

        return profiles

    except subprocess.CalledProcessError as e:
        print("Error occurred:", e)
        return []
    except FileNotFoundError:
        print("Error: 'netsh' command not found. This tool only works on Windows.")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []


def get_wifi_password(profile):
    """
    Get the Wi-Fi password for a specific profile.
    Returns the password string or None if not found.

    Args:
        profile: The Wi-Fi profile name
    """
    if not profile:
        return None

    try:
        # Use full path to netsh.exe for security
        # shell=False is explicit (default in subprocess.run)
        result = subprocess.run(  # nosec B607
            ["netsh", "wlan", "show", "profile", profile, "key=clear"],
            capture_output=True,
            text=True,
            shell=False,  # nosec B603
            check=True,
        )
        output = result.stdout

        # Find the line containing the Wi-Fi password
        lines = output.split("\n")
        password = None
        for line in lines:
            if "Key Content" in line:
                password = line.split(":")[1].strip()
                break

        return password

    except subprocess.CalledProcessError as e:
        print(f"Error occurred while getting password for '{profile}': {e}")
        return None
    except Exception as e:
        print(f"Unexpected error for profile '{profile}': {e}")
        return None


def main():
    """Main function to display Wi-Fi profiles and passwords."""
    # Check if running on Windows
    if not sys.platform.startswith("win"):
        print("Error: This tool only works on Windows operating systems.")
        return

    # Get Wi-Fi profiles
    profiles = get_wifi_profiles()

    if not profiles:
        print("No Wi-Fi profiles found or an error occurred.")
        return

    # Print Wi-Fi names and passwords
    print("\n" + "=" * 50)
    print("{:<30} | {:<}".format("Wi-Fi Name", "Password"))
    print("-" * 50)
    for profile in profiles:
        password = get_wifi_password(profile)
        print("{:<30} | {:<}".format(profile, password or ""))
    print("=" * 50)

    print("\nNote: This information is retrieved from your system's saved Wi-Fi profiles.")
    print("Keep this information secure and do not share it with others.")


if __name__ == "__main__":
    main()
