def get_proxy_urls():
    url_list = [
        "https://hidemy.name/en/proxy-list/",
        "https://proxyscrape.com/free-proxy-list",
        "https://spys.one/en/http-proxy-list/",
        "https://spys.one/en/http-proxy-list/",
        "https://free-proxy-list.net/",
        "https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers/",
        "https://www.proxynova.com/proxy-server-list/",
        "https://www.freeproxy.world/?type=http&anonymity=&country=&speed=&port=&page=1",
        "https://www.freeproxy.world/?type=http&anonymity=&country=&speed=&port=&page=2",
        "https://www.freeproxy.world/?type=http&anonymity=&country=&speed=&port=&page=3",
        "https://www.proxydocker.com/en/proxylist/type/http-https",
        "https://www.experte.com/proxy-server"
    ]

    page = 0
    for i in range(179):
        page += 64
        url_list.append("https://hidemy.name/en/proxy-list/?type=hs&start=" + str(page) + "#list")

    url_json_list = [
        "https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc&protocols"
        "=http%2Chttps",
        "https://proxylist.geonode.com/api/proxy-list?limit=500&page=2&sort_by=lastChecked&sort_type=desc&protocols"
        "=http%2Chttps",
    ]

    url_txt_list = [
        "https://api.proxyscrape.com/?request=displayproxies&proxytype=https",
        "https://openproxylist.xyz/http.txt",
        "https://multiproxy.org/txt_all/proxy.txt",
        "http://alexa.lr2b.com/proxylist.txt",
        "http://rootjazz.com/proxies/proxies.txt",
        "https://www.freeproxychecker.com/result/http_proxies.txt",
    ]

    return url_list, url_json_list, url_txt_list


def get_user_agents_urls():
    url_user_agents = [
        "http://useragent.fr/liste-populaire.php",
        "https://deviceatlas.com/blog/list-of-user-agent-strings",
        "https://www.useragentstring.com/pages/Browserlist/"
    ]

    return url_user_agents
