import requests
from requests_oauthlib import OAuth1
import os


class IconSaver:
    def __init__(self):
        self._auth = OAuth1(os.getenv("KEY"), os.getenv("SECRET"))
        self._base_url = "http://api.thenounproject.com/icon/"
        self._id_icon = 1

    def get_icon(self, id_icon):
        self._id_icon = id_icon
        try:
            url_icon = self._get_icon_url()
            icon_data = self._get_icon_data(url_icon)
            self._save_icon(icon_data)
        except Exception:  # TODO
            pass

    def _get_icon_url(self):
        endpoint = self._base_url + str(self._id_icon)
        response = requests.get(endpoint, auth=self._auth)
        res = response.json()
        return res["icon"]["icon_url"]

    def _get_icon_data(self, url_icon):
        response_icon = requests.get(url_icon)
        return response_icon.content

    def _save_icon(self, icon_data):
        with open(f"icons/{self._id_icon}.svg", "wb") as icon_file:
            icon_file.write(icon_data)


icon_saver = IconSaver()
icon_saver.get_icon("water")