import re
import requests
import urllib3
from bs4 import BeautifulSoup, SoupStrainer

def collectSubLinks(url):
    page = requests.get(url)    
    data = page.text
    soup = BeautifulSoup(data)

    links = []

    for link in soup.find_all('a'):
        links.append(link.get('href'))
        
    love_letter_links = []
    for i in range (21,111):
        love_letter_links.append(links[i])
    
    return love_letter_links

def textCollect(love_letter_links):
    for i in range(len(love_letter_links)):
        url = love_letter_links[i]

        req = urllib3.PoolManager()
        res = req.request('GET',url)
        soup = BeautifulSoup(res.data,'html.parser')

        content = soup.find(attrs={'class':'paracontent'}).find_all('p')
    return content


def textRangeSelector(content):
    final_text = ''
    
    for i in range(3):
        print(i)
        print(content[i])
        print()

    print('Enter range to parse: ')

    a = input('Enter lower limit')
    b = input('Enter one more than upper limit')

    text = ''

    for i in range(a,b):
        text += str(content[i])
    print(text)

    soup = BeautifulSoup(text)
    final_text += str(soup.get_text())

    return final_text

def main():
    url = "https://theromantic.com/LoveLetters/main.htm"
    love_letter_links = collectSubLinks(url)
    content = textCollect(love_letter_links)
    text = textRangeSelector(content)
    text_file = open('scraped_letters.txt','wt')
    n = text_file.write(text)
    text_file.close()
    print(n)

if __name__ == "__main__":
    main()