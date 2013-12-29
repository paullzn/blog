import os
import sys

root_dir = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(root_dir, 'site-packages.zip'))

import sae
import cherrypy
import MySQLdb
from controllers.main import Site

from sae.const import (MYSQL_HOST, MYSQL_HOST_S,
            MYSQL_PORT, MYSQL_USER, MYSQL_PASS, MYSQL_DB)

def connect(thread_index):
    #cherrypy.thread_data.db = MySQLdb.connect('localhost', 'root', '', 'app_paullzn')
    cherrypy.thread_data.db = MySQLdb.connect(host=MYSQL_HOST, port=int(MYSQL_PORT), user=MYSQL_USER, passwd=MYSQL_PASS, db=MYSQL_DB)

cherrypy.engine.subscribe('start_thread', connect)

root = Site(os.path.dirname(os.path.abspath(__file__)))

app_config = {
    '/': {
        'tools.sessions.on': True,
        'tools.sessions.timeout': 60
    }
}

app = cherrypy.Application(root, script_name=None, config=app_config)

application = sae.create_wsgi_app(app)
