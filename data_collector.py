import re
import requests
import urllib3
from os import system
from bs4 import BeautifulSoup, SoupStrainer

def collectSubLinks(url):
    page = requests.get(url)    
    data = page.text
    soup = BeautifulSoup(data,features='lxml')

    links = []
    print('Collecting urls...')
    for link in soup.find_all('a'):
        links.append(link.get('href'))
        
    love_letter_links = []
    for i in range (21,111):
        love_letter_links.append(links[i])
    print('Final love letter links collected!')
    return love_letter_links

def textCollect(love_letter_links):
    print('Collecting content from links...')
    content = []
    for i in range(len(love_letter_links)):
        print('Collecting letter '+str(i))
        print(' ')
        url = love_letter_links[i]
        
        req = urllib3.PoolManager()
        res = req.request('GET',url)
        soup = BeautifulSoup(res.data,'html.parser')

        content.append(soup.find(attrs={'class':'paracontent'}).find_all('p'))
    print('All text collected!')
    return content


def textRangeSelector(content):
   final_text = ''
   for i in range(3):
       print(i)
       for j in range(len(content[i])):
           print(j)
           print(content[i][j])
           print()
       print('Enter range to parse')
       a = int(input('Enter lower limit'))
       b = int(input('Enter one more than upper limit'))

       text = ''

       for j in range(a,b):           
           text += str(content[i][j])
       
       soup = BeautifulSoup(text)
       final_text += str(soup.get_text())
       final_text += "\n\n"
       system('clear')
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