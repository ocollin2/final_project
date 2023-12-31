from bs4 import BeautifulSoup
import requests
import pandas as pd

# This Wikipedia web page contains information about Taylor Swift's albums. It includes a table
# listing how many albums she's done that fall into different categories.
swift_albums_page = requests.get("https://en.wikipedia.org/wiki/Taylor_Swift_albums_discography")

# Using bs4 to scrape the web page.
swift_albums_soup = BeautifulSoup(swift_albums_page.content, "html.parser")
# I just want the table at the top of the page.
swift_albums_table = swift_albums_soup.find("table")
# Getting the headers from the table.
swift_albums_th = swift_albums_table.find_all("th")
swift_albums_headers = []
for th in swift_albums_th[1:]:
    swift_albums_headers.append(th.get_text().strip())
print("Here are the types of albums in this table: ")
swift_albums_headers

table_rows = swift_albums_table.find_all("tr")
swift_albums_rows = []
# Getting the count values for each of the headers scraped above.
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


# Reading in a CSV of data into a data frame using pandas 
songs = pd.read_csv("taylor_swift_songs.csv")
del songs["Danceability"]
del songs["Energy"]
del songs["Loudness"]
del songs["Key"]
del songs["Mode"]
del songs["Speechiness"]
del songs["Acousticness"]
del songs["Instrumentalness"]
del songs["Liveness"]
del songs["Valence"]
del songs["Tempo"]
del songs["Time Signature"]
del songs["Playlist ID"]
print(songs)
# Using a Series to perform a vectorized computation instead of a loop.
songs["Duration (mins)"] = songs["Duration_ms"] / 60000
print(songs)
# Using pandas to get a subset of a data frame using a boolean
long_songs = songs[songs["Duration (mins)"] > 5]
print(long_songs)
# Writing data that I created/changed to a CSV using pandas
long_songs.to_csv("swift_long_songs.csv")