from newspaper import Article
from bs4 import BeautifulSoup
import requests
def newsTitle(url):
    r = requests.get(url.strip())
    soup = BeautifulSoup(r.content, 'html.parser')
    title = soup.title.string
    return title
    # print '\nSummary: ', summary
    # print '\nPublish Date: ', publishDate
    # print '\nImage:', image
    
def newsSummary(url):
    article = Article(url.strip())
    article.download()
    article.parse()
    summary = article.text[0:150]#remove slice if you need entire article summary
    return summary

def newsPublishedDate(url):
    article = Article(url.strip())
    article.download()
    article.parse()
    publishDate = article.publish_date
    return publishDate

def imageUrl(url):
    article = Article(url.strip())
    article.download()
    article.parse()
    image = article.top_img
    return image
