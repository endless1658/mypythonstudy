class URLManager(object):
    def __init__(self):
        self.new_urls=set() #未爬去的url集合
        self.old_urls=set() #已爬去的url集合
    def has_new_url(self):
        '''
        判断是否有未爬去完的爬虫
        :return:
        '''
        return self.new_url_size()!=0
    def get_new_url(self):
        '''
        获取一个未爬去的爬虫
        :return:
        '''
        new_url=self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
    def add_new_url(self,url):
        '''
        将一个新的URL添加进未爬去的集合
        :return:
        '''
        if url is None:
            return
        if url not in self.new_urls or url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        '''
        将url集合添加进未爬去的集合中
        :param urls: url集合
        :return:
        '''
        if urls is None or len(urls)==0:
            return
        for url in urls:
            self.add_new_url(url)
    def new_url_size(self):
        '''
        获取未爬去的集合大小
        :return:
        '''
        return len(self.new_urls)
    def old_url_size(self):
        '''
        获取已爬去的集合大小
        :return:
        '''
        return len(self.old_urls)