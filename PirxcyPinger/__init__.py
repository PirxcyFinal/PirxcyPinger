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

import aiohttp, asyncio

async def post(url):
  async with aiohttp.ClientSession() as session:
    async with session.request(
      method='POST', 
      url='https://pinger.pirxcy.xyz/api/add',
      json=({'url': url})
    ) as r:
      if "http" not in url:
        print("[PirxcyPinger] Invalid URL")
      elif "https" not in url:
        print("[PirxcyPinger] Invalid URL")        
      elif r.status == 500:
        print("[PirxcyPinger] Ping Response: URL Already Uploaded!")
      elif r.status == 200:
        print(f"[PirxcyPinger] Uploaded {url}")        
  
  while True:
    async with aiohttp.ClientSession() as session:
      async with session.request(
        method='GET', 
        url='https://pinger.pirxcy.xyz/'
      ) as r:
        print(f"[PirxcyPinger] Pinged PirxcyPinger")
        await asyncio.sleep(300)
  return

async def remove(url):
  async with aiohttp.ClientSession() as session:
    async with session.request(
      method='POST', 
      url='https://pinger.pirxcy.xyz/api/remove',
      json=({'url': url})
    ) as r:
      if "http" not in url:
        print("[PirxcyPinger] Invalid URL")
      elif "https" not in url:
        print("[PirxcyPinger] Invalid URL")        
      elif r.status == 400:
        print("[PirxcyPinger] URL Not Found!")
      elif r.status == 200:
        print(f"[PirxcyPinger] Removed {url}")   
        
  while True:
    async with aiohttp.ClientSession() as session:
      async with session.request(
        method='GET', 
        url='https://pinger.pirxcy.xyz/'
      ) as r:
        print(f"[PirxcyPinger] Pinged PirxcyPinger")
        await asyncio.sleep(300)
  return        
