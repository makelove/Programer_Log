# -*- coding: utf-8 -*-
# @Time    : 2020/2/18 20:10
# @File    : middlewares_proxy_redis.py


"""
middlewares_proxy_redis.py:

使用Redis来控制 获取代理
Redis 5.0.7 (00000000/0) 64 bit
"""

import traceback
import redis
import logging

logger = logging.getLogger(__name__)


class redisProxy(object):
    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls(crawler)
        # crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)

        return s

    def __init__(self, crawler):
        self.red = redis.Redis(decode_responses=True)
        self.proxy_key = 'proxy'
        self.error_proxy_key = 'error_proxy'
        pass

    def process_request(self, request, spider):
        rs = self.red.zpopmax(self.proxy_key)  # 取出
        if len(rs) > 0:
            ip, score = rs[0]
            self.red.zincrby(self.proxy_key, score - 10, ip)  # 放回 score - 1
            # print(self.red.zscan(key))

            request.meta["proxy"] = ip
            logger.info(f'获得代理Redis {ip}\t{score}')
        else:
            logger.error('没有获得代理Redis')
            pass
        pass

    def process_response(self, request, response, spider):
        proxy = request.meta.get('proxy', '')
        logger.info(f'process_response 获得代理proxy{proxy}')  # TODO
        if proxy:
            if response.status != 200:
                # logger.info(f'代理失效{request.meta}')
                logger.error(f'代理失效response {response.status}')  # TODO 429

                self.red.zincrby(self.proxy_key, 3, proxy)  # 放到队尾 3-10=-7
                self.red.zincrby(self.error_proxy_key, -2, proxy)

                if response.status == 429:
                    self.red.zincrby(self.proxy_key, -100, proxy)  # 放到队尾 3-10=-7
                    logger.error(f'放到队尾 -100 {proxy}')  # TODO 429

            else:  # 正常情况
                self.red.zincrby(self.proxy_key, 7, proxy)
        else:
            logger.error('process_response 不能获取meta代理')

        return response
        pass

    def process_exception(self, request, exception, spider):
        try:
            logger.error('process_exception')
            logger.error(request.meta)
            logger.error(exception)
            # TODO
            proxy = request.meta.get('proxy', 'process_exception')
            self.red.zincrby(self.proxy_key, -2, proxy)  # 放回 score - 1
            self.red.zincrby(self.error_proxy_key, -2, proxy)
            logger.info(f'process_exception 获得代理proxy{proxy}')  # TODO
        except:
            print(traceback.format_exc())
        pass

    pass
