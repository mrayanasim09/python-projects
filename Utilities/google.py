# This code is made by MRayan Asim
# Packages needed:
# pip install beautifulsoup4
from googlesearch import search

query = input("Search: ")
for j in search(query, tld="co.in", num=10, stop=10, pause=2):
    print(j)
