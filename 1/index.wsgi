import os
import sys

root = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(root, 'site-packages.zip'))

import sae
import cherrypy

def app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return ['Hello, world!']

class Root(object):
    """Root Controller"""
    def __init__(self):
        pass
    
    @cherrypy.expose
    def index(self):
        """Index handler"""
        return "Hello world, please fill one up for me"

    @cherrypy.expose
    def default(self, *args, **kwargs):
        """Default handler"""
        raise cherrypy.NotFound()

app_config = {}

root = Root()
#app = cherrypy.tree.mount(root, '/', app_config)
app = cherrypy.Application(Root(), script_name=None, config=None)

application = sae.create_wsgi_app(app)
