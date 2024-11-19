# 导入数据请求模块
import requests
# 导入数据解析模块
import parsel

# 定义请求头
headers = {
    # Cookie 用户信息，常用于检测是否有登录账号
    'Cookie': "_ga=GA1.2.1930843405.1731741854; _gid=GA1.2.425953489.1731741854; _ga_PJ0N20S6JN=GS1.2.1731741854.1.1.1731741872.42.0.0",
    # User-Agent 用户代理，表示浏览器/设备的基本身份信息
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
}
# url 地址
url = "https://www.quanben.io/n/mingyiguinu/list.html"
# 用requests库发送请求，注意请求参数与请求方法（GET获取信息/POST传递信息）
response = requests.get(url=url, headers=headers)

# 获取响应文本数据(html字符串数据)
html = response.text
# 转换为可解析的对象
selector = parsel.Selector(html)
# 提取书名：.info-name利用class类名进行定位，h1定位h1标签，::text获取标签内文本内容
title = selector.css("h1[itemprop='name headline']::text").get()
print(title)

# 提前章节ID和章节名
chapter_titles = selector.css(".list3 li a span[itemprop='name']::text").getall()
print(chapter_titles)
# 章节ID是href=的值，利用::attr获取href属性值
chapter_ids = selector.css(".list3 li a::attr(href)").getall()
print(chapter_ids)

# for循环遍历获取列表中的元素
for chapter_title, link in zip(chapter_titles, chapter_ids):
    # print(chapter_title)
    link_url = "https://www.quanben.io" + link
    # print(link_url)
    # 发送请求，获取响应文本数据
    link_data = requests.get(url=link_url, headers=headers).text
    # 解析数据提取小说内容
    link_selector = parsel.Selector(link_data)
    content_list = link_selector.css(".articlebody p ::text").getall()
    # 将列表合并成字符串
    content = "".join(content_list[1:]) # 去掉第一行(标题)
    with open(title + ".txt", mode="a", encoding="utf-8") as f:
        f.write(chapter_title)
        f.write("\n")
        f.write(content)
        f.write("\n")
