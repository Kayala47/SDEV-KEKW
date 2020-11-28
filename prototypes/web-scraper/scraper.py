import requests
from bs4 import BeautifulSoup as bs
import imgkit
import sys

# command line arguments start at 0 with the name of script
# 1 is the type of object we look for and the rest make up the string of the searchable object
# we're only doing spells for this prototype


object_type = sys.argv[1]

searchable = ("-").join(sys.argv[2:])

URL = "http://dnd5e.wikidot.com/" + object_type + ":" + searchable

page = requests.get(URL)
path_wkhtmltoimage = "F:\Programming\\wkhtmltopdf\\bin\\wkhtmltoimage.exe"
config = imgkit.config(wkhtmltoimage=path_wkhtmltoimage)

soup = bs(page.content, 'html.parser')

results = soup.find(id='page-content')


print(results.find_all("p"))
