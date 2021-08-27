# PirxcyPinger
Use This To Upload Files To PirxcyPinger

[![Downloads](https://pepy.tech/badge/PirxcyPinger)](https://pepy.tech/project/PirxcyPinger)
[![Requires: Python 3.x](https://img.shields.io/pypi/pyversions/PirxcyPinger.svg)](https://pypi.org/project/PirxcyPinger/)
[![Version: 1.0.0](https://img.shields.io/pypi/v/PirxcyPinger.svg)](https://pypi.org/project/PirxcyPinger/)

### Setup:
Windows: ``py -3 -m pip install GummyFNAsync``<br>
Linux/macOS: ``python3 -m pip install GummyFNAsync``

## Examples:
```python
import PirxcyPinger
import os
import asyncio

async def upload():
  await PirxcyPinger.post(f"https://{os.environ['REPL_ID'].id.repl.co")

loop = asyncio.get_event_loop()
loop.run_until_complete(upload())
loop.close()
```

This would output:<br>
```
[PirxcyPinger] Uploaded {id}.id.repl.co
[PirxcyPinger] Pinged PirxcyPinger
```

discord.py example:
```python
import PirxcyPinger
import os
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='>')
url = f"https://{os.environ['REPL_ID']}1.id.repl.co"


@bot.event
async def on_ready():
  await PirxcyPinger.post(url)

@bot.command()
async def ping(ctx):
  await ctx.send('pong')

bot.run('token')
```
