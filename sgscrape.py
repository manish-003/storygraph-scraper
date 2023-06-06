import requests
from bs4 import BeautifulSoup


def search(bookname,lim=1):
    url = f"https://app.thestorygraph.com/browse?search_term={bookname}"
    ol=[]
    sp = requests.get(url).content
    soup = BeautifulSoup(sp, 'lxml')
    divi = soup.find_all('div', class_ = 'book-pane-content',limit = 2*int(lim))
    for i in divi[::2]:
        img = i.find('img').get('src')
        i= i.find('div', class_ = 'book-title-author-and-series')
        bli = i.find('a')
        bname = bli.text
        aname = i.find('p','font-body').text.strip()
        try:
            seriesname = i.find('p','font-semibold').text
        except:
            seriesname = 'N/A'
        burl = 'https://app.thestorygraph.com' + bli.get('href')
        ol.append((bname,seriesname,aname,img,burl))
    return ol

def peek(bookname):
    url = f"https://app.thestorygraph.com/browse?search_term={bookname}"
    sp = requests.get(url).content
    soup = BeautifulSoup(sp, 'lxml')
    divi = soup.find('div', class_ = 'book-pane-content')
    img = divi.find('img').get('src')
    divi = divi.find('div', class_ = 'book-title-author-and-series')
    bli = divi.find('a')
    bname = bli.text
    aname = divi.find('p','font-body').text.strip()
    try:
        seriesname = divi.find('p','font-semibold').text
    except:
        seriesname = 'N/A'
    burl = 'https://app.thestorygraph.com' + bli.get('href')
    return (bname,seriesname,aname,img,burl)


if __name__ == '__main__':
    #print(search(input(),input()))
    print(peek(input()))
