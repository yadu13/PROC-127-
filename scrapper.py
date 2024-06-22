from bs4 import BeautifulSoup
import requests
import pandas as pd

START_URL = (
    "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
)
scraped_data=[]
wiki = requests.get(START_URL)
soup = BeautifulSoup(wiki.text, "html.parser")
temp_list = []
for tr in soup.find("table").find_all("tr"):
    td = tr.find_all("td")
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)
    scraped_data.append(temp_list)

name = []
distance = []
mass = []
radius = []
luminosity=[]

for i in range(1, len(scraped_data)):
    name.append(scraped_data[i][1])
    distance.append(scraped_data[i][3])
    mass.append(scraped_data[i][5])
    radius.append(scraped_data[i][6])
    luminosity.append(scraped_data[i][7])

stars_df_1 = pd.DataFrame(
    list(zip(name, distance, mass, radius,luminosity)),
    columns=["Star_name", "Distance", "Mass", "Radius","Luminosity"],
)
stars_df_1.to_csv("data.csv")