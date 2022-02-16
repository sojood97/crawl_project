from deviceip.spiders.spiderip import SpideripSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

class CrawlerExecutor:
    def __init__(self, crawler_name=None, crawler_class=None, config=None, kwargs={}):
        self.config = config
        self.crawler_name = crawler_name
        self.crawler_class = crawler_class
        self.kwargs = kwargs
        super(__class__, self).__init__()
    def scrap(self):
        setting = get_project_settings()
        process = CrawlerProcess(settings=setting)
        process.crawl(self.crawler_class, config=self.config, **self.kwargs)
        process.start()

if __name__ == '__main__':
    print("Start scraping")
    CrawlerExecutor(crawler_name='deviceip',
                    crawler_class=SpideripSpider,
                    ).scrap()
    print("Finish scraping")