# PirxcyPinger

Use This To Upload Files To PirxcyPinger


## Examples

Currently Extensions Only Work With Sanic
Here is a Basic Example:
 ```py
import sanic
import PirxcyPinger

from PirxcyPinger.extensions import sanic_extension

app = sanic.Sanic("PirxcyPinger")
app.blueprint(
  sanic_extension(), 
  url_prefix='/pinger'
)

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
  return sanic.response.redirect("/pinger")


app.add_task(post())
app.run(
  host="0.0.0.0"
)
```
