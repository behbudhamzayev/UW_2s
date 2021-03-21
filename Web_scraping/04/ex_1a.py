################################################################################################
#########                                                                          #############
#########                 Firt Method                                              #############
#########                                                                          #############                          
#########                                                                          #############                  
################################################################################################

from bs4 import BeautifulSoup
import urllib.request
import re

parser = 'html.parser'  
resp = urllib.request.urlopen("https://en.wikipedia.org/wiki/Lists_of_musicians")
soup = BeautifulSoup(resp, parser, from_encoding=resp.info().get_param('r'))

tags = soup.find_all('a', {'title':re.compile('List of [Rr].*')})
links = ['http://en.wikipedia.org' + tag['href'] for tag in tags]

for r in links:
    print("The following is music genre beginning with R: ",  r)


################################################################################################
#########                                                                          #############
#########                 Second Method                                            #############
#########                                                                          #############                          
#########                                                                          #############                  
################################################################################################
from urllib import request
from bs4 import BeautifulSoup as BS
import re

url = 'https://en.wikipedia.org/wiki/Lists_of_musicians' 
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')

tags = bs.find_all('a', {'title':re.compile('List of R.*')})

links = ['http://en.wikipedia.org' + tag['href'] for tag in tags]

for link in links:
    print(link)