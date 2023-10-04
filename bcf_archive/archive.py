import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime, timedelta
from pathlib import Path


class scrape:
    def __init__(self, stream_id, stream_name, secret) -> None:
        self.id = stream_id
        self.stream_name = stream_name
        self.access = secret

    def get_archive_ids(self, date):
        try:
            URL = f"https://m.broadcastify.com/archives/ajax.php?feedId={self.id}&date={date}&_=1664130786431"
            page = requests.get(URL, cookies=self.access)
            soup = BeautifulSoup(page.content, "lxml")
            # print(soup)
            ids = soup.find("p").getText()
            searchable_ids = json.loads(ids)
            searchable_ids = searchable_ids["data"]
            return searchable_ids
        except:
            return {}

    def get_audio_url(self, id):
        URL = f"https://m.broadcastify.com/archives/idv2/{id}"
        try:
            page = requests.get(URL, cookies=self.access)
            soup = BeautifulSoup(page.content, "lxml")
            ids = soup.find("audio")
            url = ids.attrs["src"]
            return url
        except:
            return ""

    def get_audio(self, audio_url, file_name):
        try:
            r = requests.get(audio_url, cookies=self.access)
            with open(file_name, "wb") as writer:
                writer.write(r.content)
        except:
            return ""

    def get_id_audio(self, days_ago, folder):
        for day in range((days_ago), 0, -1):
            # print(day)

            working_date = datetime.now() - timedelta(days=day)

            filename_date = working_date.strftime("%Y_%m_%d")
            url_date = working_date.strftime("%m/%d/%Y")
            print(f"Getting audio for {self.stream_name} on {filename_date}")
            ids = self.get_archive_ids(url_date)
            if ids == {}:
                break

            count = 0
            for id in ids:
                day_folder = Path(folder, self.id, filename_date)
                day_folder.mkdir(parents=True, exist_ok=True)
                file_name = f"{filename_date}_{self.id}_{count}.mp3"
                file_path = Path(day_folder, file_name)
                audio_url = self.get_audio_url(id[0])
                if audio_url == "":
                    break
                self.get_audio(audio_url, file_path)
                count += 1

    def get_stream_ids(audio_type):
        id_data = {"archives": []}
        countTotal = 0

        for x in range(0, 51):
            URL = (
                "https://www.broadcastify.com/listen/stid/" + str(x) + "/" + audio_type
            )
            page = requests.get(URL)
            soup = BeautifulSoup(page.content, "html.parser")
            divs = soup.findAll("table", {"class": "btable"})
            for div in divs:
                rows = div.findAll("tr")
                for row in rows:
                    statusData = row.findAll("td", {"class": "online"})
                    for status in statusData:
                        online = status.get_text()
                        if online == "Online":
                            idData = row.findAll("td", {"class": "w1p"})
                            for id in idData:
                                links = id.findAll("a")
                                for link in links:
                                    link_url = link["href"]
                                    just_id = link_url.split("/")[-1]
                                    text = link.get_text()
                                    id_data["archives"].append(
                                        {"name": text, "id": just_id}
                                    )
            countTotal = countTotal + 1
        return id_data
