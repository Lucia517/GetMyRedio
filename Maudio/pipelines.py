# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from curses import meta
import imp
from urllib.request import Request
from itemadapter import ItemAdapter
from scrapy.pipelines.files import FilesPipeline
from .items import MaudioItem
import scrapy
class MaudioPipeline:
    def process_item(self, item, spider):
        return item
# class MaudioPipeline(FilesPipeline):
 
#     # item['url']为音乐请求地址，item['name']为音乐名
#     def get_media_requests(self, item, info):
#         # print(item['audUrls'])
#         file_url = item['audUrls']
#         print(type(file_url))
#         # yield scrapy.Request(item['audUrls'], meta={'name': item['name']})
#         yield scrapy.Request(url=file_url, meta={'name': item['name']})
 
#     def file_path(self, request, response=None, info=None, *, item=None):
#         # print()
#         filename=request.meta['name']
#         file_path = '/home/chenlu/miandianaudio/Maudio/audiomp3'+filename
#         # print(file_path)
#         return file_path
 
#     def item_completed(self, results, item, info):
#         # print(results)
#         return item