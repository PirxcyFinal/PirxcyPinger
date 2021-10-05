"""
“Commons Clause” License Condition v1.0
Copyright Pirxcy 2020
The Software is provided to you by the Licensor under the
License, as defined below, subject to the following condition.
Without limiting other conditions in the License, the grant
of rights under the License will not include, and the License
does not grant to you, the right to Sell the Software.
For purposes of the foregoing, “Sell” means practicing any or
all of the rights granted to you under the License to provide
to third parties, for a fee or other consideration (including
without limitation fees for hosting or consulting/ support
services related to the Software), a product or service whose
value derives, entirely or substantially, from the functionality
of the Software. Any license notice or attribution required by
the License must also include this Commons Clause License
Condition notice.
Software: PirxcyPinger
License: Apache 2.0
"""

import aiohttp, asyncio, requests

base = "https://pirxcypingerfinal.pirxcyfinal.repl.co"
db_base = requests.get(f"{base}/db").text

class PingerException(Exception):
  pass

class AlreadyPinging(PingerException):
  pass

class InvalidURL(PingerException):
  pass

async def check_database():
  async with aiohttp.ClientSession() as session:
    async with session.request(
      method='GET', 
      url=f"{db_base}/pings"
    ) as r:
      data = await r.text()
  return str(data)
  
async def revive_pinger():
  while True:
    async with aiohttp.ClientSession() as session:
      async with session.request(
        method='GET', 
        url=base
      ) as r:
        print(f"[PirxcyPinger] Pinged PirxcyPinger")
        await asyncio.sleep(300)
  return  

async def post(url):
  database = await check_database()
  async with aiohttp.ClientSession() as session:
    async with session.request(
      method='POST', 
      url=f'{base}/api/add',
      json=({'url': url})
    ) as r:
      if url in database:
        raise AlreadyPinging('Already Pinging This URL')
      elif "http" not in url:
        raise InvalidURL('Invalid URL Requested')
      elif "https" not in url:
        raise InvalidURL('Invalid URL Requested')
      else:
        print(f"[PirxcyPinger] Uploaded {url}") 
  await revive_pinger()
  return

async def remove(url):
  database = await check_database()
  async with aiohttp.ClientSession() as session:
    async with session.request(
      method='POST', 
      url=f'{base}/api/remove',
      json=({'url': url})
    ) as r:
      if url not in database:
        raise InvalidURL('Unable To Find This URL')
      elif "http" not in url:
        raise InvalidURL('Invalid URL')
      elif "https" not in url:
        raise InvalidURL('Invalid URL')
      else:
        print(f"[PirxcyPinger] Removed {url}")   
  await revive_pinger()
  return    
