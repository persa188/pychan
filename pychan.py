import urllib2
from BeautifulSoup import BeautifulSoup
import os

def get_images():
	url = "http://boards.4chan.org/wg/"
	text = urllib2.urlopen(url).read();
	soup = BeautifulSoup(text);

	data = soup.findAll('div',attrs={'class':'fileText'});

	if not os.path.exists("./images"):
		os.mkdir("images")
	incr = 0;

	for i in data:
		img = urllib2.urlopen("http:"+i.a['href'])
		with open('./images/img'+str(incr)+i.a['href'][-4:], 'wb') as localfile:
			localfile.write(img.read())
		incr += 1

get_images()