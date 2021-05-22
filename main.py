#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

while True:
    choice = int(input('vuoi inserire il tuo risultato in un file? (1 per sì) (2 per il no) (0 per uscire): '))
    if choice == 0:
        quit()
    link = str(input('inserisci il link: '))
    second_choice = int(input('vuoi scaricare tutto il capitolo? (1 per sì) (2 per no)'))
    soup = BeautifulSoup(requests.get(link).content, 'html.parser')
    manga_container = soup.findAll('img', {"class": "img-fluid"})
    if second_choice == 2:
        print(str(manga_container[1]['src']))
        if(choice == 1):
            file = open('link.txt', 'a')
            file.write(str(manga_container[1]['src']) + "\n")
            file.close()
    elif second_choice == 1:
        chapter_index = soup.find("option", {"value": "0"}).text
        chapter_index = str(chapter_index[2:len(str(chapter_index))])
        for i in range(int(chapter_index)):
            if i < 10:
                link = link[:-1]
                link += str(i + 1)
            if i > 10:
                link = link[:-2]
                link += str(i + 1)
            if i > 100:
                link = link[:-3]
                link += str(i + 1)
            soup = BeautifulSoup(requests.get(link).content, 'html.parser')
            manga_container = soup.findAll('img', {"class": "img-fluid"})
            print(str(manga_container[1]['src']))
            if(choice == 1):
                file = open('link.txt', 'a')
                file.write(str(manga_container[1]['src']) + "\n")
                file.close()
        