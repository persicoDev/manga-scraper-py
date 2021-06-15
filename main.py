# !/usr/bin/env python
# -*- coding: utf-8 -*-
from choices import single_page, single_chapter, single_manga

if __name__ == "__main__":
    while True:
        try:
            choice = int(input('vuoi inserire il tuo risultato in un file? (1 per sì) (2 per il no) (0 per uscire): '))
            if choice == 0:
                quit()
            link = str(input('inserisci il link: '))
            second_choice = int(input('inserisci uno per scaricare una singola pagina, inserisci due per scaricare un capitolo intero, inserisci 3 per scaricare il manga intero: '))
            if second_choice == 1:
                single_page.get_single_page(link, choice)
            elif second_choice == 2:
                single_chapter.get_single_chapter(link, choice)     
            elif second_choice == 3:
                single_manga.get_single_manga(link, choice)
        except:
            print('error')