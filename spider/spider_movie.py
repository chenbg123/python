
# 1.将目标网站页面爬取下来
import requests
import json
from lxml import etree

class movie_spider:

    def __init__(self):
        self.page = 1
        self.movies=[]

        self.base_url='https://www.dygod.net'
        self.page_url='https://www.dygod.net/html/gndy/dyzz/index.html'
        self.parse_url='https://www.dygod.net/html/gndy/dyzz/index_{}.html'

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
            'Referer': 'https://www.dygod.net/html/gndy/dyzz/index_3.html'
        }

    def main(self):
        while (self.page <6):
            if (self.page > 1):
                self.page_url = self.parse_url.format(self.page)
            text=self.send_request(self.page_url)
            self.parse_detail_page(text)
            self.page+=1
        self.save_data()

    def send_request(self,url):
            response=requests.get(url,headers=self.headers)
            # 如果产生乱码，先用text默认解析把数据拿出来，再对具体内容编码和解码
            text=response.content.decode('gbk')
            return text

    def parse_detail_page(self,text):
        urls=self.get_details_url(text)

        for url in urls:
            movie = {}
            text = self.send_request(url)
            html = etree.HTML(text)
            title = html.xpath("//h1/text()")[0]
            # for x in title
            # etree.tostring(x, encoding='utf-8').decode('utf-8')
            movie['title']=title
            # for x in title
            # etree.tostring(x, encoding='utf-8').decode('utf-8')
            zoom=html.xpath("//div[@id='Zoom']")[0]
            cover=zoom.xpath(".//img/@src")[0]
            movie['cover']=cover

            infos=zoom.xpath("./text()")
            for index,info in enumerate(infos):

                if info.startswith("◎年　　代"):
                    info=info.replace('◎年　　代',' ').strip()
                    movie['year']=info

                elif info.startswith('◎产　　地'):
                    info=info.replace('◎产　　地',' ').strip()
                    movie['country']=info

                elif info.startswith('◎类　　别'):
                    info=info.replace('◎类　　别',' ').strip()
                    movie['class']=info

                elif info.startswith('◎语　　言'):
                    info=info.replace('◎语　　言'," ").strip()
                    movie['language']=info

                elif info.startswith('◎豆瓣评分'):
                    info=self.parse_info(info,'◎豆瓣评分')
                    movie['douban_rating']=info

                elif info.startswith('◎片　　长'):
                    info=self.parse_info(info,'◎片　　长')
                    movie['duration']=info

                elif info.startswith('◎主　　演'):
                    info=self.parse_info(info,'◎主　　演')
                    actors=[info]
                    for x in range(index+1,len(infos)):
                        actor=infos[x].strip()
                        if actor.startswith('◎'):
                            break
                        actors.append(actor)
                    movie['actors']=actors

                elif info.startswith('◎简　　介'):
                    introduction=infos[index+1].strip()
                    movie['introduction']=introduction

            download=html.xpath("//td[@bgcolor='#fdfddf']/a/@href")
            if(len(download)==0):
                download=html.xpath('//div[@class="player_list"]//a/@href')
            movie['download']=download[0]
            self.movies.append(movie)


    def parse_info(self,info,rule):
        return info.replace(rule,' ').strip()

    def get_details_url(self,text):
        html = etree.HTML(text)
        urls = html.xpath("//table[@class='tbspan']//a/@href")
        # 等效于：
        # def abc(url):
        #     return self.base_url
        # index=0
        # for url in urls:
        #     url=abc(url)
        #     urls[index]=url
        #     index+=1
        urls=map(lambda url:self.base_url+url,urls)
        return urls

    def save_data(self):
        with open('movie.json','w') as fp:
            json.dump(self.movies,fp)

if __name__ == '__main__':
    spider=movie_spider()
    spider.main()






