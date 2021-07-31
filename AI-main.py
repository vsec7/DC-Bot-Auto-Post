import discord
import requests
import time
import numpy as np
import webserver
from webserver import keep_alive

class MyClient(discord.Client):
    async def on_ready(self):
      print('Logged on as {0}!'.format(self.user))
      
      while (True):
        msg = await self.get_channel(867718409630646323).history(limit=1).flatten()
        msg = msg[0].content
        msg = ' '.join(msg.split()[:3])
        chan = self.get_channel(867718409630646323)
        r = requests.get("https://fdciabdul.tech/api/ayla/?pesan=" + msg)
        data = r.json()
        await chan.send(data['jawab'])
        time.sleep(30)

keep_alive()
client = MyClient()
client.run("Token Discord", bot=False)
