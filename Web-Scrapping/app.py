import requests
from bs4 import BeautifulSoup
import threading
import time


urls = ['https://www.google.in','https://www.coursera.org/en-IN']


def get_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print("Title of the page: ", soup.title.string)

threads = []

start_time = time.time()

for url in urls:
    thread = threading.Thread(target=get_data, args=(url,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print()

print("Time taken: ", time.time() - start_time)

