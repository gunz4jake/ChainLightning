from bs4 import BeautifulSoup
import requests



UserSearchTerm = input('Enter search criteria: ')

def scraper(term, URL, URL_search):
    r = requests.get(URL_search + term)
    soup = BeautifulSoup(r.text, 'html.parser')
    #The below line will need to be changed to mirror a text file on the users system
    #This will be updated to form a general use case in the future
    #This line will needed to be altered in multiple places in this script
    with open('/home/marketechbarry/Python/Projects/links.txt', 'w') as f:
        for link in soup.find_all('a'):
            f.write(link.get('href'))
            f.write('\n')
        f.close()

def LSJ():
    print('Lansing State Journal results below: ')
    print()
    URL_search = 'https://www.lansingstatejournal.com/search/?q='
    URL = 'https://www.lansingstatejournal.com'
    scraper(UserSearchTerm, URL, URL_search)
    with open('/home/marketechbarry/Python/Projects/links.txt', 'r+') as f:
        total = []
        for line in f.readlines():
            if '/story' in line and len(line) >= 50:
                total.append(line.rstrip('\n'))
        x = list(set(total))
        for entry in x:
            r = requests.get(URL + entry)
            soup = BeautifulSoup(r.text, 'html.parser')
            print('*' * 50)
            print(soup.title.string)
            print('URL: ' + URL + entry)

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
        for y in total:
            if 'gannett'in y:
                total.remove(y)
            elif '//profile' in y:
                total.remove(y)
        x = list(set(total))
        for entry in x:
            if len(entry) >= 50:
                r = requests.get(entry)
                soup = BeautifulSoup(r.text, 'html.parser')
                print('*' * 50)
                print(soup.title.string)
                print('URL: ' + entry)
WLNS()
LSJ()
                
