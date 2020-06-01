import requests 
from bs4 import BeautifulSoup
import pprint


def set_up(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    links = soup.select('.storylink')
    subtext = soup.select('.subtext')
    return create_custom_news(links, subtext)


def sort_stories_by_votes(news_list):
    return sorted(news_list, key= lambda item: item['votes'], reverse = True)


def create_custom_news(links, subtext):
    news = []
    for index, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                news.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(news)


url = "https://news.ycombinator.com/news?p=1"


pprint.pprint(set_up(url))
