import requests
from bs4 import BeautifulSoup
from bcf_archive.archive import scrape
from pathlib import Path

import json

# print(len(id_arr))

# data_folder = Path("/mnt/md0/nlp_capstone/second_audioFiles")
# data_folder.mkdir(parents=True, exist_ok=True)


cookie = json.load("secret.json")
already_done = []

streams = scrape.get_stream_ids('marine')["ids"]
print(streams)
# streams = ["35683", "32260", "28171", "26383"]
for each_stream in streams:
    if each_stream not in already_done:
        # print(each_stream)
        # if each_stream["id"] in ["22612", "22851", "23761", "26383", "28171", "31444"]:
        #     continue
        # print(each_stream["id"])
        # id_handler = scrape_archive(each_stream["id"], each_stream['name'], cookie)
        id_handler = scrape(each_stream, each_stream, cookie)
        # print(id_handler)
        # id_handler.get_id_audio(361, data_folder)
        # already_done.append(each_stream)