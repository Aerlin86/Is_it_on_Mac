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

    pp = request.form['game']

    # ASKING FOR GAME NAME AND CREATING LINK FOR SITE SCRAPING

    link_input = pp
    query = "steam" + link_input

    list_of_sites = search(query, num_results=1, lang="en")
    steam_site = list_of_sites[0]

    # SITE SCRAPING

    page = requests.get(steam_site)
    soup = BeautifulSoup(page.content, "html.parser")
    result = soup.find("div", class_="sysreq_tabs")
    if result:
        return render_template("yes.html", game=request.form['game'])
    return render_template("no.html", game=request.form['game'])


if __name__ == "__main__":
    app.run()
