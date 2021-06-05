from .single_chapter import get_single_chapter
from bs4 import BeautifulSoup
import requests

def get_single_manga(link, choice):
    try:
        link = link.split("/")
        i = 0
        new_link = ''
        for i in range(6):
            new_link += str(link[i])
            new_link += '/'
        link = new_link
        soup = BeautifulSoup(requests.get(link).content, 'html.parser')
        all_volumes = soup.find('a', class_='chap')
        for chapter in all_volumes:
            link = all_volumes['href']
            link += "/1"
            get_single_chapter(link, choice)
    except:
        print('-errore-')
