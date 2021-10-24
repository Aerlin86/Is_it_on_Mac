# code to search steam store for given game title
try:
    from googlesearch import search
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("You have to install some of the modules")

# ASKING FOR GAME NAME AND CREATING LINK FOR SITE SCRAPING


link_input = input("Tell me, what game title do you looking for: ")
query = "steam" + link_input

list_of_sites = search(query, num_results=1, lang="en")
steam_site = list_of_sites[0]

# SITE SCRAPING

page = requests.get(steam_site)
soup = BeautifulSoup(page.content, "html.parser")
result = soup.find("div", class_="sysreq_tabs")
if result:
    print("SUCCESS")
else:
    print("FAILURE")
