import scrapy

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

# Create class to start scraping the data
class BeerScraper(scrapy.Spider):
    name = "BeerScrap"
    start_urls = ['https://birrapedia.com/beers-united-states/b-73656365722d706175732d7074776f#']

    def parse(self, response):
        beerData = []   # List to hold all beers information
        for result in response.css('.lista-cab'):
            beer = {}   # Dictionary to hold each beers' information

            # Extracting the text from the header and the extra, and extract the title from the images
            header = result.xpath('.//strong/text()').extract()
            imgs = result.xpath('.//img/@title').extract()
            extra = result.xpath(".//p[@class='colorNegro linea-alta']/text()").extract()
            
            # Manipulating the data
            imgs.pop(0) # Remove first image, the image of the beer
            extra = extra[0].split(' - ')
            if extra[0] == 'NEIPA':
                extra[0] += ' - ' + extra.pop(1)
            brand = extra[0]
            degree = extra[1]
            ibu = 0
            if len(extra) == 3:
                ibu = int(extra[2].replace('\xa0IBU', ''))
            offers = header[2].replace('\xa0Offers', '')
            offers = offers.replace('\xa0Offer', '')

            # Fill the beer dictionary with the data and append it to the list of beers
            beer['Name'] = header[0]
            beer['Rating'] = float(header[1].replace(',', '.'))
            beer['Offers'] = int(offers)
            beer['Brand'] = brand
            beer['Degree'] = degree
            beer['IBU'] = ibu
            beer['Countries'] = []
            for img in imgs:
                beer['Countries'].append(img)
            beerData.append(beer)
        
        analyze(beerData)

