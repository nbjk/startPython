from sys import argv
from BeautifulSoup import BeautifulSoup
import urllib2
import re

prefix_url = "http://as.baidu.com/a/item?"

# GET docid by argv
docids_argv = []
urls = []
download_urls = []
source_pages = []

i = 1
argvNum = len(argv)

while ( i < argvNum ):
    docids_argv.append(argv[i])

    url = prefix_url + "docid=" + argv[i] # GET source page url list
    urls.append(url)

    source_page = urllib2.urlopen(url).read() # GET source page code
    source_pages.append(source_page)

    soup = BeautifulSoup(source_page)
    for link in soup.findAll('a'):
        print link.get('href')

    i = i + 1

# Print download source page url
for url in urls:
    print url

#for source_page in source_pages:
#    print source_page

# GET docid manually, finished later...

# GET source page


