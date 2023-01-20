"""
This python program tries to get the entire article from a given url and prints that in the console.
It uses requests and beautifulsoup modules for this purpose.

⚠️ --DISCLAIMER --
This program may not work on all the websites as some websites might ban the use of these modules to
scrap their content and also scraping might be illegal and this program is only built for educational
purposes and you hold the responsibility of using it. Use it carefully!
"""
import requests
from bs4 import BeautifulSoup

# Terminal Colors
CRED = '\033[91m' # Red color is for the headings!
CYELLOW = '\33[33m' # Yellow color is for the paragraphs!
CGREENBG  = '\33[42m' # Green Background Color!
CEND = '\033[0m'


def getHtmlFile(url):
    req = requests.get(url)
    return req.text # this will return entire HTML document


def getArticleData():
    print("\n"+CGREENBG + "Python Article Scraper" + CEND+"\n")
    input_url = input("Paste a url: ")
    soup = BeautifulSoup(getHtmlFile(input_url),'html.parser')
    for headers in soup.find_all(['h1','h2','h3','h4']):
        print(CRED +headers.get_text()+ CEND + '\n')
        for element in headers.next_elements:
            if element.name and element.name.startswith('h'):
                break
            if element.name == 'footer' or element.name == 'nav' or element.name == 'form':
                break
            if element.name == 'p':
                print(CYELLOW +element.get_text()+ CEND + '\n')

while True:
    getArticleData()
    choice = input("Do you want to use another link ? (y/n): ")
    if choice == "y":
        continue
    elif choice == "n":
        break
    else:
        print(CRED + "Invalid Selector, Exiting the program..." + CEND)
        break