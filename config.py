import pathlib
from typing import Union

import httpx

TIMEOUT = 30
LIMITS = httpx.Limits(max_keepalive_connections=10, max_connections=20)

info_path = pathlib.Path('info.json')
download_path = pathlib.Path('download')
api_url = "https://mirlkoi.ifast3.vipnps.vip/Tag/Random/mobile.php"
