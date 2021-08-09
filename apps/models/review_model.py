from apps import app    #goes to __init__.py get app variable
from flask_mongoengine import MongoEngine
import apps.configuration.db_config

db = MongoEngine(app)


class ReviewModel(db.Document):
    user_id=db.IntField()
    product_id = db.IntField()
    rating = db.IntField()
    review_title = db.StringField()
    review_description = db.StringField()


    def to_json(self): 
        return {
            # "object_id":self.object_id,
            "user_id": self.user_id,
            "product_id":self.product_id,
            "rating":self.rating,
            "review_title":self.review_title,
            "review_description":self.review_description
        }

    def save_to_db(self):
        return self.save(self)
    
    def delete_from_db(self):
        return self.delete(self)

    def from_json(self):
        return {
            'user_id': self.user_id,
            'review_title': self.review_title,
            'review_description':self.review_description
        }