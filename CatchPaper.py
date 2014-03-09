import urllib2
from DownFile import down_file
from bs4 import *
import Paper

# output = open('data.txt', 'w')	# create a file to save

def c0(content):
	print("Pdf Link: %s" % content.a['href'])
	return content.a['href']
	
def c1(content):
	title_a = content.h3.a
	if title_a == None:
		return None
	else:
		try:
			print("Paper Title: %s" % title_a.text)
			print("Paper Link: %s" % title_a['href'])
			print("Paper Author: %s" % content.contents[1].text)
			print("Paper Abstract: %s" % content.contents[2].text)			#abstract
			print("Cited Times: %s" % content.contents[3].contents[0].text)#citetimes
			allversion_link = content.contents[3].contents[4]['href']
			print("Versions: %s" % allversion_link)   #versions
			print("\n")
			return title_a.text
		except UnicodeEncodeError as e:
			print("UnicodeEncodeError at: %s" % title_a)

def down_task(url):
	print("Process URL: %s" % url)
	req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"}) 
	webpage = urllib2.urlopen(req)
	soup = BeautifulSoup(webpage.read().decode('gbk'))		# decode gbk and create soup
	for item in soup.find_all('div', {'class':'gs_r'}):		# find all paper title
		contents = item.contents;
		if(len(contents)==2):
			paperTitle= c1(item.contents[1])
			pdfLink = c0(item.contents[0])
			down_file(pdfLink, "E:/Papers/", paperTitle.replace(":","_")+".pdf")
		else:
			paperTitle = c1(item.contents[0])
	print("Task ended.")

if __name__ == "__main__":
	urlHeader = "http://scholar.google.com"
	b = "/scholar?start="
	d = "&q=link+prediction&hl=zh-CN&as_sdt=0,5"
	for i in range(0, 100, 10):
		url = urlHeader+b+str(i)+d
		down_task(url)
	print("Ended.")
