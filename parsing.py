from bs4 import BeautifulSoup
import requests


url = 'https://studynow.ru/dicta/allwords'
index =[]
en_w = []
rus_w = []
w_link = []
def parsing():
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html,"lxml")
    words = soup.find_all('table', id='wordlist')
    for word in words:
        word_row = word.find_all('td')
        n = 0
        while n < len(word_row):
            try:
                b = word_row[n].text
                index.append(b)
                d = word_row[n+1].text
                en_w.append(d)
                g = word_row[n+2].text
                rus_w.append(g)
                n += 3
                sep = " ("
                d_r = d.split(sep, 1)[0]
                d_str = d_r.replace(" ", "%20")
                l = f"https://britlex.ru/mp3/{d_str}.mp3"
                w_link.append(l)
            except:
                break
    return
