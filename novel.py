# #怎么发送请求
# #pip install requests
# #发送给谁
# import requests
# from lxml import etree
# url = 'https://dl.131437.xyz/book/douluodalu1/1.html'
# while True:
# #伪装自己 
#   headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
#   }
#   #发送请求
#   resp = requests.get(url,headers = headers)
#   #响应信息
#   resp.encoding = 'utf-8'
#   # print(resp.text)

#   e = etree.HTML(resp.text)
#   info = '\n' .join(e.xpath('//div[@class ="m-post"]/p/text()') ) 
#   title = e.xpath('//h1/text()')[0]
#   url =f'https://dl.131437.xyz{e.xpath("//tr/td[2]/a/@href")[0]}' 
#   # print(info)
#   # print(title)
#   #保存


# 安装所需的库
# pip install requests
# pip install lxml

import requests
from lxml import etree

url = 'https://dl.131437.xyz/book/douluodalu1/1.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
}
stop_url = 'book/douluodalu1'  # 假设这是你用来判断是否停止的URL
chapters = []

while url and not url.endswith(stop_url):
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    html_parser = etree.HTML(response.text)

    title = html_parser.xpath('//h1/text()')[0]
    content = '\n'.join(html_parser.xpath('//div[@class="m-post"]/p/text()'))
    
    # 下一章的URL
    next_url_path = html_parser.xpath("//tr/td[2]/a/@href")
    if next_url_path:
        url = f'https://dl.131437.xyz{next_url_path[0]}'
    else:
        url = None

    # 将章节标题和内容存储到列表中
    chapters.append(f"{title}\n\n{content}\n\n")
    
    print(f"已完成 {title} 的抓取。")

# 当所有章节抓取完成后，将列表中的内容写入文件
with open('斗罗大陆全集.txt', 'w', encoding='utf-8') as file:
    for chapter in chapters:
        file.write(chapter)

print("所有章节已全部抓取并保存至斗罗大陆全集.txt")
 