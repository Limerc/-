import scrapy


# 在Scrapy框架下实现BeautifulSoup库
class MySpider(scrapy.Spider):
    name = "beautifulsoup_spider"
    start_urls = [
        'https://www.quanben.io/n/mingyiguinu/list.html',  # 将其替换为你想爬取的URL
    ]

    def parse(self, response):
        # 使用 Scrapy 的选择器来提取页面标题
        title = response.xpath('//title/text()').get()
        print(f"Page title: {title}")

        # 查找所有链接
        for link in response.xpath('//a'):
            href = link.xpath('@href').get()
            text = link.xpath('text()').get()
            print(f"Found link: {href}, Link text: {text}")

            # 在实际项目中，你可以根据需要使用 response.follow 进行后续爬取
            if href and not href.startswith('#'):
                yield response.follow(href, callback=self.parse)

        # 提取段落内容
        paragraphs = response.xpath('//p/text()').getall()
        for p in paragraphs:
            print(f"Paragraph: {p}")

        # 提取图片的 src 属性和 alt 属性
        images = response.xpath('//img')
        for img in images:
            src = img.xpath('@src').get()
            alt = img.xpath('@alt').get()
            print(f"Image found: src={src}, alt={alt}")

        # 提取表格内容
        tables = response.xpath('//table')
        for table in tables:
            rows = table.xpath('.//tr')
            for row in rows:
                cells = row.xpath('.//td/text() | .//th/text()').getall()
                print(f"Table row: {cells}")

        # 提取页面中的所有标题 (h1 - h6)
        for i in range(1, 7):
            headers = response.xpath(f'//h{i}/text()').getall()
            for header in headers:
                print(f"H{i} Header: {header}")
