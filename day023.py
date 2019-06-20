import urllib.request
url = 'http://www.17k.com./chapter/2933095/36699279.html'
response=urllib.request.urlopen(url)
HTML = response.read().decode('utf8')
print(HTML)