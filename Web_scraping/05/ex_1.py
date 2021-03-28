import requests
from urllib import request
from bs4 import BeautifulSoup as BS
import re
import pandas as pd

###################################################################################################
#####   Extract links to web pages containing information about musicians specialising   ##########
#####                    in music genre beginning with "A".                              ##########
###################################################################################################
url = 'https://en.wikipedia.org/wiki/Lists_of_musicians'
page = request.urlopen(url)
parser = BS(page.read(), 'html.parser')

tags = parser.find(id="A").parent.nextSibling.nextSibling.nextSibling.find_all("a")

links = ["https://en.wikipedia.org" + tag['href'] for tag in tags]

###################################################################################################
#####   Extract links to artists' web pages for the rst of the links from              ##########
#####                    the previous step.                                              ##########
###################################################################################################
bands = []

for link in links:
    print(link)
    html = request.urlopen(link)
    bs = BS(html.read(), 'html.parser')
    
    tags = bs.find_all('ul')[1].find_all('li')

    link_temp_list = []
    for tag in tags:
        try:
            link_temp_list.append('http://en.wikipedia.org' + tag.a['href'])
        except:
            0 

    bands.extend(link_temp_list)


A_bands = pd.DataFrame({'name':[], 'years_active':[]})

for band in bands[:100]:
    print(band)

    html = request.urlopen(band)
    bs = BS(html.read(), 'html.parser')
    
    try:
        name = bs.find('h1').text
    except:
        name = ''
    
    try:
        years_active = bs.find('th', string =re.compile('Years.*active')).next_sibling.text
    except:
        years_active = ''
    
    band = {'name':name, 'years_active':years_active}
    
    A_bands = A_bands.append(band, ignore_index = True)
    print(A_bands)

###################################################################################################
#####         As an output use default print function on pandas data frame.              ##########
###################################################################################################
A_bands.to_csv('A_bands.csv')

