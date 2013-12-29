#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cherrypy

def fetchAll():
    c = cherrypy.thread_data.db.cursor()
    c.execute('select id from blog')
    items = []
    for (blog_id,) in c.fetchall():
        items.append(Blog(blog_id).getObj())
    return items

def fetchOne(blog_id):
    blog = Blog(blog_id)
    return blog.getObj()


# Blog Class for Blog Data Model
class Blog(object):

    def __init__(self, blog_id):
        c = cherrypy.thread_data.db.cursor()
        c.execute('select * from blog where id = %s ' % blog_id)
        res = c.fetchone()
        if (res == None):
            self.errorObj = {'error': 'Blog Not Found!'}
            return
        (id, title, content, gallery_id, comment_group_id, created_time, modified_time) = res

        self.item = {
            'id': id,
            'title': title,
            'content': content,
            'gallery_id': gallery_id,
            'comment_group_id': comment_group_id,
            'created_time': str(created_time),
            'modified_time': str(modified_time)
        }
        self.error = False

    def getObj(self):
        if (not self.error):
            return self.item
        else:
            return self.errorObj

