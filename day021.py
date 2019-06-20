import urllib.request
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36'}
url = 'http://www.baidu.com'
#构建代理
proxy_handle = {
    'http':'http://163.204.240.162:9999'
}
request = urllib.request.Request('http://www.baidu.com')
response = urllib.request.urlopen(request)
if response.status!=200:
    #处理代理
    proxy_handle = urllib.request.ProxyHandler(proxy_handle)
    #构建代理
    opener = urllib.request.build_opener(proxy)
    # request = urllib.request.Request(url=url)
    response = urllib.request.urlopen(request)
    print(response.status)
else:
    print('爬取失败')
   