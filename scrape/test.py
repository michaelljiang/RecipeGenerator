from scraper import scrape, scrapeI
import csv
from itertools import chain
from collections import Counter

with open('url.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    urls = [row['URL'] for row in reader]

i = []
for u in urls:
    t = scrapeI(u)
    i = list(chain(i, t))

count = Counter(i)

print(count)



