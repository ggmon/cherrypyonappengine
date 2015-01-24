from models import Tracking

class Adtags(object):
    
    def __init__(self, path, params, headers):
        self.path = path
        self.params = params
        self.headers = headers

                            

    def pathstring(self):
        return "/".join(self.path)        
    
    def valid(self):
        return True

        
    
