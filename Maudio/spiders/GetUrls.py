from turtle import st
import scrapy


class GeturlsSpider(scrapy.Spider):
    name = 'GetUrls'
    allowed_domains = ['mrtv.gov.mm']
    start_urls = ['https://mrtv.gov.mm/mm/radio?qt-radio=1&page=0']
    #https://mrtv.gov.mm/mm/radio?qt-radio=0&page=1
    

    def parse(self, response):
        # print("parse-->", response.text)
        # demain = 'https://mrtv.gov.mm/mm/radio'
        audio_urls = response.xpath('//*[@id="quicktabs-tabpage-radio-0"]/div/div[1]/div/div/span/div/div[1]/a/@href')
        for audio_url in audio_urls:
            finall_url = "https://mrtv.gov.mm/"+audio_url.extract()
            with open("redio_program.txt","a+")as f:
                f.write(finall_url+'\n')
            # print(finall_url)
        
        for i in range(1,7):
            print("已完成"+str(i)+"页链接爬取")
            url = 'https://mrtv.gov.mm/mm/radio?qt-radio=0&page='+str(i)
            yield scrapy.Request(url,callback=self.parse,dont_filter = False)


