# This code imports data from birrapedia about different beverages and compares the ratings of the products
# Import required libraries

import requests
from bs4 import BeautifulSoup

def printInfo(beer):
    # This function takes one beer's dictionary and prints out the information about it
    print(f"Name: {beer['Name']}")
    print(f"Brand: {beer['Brand']}")
    print(f"Rating: {beer['Rating']}")
    print(f"Number of Offers: {beer['Offers']}")
    if beer['IBU'] == 0:
        print("IBU: Not Specified")
    else:
        print(f"IBU: {beer['IBU']}")
    countries = beer['Countries']
    print(f"Available in the following countries: {countries[0]}", end='')
    for i in range(1, len(countries)-1):
        print(', ' + countries[i],end='')
    print(f"\nBest served at: {beer['Degree']} degrees")

def analyze(beers):
    # This function takes a list of beers dictionaries and does some simple analysis on them
    # First get the top 10 beers by sorting the list (reference:https://stackoverflow.com/questions/72899/how-do-i-sort-a-list-of-dictionaries-by-a-value-of-the-dictionary)
    sortedBeers = sorted(beers, key=lambda k: k['Rating'], reverse=True)

    topTen = sortedBeers[:10]
    
    # Print out their data
    print('======================================')
    print("Top 10 Beers in this query")
    for beer in topTen:
        print('======================================')
        printInfo(beer)

    # Get the beer that is server in the most countries
    mostCountries = beers[0]
    for beer in beers:
        if len(beer['Countries']) > len(mostCountries['Countries']):
            mostCountries = beer

    print('======================================')
    print("Top Beer that is served in most conutries")
    print('======================================')
    printInfo(mostCountries)


# This url contains search results for beers in the US
url = "https://birrapedia.com/beers-united-states/b-73656365722d706175732d7074776f#"
page = requests.get(url)

# Create a BeautifulSoup object using html parser mode
soup = BeautifulSoup(page.content, 'html.parser')

# Fetch all the results of each beer
results = soup.find_all(class_='lista-cab')

# Iterate through the results to extract the useful data
beerData = []   # List to hold all beers information
for result in results:
    beer = {}   # Dictionary to hold each beers' information

    # Extracting the data
    header = result.find_all('strong')
    imgs = result.find_all('img')
    extra = result.find_all(class_="colorNegro linea-alta")

    # Manipulating the data
    imgs.pop(0)
    extra = extra[1].text.split(' - ')
    if extra[0] == 'NEIPA':
        extra[0] += ' - ' + extra.pop(1)
    brand = extra[0]
    degree = extra[1]
    ibu = 0
    if len(extra) == 3:
        ibu = int(extra[2].replace('\xa0IBU', ''))
    offers = header[2].text.replace('\xa0Offers', '')
    offers = offers.replace('\xa0Offer', '')

    # Fill the beer dictionary with the data and append it to the list of beers
    beer['Name'] = header[0].text
    beer['Rating'] = float(header[1].text.replace(',', '.'))
    beer['Offers'] = int(offers)
    beer['Brand'] = brand
    beer['Degree'] = degree
    beer['IBU'] = ibu
    beer['Countries'] = []
    for img in imgs:
        beer['Countries'].append(img.get('title'))
    beerData.append(beer)

# Analyze the extracted data
analyze(beerData)
