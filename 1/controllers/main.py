#!/usr/bin/env python

import cherrypy
import json

class Site(object):
    """Root Controller"""
    def __init__(self):
        pass
    
    @cherrypy.expose
    def index(self):
        """Index handler"""
        return "Paullzn's homgpage"

    @cherrypy.expose
    def blog(self):
        cherrypy.response.headers['Content-Type'] = "application/json"
        obj = {
            'title': 'Blog Page',
            'content': 'Blog Page is still working.'
        }
        return json.dumps(obj)

    @cherrypy.expose
    def photo(self):
        return "Photo's page"

    @cherrypy.expose
    def about(self):
        return "About Myself.."

    @cherrypy.expose
    def admin(self):
        return "Admin page should be here"

    @cherrypy.expose
    def api(self):
        return ""

    @cherrypy.expose
    def default(self, *args, **kwargs):
        """Default handler"""
        raise cherrypy.NotFound()

