import urllib.request
from bs4 import BeautifulSoup

ArcaUrl = "https://arca.live"

channel = input("Input Channel ID (Default: All): ")
if not channel:
    channel = "breaking"
target = input("Input Name#ID: ")
name = target.split("#")[0]

DefaultPageUrl = ArcaUrl+"/b/"+channel+"?target=nickname&keyword="+urllib.parse.quote_plus(name)
PageUrl = DefaultPageUrl
index = 1

while True:
    reqUrl = urllib.request.Request(PageUrl, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(urllib.request.urlopen(reqUrl).read(), 'html.parser')
    code = soup.find_all("span", {"data-filter": target})

    for X in code:
        mother = X.parent.parent.parent.parent
        title = mother.find("span", {"class": "title"}).getText(strip=True)
        url = ArcaUrl+mother["href"].split("?")[0]
        time = mother.find("time")["datetime"].replace("T", " ").replace(".000Z", "")
        print(index, time, title, url)
        index += 1

    LastID = soup.find_all("a", {"class": "vrow"})[-1]["href"].split("/")[-1].split("?")[0]
    PageUrl = DefaultPageUrl +"&before=" + LastID
