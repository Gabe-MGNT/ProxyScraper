import json
import random
import re
import sys
from threading import Thread

import requests
from bs4 import BeautifulSoup

class UserAgentsScraper:
    def __init__(self):
        self.list_userAgent = []
        self.regex = r"(.+?)[/][\d.].+(.+?)"

    def _get_user_agent(self, url):
        r = requests.get(url).content
        soup = BeautifulSoup(r, "html.parser")
        td_elements = soup.find_all("td")
        li_elements = soup.find_all("li")
        for element in td_elements + li_elements:
            user_agent = element.text
            if re.match(self.regex, user_agent):
                self.list_userAgent.append(user_agent)

    def from_url_list(self, url_list):
        self.list_userAgent = []

        for url in url_list:
            self._get_user_agent(url)

    def get_list(self):
        return self.list_userAgent

    def to_txt(self, file_name):
        with open(file_name, 'w') as file:
            for user_agent in self.list_userAgent:
                file.write(user_agent + '\n')

