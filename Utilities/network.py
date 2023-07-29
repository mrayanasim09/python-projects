# This code is made by MRayan Asim
import subprocess
import time

print(
    "This network password teller code is made by MRayan Asim hope you will like this !😊"
)
time.sleep(3)


def get_wifi_profiles():
    try:
        # Get the Wi-Fi profiles using the 'netsh' command
        result = subprocess.run(
            ["netsh", "wlan", "show", "profiles"], capture_output=True, text=True
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


def get_wifi_password(profile):
    try:
        # Get the Wi-Fi password for a specific profile
        result = subprocess.run(
            ["netsh", "wlan", "show", "profile", profile, "key=clear"],
            capture_output=True,
            text=True,
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
        print("Error occurred:", e)
        return None


# Get Wi-Fi profiles
profiles = get_wifi_profiles()

# Print Wi-Fi names and passwords
print("{:<30} | {:<}".format("Wi-Fi Name", "Password"))
print("-----------------------------------------")
for profile in profiles:
    password = get_wifi_password(profile)
    print("{:<30} | {:<}".format(profile, password or ""))
