from Scraper.ProxyScraper import *
from Scraper.UserAgentScraper import *
from Scraper.GetSources import *


# Get sources to get proxies and user agents
url_list, url_json_list, url_txt_list = get_proxy_urls()
url_userAg=get_user_agents_urls()

# Create instance of UserAgents
userAgent=UserAgentsScraper()

# Add URL Sources
userAgent.from_url_list(url_userAg)

# Export list to txt
userAgent.to_txt("User_Agents.txt")

# Create instance of ProxyScraper with timeout of 10 seconds, taking user agents from a file
proxy_scraper = ProxyScraper(timeout=10, user_agents_file="data/User_Agents.txt")

# Add URL sources
proxy_scraper.get_proxy_from_url(url_list)

# Add JSON sources
proxy_scraper.get_proxy_from_json(url_json_list)

# Add TXT sources
proxy_scraper.get_proxy_from_txt(url_txt_list)

# Check proxies address
proxy_scraper.check_proxy_list()

# Export proxies list to .txt file
proxy_scraper.to_txt("WithUserAgent.txt",prefix="http://")
