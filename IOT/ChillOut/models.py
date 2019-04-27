from django.db import models
from mongoengine import Document, EmbeddedDocument, fields

### THE EVENT CATEGORY ###
#         {'Movie': 'Movie',
#          'Fitness': 'Fitness',
#          'Sports': 'Sports',
#          'Study': 'Study',
#          'Shopping': 'Shopping',
#          'Travelling': 'Travelling',
#          'Party': 'Party',
#          'Hiking': 'Hiking'，
#          'Photography': 'Photography',
#          'Dining': 'Dining',
#          'Gaming': 'Gaming',
#          'Others': 'Others'

#          }


### EVENT INFO ###
class Event(Document):
    eid = fields.LongField(primary_key=True)
    published_time = fields.DateTimeField(default=datetime.utcnow)
    basic_info = fields.ListField(fields.EmbeddedDocumentField(EventBasicInfo), required=True, null=False)
    filter_info = fields.ListField(fields.EmbeddedDocumentField(EventFilterInfo), required=True, null=False)
    ratings = fields.ListField(fields.EmbeddedDocumentField(EventRatings), null=True)
    comments = fields.ListField(fields.EmbeddedDocumentField(EventComments), null=True)
    
class EventBasicInfo(EmbeddedDocument):
    name = fields.StringField(required=True, null=False, max_length=100)
    description = fields.StringField(required=True, null=False, max_length=1000)
    host = fields.ListField(fields.EmbeddedDocumentField(EventHostInfo), required=True, null=False)

class EventHostInfo(EmbeddedDocument):
    username = fields.StringField(required=True, null=False, max_length=100)
    gender = fields.IntField(required=True, null=False)
    age = fields.IntField(required=True, null=False)
    rating = fields.FloatField(required=True, null=True)
    avatar = fields.URLField(required=True, null=False)

class EventFilterInfo(EmbeddedDocument):
    capacity = fields.IntField(required=True, null=False)
    category = fields.StringField(required=True, null=False)
    time = fields.DateTimeField(required=True, null=False)
    duration = fields.FloatField(required=True, null=False)
    location = fields.PointField(required=True, null=False) # the longitude and latitude coordinates

class EventRatings(EmbeddedDocument):
    username = fields.StringField(null=True, max_length=100)
    created_time = fields.DateTimeField(default=datetime.utcnow)
    rating = fields.FloatField(null=True)

class EventComments(EmbeddedDocument):
    username = fields.StringField(null=True, max_length=100)
    created_time = fields.DateTimeField(default=datetime.utcnow)
    comment = fields.StringField(null=True, max_length=1000)
  

#### USER INFO ###
class User(Document):
    eid = fields.LongField(primary_key=True)
    created_time = fields.DateTimeField(default=datetime.utcnow)
    basic_info = fields.ListField(fields.EmbeddedDocumentField(UserBasicInfo), required=True, null=False)

    ratings = fields.ListField(fields.EmbeddedDocumentField(EventRatings), null=True)
    comments = fields.ListField(fields.EmbeddedDocumentField(EventComments), null=True)

    facebook = fields.URLField(required=True, null=False)

class UserBasicInfo (EmbeddedDocument):
    username = fields.StringField(required=True, null=False, max_length=100)
    gender = fields.IntField(required=True, null=False)
    age = fields.IntField(required=True, null=False)
    rating = fields.ListField(fields.EmbeddedDocumentField(UserRatings), null=True)
    avatar = fields.URLField(required=True, null=False)  

class UserRatings(EmbeddedDocument):
    event_url = fields.URLField(required=True, null=False)
    event_name = fields.StringField(required=True, null=False)
    rating = fields.FloatField(required=True, null=False)
    created_time = fields.DateTimeField(default=datetime.utcnow)

