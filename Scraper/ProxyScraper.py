import json
import random
import re
import sys
from threading import Thread

import requests
from bs4 import BeautifulSoup

class ProxyScraper:

    def __init__(self, timeout, user_agents_file=None):
        self.good_proxies = []
        self.proxies_list = []
        self.timeout = timeout
        self.links = [
            "https://www.youtube.com/",
            "https://www.vinted.fr/",
            "https://www.facebook.com/",
            "https://www.ebay.fr/",
            'https://google.fr',
            "https://www.leboncoin.fr/",
            "https://www.twitch.tv/",
            "https://twitter.com/home?lang=fr",
            "https://stackoverflow.com/",
            "https://www.cnrtl.fr/",
            "https://www.20minutes.fr/",
            "https://www.ouest-france.fr/",
            "https://creapills.com/",
            "https://www.bfmtv.com/economie/"
        ]

        try:
            self.headers_list = self._set_user_agents(user_agents_file)
        except OSError:
            print("Bad file specified, use of default user agent")
            self.headers_list = [
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/39.0.2171.95 Safari/537.36']

    @staticmethod
    def _set_user_agents(filename):
        final_list = []
        with open(filename) as f:
            print("OK !")
            for line in f.readlines():
                final_list.append(line.replace('\n', ''))
        return final_list

    def get_proxy_from_json(self, url_json_list):
        bad_url = 0
        for iteration, url_json in enumerate(url_json_list):
            b = 'JSON List processing : ' + str(iteration + 1) + " / " + str(len(url_json_list))
            sys.stdout.write('\r' + b)
            sys.stdout.flush()

            try:
                header = {'User-Agent': random.choice(self.headers_list)}
                r = requests.get(url_json, headers=header).text
            except:
                bad_url += 1
                continue
            json_l = json.loads(r)

            for proxy in json_l["data"]:
                ip_address = proxy['ip']
                port = proxy['port']
                proxy_address = ip_address + ':' + port
                self.proxies_list.append(proxy_address)

        print("\n{} URL were not working and {} were.".format(bad_url, len(url_json_list) - bad_url))
        pass

    def _test_proxy(self, proxy_address):
        try:
            proxies = {
                'http': proxy_address,
                'https': proxy_address,
            }
            s = requests.Session()

            selected_link = random.choice(self.links)

            header = {'User-Agent': random.choice(self.headers_list)}
            r = s.get(selected_link, timeout=self.timeout, proxies=proxies, headers=header)
            s.close()
        except IOError:
            # print(traceback.format_exc())
            pass
        else:
            if r.status_code == 200:
                self.good_proxies.append(proxy_address)
                return 1

    def check_proxy_list(self):
        thread_list = []
        for proxy in self.proxies_list:
            if len(proxy) > 1:
                thread_list.append(Thread(target=self._test_proxy, args=[proxy]))

        print('\nLaunching proxies thread')
        for t in thread_list:
            t.start()

        max_len = len(thread_list)
        iteration = 1
        for t in thread_list:
            b = 'Checking proxies : ' + str(iteration) + " / " + str(max_len)
            sys.stdout.write('\r' + b)
            sys.stdout.flush()
            t.join()
            iteration += 1

        print()
        print("Proxies checked")
        print(str(len(self.good_proxies)) + " proxies are working !")

    def get_proxies_list(self):
        return self.proxies_list

    def get_good_proxies(self):
        return self.good_proxies

    def change_timeout(self, new_timeout: int):
        self.timeout = new_timeout

    def get_proxy_from_url(self, url_list):
        iteration = 0
        bad_url = 0
        total_len = len(url_list)

        for url in url_list:
            iteration += 1
            b = 'URL List processing : ' + str(iteration) + " / " + str(len(url_list))
            sys.stdout.write('\r' + b)
            sys.stdout.flush()

            try:
                header = {'User-Agent': random.choice(self.headers_list)}
                soup = BeautifulSoup(requests.get(url, headers=header).content, "html.parser")
            except:
                bad_url += 1
                continue
            all_tr = soup.find_all('tr')
            for tr in all_tr[1:]:
                try:
                    all_td = tr.find_all('td')
                    address = all_td[0].text
                    port = all_td[1].text
                    proxy_adress = str(address) + ":" + str(port)
                    self.proxies_list.append(proxy_adress)
                except:
                    continue

        print("\n{0} URL were not working and {1} were.".format(bad_url, total_len - bad_url))
        pass

    def get_proxy_from_txt(self, url_list):
        iteration = 0

        bad_url = 0
        for url in url_list:
            iteration += 1
            b = 'TXT List processing : ' + str(iteration) + " / " + str(len(url_list))
            sys.stdout.write('\r' + b)
            sys.stdout.flush()

            try:
                header = {'User-Agent': random.choice(self.headers_list)}
                r = requests.get(url, headers=header)
            except:
                bad_url += 1
                continue
            content = r.text
            for proxy in content.split('\n'):
                self.proxies_list.append(proxy)

        print("\n{0} URL were not working and {1} were.".format(bad_url, len(url_list) - bad_url))
        pass

    def to_txt(self, file_name, prefix=""):
        with open(file_name, 'w') as file:
            for proxy in self.good_proxies:
                file.write(prefix + proxy + "\n")
