
from lxml import etree

# 获取所有的tr标签
# 获取第2个tr 标签
# 获取所有的class 等于even的tr标签
# 获取所有a 标签的hre属性
# 获取所有的职位信息（纯文本）

def parse_tencent_file():
    parser=etree.HTMLParser(encoding='utf-8')
    htmlElement=etree.parse('tencent.html',parser=parser)

    # 获取所有的tr标签
    # //tr
    # xpath 函数返回的是列表
    trs=htmlElement.xpath("//tr")
    for tr in trs:
       print(etree.tostring(tr,encoding='utf-8').decode('utf-8'))


    # 获取第2个tr 标签
    # //tr[2]
    tr=htmlElement.xpath("//tr[2]")[0]
    print(etree.tostring(tr,encoding='utf-8').decode('utf-8'))

    # 获取所有的class 等于even的tr标签
    # //tr[@class='even']
    trs=htmlElement.xpath("//tr[@class='even']")
    for tr in trs:
        print(etree.tostring(tr,encoding='utf-8').decode('utf-8'))

    # 获取所有a 标签的hre属性,爬取到详细的url的值
    # //a/@href,  注意与 //a[@href] 区别
    aList=htmlElement.xpath("//a/@href")
    # xpath 返回列表, 但是获取的 href 值已经是字符串，所有不需要转换
    # 当前获取的url是后半段， 跳转网页时，浏览器加上前面域名组成完整的url
    for a in aList:
       print("http://hr.tencent.com/"+a)

    # 获取所有的职位信息（纯文本）
    # 用text()函数
    # 获取从第二个开始的所有tr标签
    positions=[]
    trs=htmlElement.xpath("//tr[position()>1]")
    for tr in trs:
        # 获取一个 tr 标签里面的 a 标签, 当写'/a'时不能直接匹配到,而写'//a'时会忽略当前标签跳转到全局里匹配，
        # 想要在当前标签下获取某个标签,使用 ".//a"
        href=tr.xpath(".//a/@href")
        # 注意·xpath返回的是列表，不能直接加字符串
        fullurl="http://hr.tencent.com/"+ href[0]
        # 获取所有 a 标签的文本
        title=tr.xpath(".//a/text()")[0]
        # 第二种获取方法：
        # title=tr.xpath("./td[1]//text()")[0]
        category=tr.xpath("./td[2]/text()")[0]
        nums=tr.xpath("./td[3]/text()")[0]
        address=tr.xpath("./td[4]/text()")[0]
        pubtime=tr.xpath("./td[5]/text()")[0]

        position={
            'url':fullurl,
            'title':title,
            'catagory':category,
            'nums':nums,
            'address':address,
            'pubtime':pubtime
        }
        positions.append(position)

    print(positions)

if __name__ == '__main__':
    parse_tencent_file()