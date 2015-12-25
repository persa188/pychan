import urllib2
from BeautifulSoup import BeautifulSoup
import os
import sys

def get_images(url):

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

#this is for handling command line args
if not sys.argv[1:]:
	_url_ = 'http://boards.4chan.org/w/'
elif sys.argv[1] == '-g' or sys.argv[1] == '--general':
	_url_ = 'http://boards.4chan.org/wg/'
else:
	print >> sys.stderr, 'usage: too many args'
	exit(127)

get_images(_url_)