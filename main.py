#!/usr/bin/env python
import os
import jinja2
import webapp2


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))

class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("base.html")

class OmeniHandler(BaseHandler):
    def get(self):
        return self.render_template("Omeni.html")

class KontaktHandler(BaseHandler):
    def get(self):
        return self.render_template("kontakt.html")

class ProjektiHandler(BaseHandler):
    def get(self):
        return self.render_template("projekti.html")

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/Omeni', OmeniHandler),
    webapp2.Route('/kontakt', KontaktHandler),
    webapp2.Route('/projekti', ProjektiHandler),
], debug=True)