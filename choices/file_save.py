def file_save(soup):
    file = open('link.txt', 'a')
    file.write(soup)
    file.close()