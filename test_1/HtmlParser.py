import re
import urllib.parse
from bs4 import BeautifulSoup
class HtmlParser(object):
    def _get_new_urls(self,page_url,soup):
        '''
        抽取新的url集合
        :param page_url:下载页面的url
        :param soup:
        :return: 返回新的URL集合
        '''
        new_urls=set()
        links=soup.find_all('a',href=re.compile(r'/item/.*'))
        for link in links:
            #提取网站的尾部
            new_url=link['href']
            #用urljoin拼成完整网站
            new_full_url=urllib.parse.urljoin(page_url,new_url)
            new_urls.add(new_full_url)
        return new_urls


    def _get_new_data(self,page_url,soup):
        '''

        :param page_url:
        :param soup:
        :return:返回有效数据
        '''
        data={}
        data['url']=page_url


        title=soup.find('h1')
        #find('dd',class_='lemmaWgt-lemmaTitle-title').

        data['title']=title.get_text()

        summary=soup.find('div',class_='lemma-summary')
        data['summary']=summary.get_text()

        return data

    def Parser(self, page_url, html_cont):
        '''
        用于解析网页内容，抽取URL和数据
        :param page_url: 下载页面的url
        :param html_cont: 下载的网页内容
        :return:
        '''
        new_urls = set()
        new_data = {}
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data
