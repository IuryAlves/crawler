# coding: utf-8

import logging
import aiohttp

from lxml import html

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0)'


class AsyncCrawler:

    def __init__(self, url, selectors, max_concurrency=200):
        self.url = url
        self.selectors = selectors
        self.session = aiohttp.ClientSession()

    async def _http_request(self, url):
        print('Fetching: {}'.format(url))
        try:
            async with self.session.get(url, timeout=30, headers={'User-Agent': USER_AGENT}) as response:
                content = await response.read()
        except Exception as e:
            logging.warning('Exception: {}'.format(e))
        else:
            return content

    async def extract_async(self, url):
        data = await self._http_request(url)
        if data:
            return self.parser(data)
        return None

    def parser(self, data):
        raise NotImplementedError

    async def crawl_async(self):
        results = await self.extract_async(self.url)
        await self.session.close()
        return results


class Crawler(AsyncCrawler):

    def parser(self, data):
        dom = html.fromstring(data)
        result = {}
        for key, value in self.selectors.items():
            element = dom.cssselect(value)
            if element:
                result[key] = element[0].text
        return result
