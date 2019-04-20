import re
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
user_id = "kamiis_99"
url = 'https://www.instagram.com/{}'.format(user_id)
def GetFollower():
    try:
        uClient = uReq(url)
        page_html = uClient.read()
        uClient.close()
        page_soup = soup(page_html, "html.parser")
        container = str(page_soup.findAll("meta", {"name": "description"}))
        m = re.search("""content="(.+?) Followers""", container)
        followers = m.group(1)
        print("getting followers")
        return followers
    except:
        print("No Internet conection")
