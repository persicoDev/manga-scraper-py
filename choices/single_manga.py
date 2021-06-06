from .single_chapter import get_single_chapter
from bs4 import BeautifulSoup
import requests
import re

def get_single_manga(link, choice):
    # try:
    link = link.split("/")
    i = 0
    new_link = ''
    for i in range(6):
        new_link += str(link[i])
        new_link += '/'
    link = new_link
    soup = BeautifulSoup(requests.get(link).content, 'html.parser')
    volume_number = str(soup.find('p', class_='volume-name d-inline'))
    new_volume_number = [float(i) for i in re.findall(r'-?\d+\.?\d*', volume_number)]
    new_volume_number = int(new_volume_number[0])
    all_volumes = soup.find_all('a', class_='chap')
    for chapter in range(int(len(all_volumes))):
        # print()
        link = all_volumes[chapter]['href']
        link += "/1"
        file = open('link.txt', 'a')
        file.write(str(new_volume_number) + "\n")
        file.close()
        new_volume_number = new_volume_number -1
        get_single_chapter(link, choice)
    # except: 
    #     print('-errore-')
