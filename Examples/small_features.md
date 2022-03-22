## Here Are Small Features You May Use in PirxcyPinger:

Getting URL's
You can use `get_url` to get the url to post to PirxcyPinger
**This only works for replit and heroku!**
Here is an example:
```python
import PirxcyPinger

replitUrl = PirxcyPinger.get_url(platform="replit")
herokuUrl = PirxcyPinger.get_url(platform="heroku")
```


Checking if The Pinger is Online ***New***
This will check if the pinger is online
Returns `True` if online `False` if offline
Here is an example
```python
import PirxcyPinger

if PirxcyPinger.is_online():
  print("PirxcyPinger is Online!")
else:
  print("PirxcyPinger is Offline!")
