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

    # VARIABLE INPUT FROM HTML PAGE

    link_input = request.form['game']

    # ASKING FOR GAME NAME AND CREATING LINK FOR SITE SCRAPING || SITE SCRAPING

    # RESULTS

    steam_answer = "NO INFORMATION"
    gog_answer = "NO INFORMATION"
    origin_answer = "NO INFORMATION"
    epic_answer = "NO INFORMATION"
    uplay_answer = "NO INFORMATION"

    # STEAM
    query = "steam" + link_input

    list_of_sites = search(query, num_results=1, lang="en")
    steam_site = list_of_sites[0]

    page = requests.get(steam_site)
    soup = BeautifulSoup(page.content, "html.parser")
    result = soup.find("div", class_="sysreq_tabs")
    if result:
        steam_answer = "YES"
    else:
        steam_answer = "NO"

    # GOG
    query = "gog" + link_input

    list_of_sites = search(query, num_results=1, lang="en")
    steam_site = list_of_sites[0]

    page = requests.get(steam_site)
    soup = BeautifulSoup(page.content, "html.parser")
    result = soup.find("div", class_="details__content table__row-content")
    if result:
        gog_answer = "YES"
    else:
        gog_answer = "NO"

    # ORIGIN
    query = "ORIGIN" + link_input

    list_of_sites = search(query, num_results=1, lang="en")
    steam_site = list_of_sites[0]
    print(steam_site)

    page = requests.get(steam_site)
    soup = BeautifulSoup(page.content, "html.parser")
    #result = soup.body.findAll(text="Mac OS")
    result = soup.body.find("div", string="Mac")
    print(result)
    if result:
        origin_answer = "YES"
    else:
        origin_answer = "NO"

    # EPIC
    query = "EPIC GAME STORE" + link_input

    list_of_sites = search(query, num_results=1, lang="en")
    steam_site = list_of_sites[0]

    page = requests.get(steam_site)
    soup = BeautifulSoup(page.content, "html.parser")
    result = soup.find("div", class_="css-13efb1d")
    if result:
        epic_answer = "YES"
    else:
        epic_answer = "NO"

    # UPLAY
    uplay_answer = "NO"

    return render_template('result.html', steam=steam_answer, gog=gog_answer, origin=origin_answer, epic=epic_answer, uplay=uplay_answer)


if __name__ == "__main__":
    app.run()
