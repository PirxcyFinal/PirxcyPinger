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
  await PirxcyPinger.remove(f"https://{os.environ['REPL_ID']}.id.repl.co")

loop = asyncio.get_event_loop()
loop.run_until_complete(upload())
loop.close()
```

This would output:<br>
```
[PirxcyPinger] Removed https://{id}.id.repl.co
[PirxcyPinger] Pinged PirxcyPinger
```
## Examples With Other Libarys

Sanic example:
```python
import PirxcyPinger
import asyncio
import os
import sanic

app = sanic.Sanic("PirxcyPinger")
url = f"https://{os.environ['REPL_ID']}.id.repl.co"

async def upload():
  await PirxcyPinger.post(url)

async def remove():
  await PirxcyPinger.remove(url)

@app.route('/')
async def add(request):
  asyncio.get_event_loop().create_task(upload()) #when the main page is visited the url is added
  return sanic.response.text("Pinging...")

@app.route('/remove')
async def remove(request):
  asyncio.get_event_loop().create_task(remove()) #when /remove is visited the url is removed from PirxcyPinger

app.run(host="0.0.0.0", port=80)
```

Discord.py example:
```python
import PirxcyPinger
import os
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='>')
url = f"https://{os.environ['REPL_ID']}.id.repl.co"


@bot.event
async def on_ready():
  await PirxcyPinger.post(url) #when the bot is ready the url is posted to PirxcyPinger

@bot.command()
async def remove(ctx):
  await PirxcyPinger.remove(url) #removes url from PirxcyPinger when >remove is excecuted!

@bot.command()
async def ping(ctx):
  await ctx.send('pong')

bot.run('token')
```
