import os
import sys

root = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(root, 'site-packages.zip'))

import sae
import cherrypy
from controllers.main import Site

root = Site()

app_config = {
}

app = cherrypy.Application(root, script_name=None, config=app_config)

application = sae.create_wsgi_app(app)
