import os
import discord as disc
from bs4 import BeautifulSoup
import random as rand
from urllib.request import Request, urlopen
from keep_alive import keep_alive
import http.client as http
http.HTTPConnection._http_vsn = 10
http.HTTPConnection._http_vsn_str = 'HTTP/1.0'

client = disc.Client()

greetings = ['hi ','hello ','heyy ','hey ','sup ','what\'s up ','hii ','yo, ']
bot_names = ['B Bot','B-Bot','b bot','b-bot','bread bot','Bread Bot']

fullgreet = greetings+bot_names

@client.event
async def on_ready():
  print('{0.user}_online'.format(client))


@client.event
async def on_message(message):
  msg = message.content
  if message.author == client.user:
        return

  if any(word in msg for word in fullgreet):
    await message.channel.send('Hey! :two_hearts:')


  def getting_links(site,attr,attr_name):
    source = Request(site, headers = {'User-Agent': 'Mozilla/5.0'})

    try:
      content = urlopen(source, timeout=10).read()
    except (http.IncompleteRead) as e:
      content = e.partial
      
    page = BeautifulSoup(content,'html.parser')
    linkparent = page.find_all('a',attrs={attr:attr_name})
    links_list = [l.attrs.get('href') for l in linkparent]
   # meaning: for l in linkparent: \ links = l.attrs.get('href')
    for links in links_list:
      if links == '' or links is None:
        continue

    links_list = list(dict.fromkeys(links_list))  

    return(links_list[rand.randint(0,len(links_list))])

  random_recipe = [getting_links('https://www.allrecipes.com/search/results/?search=bread','class','card__titleLink manual-link-behavior'),getting_links('https://www.southernliving.com/search?q=bread','class','search-result-title-link elementFont__subhead elementFont__subheadLinkOnly--innerHover')]

  if msg.startswith('#givebread'):
  
    try:
      await message.channel.send(f'''
    Here\'s a recipe I absolutely adore! :tada:
    
    {random_recipe[rand.randint(0,len(random_recipe))]}''')
    except IndexError:
      pass

  if msg.startswith('#help'):
    await message.channel.send('''#givebread - random bread recipes!
    
  more coming soon :orange_heart:''')



 
my_secret = os.environ['TOKEN']
client.run(my_secret)
keep_alive()
