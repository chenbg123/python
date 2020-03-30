import json
import requests
import time
from jsonpath import jsonpath

class LagouSpider():

    def __init__(self):
        #原始url
        self.base_url="https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput="

        #实际需要爬取的url
        self.second_url="https://www.lagou.com/jobs/positionAjax.json?"

        self.headers={
            #'Accept': 'application/json, text/javascript, */*; q=0.01',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
            'Referer': 'www.lagou.com/jobs/list_python/p-city_2?px=default'
        }

        self.page=1
        self.timeout=3

        self.form_data={
            "first": 'true',
            "pn": self.page,
            "kd":input("please enter an occupation:")
        }

        self.params={
            'city':input("please enter a city:"),
            'needAddtionalResult':'false'
        }

        #在列表中储存字典
        self.item_list=[]

    def main(self):
        while True:
        #while self.page<=3:
            response=self.send_request()
            r=self.parse_page(response)
            self.page+=1
            #注意要修改字典里的值！
            self.form_data['pn']=self.page
            if r==True:
                break
            #self.timeout+=
        #print(self.item_list)
        self.save_data()

    def send_request(self):
        print("[INFO]: send request {} {} ".format(self.second_url,self.page))
        response=requests.post(self.second_url,params=self.params,data=self.form_data,headers=self.headers, cookies=self.get_cookie(), timeout=self.timeout+2)  # 获取此次文本
       # time.sleep(5)
       # response.encoding=response.apparent_encoding
        return response


    def get_cookie(self):
        #建立session
        s=requests.Session()
        #获取首页的cookie
        s.get(self.base_url,headers=self.headers,timeout=self.timeout)
        #为此次获取的cookie
        cookie=s.cookies
        return cookie


    def parse_page(self,response):
        text=json.loads(response.content)
        #info=text['content']['positionResult']['result']
        info=jsonpath(text,"$..result")[0]

        if len(info)==0:
            return True
        #建立一个字典
        #注意List和str的相互转换方法
        for i in info:
            item = {}
            item['公司']=i['companyFullName']
            print("\n"+"公司"+" : "+str(item['公司']))
            item['职位'] = i['positionName']
            print("职位"+" : "+str(item['职位']))
            item['技能'] = i['skillLables']
            print("技能"+" : "+str(item['技能']))
            item['创建时间'] = i['createTime']
            print("创建时间"+" : "+str(item['创建时间']))
            item['城市']=i['city']
            print("城市"+" : "+str(item['城市']))
            item['工资'] = i['salary']
            print("工资"+" : "+str(item['工资']))
            self.item_list.append(item)
        return False


    #保存数据，不能向文件中保存列表或者字符串，必须转换成字符串，所以转换成json字符串
    #主要dump和dumps 的区别
    def save_data(self):
        #lagou=json.dumps(self.item_list)
        with open('lagou.json','w') as f:
            #f.write(lagou)
            json.dump(self.item_list,f)

if __name__ == '__main__':
    spider=LagouSpider()
    spider.main()


