# tests/test_news.py
import unittest

from client import News

class NewsTest(unittest.TestCase):
    # tester la méthode top-headlines
    def test_top_headlines(self):
        news = News()
        articles = news.top_headlines("fr")
        assert type(articles) == list
        assert len(articles) > 0



    #tester la méthode search keyword
    def test_search_keyword(self):
        news = News()
        articles = news.search_keyword("shark")
        assert type(articles) == list
        assert len(articles) > 0
