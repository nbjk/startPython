# Download apk to current folder from as.baidu.com using app's id
#
# Reason: App's id is not changed, but download url may changes, So this is why I wrote this script
#
# Example: 
# python downloadApkFromBaidu.py 2306672 2381979 2372170 


from sys import argv
from BeautifulSoup import BeautifulSoup
import urllib2
import re

prefix_url = "http://as.baidu.com/a/item?"

source_urls = [] # Baidu app detail page url
source_pages = []

download_info = {}

i = 1
argvNum = len(argv)

while ( i < argvNum ):

    source_url = prefix_url + "docid=" + argv[i] # GET source page url list
    source_urls.append(source_url)

    source_page = urllib2.urlopen(source_url).read() # GET source page code
    source_pages.append(source_page)

    soup = BeautifulSoup(source_page)
    
    download_app_name = soup.find(id="appname").contents[0] # App name from Baidu app detail page
    down_as_durl = soup.find(id="down_as_durl").get('href') # ID down_as_durl from Baidu app detail page

    download_info[download_app_name] = down_as_durl

    i = i + 1

# Start download from down_as_urls
for download_app_name, down_as_durl in download_info.items():
    print "Downloading %s from %s" % (download_app_name, down_as_durl)
    apkFile = urllib2.urlopen(down_as_durl)
    output = open(download_app_name + '.apk', 'wb')
    output.write(apkFile.read())
    output.close()

