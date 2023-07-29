# This program is made by MRayan Asim
# Packages needed:
# pip install instaloader
import instaloader

# Create an instance of Instaloader class
bot = instaloader.Instaloader()

username = input("Enter the user name: ")
# Load a profile from an Instagram handle
profile = instaloader.Profile.from_username(bot.context, username)

print("Username: ", profile.username)
print("User ID: ", profile.userid)
print("Number of Posts: ", profile.mediacount)
print("Followers: ", profile.followers)
print("Followees: ", profile.followees)
print("Bio: ", profile.biography, profile.external_url)
