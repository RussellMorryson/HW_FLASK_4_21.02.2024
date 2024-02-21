import requests
import asyncio
import aiohttp
import time

start_time = time.time()

async def download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response = requests.get(url)
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
            out.write(response.content)
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

async def main():
    print('Асинхронный подход')
    print('Программа для парсинга файлов из URL адреса')
    print('Введите \'0\' для выхода из режима ввода')    
    urls = userInput()  
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(download(url))
        tasks.append(task)
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())