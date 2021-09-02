# PirxcyPinger
Use This To Upload Files To PirxcyPinger


### ModuleNotFoundError:
``pip3 install PirxcyPinger``

## Errors:

Invalid URL Error

If You Did This:
```python
import PirxcyPinger
import os
import asyncio

async def upload():
  await PirxcyPinger.post(f"{os.environ['REPL_ID']}.id.repl.co")

loop = asyncio.get_event_loop()
loop.run_until_complete(upload())
loop.close()
```
You Would Get:

``[PirxcyPinger] Invalid URL``

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

