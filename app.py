try:
    from googlesearch import search
    import requests
    from bs4 import BeautifulSoup
    from flask import Flask, request, render_template
except ImportError:
    print("You have to install some of the modules")

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def home():
    return render_template("index.html")


@app.route('/hello', methods=['POST', 'GET'])
def hello():

    # STANDARD ANSWERS
    steam_answer = "NO"
    gog_answer = "NO"
    now_answer = "NO"
    epic_answer = "NO"
    uplay_answer = "NO"

    # VARIABLE INPUT FROM HTML PAGE

    link_input = request.form['game']

    # =========================
    # SITE SCRAPING STARTS HERE
    # =========================

    # STEAM
    query = "steam" + link_input

    list_of_sites = search(query, num_results=0, lang="en")
    steam_site = list_of_sites[0]

    page = requests.get(steam_site)
    soup = BeautifulSoup(page.content, "html.parser")
    result = soup.find("div", class_="sysreq_tabs")
    if result:
        steam_answer = "YES"

    # GOG
    query = "gog" + link_input

    list_of_sites = search(query, num_results=0, lang="en")
    gog_site = list_of_sites[0]
    print(gog_site)

    page = requests.get(gog_site)
    soup = BeautifulSoup(page.content, "html.parser")
    result = soup.find("svg", class_="ic-svg productcard-os-support__system productcard-os-support__system--osx")
    print(result)
    if result:
        gog_answer = "YES"

    # NOW
    now_site = "https://www.nvidia.com/pl-pl/geforce-now/games/"

    page = requests.get(now_site)
    soup = BeautifulSoup(page.content, "html.parser")

    child_soup = soup.find_all('span')
    # print(child_soup)
    for i in child_soup:
        if (i == link_input):
            print(i)

    # EPIC
    query = "EPIC GAME STORE" + link_input

    list_of_sites = search(query, num_results=0, lang="en")
    epic_site = list_of_sites[0]

    page = requests.get(epic_site)
    soup = BeautifulSoup(page.content, "html.parser")
    result = soup.find("div", class_="css-13efb1d")
    if result:
        epic_answer = "YES"

    return render_template('result.html', steam=steam_answer, gog=gog_answer, now=now_answer, epic=epic_answer, uplay=uplay_answer)


if __name__ == "__main__":
    app.run()
