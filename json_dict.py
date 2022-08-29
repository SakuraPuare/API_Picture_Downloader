import json
import pathlib
from typing import Dict, List, Union

import imagehash
from PIL import Image
from PIL import UnidentifiedImageError

from config import *


def read_info(path: pathlib.Path = info_path) -> list:
    with open(path, 'r', encoding='utf-8') as f:
        info = json.load(f)
        f.close()
        return info


def save_info(info: List[Dict[str, Union[str, int]]], path: pathlib.Path = info_path) -> None:
    with open(path, 'w', encoding='utf-8') as f:
        temp: List[Dict[str, Union[str, int]]] = []
        for i in info:
            if i not in temp:
                temp.append(i)
        json.dump(temp, f)
        f.close()
    return None


def serilize(path: pathlib.Path, url: str = api_url) -> Union[Dict, None]:
    try:
        name = path.name
        image = Image.open(path)
        dhash = str(imagehash.dhash(image))
        h, w = image.size[:2]
        return {'name': name, 'dhash': dhash,
                'height': h, 'width': w, 'url': url}
    except FileNotFoundError:
        return None
    except UnidentifiedImageError:
        path.unlink()
        return None


if __name__ == '__main__':
    pic_list = []
    if not info_path.exists():
        for i in download_path.iterdir():
            js_str = serilize(i)
            if js_str is not None:
                pic_list.append(js_str)
    else:
        info_list = read_info()
        url_list = [i['url'] for i in info_list]
        for i in url_list:
            name = download_path / str(i).split('/')[-1]
            js_str = serilize(name, str(i))
            if js_str is not None:
                pic_list.append(js_str)
        name_list = set([i.split('/')[-1] for i in url_list])
        file_list = set([i.name for i in download_path.iterdir()])
        for i in file_list - name_list:
            (download_path / i).unlink()
    save_info(pic_list)
