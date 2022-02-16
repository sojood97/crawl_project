import scrapy
from scrapy.http import FormRequest
import itertools

class SpideripSpider(scrapy.Spider):
    name = 'spiderip'
    start_urls = ['https://me.motorsport.com/']
    resulted_data = {}
    counter=0

 
        
    def parse(self, response):
        self.scraping_data(response)

        yield FormRequest(
            url="https://me.motorsport.com/f1/news/?p=2",
            callback=self.parse_page2
        )

    def parse_page2(self, response):  
        self.scraping_data( response)

        yield FormRequest(
            url="https://me.motorsport.com/f1/news/?p=3",
            callback=self.parse_page3
        )
  
    def parse_page3(self, response):
        self.scraping_data(response) 
        
        yield FormRequest(
            url="https://me.motorsport.com/f1/news/?p=4",
            callback=self.parse_page4
        )

    def parse_page4(self, response): 
        self.scraping_data( response)

        yield dict(itertools.islice(self.resulted_data.items(), 0,25,1))  
        yield dict(itertools.islice(self.resulted_data.items(), 25,50,1))
        yield dict(itertools.islice(self.resulted_data.items(), 50,75,1))
        yield dict(itertools.islice(self.resulted_data.items(), 75,100,1))
        yield dict(itertools.islice(self.resulted_data.items(), 100,125,1))
        yield dict(itertools.islice(self.resulted_data.items(), 125,150,1))
        yield dict(itertools.islice(self.resulted_data.items(), 150,175,1))
        yield dict(itertools.islice(self.resulted_data.items(), 175,200,1))
        yield dict(itertools.islice(self.resulted_data.items(), 200,225,1))


    def scraping_data(self, response):
        data=response.xpath('//*')
        for data_scrapped in data:
            title = data_scrapped.xpath('.//div[@class="ms-item_info"]/a[@class="ms-item_link ms-item_link--text"]/text()').extract()
            text  = data_scrapped.xpath('.//p[@class="ms-item_subheader"]/text()').extract()
            img_url=data_scrapped.xpath('.//div[@class="ms-item_thumb"]/a[@class="ms-item_link"]/picture/img/@src').extract()
            category=data_scrapped.xpath('.//div[@class="ms-item_info-top"]/div[@class="ms-item_series"]/span[@class="ms-item_series--title"]/text()').extract()
            self.resulted_data[self.counter] = {
                'text': text,
                'title': title,
                'category': category,
                'img_url' :img_url,
            }
           
            self.counter=self.counter+1

        


        

   


    
    
    
        
