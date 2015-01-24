import datetime
from google.appengine.ext import db
from google.appengine.api import users

class Tracking(db.Model):
    ad_id = db.StringProperty(required=True)
    user_agent_string = db.StringProperty(required=True)
    tracktype = db.StringProperty(required=True,
                             choices=set(["click", "other"]))



