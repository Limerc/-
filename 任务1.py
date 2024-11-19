# 模板代码
# import urllib.request
#
# fp = urllib.request.urlopen(r'https://www.python.org')
# print(fp.read(100))  # 输出前100个字节（二进制数据）
# print(fp.read(100).decode()) # 输出前100个字节并解码
# fp.close()

import urllib.request

try:
    # 设置超时时间为5秒
    url = 'https://www.baidu.com'
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req, timeout=5) as response:
        # 分块读取数据
        data = []
        block_size = 1024  # 每次读取1024字节
        while True:
            block = response.read(block_size)
            if not block:
                break
            data.append(block)
        content = b''.join(data)
        decoded_content = content.decode('utf - 8')
        print(decoded_content)
except urllib.request.URLError as e:
    print(f"网络请求出现错误: {e}")
except Exception as ex:
    print(f"其他错误: {ex}")