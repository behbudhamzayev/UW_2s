################################################################################
# First_method:

from urllib import request
from bs4 import BeautifulSoup as BS
import re
import pandas as pd

d = pd.DataFrame({'name':[], 'Genre':[], 'Years_active':[]})

url = 'https://en.wikipedia.org/wiki/Queen_(band)' 
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')

try:
    name = bs.find('h1').text
except:
    name = ''

try:
    Genre = bs.find('th',string = 'Genres').next_sibling.text
    Genre = re.findall('[0-9]+\s+[A-Za-z]+\s+[0-9]+', Genres)
except:
    Genre = ''

try:
    Years_active = bs.find('th',string = 'Years active').next_sibling.text
    Years_active = re.findall('[0-9]+\s+[A-Za-z]+\s+[0-9]+', Years_active)
except:
    Years_active = ''



painter = {'name':name, 'Genre':Genre, 'Years_active':Years_active}

d = d.append(painter, ignore_index = True)

print(d)




################################################################################
# Second_method:



from urllib import request
from bs4 import BeautifulSoup as BS
import re


url = 'https://en.wikipedia.org/wiki/Queen_(band)'
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')

#Name of the band
name = bs.find('div', {'class':"fn org"})
name = ''

#Genre
genre = bs.find('a', {'title':re.compile("Rock music")})
genre = ''

#Number of years active
Years_active = bs.find('td', {'class':'nowrap'==("Years active")})
Years_active = ''

print(name, genre,Years_active)