#!/usr/bin/env python

import cherrypy

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
        return "Blog Page."

    @cherrypy.expose
    def photo(self):
        return "Photo's page"

    @cherrypy.expose
    def about(self):
        return "About Myself.."

    @cherrypy.expose
    def default(self, *args, **kwargs):
        """Default handler"""
        raise cherrypy.NotFound()

