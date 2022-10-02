from bcf_archive.archive import scrape
from pathlib import Path

import json

cookie = json.load(open("secret.json", 'r'))

streams = scrape.get_stream_ids('marine')['archives']
# print(len(streams))
for each_stream in streams:
    print(each_stream)