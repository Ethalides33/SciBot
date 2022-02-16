import os
import discord
import requests
import json
import random
from discord.ext import commands

import words
import articles

bot = commands.Bot(command_prefix='scibot ', case_insensitive=True)

@bot.event
async def on_ready():
  print("I am ready! Logged in as {0.user}".format(bot))


@bot.command(help="Says hello in a random language.",
        brief="Says hello.")
async def hello(ctx):
  await ctx.channel.send((random.choice(words.HELLO)).capitalize()+", "+ ctx.author.name + ".")


def to_lower(string):
  return string.lower()


@bot.command(help="Finds an article in the litterature (Nature and Elservier) according to the keyword / author specified.",
        brief="Looks for an article in the litterature.")
async def article(ctx, typeofsearch:to_lower, info:to_lower):
  await ctx.channel.send("Got it, " + ctx.author.name + ". Let me have a look...")

  if typeofsearch == 'keyword':
    titre, author,url=articles.from_keyword(info)
    await ctx.channel.send("I found the following: \"{0}\", by {1}. See {2} for more information.".format(titre,author,url))
  elif typeofsearch == 'author':
    titre, author, url = articles.from_author(info)
    await ctx.channel.send("I found the following: \"{0}\", by {1}. See {2} for more information.".format(titre,author,url))


@bot.command(help="Browses science news feeds to look for n news articles related to science and technology",
        brief="Looks for an article in the news.")
async def news(ctx, nbr:int):
  await ctx.channel.send("Got it, " + ctx.author.name + ". Let me have a look...")
  items = articles.from_popular(nbr)
  #print(items)
  string = ''
  for item in items:
    string += '* ' + item.title + '. See <' + item.link + '> for more information.\n\n'
  await ctx.channel.send("I found the following news articles:\n\n " + string)


@bot.command(help="Way too long story about me.",
        brief="Tells you about me.")
async def about(ctx):
  await ctx.send("Hello, my name is Scibot and I'm a sexy scientist (Hence, not real). I can help you to stay aware of what is happening in research science all over the world. Or you can use several keywords in order to refine your search about a specific author, domain or subject. Here is the list of existing commands : \n - help : do not worry anymore, Scibot is here to help you interact with him by granting a list of the available commands! \n - author + 'name' : wanna learn more about the work of a particular scientist that caught your eye? Scibot is always here to help! \n - keyword + 'subject keyword' : wanna learn more about a particular subject? Scibot will help you grasp it and make it yours! \n - popular + 'subject keyword' : what has been trending this past year in the 'subject keyword' field? Discover it now with Scibot! \n - hot : hey, do you know what is the hot topic that has shaken the scientific community this past month? It's time to flex in high-society dinner thanks to Scibot! \n - mystery words? : I have a few Easter-eggs commands, can you find them all? Here are a few indices : I have a thing for polite people and I love being praised... :smirk: \n NOTE : all the articles currently issued by Scibot are collected using Springer-Nature API. Other articles sources might follow : keep in touch!")

@bot.event
async def on_command_error(ctx, error):
  if isinstance(error,commands.MissingRequiredArgument):
    await ctx.send('I need more information. Please try again. Type \"scibot help\" for more information.')
  if isinstance(error, commands.CommandNotFound):
    await ctx.send('I did not understand. Please try again. Type \"scibot help\" for more information.')


bot.run(os.environ['DISCORD_TOKEN'])
