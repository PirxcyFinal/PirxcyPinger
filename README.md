# GummyFNAsync
Python wrapper for the GummyFn API.

[![Downloads](https://pepy.tech/badge/GummyFNAsync)](https://pepy.tech/project/GummyFNAsync)
[![Requires: Python 3.x](https://img.shields.io/pypi/pyversions/GummyFNAsync.svg)](https://pypi.org/project/GummyFNAsync/)
[![Version: 1.0.0](https://img.shields.io/pypi/v/GummyFNAsync.svg)](https://pypi.org/project/GummyFNAsync/)

### Setup:
Windows: ``py -3 -m pip install GummyFNAsync``<br>
Linux/macOS: ``python3 -m pip install GummyFNAsync``

## Examples:
```
import GummyFNAsync
import asyncio

async def skinsearch():
    result = await GummyFNAsync.get_cosmetic(
        name="Ghoul Trooper"
    )

    print(result.id)

loop = asyncio.get_event_loop()
loop.run_until_complete(skinsearch())
loop.close()
```

This would output:<br>
```CID_029_Athena_Commando_F_Halloween```

fortnitepy example:
```
import GummyFNAsync

import fortnitepy
from fortnitepy.ext import commands

client = commands.Bot(
    command_prefix=prefix
    auth=fortnitepy.AuthorizationCodeAuth(
        code = input('Enter Code\n')
    )

@client.command()
async def skin(ctx, *, item = None):
    if item is None:
        await ctx.send('No Item Was Given Try !skin ikonik')
    else:
        try:
            skin = await GummyFNAsync.get_cosmetic(
                name=content
            )
            await client.party.me.set_outfit(asset=skin.id)
            await ctx.send(f'Skin Set To {skin.name}')
        except GummyFNAsync.exceptions.NotFound:
            await ctx.send(f'Could not find a skin named: {skin}')

            
client.run()
```
