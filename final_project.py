from bs4 import BeautifulSoup
import requests

# This Wikipedia web page contains information about Taylor Swift's albums. It includes a table
# listing how many albums she's done that fall into different categories.
swift_albums_page = requests.get("https://en.wikipedia.org/wiki/Taylor_Swift_albums_discography")

swift_albums_soup = BeautifulSoup(swift_albums_page.content, "html.parser")
swift_albums_table = swift_albums_soup.find("table")
swift_albums_table
swift_albums_th = swift_albums_table.find_all("th")
swift_albums_th
swift_albums_headers = []
for th in swift_albums_th[1:]:
    swift_albums_headers.append(th.get_text().strip())
print("Here are the types of albums in this table: ")
swift_albums_headers

table_rows = swift_albums_table.find_all("tr")
swift_albums_rows = []
for row in table_rows[2:]:
    row_list = []
    print(row)
    for cell in row.find_all("td"):
        cell_text = cell.get_text().strip()
        row_list.append(cell_text)
    row_string = ",".join(row_list)
    swift_albums_rows.append(row_string)

print("Here are the corresponding values for the above categories: ")
swift_albums_rows