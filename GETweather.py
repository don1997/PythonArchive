""""
This takes the weather site and prints the current weather to the terminal

"""
from urllib.request import urlopen
from bs4 import BeautifulSoup

#ASSIGNS URL to var
url = "https://forecast.weather.gov/MapClick.php?lat=34.8756&lon=-76.9034"
#Opens page and assigns it to page
page = urlopen(url)
#decodes page and assigns it to html var
html = page.read().decode("utf-8")

doc = BeautifulSoup(html, "html.parser")

title = doc.find(id = "current_conditions-summary")

thingy = title.contents[5]
#for celsius
celc = title.contents[7]


a = thingy.text
#for celsius
c = celc.text
print("The current temp in Morehead City, NC is: " + a + " and " + c)

feel = title.contents[3]

b = feel.text
print("It feels " + b)

if(b == 'Fair'):
    print("it is very nice out")
else:
    print("It is not nice out")

###This selects the data by class instead of by id and going down the DOM
data = doc.find_all("p", class_="myforecast-current-lrg")
###This allows for temp to be isolated from tags
for z in data:
    print(z.text)

#Here I learned the difference between doc.find_all and doc.find
#One finds literally all and find finds ONLY the first element in the tag.

data = doc.find("div", class_="col-sm-10 forecast-text")

for z in data:
    print("Current forecast: " + z.text)