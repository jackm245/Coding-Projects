import re
import requests
from bs4 import BeautifulSoup

# a list of sites to download images from
sites = ['https://www.python.org/']

for site in sites:
    # creates a parser response to the website
    response = requests.get(site)
    soup = BeautifulSoup(response.text, 'html.parser')

    # finds all images on the site
    img_tags = soup.find_all('img')
    print(img_tags)

    # creates urls of the found images
    urls = [img['src'] for img in img_tags]
    for url in urls:
        # save image to file
        filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
        if hasattr(filename, 'group'):
            with open(filename.group(1), 'wb') as f:
                # correctly formatting image for if a filename is not relative
                if 'http' not in url:
                    url = '{}{}'.format(site, url)
                response = requests.get(url)
                # writes the image to afile
                print(f"writing {url}...")
                f.write(response.content)
