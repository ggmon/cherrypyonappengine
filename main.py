import cherrypy
import wsgiref.handlers
import adtags
from user_agents import parse

class HelloWorld:
    @cherrypy.expose
    def index(self):
        return "Hello World!"

    @cherrypy.expose
    def demo(self, *args, **kwargs):
        return u'It is me again at {0} with {1}'.format("/".join(args), kwargs, len(args), len(kwargs))
    
    @cherrypy.expose
    def another(self, *args, **kwargs):
        requested_with = cherrypy.request.headers.get('User-Agent')
        user_agent = parse(requested_with)        
        return u'It is me again at {0} with {1}, size of args {2} , size of kwargs {3} {4}'.format(args, kwargs, len(args), len(kwargs), user_agent.device )

    @cherrypy.expose
    def default(self, *args, **kwargs):
        adtag = adtags.Adtags(args, kwargs, cherrypy.request.headers)
        if (adtag.valid() == True):
            return adtag.pathstring()
        else:
            return "Yes"        


app = cherrypy.tree.mount(HelloWorld(), "/")
wsgiref.handlers.CGIHandler().run(app)


    

    
