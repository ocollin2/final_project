from bs4 import BeautifulSoup
import requests

# This Wikipedia web page contains information about Taylor Swift's albums. It includes a table
# listing how many albums she's done that fall into different categories
swift_albums_page = requests.get("https://en.wikipedia.org/wiki/Taylor_Swift_albums_discography")

swift_albums_soup = BeautifulSoup(swift_albums_page.content, "html.parser")
swift_albums_table = swift_albums_soup.find("table")
swift_albums_table
swift_albums_th = swift_albums_table.find_all("th")
swift_albums_th
swift_albums_headers = []
for th in swift_albums_th:
    swift_albums_headers.append(th.get_text().strip())
header_string = ",".join(swift_albums_headers)
header_string