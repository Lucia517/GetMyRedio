from gc import callbacks
import imp
from tkinter import N
from urllib.request import Request
import scrapy
import re
import wget
from ..items import MaudioItem

class Getmp3urlSpider(scrapy.Spider):
    name = 'GetMp3Url'
    # allowed_domains = ['mrtv.gov.mm']
    # start_urls = ['http://mrtv.gov.mm/']
    def start_requests(self):
        with open('./audio_urls.txt','r')as f:
            content_urls = f.readlines()
            # content_urls = ['https://www.churchofjesuschrist.org/'+c.strip() for c in content_urls]
            # print(content_urls)
        for i in content_urls:
            i=i.replace("\n","")
            # print(i)
            yield scrapy.Request(i,self.parse)



    def parse(self, response):
        clAudio = re.findall('"mp3":"(.*)"}],"s',response.text,re.S)
        # wget.download(clAudio[0],out=None)
        clAudioName = re.findall('[^/]+(?!.*mp3)',clAudio[0],re.S)
        item = MaudioItem()
        item['audUrls'] = clAudio[0]
        item['name'] = clAudioName
        with open('mp3_urls.txt','a+')as f:
            f.write(item['audUrls']+'\n')
        # print(item['audUrls'])
        # wget.download(item['audUrls'],out='/home/chenlu/miandianaudio/Maudio/audiomp3'+item['name'])

        # print(item)
        # yield item
        # print(clAudio[0])
        # print(clAudioName[0])
        # clContent = response.xpath('//*[@id="main"]//p/text()')
        # for i in clContent:
        #     item = {}
        #     item['clcontent'] = i.extract()
        #     print(item)
        #     yield item
        # print(response.url)
