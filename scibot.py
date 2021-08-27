import os
import discord
import requests
import json
import random

client = discord.Client()
NATURE_TOKEN = "7badc2a1440f13ae514eff5b58b32f90"

HELLO = ['Hi','Hello','Bonjour','Salut','Hallo','Holà','안녕하십니까','你好','dzień dobry','こんにちは','Kon\'nichiwa','Nǐ hǎo','Annyeonghasibnikka','Hei','Merhaba','Alo','أهلا','Ahlan','שלום','Ciao','สวัสดี','S̄wạs̄dī','Здравствуйте','Zdravstvuyte','Xin chào','Ahoj','Zdravo','Привет','Privet','салам','Salam','Sveiki','Tere','გამარჯობა','gamarjoba','tena koutou','Sawubona','Helo','Halo','नमस्ते','Namastē','nuqneH','Olá','Máriessë','aloha','γεια σας','geia sas','Salve','Përshëndetje']

TY = ['You\'re welcome','Ask whenever','My pleasure','Hope this helped!']


def get_article_from_keyword(keyword):
  req = "http://api.springernature.com/metadata/json?q=keyword:" + keyword + "&p=1&api_key="+NATURE_TOKEN
  article = requests.get(req)
  formatted =article.json()
  return(formatted['records'][0]['title'],formatted['records'][0]['creators'][0]['creator'], formatted['records'][0]['url'][0]['value'])

def get_article_from_author(author):
  req = "http://api.springernature.com/metadata/json?q=name:" + author + "&p=1&api_key="+NATURE_TOKEN
  article = requests.get(req)
  formatted =article.json()
  return(formatted['records'][0]['title'],formatted['records'][0]['creators'][0]['creator'], formatted['records'][0]['url'][0]['value'])

def get_popular_article():
  req = "https://api.elsevier.com/content/abstract/citations?doi=10.1016%2FS0014-5793(01)03313-0&apiKey=7f59af901d2d86f78a1fd60c1bf9426a&httpAccept=application%2Fjson"
  article = requests.get(req)
  print(article)
  formatted =article.json()
  print(formatted)


@client.event
async def on_ready():
  print("I am ready! Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith("scibot "):
    l = message.content.split()
    if l[1] == "author":
      await message.channel.send("Got it, " + message.author.name + ". Let me have a look...")
      titre, author, url = get_article_from_author(l[2])
      await message.channel.send("I found the following: \"{0}\", by {1}. See {2} for more information.".format(titre,author,url))

    elif (l[1] in HELLO) :
      await message.channel.send(random.choice(HELLO)+", "+ message.author.name + ".")

    elif (l[1] == "Yay") :
      await message.channel.send("Yeeeeeeeeeey")

    elif (l[1] == "I" and l[2] == "love" and l[3] == "u") :
      await message.channel.send("I know, I'm often told that baby :smirk::sunglasses:")

    elif (l[1] == "Thank" and l[2] == "you") :
      await message.channel.send(random.choice(TY) +", "+ message.author.name + ".")

    elif(l[1] == 'keyword'):
      await message.channel.send("Got it, " + message.author.name + ". Let me have a look...")
      titre, author,url=get_article_from_keyword(l[2])
      await message.channel.send("I found the following: \"{0}\", by {1}. See {2} for more information.".format(titre,author,url))

    elif(l[1] == 'popular'):
      await message.channel.send("Got it, " + message.author.name + ". Let me have a blup...")
      titre, author,url=get_popular_article(l[2])
      await message.channel.send("I found the following: \"{0}\", by {1}. See {2} for more information.".format(titre,author,url))
    
    elif(l[1] == 'help'):
      await message.channel.send("Hello, my name is Scibot and I'm a sexy scientist (Hence, not real). I can help you to culture yourself by searching articles using keywords or author you request, but I also like being praised so don't be shy :smirk: .")
    elif (l[1] == 'hot'):
      get_popular_article()
    else:
      await message.channel.send("I am sorry, but I did not understand. Type \"scibot help\" for more information on how to use me.")
    



client.run(os.environ['DISCORD_TOKEN'])
