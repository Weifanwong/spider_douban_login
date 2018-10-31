# -*- coding: utf-8 -*-
import scrapy


class XlwbSpider(scrapy.Spider):
	name = 'xlwb_login'
	#allowed_domains = ['weibo.com']
	#start_urls = ['http://weibo.com/']
	headers = {

#    'Accept': '*/*',
# 'Accept-Encoding': 'gzip, deflate, br',
# 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
# 'Cache-Control': 'max-age=0',
# 'Connection': 'keep-alive',
# #'Content-Length': '87',
# 'Content-Type': 'application/x-www-form-urlencoded',
'Cookie': 'login=13a0857768fc0c0abafd3d70c0f4538a; SINAGLOBAL=172.16.138.138_1540969570.352783; Apache=172.16.138.138_1540969570.352786; SCF=AiFI7t5ns6NmP-dtBL7T3tygR0jYjOw3CKIn0r48rYiBO3ToOYOavq0CSaEVa9UrOgcJC6bXIMhOjmQdfLMFgaA.; U_TRS1=00000054.6ba4d907.5bd965e3.b0e6cc60; U_TRS2=00000054.6bafd907.5bd965e3.c8ad7c9b; UOR=my.sina.com.cn,www.sina.com.cn,; ULV=1540974084776:1:1:1:172.16.138.138_1540969570.352786:; SGUID=1540974087714_19780280; SessionID=octmqed671dpt0m9s05fkfp2r3; SSO-DBL=903b2dfe558d757c50a86dbd7d018964; SUB=_2AkMshRcidcPxrAZVmf4dzGrrZY5H-jyfUH7UAn7tJhMyAhh77gksqSVutBF-XD3jqQ1b6V4UUs4JLKH_Bfa9zfVW; SUBP=0033WrSXqPxfM72wWs9jqgMF55529P9D9Whh4h34Gi_jawDnV6vY-g4n5JpVF02ReoefShBpeK2p; ULOGIN_IMG=yf-45060f0453229a5e50ab2c2b0ead0954128c',
#  'DNT': '1',
# #'Host': 'login.sina.com.cn',
#  'Origin': 'https://weibo.com',
#  'Referer': 'https://weibo.com/',
#  'Upgrade-Insecure-Requests': '1',
 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    }


	def start_requests(self):
		url = 'https://weibo.com/'
		yield scrapy.Request(url=url,headers = self.headers,  callback=self.parse)
    
	def parse(self, response):
		print(response.text)
		# test = response.xpath('//span[@class="tit"]//text()').extract()
		# img_url = response.xpath('//img[@node-type="verifycode_image"]/@src').extract()
		# user_name = get_user_name('18235441111'):
		# sp = get_password('1q2w3e4r')
		# data = {
		# 'entry': 'account',
		# 'gateway': '1',
		# 'su': user_name,
		# 'servertime':servertime,
		# 'sp': password,
		# 'nounce':nounce,
		# }


		#print(response.text)
