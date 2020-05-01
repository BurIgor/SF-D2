import os
import sentry_sdk

from bottle import route, run
from sentry_sdk.integrations.bottle import BottleIntegration

my_SENTRY_DSN = "https://ee1e5ff5313446139d0203a87b90cd09@o385795.ingest.sentry.io/5219066"

if "SENTRY_DSN" in globals():
    SENTRY_DSN = os.environ["SENTRY_DSN"]
else:
    from env import SENTRY_DSN

if len(SENTRY_DSN) < 11:
    SENTRY_DSN = my_SENTRY_DSN

sentry_sdk.init(
    dsn=SENTRY_DSN,
    integrations=[BottleIntegration()]
)


@route('/')
def init_way():
    return """<h1> It's OK.</h1> 
    <h2> You should try:  /success   and   /fail</h2>"""


@route('/fail')
def fail():
    raise RuntimeError("It's an error!!")


@route('/success')
def success():
    return "<h1> It's OK.</h1>  <h2> /success works </h2>"


if os.environ.get("APP_LOCATION") == "heroku":
    run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    run(host="localhost", port=8081, debug=True)
