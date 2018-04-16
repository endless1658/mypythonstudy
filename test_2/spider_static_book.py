import requests
from bs4 import BeautifulSoup
import re
def geturl(url):
    '''
    :param url:目录的url
    :return: 所有章节的url列表
    '''
    if url is None:
        return
    url_list=[]
    html=htmlDownload(url)
    soup=BeautifulSoup(html,'html.parser',from_encoding='utf-8')
    dds=soup.find_all('dd')
    for dd in dds:
        a=dd.a['href']
        # print(a)
        url_list.append(a)
    return url_list
def htmlDownload(url):
    '''
    html下载器
    :param url:某一章节的url
    :return: html的内容
    '''
    if url is None:
        return
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    headers={'User-Agent':user_agent}
    r=requests.get(url,headers=headers)
    if r.status_code==200:
        r.encoding=r.apparent_encoding
        return r.text
    return None
def htmlparser(html):
    '''
    :param html:html内容
    :return:正则匹配的章节名和内容
    '''
    s=re.compile('<h1>(.*?)</h1>.*?<div id="content">(.*?)</div>',re.S)
    chapter=s.findall(html)[0]
    return chapter


def ouput(chapter):
    '''
    将数据存入文本中
    :param chapter:
    :return:
    '''
    #print(chapter)
    title = chapter[0]
    content = chapter[1].replace('<br/>', '\n')
    #print(title)
    with open('动画世界大冒险.txt', 'a') as f:
        f.writelines(title)
        f.writelines(content)
if __name__ == '__main__':
    url="https://www.biquge5200.com/70_70486/"
    urls=geturl(url)
    print(len(urls))
    for url1 in urls:
        try:
            html=htmlDownload(url1)
            chapter=htmlparser(html)
            ouput(chapter)
            print('正在爬取%s'%chapter[0])
        except Exception as e:
            print(e)
            print(url1,'爬取失败')


