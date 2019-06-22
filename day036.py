import requests

url=' <div class="op-tieba-general-lookmore op-tieba-general-mainpl"><a href="http://www.baidu.com/link?url=eL9eZiFGhJgvEc3-eli9SC072o51oWLlEUfreqWuukcN1SMqZ8KxjaZcISvSq1BL8vDCNn9E_y90usxmZbLhx_" target="_blank">查看更多<em>joker</em>吧的内容&gt;&gt;</a></div>'
response = requests.get(url)
res = url.split('<')
print(res)
for url in res:
    if 'href' in url:
        res2 = url.split('>')[0]
        print(res2)
        res3=res2.split('=')
        print(res3)
content = response.content
with open(res,'wb') as f:
        f.write(content)