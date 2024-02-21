import requests
import threading
import time

def download(url):
    print('Парсинг...') 
    resource = requests.get(url)
    filename = ''
    url_address = str(url)
    i = len(url_address)
    while True:
        i-=1
        if url_address[i] != '/': 
            filename = url_address[i] + filename
        else: 
            break
    out = open(filename, 'wb')
    out.write(resource.content)
    out.close()
    print(f"Downloaded {url} in {time.time()-start_time:.2f} seconds")

def userInput():
    urls = []
    while True:
        print('Введите Url адрес:')
        address = input()
        if address != '0':
            urls.append(address)
        else:
            break
    return urls

if __name__ == '__main__':
    print('Многопоточный подход')
    print('Программа для парсинга файлов из URL адреса')
    print('Введите \'0\' для выхода из режима ввода')
    urls = userInput()

    threads = []
    start_time = time.time()

    print('Подготовка к многопоточному парсингу')
    for url in urls:
        thread = threading.Thread(target=download, args=[url])
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()