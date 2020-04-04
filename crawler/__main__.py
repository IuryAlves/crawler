# coding: utf-8

import asyncio
import sys
import json


from os.path import dirname, abspath, join
from crawler import Crawler
from file_utils import list_files


basedir = abspath(dirname(dirname(__file__)))
queries_dir = 'queries'


def crawl():
    results = []
    queries = []
    loop = asyncio.get_event_loop()
    for query in list_files(join(basedir,  queries_dir), filter_by_extensions=['json']):
        queries.append(query)
    for query in queries:
        urls = query.get('urls', [])
        while len(urls) > 0:
            futures = []
            urls_slice = urls[:500]
            del urls[:500]
            for url in urls_slice:
                crawler = Crawler(url, query.get("queries", {}))
                futures.append(crawler.crawl_async())
            results = loop.run_until_complete(asyncio.gather(*futures))

    json.dump(results, sys.stdout, indent=2)
    loop.close()


if __name__ == '__main__':
    crawl()
