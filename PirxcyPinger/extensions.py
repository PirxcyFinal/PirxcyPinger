import sanic
from sanic import Blueprint

skidded_html = """


<!doctype html>

<html>
    <head>
        <meta charset="utf-8">
        <title>PirxcyPinger</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" type="text/css" href="/static/admin/css/fonts.css">
        <style type="text/css">
          body, main {
            margin: 0 auto;
          }
          .body, .tip {
            stroke: #fff;
          }
          html {
            line-height: 1.15;
            -ms-text-size-adjust: 100%;
            -webkit-text-size-adjust: 100%;
            box-sizing: border-box;
          }
          footer, header, main {
            display: block;
          }
          a {
            background-color: transparent;
            -webkit-text-decoration-skip: objects;
            color: #000000;
            text-decoration: none;
          }
          img {
            border-style: none;
          }
          header {
            border-bottom: 1px solid #efefef;
          }
          svg:not(:root) {
            overflow: hidden;
          }
          body {
            max-width: 960px;
            color: #525252;
            font-family: Roboto, sans-serif;
          }
          main {
            text-align: center;
          }
          .u-clearfix:after {
            content: "";
            clear: both;
            display: table;
          }
          .exhaust.two, .fuel, .removehole {
            display: none;
          }
          h1, h2, h3, h4, h5, p, ul {
            padding: 0;
            margin: 0;
            font-weight: 400;
          }
          header {
            padding-top: 20px;
            padding-bottom: 10px;
          }
          .logo {
            float: left;
          }
          .logo h2 {
            font-weight: 700;
            margin-top: 0px;
          }
          .release-notes {
            float: right;
            margin-top: 7px;
          }
          .release-notes p {
            font-size: 14px;
          }
          .figure {
            margin-top: 19vh;
            height: 181px;
          }
          .figure__animation {
            max-width: 265px;
            position: relative;
            z-index: -9;
          }
          .tip {
            stroke-width: 3px;
            -webkit-transform: translateY(-7px);
            transform: translateY(-7px);
          }
          .body {
            fill: #2b2929;
            -webkit-transform: scaleX(1.25);
            transform: scaleX(1.25);
            -webkit-transform-origin: center;
            transform-origin: center;
            stroke-width: 3px;
          }
          .box {
            position: absolute;
            bottom: 0;
            left: 0;
          }
          .circle {
            fill: #2b2929;
            stroke: #fff;
            stroke-width: 7px;
          }
          .exhaust {
            border-bottom-left-radius: 4px;
          }
          .exhaust.two, .exhaust__line {
            -webkit-animation: thurst 70ms infinite ease-in-out alternate;
            animation: thurst 70ms infinite ease-in-out alternate;
          }
          .smoke {
            -webkit-animation: smoke .1s infinite ease-in-out alternate;
            animation: smoke .1s infinite ease-in-out alternate;
            -webkit-transform-origin: center;
            transform-origin: center;
            opacity: .8;
          }
          @-moz-document url-prefix() {
            .smoke {
              animation: smokeFirefox .2s infinite ease-in-out alternate;
            }
          }
          @-webkit-keyframes smoke {
            0% {
              -webkit-transform: scale(1.58, 1.2) translateY(-55px) skew(3deg);
              transform: scale(1.58, 1.2) translateY(-55px) skew(3deg);
            }
            100% {
              -webkit-transform: scale(1.6, 1.22) translateY(-55px) skew(-3deg);
              transform: scale(1.6, 1.22) translateY(-55px) skew(-3deg);
            }
          }
          @keyframes smoke {
            0% {
              -webkit-transform: scale(1.58, 1.2) translateY(-55px) skew(3deg);
              transform: scale(1.58, 1.2) translateY(-55px) skew(3deg);
            }
            100% {
              -webkit-transform: scale(1.6, 1.22) translateY(-55px) skew(-3deg);
              transform: scale(1.6, 1.22) translateY(-55px) skew(-3deg);
            }
          }
          @-webkit-keyframes smokeFirefox {
            0% {
              -webkit-transform: scale(1.58, 1.2) translateY(-75px) skew(0);
              transform: scale(1.58, 1.2) translateY(-75px) skew(0);
            }
            100% {
              -webkit-transform: scale(1.58, 1.21) translateY(-75px) skew(1deg);
              transform: scale(1.58, 1.21) translateY(-75px) skew(1deg);
            }
          }
          @keyframes smokeFirefox {
            0% {
              -webkit-transform: scale(1.58, 1.2) translateY(-75px) skew(0);
              transform: scale(1.58, 1.2) translateY(-75px) skew(0);
            }
            100% {
              -webkit-transform: scale(1.58, 1.21) translateY(-75px) skew(1deg);
              transform: scale(1.58, 1.21) translateY(-75px) skew(1deg);
            }
          }
          .flame 0%, .flame 100% {
            -webkit-transform: translate(265px, 249px) scale(1.9) rotate(180deg);
            transform: translate(265px, 249px) scale(1.9) rotate(180deg);
          }
          .flame {
            -webkit-animation: burnInner2 .1s infinite ease-in-out alternate;
            animation: burnInner2 .1s infinite ease-in-out alternate;
          }
          @-webkit-keyframes burnInner2 {
            0% {
              -webkit-transform: translate(265px, 249px) scale(1.9) rotate(180deg) skew(5deg);
              transform: translate(265px, 249px) scale(1.9) rotate(180deg) skew(5deg);
            }
            100% {
              -webkit-transform: translate(265px, 253px) scale(2.2) rotate(180deg) skew(-5deg);
              transform: translate(265px, 253px) scale(2.2) rotate(180deg) skew(-5deg);
            }
          }
          @keyframes burnInner2 {
            0% {
              -webkit-transform: translate(265px, 249px) scale(1.9) rotate(180deg) skew(5deg);
              transform: translate(265px, 249px) scale(1.9) rotate(180deg) skew(5deg);
            }
            100% {
              -webkit-transform: translate(265px, 253px) scale(2.2) rotate(180deg) skew(-5deg);
              transform: translate(265px, 253px) scale(2.2) rotate(180deg) skew(-5deg);
            }
          }
          @-webkit-keyframes thurst {
            0% {
              opacity: 1;
            }
            100% {
              opacity: .5;
            }
          }
          @keyframes thurst {
            0% {
              opacity: 1;
            }
            100% {
              opacity: .5;
            }
          }
          h2 {
            font-size: 22px;
            max-width: 500px;
            margin: 5px auto 0;
          }
          main p {
            font-size: 16px;
            line-height: 20px;
            max-width: 390px;
            margin: 15px auto 0;
            color: #888888;
          }
          footer {
            padding: 25px 0;
            position: fixed;
            left: 50%;
            bottom: 0;
            width: 960px;
            -webkit-transform: translateX(-50%);
            transform: translateX(-50%);
            -webkit-transform-style: preserve-3d;
            transform-style: preserve-3d;
            border-top: 1px solid #efefef;
          }
          .option {
            float: left;
            width: 33.33%;
            box-sizing: border-box;
            padding-right: 5px;
          }
          .option svg {
            width: 25px;
            height: 25px;
            fill: gray;
            border: 1px solid #d6d6d6;
            padding: 5px;
            border-radius: 100%;
            float: left;
            margin-right: 10px;
          }
          .option div {
            display: table;
          }
          .option h4 {
            color: #000000;
            font-size: 19px;
          }
          .option p {
            font-weight: 300;
            font-size: 15px;
            padding-top: 3px;
            color: #757575;
          }
          @media (max-width: 996px) {
            body, footer {
              max-width: 780px;
            }
            .logo h2 {
              margin-left: 0px;
            }
          }
          @media (max-width: 800px) {
            footer, main {
              position: relative;
            }
            footer {
              height: 100%;
            }
            .option {
              position: relative;
              width: 100%;
              left: auto;
              right: auto;
              top: auto;
              padding: 0 25px;
              margin-bottom: 60px;
            }
            .two {
              margin-left: 0px;
              -webkit-transform: none;
              transform: none;
            }
            .logo, .option, .release-notes {
              float: none;
            }
            .figure {
              margin-top: 10px;
            }
            main {
              padding: 0 25px;
            }
            main h2 {
              font-size: 18px;
            }
            main p {
              font-size: 14px;
            }
            header {
              padding-left: 20px;
              padding-right: 20px;
            }
            footer {
              overflow: hidden;
              width: 100%;
              margin-top: 50px;
            }
          }
          @media (min-width: 801px) and (max-height: 730px) {
            .figure {
              margin-top: 80px;
            }
          }
          @media (min-width: 801px) and (max-height: 600px) {
            footer {
              position: relative;
              margin: 135px auto 0;
            }
            .figure {
              margin-top: 50px;
            }
          }
        </style>
    </head>
    <body>
      <header class="u-clearfix">
          <div class="logo">
            <a href="https://pirxcypingerfinal.pirxcy1942.repl.co/" target="_blank" rel="noopener">
              <h2>PirxcyPinger</h2>
            </a>
          </div>
      </header>
      <main>
        <div class="figure">
          <svg class="figure__animation" viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg">
            <path fill="#FFF" d="M0 0h512v512H0z"></path>
            <text transform="translate(97.173 475.104)"></text>
            <path d="M307.2 224.6c0 4.6-.5 9-1.6 13.2-2.5-4.4-5.6-8.4-9.2-12-4.6-4.6-10-8.4-16-11.2 2.8-11.2 4.5-22.9 5-34.6 1.8 1.4 3.5 2.9 5 4.5 10.5 10.3 16.8 24.5 16.8 40.1zM232.2 214.6c-6 2.8-11.4 6.6-16 11.2-3.5 3.6-6.6 7.6-9.1 12-1-4.3-1.6-8.7-1.6-13.2 0-15.7 6.3-29.9 16.6-40.1 1.6-1.6 3.3-3.1 5.1-4.5.6 11.8 2.2 23.4 5 34.6z" fill="#000000"></path>
            <path class="body" d="M279.7 217.6c12.9-48.1 5.1-104-23.4-142.6-28.5 38.5-36.2 94.5-23.4 142.6h46.8z" fill="#000000"></path>
            <path class="tip" d="M273 104.7c-4.4-10.6-9.9-20.6-16.6-29.7-6.7 9-12.2 19-16.6 29.7H273z" fill="#2E3B39"></path>
            <circle cx="256.3" cy="144.8" fill="#FFF" r="15.5"></circle>
            <circle class="circle" cx="256.3" cy="144.8" fill="#84DBFF" r="12.2"></circle>
            <path class="removehole" d="M267.5 139.9l-16 16c4.5 2 9.8 1.1 13.5-2.5 3.6-3.7 4.5-9.1 2.5-13.5z" fill="#54C0EB"></path>
            <path class="fuel" d="M276.8 234.9c.4-2.4.6-5.1.6-7.9 0-12.1-3.9-21.8-8.8-21.8s-8.8 9.8-8.8 21.8c0 2.8.2 5.4.6 7.9h16.4zM252.3 234.9c.4-2.4.6-5.1.6-7.9 0-12.1-3.9-21.8-8.8-21.8-4.8 0-8.8 9.8-8.8 21.8 0 2.8.2 5.4.6 7.9h16.4z" fill="#FFD05B"></path>
            <path class="smoke" d="M416.6 358.8c0-1.8-.4-3.6-1-5.2-2.1-5.6-7.5-9.6-13.8-9.6-.7 0-1.4.1-2.1.2-.3-9.6-8.2-17.3-17.9-17.3-2.1 0-4.2.4-6.1 1.1-3-5.6-8.9-9.4-15.7-9.4-.5 0-1 0-1.5.1-.5 0-1-.1-1.5-.1-6.8 0-12.7 3.8-15.7 9.4-1.9-.7-3.9-1.1-6.1-1.1-9.9 0-17.9 8-17.9 17.9 0 1.1.1 2.3.3 3.3-.9-.2-1.8-.3-2.8-.3-5.1 0-9.5 2.6-12.1 6.5-2.2-1.4-4.9-2.3-7.8-2.3-7.6 0-13.8 5.9-14.4 13.3h-.1c-5.9 0-11 3.6-13.2 8.7-2.6-3-6.5-5-10.9-5h-.1-.5-.1-.1c-4.3 0-8.2 1.9-10.9 5-2.2-5.1-7.3-8.7-13.2-8.7h-.1c-.6-7.5-6.8-13.3-14.4-13.3-2.9 0-5.5.8-7.8 2.3-2.6-3.9-7-6.5-12.1-6.5-.9 0-1.9.1-2.8.3.2-1.1.3-2.2.3-3.3 0-9.9-8-17.9-17.9-17.9-2.1 0-4.2.4-6.1 1.1-3-5.6-8.9-9.4-15.7-9.4-.5 0-1 0-1.5.1-.5 0-1-.1-1.5-.1-6.8 0-12.7 3.8-15.7 9.4-1.9-.7-3.9-1.1-6.1-1.1-9.7 0-17.6 7.7-17.9 17.3-.7-.1-1.4-.2-2.1-.2-6.3 0-11.7 4-13.8 9.6-.6 1.6-1 3.4-1 5.2 0 4 1.6 7.6 4.2 10.3-.5 1.2-.8 2.6-.8 4 0 6 4.9 10.9 10.9 10.9H402c6 0 10.9-4.9 10.9-10.9 0-1.4-.3-2.8-.8-4 2.9-2.7 4.5-6.3 4.5-10.3z" fill="#050505"></path>
            <rect class="exhaust" fill="#383a3d" x="241" y="220" width="30" height="8"></rect>
            <rect class="exhaust two" fill="#383a3d" x="245" y="231" width="20" height="9"></rect>
            <rect class="exhaust__line" fill="#383a3d" x="252" y="240" width="5" height="90"></rect>
            <path class="flame" d="M 6.7 1.14 l 2.8 4.7 s 1.3 3 -1.82 3.22 l -5.4 0 s -3.28 -.14 -1.74 -3.26 l 2.76 -4.7 s 1.7 -2.3 3.4 0 z" fill="#AA2247"></path>
          </svg>
        </div>
        <h2>Thanks For Using PirxcyPinger (This HTML is Skidded BTW)</h2>
        <p>You Are Seeing This Page Because You Implemented <a href="https://pypi.org/project/PirxcyPinger/" target="_blank" rel="noopener">PirxcyPinger</a> into Your Sanic Code!</p>
      </main>
      <footer class="u-clearfix">
        <a href="https://docs.djangoproject.com/en/3.1/" target="_blank" rel="noopener">
        <div class="option one">
            <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                <defs>
                    <path d="M0 0h24v24H0V0z" id="a"></path>
                </defs>
                <clipPath id="b">
                    <use overflow="visible" xlink:href="#a"></use>
                </clipPath>
                <path clip-path="url(#b)" d="M9 21c0 .55.45 1 1 1h4c.55 0 1-.45 1-1v-1H9v1zm3-19C8.14 2 5 5.14 5 9c0 2.38 1.19 4.47 3 5.74V17c0 .55.45 1 1 1h6c.55 0 1-.45 1-1v-2.26c1.81-1.27 3-3.36 3-5.74 0-3.86-3.14-7-7-7zm2.85 11.1l-.85.6V16h-4v-2.3l-.85-.6C7.8 12.16 7 10.63 7 9c0-2.76 2.24-5 5-5s5 2.24 5 5c0 1.63-.8 3.16-2.15 4.1z"></path>
            </svg>
            <div>
                <h4>PirxcyPinger Documentation</h4>
                <p>Docs On How To Get Started</p>
            </div>
        </div>
      </a>
      <a href="https://github.com/PirxcyFinal/PirxcyPinger/tree/main/Examples" target="_blank" rel="noopener">
        <div class="option two">
          <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
            <path d="M0 0h24v24H0V0z" fill="none"></path>
            <path d="M9.4 16.6L4.8 12l4.6-4.6L8 6l-6 6 6 6 1.4-1.4zm5.2 0l4.6-4.6-4.6-4.6L16 6l6 6-6 6-1.4-1.4z"></path>
          </svg>
          <div>
            <h4>Main Site</h4>
            <p>Get started with PirxcyPinger</p>
            <p>For Replit and Heroku</p>
          </div>
        </div>
      </a>
      <a href="https://discord.com/invite/VHtvszBAx3" target="_blank" rel="noopener">
        <div class="option three">
          <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
            <path d="M0 0h24v24H0z" fill="none"></path>
            <path d="M16.5 13c-1.2 0-3.07.34-4.5 1-1.43-.67-3.3-1-4.5-1C5.33 13 1 14.08 1 16.25V19h22v-2.75c0-2.17-4.33-3.25-6.5-3.25zm-4 4.5h-10v-1.25c0-.54 2.56-1.75 5-1.75s5 1.21 5 1.75v1.25zm9 0H14v-1.25c0-.46-.2-.86-.52-1.22.88-.3 1.96-.53 3.02-.53 2.44 0 5 1.21 5 1.75v1.25zM7.5 12c1.93 0 3.5-1.57 3.5-3.5S9.43 5 7.5 5 4 6.57 4 8.5 5.57 12 7.5 12zm0-5.5c1.1 0 2 .9 2 2s-.9 2-2 2-2-.9-2-2 .9-2 2-2zm9 5.5c1.93 0 3.5-1.57 3.5-3.5S18.43 5 16.5 5 13 6.57 13 8.5s1.57 3.5 3.5 3.5zm0-5.5c1.1 0 2 .9 2 2s-.9 2-2 2-2-.9-2-2 .9-2 2-2z"></path>
          </svg>
          <div>
            <h4>Discord Server</h4>
            <p>Check Out My Other Projects In The Server!</p>
          </div>
        </div>
      </a>
      </footer>
    </body>
</html>
"""

def sanic_extension():
  extension = Blueprint("PINGER_SANIC_EXTENSION")
  
  @extension.route(
    '/',
    methods=[
      "GET",
      "POST"
    ]
  )
  async def pinger_index(request):
    if request.method == "GET":
      return sanic.response.html(skidded_html)
    elif request.method == "POST":
      return sanic.response.json({"status": "online"})
  
  return extension