from bs4 import BeautifulSoup
import requests

# This Wikipedia web page contains information about Taylor Swift's Reputation Stadium Tour. I am
# interested in the Tour dates table which contains data such as Attendance and Revenue for each
# show.
reputation_page = requests.get("https://en.wikipedia.org/wiki/Reputation_Stadium_Tour")

