import requests
from bs4 import BeautifulSoup
from bcf_archive.archive import scrape
from pathlib import Path

import json

cookie = json.load("secret.json")
already_done = []

streams = scrape.get_stream_ids('marine')["ids"]
for each_stream in streams:
    if each_stream not in already_done:
        id_handler = scrape(each_stream, each_stream, cookie)