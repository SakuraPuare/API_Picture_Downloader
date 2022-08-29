import asyncio
import pathlib
from typing import Any, Dict, List, Union

import httpx
from bs4 import BeautifulSoup

import json_dict
from config import *

if not download_path.exists():
    download_path.mkdir()


def get_url_list(dom: str) -> list:
    soup = BeautifulSoup(dom, 'html.parser')
    url_list = [i.attrs['src'] for i in soup.find_all('img')]
    return url_list


async def download(url: str, path: pathlib.Path = download_path) -> None:
    name = path / url.split('/')[-1]
    if not name.exists():
        try:
            async with httpx.AsyncClient(limits=LIMITS, timeout=TIMEOUT) as client:
                res = await client.get(url)
                with open(name, "wb") as f:
                    f.write(res.content)
                    f.close()
        except httpx.ConnectTimeout:
            print(f"Connection timed out.")
            await download(url)


async def main() -> None:
    if not info_path.exists():
        info_list: List[Dict[str, Union[str, int]]] = []
    else:
        info_list = json_dict.read_info()
        print(f"Already downloaded {len(info_list)}")
    for _ in range(50):
        print(f"{_} times downloaded")
        dom = httpx.get(api_url).text
        pic_list = get_url_list(dom)

        print(f"Downloading {len(pic_list)}")
        tasks: list[asyncio.Task] = []
        for pic_url in pic_list:
            task = asyncio.create_task(download(pic_url))
            tasks.append(task)
        await asyncio.wait(tasks)

        for pic in pic_list:
            name = download_path / str(pic).split('/')[-1]
            pic_json = json_dict.serilize(name, pic)
            if pic_json is not None:
                info_list.append(pic_json)

        print(f"Downloaded {len(info_list)}")
        json_dict.save_info(info_list)

if __name__ == '__main__':
    asyncio.run(main())
