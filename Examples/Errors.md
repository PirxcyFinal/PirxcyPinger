# PirxcyPinger
Use This To Upload Files To PirxcyPinger


### ModuleNotFoundError:
``pip3 install PirxcyPinger``

## Resolving Errors:

Invalid URL Error

If You Did This:
```python
import PirxcyPinger
import os
import asyncio

async def upload():
  try:
    await PirxcyPinger.post(f"https://{os.environ['REPL_ID']}.id.repl.co")
  except PirxcyPinger.AlreadyPinging: #if url is already submitted
    pass #do something
    
loop = asyncio.get_event_loop()
loop.run_until_complete(upload())
loop.close()
```
You Would Get:

``PirxcyPinger.InvalidURL: InvalidURL``

You Would Need To Add `https://` or `http://` to your url
```python
import PirxcyPinger
import os
import asyncio

async def upload():
  await PirxcyPinger.post(f"https://{os.environ['REPL_ID']}.id.repl.co")

loop = asyncio.get_event_loop()
loop.run_until_complete(upload())
loop.close()
```

If You Get ``PirxcyPinger.InvalidURL: Already Pinging This URL``
It Means Your URL Has Already Been Submitted and No Changed will be made to the database!

## Resolving Errors:

Lets Say You Had a discord.py bot and you had a command that would submit urls but you wanted to do something if the url was submitted 
you can now catch your pirxcypinger errors

Catching URL Already Submitted Error with discord.py

```python
import PirxcyPinger
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=">")

@bot.event
async def on_ready():
  try:
    await PirxcyPinger.post(f"https://{os.environ['REPL_ID']}.id.repl.co")
  except PirxcyPinger.AlreadyPinging: #if url is already submitted
    pass #do something

@bot.command()
async def upload(ctx, url):
  try:
    await PirxcyPinger.post(url)
  except PirxcyPinger.InvalidURL: #if url is invalid
    await ctx.reply('send a valid url pls')
  except PirxcyPinger.AlreadyPinging: #if url is already submitted
    await ctx.reply('im already pinging this url!') #do something

bot.run('token')
```
You Can Catch Other Errors With `InvalidURL` `AlreadyPinging` `InvalidPlatform`

Enjoy <3
