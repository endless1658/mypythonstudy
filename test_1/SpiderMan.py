from URLManager import URLManager
from DataOutput import DataOutput
from HtmlParser import HtmlParser
from HtmlDownloader import HTMLDownloader

class Spiderman(object):
    def __init__(self):
        self.manager=URLManager()
        self.parser=HtmlParser()
        self.downloader=HTMLDownloader()
        self.output=DataOutput()
    def crawl(self,begin_url,url_number):
        '''

        :param begin_url: 初始url
        :return:
        '''
        self.manager.add_new_url(begin_url)
        # 判断url管理器中是否有新的url，同时判断抓取了多少个url
        size=1
        while (self.manager.has_new_url() ):
           try:
                # 从URL管理器获取新的url
                new_url = self.manager.get_new_url()
                # HTML下载器下载网页
                html = self.downloader.Download(new_url)
                # HTML解析器抽取网页数据
                new_urls,data = self.parser.Parser(new_url,html)
                # 将抽取到url添加到URL管理器中
                self.manager.add_new_urls(new_urls)
                # 数据存储器储存文件
                self.output.store_data(data)
                print("已经抓取%d个链接" %size)

           except Exception as e:
                print("crawl failed")
                print(e)
           if(size==url_number):
                break
           size = size + 1
                #print(e.reason)
        # 数据存储器将文件输出成指定格式
        self.output.output_html()

if __name__ == "__main__":
    spider_man = Spiderman()
    spider_man.crawl('https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB',100)