import requests
import json
import os
import feedparser

NATURE_TOKEN = os.environ['NATURE_TOKEN']

def from_keyword(keyword):
  req = "http://api.springernature.com/metadata/json?q=keyword:" + keyword + "&p=1&api_key="+NATURE_TOKEN
  article = requests.get(req)
  formatted =article.json()
  return(formatted['records'][0]['title'],formatted['records'][0]['creators'][0]['creator'], formatted['records'][0]['url'][0]['value'])

def from_author(author):
  req = "http://api.springernature.com/metadata/json?q=name:" + author + "&p=1&api_key="+NATURE_TOKEN
  article = requests.get(req)
  formatted =article.json()
  return(formatted['records'][0]['title'],formatted['records'][0]['creators'][0]['creator'], formatted['records'][0]['url'][0]['value'])

def from_popular(n):
  news = feedparser.parse("https://www.sciencedaily.com/rss/top/technology.xml")
  return news.entries[:n]
