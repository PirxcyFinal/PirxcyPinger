# PirxcyPinger
Use This To Upload Files To PirxcyPinger


### Setup:
``pip3 install PirxcyPinger``

## Examples:

Basic Example

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

This would output:<br>
```
[PirxcyPinger] Uploaded https://{id}.id.repl.co
[PirxcyPinger] Pinged PirxcyPinger
```
## Examples With Other Libarys

Sanic example:
```python
import sanic
import PirxcyPinger

app = sanic.Sanic("PirxcyPinger")

async def post():
  url = PirxcyPinger.get_url(platform='replit')
  try:
    await PirxcyPinger.post(url)
    print(f"Uploaded {url}")
  except PirxcyPinger.AlreadyPinging: #if url is already submitted
    print("URL Already Submitted!") #do something
  except:#uncaught error
    pass

@app.route('/')
async def index(request):
  return sanic.response.text("PirxcyPinger Example!")


app.add_task(post())
app.run(
  host="0.0.0.0"
)
```

Discord.py example:
```python
import PirxcyPinger
import os
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='>')
url = PirxcyPinger.get_url(platform='replit')

@bot.event
async def on_ready():
  try:
    await PirxcyPinger.post(url)
  except PirxcyPinger.AlreadyPinging: #if url is already submitted
    pass #do something

@bot.command()
async def ping(ctx):
  await ctx.send('pong')

bot.run('token')
```

External Pinger example:
```python
import PirxcyPinger
import os
import asyncio

async def upload():
  try:
    await PirxcyPinger.post(
      url=f"https://{os.environ['REPL_ID']}.id.repl.co",
      external_urls=[
        "https://publicpinger--gomashio1596.repl.co/",
        "https://publicpinger.gomanshiopirxcy.repl.co/"
      ]
    )
  except PirxcyPinger.AlreadyPinging: #if url is already submitted
    pass #do something
    
loop = asyncio.get_event_loop()
loop.run_until_complete(upload())
loop.close()
```
Please Note This Feature is experimental i have no idea to comfirm this full works
