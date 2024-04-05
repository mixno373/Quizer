import os, sys
import locale

from quart import Quart, request, jsonify, send_file
from quart_cors import cors

from conf.const import *
from config.settings import settings
from conf.classes import *
from conf.responses import ApiResponse



__name__ = "Discoin-API"
__version__ = "0.1.0"

app = Quart(__name__)
app = cors(app, allow_origin="*")

APIRESP = ApiResponse()

if sys.platform == 'win32':
    locale.setlocale(locale.LC_ALL, 'rus_rus')
else:
    locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
    
    
@app.before_first_request
async def create_db():
    try:
        app.pool = PostgresqlDatabase(dsn=settings['psql'])
        await app.pool.connect()
        print('PostgreSQL successfully loaded!')
    except Exception as e:
        print('PostgreSQL doesn\'t load.\n'+str(e))
        exit(0)