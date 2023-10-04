# bcf_archive
Broadcastify archive interface library


Hello, this is a project that I built as part of my capstone project.

This was created to scrape over 1.5 Tb of audio files that I could then use for the classification and transcription of.

My one note is that you need to pay the like 5 dollars for 3 months to get a vailid cookie that you can use. 

## Example


```python
from bcf_archive.archive import scrape
from pathlib import Path

import json

cookie = json.load(open("secret.json", "r"))
vailid_use = scrape(secret=cookie["secret"])
streams = vailid_use.get_stream_ids("marine")["archives"]
# print(len(streams))
for each_stream in streams:
    print(each_stream)
```