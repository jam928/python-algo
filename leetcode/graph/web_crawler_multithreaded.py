from collections import deque
from concurrent import futures
from typing import List

# https://leetcode.com/problems/web-crawler-multithreaded/description/
# T: O(N * L) Where n is the number unique URL's created and L is the avg number of urls per page
# S: O(N * L)

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:

        # split start url to retrieve only the hostname
        hostname = lambda url: url.split('/')[2]
        visited = set()

        visited.add(startUrl)
        with futures.ThreadPoolExecutor(max_workers=16) as executor:
            tasks = deque([executor.submit(htmlParser.getUrls, startUrl)])

            while tasks:
                for url in tasks.popleft().result():
                    if url not in visited and hostname(startUrl) == hostname(url):
                        visited.add(url)
                        tasks.append(executor.submit(htmlParser.getUrls, url))

        return list(visited)