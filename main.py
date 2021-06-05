#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
from choices.single_page import get_single_page
from choices.single_chapter import get_single_chapter

if __name__ == "__main__":
    while True:
        choice = int(input('vuoi inserire il tuo risultato in un file? (1 per sì) (2 per il no) (0 per uscire): '))
        if choice == 0:
            quit()
        link = str(input('inserisci il link: '))
        second_choice = int(input('inserisci uno per scaricare una singola pagina, inserisci due per scaricare un capitolo intero 
        '))
        if second_choice == 2:
            get_single_page(link, choice)
        elif second_choice == 1:
            get_single_chapter(link, choice)