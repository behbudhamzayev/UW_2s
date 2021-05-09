from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Add headless option to run without opening a browser window
options = Options()
options.add_argument("--headless")

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


# Initialize the chrome driver and access the website
driver = webdriver.Chrome(options=options)
driver.get("https://birrapedia.com/beers-united-states/b-73656365722d706175732d7074776f#")

# Fetch all the results of each beer
results = driver.find_elements_by_class_name('lista-cab')

# Iterate through the results to extract the useful data
beerData = []   # List to hold all beers information
for result in results:
    beer = {}   # Dictionary to hold each beers' information

    # Extracting the data
    header = result.find_elements_by_tag_name('strong')
    imgs = result.find_elements_by_tag_name('img')
    extra = result.find_elements_by_xpath(".//p[@class='colorNegro linea-alta']")

    print(extra)

    # Manipulating the data
    imgs.pop(0) # Remove first image, the image of the beer
    extra = extra[1].text.split(' - ')
    if extra[0] == 'NEIPA':
        extra[0] += ' - ' + extra.pop(1)
    brand = extra[0]
    degree = extra[1]
    ibu = 0
    if len(extra) == 3:
        ibu = int(extra[2].replace(' IBU', ''))
    offers = header[2].text.replace(' Offers', '')
    offers = offers.replace(' Offer', '')

    # Fill the beer dictionary with the data and append it to the list of beers
    beer['Name'] = header[0].text
    beer['Rating'] = float(header[1].text.replace(',', '.'))
    beer['Offers'] = int(offers)
    beer['Brand'] = brand
    beer['Degree'] = degree
    beer['IBU'] = ibu
    beer['Countries'] = []
    for img in imgs:
        beer['Countries'].append(img.get_attribute('title'))
    beerData.append(beer)

# Analyze the extracted data
analyze(beerData)
