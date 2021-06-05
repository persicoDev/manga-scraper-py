def file_save(manga_container):
    file = open('link.txt', 'a')
    file.write(str(manga_container[1]['src']) + "\n")
    file.close()