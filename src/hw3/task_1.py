import asyncio
import urllib.request
from bs4 import BeautifulSoup

directory = "homer_pictures/"
URL = "https://www.thisfuckeduphomerdoesnotexist.com/"


def save_pic_from_url(url):
    pic_name = url.split("/")[-1]
    urllib.request.urlretrieve(url, directory + pic_name)


async def download_pic():
    with urllib.request.urlopen(URL) as site:
        soup = BeautifulSoup(site, "html.parser")
        url = soup.img["src"]
        save_pic_from_url(url)


def input_number():
    print("Input the amount of homers you want to download: ")
    times = input()
    while type(times) != int:
        try:
            times = int(times)
        except ValueError:
            print("Incorrect value\n")
            times = input()
    return times


async def main():
    times = input_number()
    tasks = [asyncio.create_task(download_pic()) for _ in range(times)]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
