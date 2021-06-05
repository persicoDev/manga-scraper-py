from .file_save import file_save
from bs4 import BeautifulSoup
import requests

def get_single_page(choice, link):
    soup = BeautifulSoup(requests.get(link).content, 'html.parser')
    manga_container = soup.findAll('img', {"class": "img-fluid"})
    print(str(manga_container[1]['src']))
    if (choice == 1):
        file_save(manga_container)
