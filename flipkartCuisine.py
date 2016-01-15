from bs4 import BeautifulSoup		
import requests
import json
import os, sys
import re
										

def page_spider():
		i=1
		count=0
		while i<1161:
			url='http://www.flipkart.com/lc/pr/pv1/spotList1/spot1/productList?p[]=facets.category[]=Cuisine&sid=1m7,att,tjw&filterNone=true&start='+str(i)+'&q=posters&ajax=true'
			source_code = requests.get(url)
			plain_text=source_code.text
			soup = BeautifulSoup(plain_text,"lxml")
			links=soup.findAll('a',{'class':'fk-display-block'})
			if links:
				for item in links:
					href="http://www.flipkart.com"+item.get('href')
					title=item.get('title')
					if "javascript:void(0)" in href:
						continue
					else:
						title=item.get('title').encode('utf-8')
					
					if href and title:
						print href 
						print title
						count+=1
						fullPageofImage(href,title,count)
						print count			
			i+=15
		print count
		
		
def fullPageofImage(url_of_Im,title,count):
	try:

		source_code = requests.get(url_of_Im)
		plain_text=source_code.text
		soup=BeautifulSoup(plain_text,"lxml")
		main=soup.find('img',{'class':'productImage'})
		if main:
			src=main.get('data-zoomimage')
			if src:
				download_Image(src,title)	 
				print "done"+" "+str(count)
	except:
		print "error" 			


		
def download_Image(url_of_image,title):
	image=requests.get(url_of_image,stream=True)
	if not os.path.exists("/home/paras/Desktop/Flipkart/Cuisine"):
		path1="/home/paras/Desktop/Flipkart/Cuisine"
		os.makedirs("/home/paras/Desktop/Flipkart/Cuisine")
	else:
		path1="/home/paras/Desktop/Flipkart/Cuisine"
	title = re.sub(r'[/|\|:|*|?|"|<|>||]',r' ',title)
	title = re.sub(r"[']",r' ',title)
	with open(path1+"/"+str(title)+".jpeg",'wb') as f:
		f.write(image.content)
		f.flush()
	print "Save"

page_spider()