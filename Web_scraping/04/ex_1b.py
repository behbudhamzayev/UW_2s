


from bs4 import BeautifulSoup
import urllib.request
import re

painter_links = []

# Look at the page and the code
parser = 'html.parser'  
resp = urllib.request.urlopen("https://en.wikipedia.org/wiki/List_of_rock_music_performers")
soup = BeautifulSoup(resp, parser, from_encoding=resp.info().get_param('q'))

tags = soup.find_all('a', {'title':re.compile('[Qq]')})
links = ['https://en.wikipedia.org/wiki/List_of_rock_music_performers' + tag['href'] for tag in tags]

for q in links:
    print(q)

