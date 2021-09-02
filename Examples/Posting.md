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
  await PirxcyPinger.post(f"https://{os.environ['REPL_ID']}.id.repl.co")

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
import PirxcyPinger
import asyncio
import os
import sanic

app = sanic.Sanic("PirxcyPinger")
url = f"https://{os.environ['REPL_ID']}.id.repl.co"

async def upload():
  await PirxcyPinger.post(url)

@app.route('/')
async def index(request):
  asyncio.get_event_loop().create_task(upload())
  return sanic.response.text("Pinging...")

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
  await PirxcyPinger.post(url)

@bot.command()
async def ping(ctx):
  await ctx.send('pong')

bot.run('token')
```
