# in this project I'll be using the following url for finding
# country_name and country_info and storing it into a csv file

import requests
from bs4 import BeautifulSoup
import pandas

ignore_missing_imports = True

url = "https://scrapethissite.com/pages/simple/"
scrapped_info_list = []

req = requests.get(url)
content = req.content

soup = BeautifulSoup(content, "html.parser")

all_countries = soup.find_all("div", {"class": "col-md-4"})

for country in all_countries:
    country_dict = {"name": country.find("h3", {"class": "country-name"}).text.strip(),
                    "capital": country.find("span", {"class": "country-capital"}).text,
                    "population": country.find("span", {"class": "country-population"}).text,
                    "area": country.find("span", {"class": "country-area"}).text}
    scrapped_info_list.append(country_dict)

dataFrame = pandas.DataFrame(scrapped_info_list)
dataFrame.to_csv("Countries.csv")
