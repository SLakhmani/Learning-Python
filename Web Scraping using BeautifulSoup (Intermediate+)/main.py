# Disclaimer: Use web scraping at your own discretion. 
# Many sites contain data which is not meant to be scraped and can have legal repercussions. 
# Check [site-url]/robots.txt to see what kind of scraping is allowed by the website.
# The script below scrapes an article on stacker.com to compile a list of 100 movies to watch.

import re
import requests
from bs4 import BeautifulSoup
import collections

URL = "https://stacker.com/stories/1587/100-best-movies-all-time"
stacker_webpage = requests.get(URL).text
soup = BeautifulSoup(stacker_webpage, "html.parser")

movie_divs = soup.select(selector=".ct-slideshow__slides h2.ct-slideshow__slide__text-container__caption div")
movie_rankings = {int(re.sub(r'\W+', '', div.get_text().split(" ", 1)[0])): div.get_text().split(" ", 1)[1]
                  for div in movie_divs}

movie_rankings_sorted = collections.OrderedDict(sorted(movie_rankings.items()))
with open("movie_rankings.txt", "wt") as file:
    for ranking, movie_title in movie_rankings_sorted.items():
        file.write(f"{ranking}) {movie_title}\n")
