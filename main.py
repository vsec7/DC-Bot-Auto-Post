import discord
import requests
import time
import numpy as np
import webserver
from webserver import keep_alive

class MyClient(discord.Client):
    async def on_ready(self):
      print('Logged on as {0}!'.format(self.user))
      chan = self.get_channel(867718409630646323)
      r = requests.get("https://raw.githubusercontent.com/lakuapik/quotes-indonesia/master/raw/quotes.json")
      data = r.json()
      
      while (True):
        await chan.send(np.random.choice(data, size=1)[0]['quote'])
        time.sleep(60)

keep_alive()
client = MyClient()
client.run("Token Discord", bot=False)
