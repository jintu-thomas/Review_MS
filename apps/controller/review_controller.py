import re
from flask_restful import Resource
from flask import request, jsonify
import json

from flask_restful import Resource,reqparse
from apps.models.review_model import ReviewModel,db


class Review(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('rating',type=int,required=True,help="This field cannot be blank.")
    parser.add_argument('review_title',type=str,required=True,help="This field cannot be blank.")
    parser.add_argument('review_description',type=str,required=True,help="This field cannot be blank.")

    def put(self,user_id,product_id):
        user = ReviewModel.objects(user_id=user_id).first()
        product = ReviewModel.objects(product_id=product_id).first()
        
        if user and product:
            for pro in ReviewModel.objects(product_id=product['product_id']):
               if pro['user_id'] == user['user_id']:
                   review = self.parser.parse_args()
                   pro.update(
                            rating=review['rating'],
                            review_title=review['review_title'],
                            review_description=review['review_description']
                        )
        else:
            return {"message": "something wrong"}
            
            # product.save()
        return pro.to_json()

    def delete(self,user_id,product_id):
        user = ReviewModel.objects(user_id=user_id).first()
        product = ReviewModel.objects(product_id=product_id).first()
        if user and product:
            for pro in ReviewModel.objects(product_id=product['product_id']):
               if pro['user_id'] == user['user_id']:
                    pro.delete()
                    return {"message":f"product {product['id']} is deleted successfully"}
            
        else:
            return {"message":"review is not found"}

class Review1(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('user_id',type=int,required=True,help="This field cannot be blank.")
    parser.add_argument('product_id',type=int,required=True,help="This field cannot be blank.")
    parser.add_argument('rating',type=int,required=True,help="This field cannot be blank.")
    parser.add_argument('review_title',type=str,required=True,help="This field cannot be blank.")
    parser.add_argument('review_description',type=str,required=True,help="This field cannot be blank.")

    def post(self):
        review = self.parser.parse_args()
        data = ReviewModel(**review)
        for pro in ReviewModel.objects(product_id=data['product_id']):
            if pro['user_id']==data['user_id']:
                return {"message": "you are already added a view. Now you can update it"}
        data.save()
        return data.to_json()
    def get(self):
        reviews = ReviewModel.objects()
        return jsonify(reviews)

class ReviewList(Review):
    def get(self,product_id):   
        list=[]
        for reviews in ReviewModel.objects(product_id=product_id):
            x = {'user_id': reviews['user_id'],
                'review_title':reviews['review_title'],
                'review_description':reviews['review_description']}
            y = x.copy()
            list.append(y)
        return list

        