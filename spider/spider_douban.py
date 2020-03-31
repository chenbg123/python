
# 1.将目标网站页面爬取下来

import requests
import json
from lxml import etree

class douban_spider:



    def __init__(self):

        self.movies=[]
        self.url='https://movie.douban.com/cinema/nowplaying/beijing/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
            'Referer': 'https: // movie.douban.com /'
        }


    def main(self):
        text=self.send_request()
        self.parse_page(text)
        self.save_data()


    def send_request(self):
        response=requests.get(self.url,headers=self.headers)
        text=response.text
        return text

    def parse_page(self,text):

        htmlElement=etree.HTML(text)
        ul=htmlElement.xpath('//ul[@class="lists"]')[0]
        lis=ul.xpath("./li")
        for li in lis:
            title=li.xpath("@data-title")[0]
            duration=li.xpath("@data-duration")[0]
            region=li.xpath("@data-region")[0]
            direcotor=li.xpath("@data-director")[0]
            post=li.xpath(".//img/@src")[0]

            movie={
                'title':title,
                'duration':duration,
                'region':region,
                'director':direcotor,
                'post':post
            }

            self.movies.append(movie)

    def save_data(self):
        with open('douban.json','w') as fp:
            json.dump(self.movies,fp)





if __name__ == '__main__':
    spider=douban_spider()
    spider.main()






