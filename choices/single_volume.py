from bs4 import BeautifulSoup
import requests

def get_single_volume(link, chioce):
    try:
        link = link.split("/")
        i = 0
        new_link = ''
        for i in range(6):
            new_link += str(link[i])
            new_link += '/'
        print(str(new_link))
        soup = BeautifulSoup(requests.get(new_link).content, 'html.parser')
        file = open('link.txt', 'a')
        file.write(soup)
        file.close()
    except:
        print('-errore-')
    volume_choice = int(input('inserisci il numero del volume che si vuole scaricare: '))


