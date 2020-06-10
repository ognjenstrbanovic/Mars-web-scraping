# import dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time

# using BeautifulSoup
# Task 1
url_1 = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
response_1 = requests.get(url_1)
soup_1 = BeautifulSoup(response_1.text, "html.parser")
news_title = soup_1.find(class_ = "content_title").text.strip()
news_p = soup_1.find(class_ = "rollover_description_inner").text.strip()

# Task 2
executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
browser = Browser("chrome", **executable_path, headless=False)
url_2 = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(url_2)
html = browser.html
time.sleep(1)
soup_2 = BeautifulSoup(html, "html.parser")
result = soup_2.find("img", class_ = "thumb").get("src")
featured_image_url = f"https://www.jpl.nasa.gov{result}"
# Task 3
url_3 = "https://twitter.com/marswxreport?lang=en"
response_2 = requests.get(url_3)
soup_3 = BeautifulSoup(response_2.text, "html.parser")
mars_weather = \
soup_3.find("p", class_ = "TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").\
text.strip(" hPapic.twitter.com/SkjAdWsePB")

# Task 4
url_4 = "https://space-facts.com/mars/"
tables = pd.read_html(url_4)
df = tables[0]
df.columns = ["Mars Facts", "Data"]
df = df.replace("\n", "", regex=True)
html_table = df.to_html()

# Task 5
url_a = "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"
url_b = "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced"
url_c = "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced"
url_d = "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"
response_a = requests.get(url_a)
soup_a = BeautifulSoup(response_a.text, "html.parser")
response_b = requests.get(url_b)
soup_b = BeautifulSoup(response_b.text, "html.parser")
response_c = requests.get(url_c)
soup_c = BeautifulSoup(response_c.text, "html.parser")
response_d = requests.get(url_d)
soup_d = BeautifulSoup(response_d.text, "html.parser")
titles = []
img_urls = []
for url in url_a, url_b, url_c, url_d:
    titles.append(soup_a.find("h2", class_ = "title").text)
    titles.append(soup_b.find("h2", class_ = "title").text)
    titles.append(soup_c.find("h2", class_ = "title").text)
    titles.append(soup_d.find("h2", class_ = "title").text)
    img_urls.append(soup_a.find("li").a["href"])
    img_urls.append(soup_b.find("li").a["href"])
    img_urls.append(soup_c.find("li").a["href"])
    img_urls.append(soup_d.find("li").a["href"])
    break
hemisphere_image_urls = dict(zip(titles, img_urls))

def scrape():
    scraped_data = dict(news_title = soup_1.find(class_ = "content_title").text.strip(), news_p = soup_1.find(class_ = "rollover_description_inner").text.strip(), featured_image_url = f"https://www.jpl.nasa.gov{result}", mars_weather = soup_3.find("p", class_ = "TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text.strip(" hPapic.twitter.com/SkjAdWsePB"), html_table = df.to_html(), hemisphere_image_urls = dict(zip(titles, img_urls)))
    return scraped_data
print(scrape())