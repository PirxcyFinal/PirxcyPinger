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

#system imports:
import requests
import os


#3rd party imports:
import aiohttp
import asyncio

#3rd party from imports:

#exceptions:
from .exceptions import InvalidPermission 
from .exceptions import InvalidPlatform
from .exceptions import AlreadyPinging
from .exceptions import InvalidURL


base = "https://pirxcypingerfinal.pirxcyfinal.repl.co"
db_base = requests.get(f"{base}/db").text
#Please Do Not Mess with the Database
#It will lead in a blacklist from the pinger and will mess peoples repls!

def get_url(platform=None):
  if platform is None:
    raise InvalidPlatform('Please Enter A Valid Platform!')
  elif platform.lower() in [
    'repl', 
    'replit'
  ]:
    try:
      return f"https://{os.environ['REPL_ID']}.id.repl.co"
    except:
      raise InvalidPlatform('Unable To Obtain URL\nPlease Try manually!')
  elif platform.lower() == 'heroku':
    try:
      return f"https://{os.environ['HEROKU_APP_NAME']}.herokuapp.com"
    except:
      raise InvalidPlatform('Unable To Obtain URL')
  
async def revive_pinger():
  while True:
    async with aiohttp.ClientSession() as session:
      async with session.request(
        method='GET', 
        url=base
      ) as r:
        await asyncio.sleep(600)
  return  

async def post(url):
  async with aiohttp.ClientSession() as session:
    async with session.request(
      method='POST', 
      url=f'{base}/api/add',
      headers={
        'BASE': url
      },      
      json=(
        {'url': url}
      )
    ) as r:
      response = await r.json()
      if response == {"result": "URL Already Stored!"}:
        raise AlreadyPinging('Already Pinging This URL')
      elif "http" not in url:
        raise InvalidURL('Invalid URL Requested')
      elif "https" not in url:
        raise InvalidURL('Invalid URL Requested')
      elif response == {"result": True}:
        return True
  return

async def remove(url):
  async with aiohttp.ClientSession() as session:
    async with session.request(
      method='POST', 
      url=f'{base}/api/remove',
      headers={
        'BASE': url
      },
      json=(
        {'url': url}
      )
    ) as r:
      response = await r.json()
      if response == {"result": "URL Not Found!"}:
        raise InvalidURL('Unable To Find This URL')
      elif "http" not in url:
        raise InvalidURL('Invalid URL')
      elif "https" not in url:
        raise InvalidURL('Invalid URL')
      elif response == {'result': 'Invalid Permission'}:
        raise InvalidPermission('You Cannot Remove Somone Elses URL!')
      elif response == {"result": True}:
        return True
  return    
