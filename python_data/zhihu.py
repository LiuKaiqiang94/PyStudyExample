import urllib.request
import re

url='http://daily.zhihu.com'

def get_html(url):
    html=urllib.request.urlopen(url).read()
    html=html.decode('utf-8')
    return html

def get_url_num(html):
	res=re.compile('<a href="/story/(.*?)"')
	url_nums=re.findall(res,html)
	urls=[]
	for url_num in url_nums:
		urls.append('http://daily.zhihu.com/story/'+url_num)
	return urls

def get_content(newurl):
	newurl_html=get_html(newurl)
	re_title=re.compile('<title>(.*?)</title>')
	title=re.findall(re_title,newurl_html)
	re_content=re.compile('<div class="content">\\n<p>(.*?)</div>',re.S)
	contents=re.findall(re_content,newurl_html)
	print(title)
	for content in contents:
		content=content.replace('<p>','')
		content=content.replace('</p>','')
		content=content.replace('<strong>','')
		content=content.replace('</strong>','')
		print(content)

for newurl in get_url_num(get_html(url)):
	get_content(newurl)
