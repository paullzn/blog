#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cherrypy
import json
from os.path import join
from cherrypy.lib.static import serve_file
from models import blog


class Site(object):
    """Root Controller"""
    def __init__(self, root):
        self.root_dir = root

    @cherrypy.expose
    def index(self):
        """Index handler"""
        return cherrypy.lib.static.serve_file(join(self.root_dir, "public/html/index.html"))

    @cherrypy.expose
    def blog(self, blog_id=None):
        cherrypy.response.headers['Content-Type'] = "application/json"
        if (blog_id == None):
            items = blog.fetchAll()
        else:
            items = [blog.fetchOne(blog_id)]
        obj = {
            'count': len(items),
            'items': items
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
        if 'token' in cherrypy.session and cherrypy.session['token'] == 'user_token':
            return cherrypy.lib.static.serve_file(join(self.root_dir, "public/html/admin.html"))
        else:
            return cherrypy.lib.static.serve_file(join(self.root_dir, "public/html/login.html"))

    @cherrypy.expose
    def login(self, *args, **kwargs):
        if 'username' in kwargs and 'password' in kwargs:
            if kwargs['username'] == 'paullzn' and kwargs['password'] == 'woaiyubaobao':
                cherrypy.session['token'] = 'user_token'
        raise cherrypy.HTTPRedirect("/admin")

    @cherrypy.expose
    def logout(self):
        if 'token' in cherrypy.session:
            cherrypy.session['token'] = 'fake'
        raise cherrypy.HTTPRedirect("/admin")

    @cherrypy.expose
    def api(self):
        return ""

    @cherrypy.expose
    def default(self, *args, **kwargs):
        """Default handler"""
        raise cherrypy.NotFound()

