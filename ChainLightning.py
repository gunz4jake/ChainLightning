from bs4 import BeautifulSoup
import requests



UserSearchTerm = 'andy schor'
#input('Enter search criteria')

def scraper(term, URL, URL_search):
    r = requests.get(URL_search + term)
    soup = BeautifulSoup(r.text, 'html.parser')
    with open('/home/marketechbarry/Python/Projects/links.txt', 'w') as f:
        for link in soup.find_all('a'):
            f.write(link.get('href'))
            f.write('\n')
        f.close()
def scanner(URL):
    with open('/home/marketechbarry/Python/Projects/links.txt', 'r') as f:
        for line in f.readlines():
            if '/news' in line:
                combine = URL + line
                r = requests.get(combine)
                soup = BeautifulSoup(r.text, 'html.parser')
                print('*' * 50)
                print(soup.title.string)
                print('URL: ' + combine)
def LSJ():
    print('Lansing State Journal results below: ')
    print()
    URL_search = 'https://www.lansingstatejournal.com/search/?q='
    URL = 'https://www.lansingstatejournal.com'
    scraper(UserSearchTerm, URL, URL_search)
    scanner(URL)

def WLNS():
    print('WLNS results below: ')
    print()
    URL_search = 'https://www.wlns.com/?s=' + UserSearchTerm + '&submit=Search&orderby=relevance'
    URL = 'https://www.wlns.com/'
    scraper(UserSearchTerm, URL, URL_search)
    with open('/home/marketechbarry/Python/Projects/links.txt', 'r+') as f:
        total = []
        for line in f.readlines():
            if '/news' in line and len(line) >= 50:
                total.append(line.rstrip('\n'))
        x = list(set(total))
        for entry in x:
            r = requests.get(entry)
            soup = BeautifulSoup(r.text, 'html.parser')
            print('*' * 50)
            print(soup.title.string)
            print('URL: ' + line)

        
WLNS()
LSJ()


        
   



        
                