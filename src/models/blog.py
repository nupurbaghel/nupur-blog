__author__ = "Nupur Baghel"

import datetime
import uuid

from src.common.database import Database
from src.models.post import Post

class Blog(object):
    def __init__(self,author,title,description,_id=None):
        self.author=author
        self.title=title
        self.description=description
        self._id= uuid.uuid4().hex if _id is None else _id

    def new_post(self,title,content,date=datetime.datetime.utcnow()):
        post=Post(self._id,title,content,self.author,date)
        post.save_to_mongo()

    def get_posts(self):
        return Post.from_blog(self._id)

    def save_to_mongo(self):
        Database.insert('blogs',self.json())

    def json(self):
        return{
            'id':self._id,
            'author':self.author,
            'title':self.title,
            'description':self.description
        }

    @classmethod
    def from_mongo(cls,id):
        blog_data=Database.find_one('blogs',query={'_id':id})
        return cls(**blog_data)