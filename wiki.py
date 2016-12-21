"""
An application to open a wikipedia page, randomly select one of the internal links on the page and access it.
Then iterate the process saving the name of the page accessed.
"""

from BeautifulSoup import *
import urllib
import random

ITERATIONS = 5

def action(url):
    to_choose = []
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')

    for tag in tags:
        oprating_on_tag = str(tag.get('href', None))
        if not ':' in oprating_on_tag:
            if not '#' in oprating_on_tag:
                if oprating_on_tag[1:5] == 'wiki':
                    to_choose.append(oprating_on_tag)
    return random.choice(to_choose)

start_with = 'Africa'
name_to_go = action('https://en.wikipedia.org/wiki/' + start_with)
path = [start_with]

for _ in range(ITERATIONS):
    path.append(name_to_go[6:])
    name_to_go = action('https://en.wikipedia.org' + name_to_go)

for _ in path:
    print _
