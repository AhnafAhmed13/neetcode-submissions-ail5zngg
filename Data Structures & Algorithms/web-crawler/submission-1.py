# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """
from collections import deque
class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        i = 7
        while i < len(startUrl):
            if startUrl[i] == "/": break
            i += 1
        hostname = startUrl[:i]
        urls = htmlParser.getUrls(startUrl)
        res = set([startUrl])
        urls = deque(urls)
        while urls:
            n = len(urls)
            for i in range(n):
                curr = urls.popleft()
                if curr.startswith(hostname):
                    res.add(curr)
                    crawl_res = htmlParser.getUrls(curr)
                    for url in crawl_res:
                        if url.startswith(hostname) and url not in res:
                            res.add(url)
                            urls.append(url)
        # print(startUrl, urls, res)
        return list(res)





