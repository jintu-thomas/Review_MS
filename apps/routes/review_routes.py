from apps.controller.review_controller import Review,Review1,ReviewList
from apps import api

print("hellow")


api.add_resource(Review, '/review/<int:user_id>/<int:product_id>') #get,delete a specefic review
api.add_resource(Review1, '/review')    #post new review
api.add_resource(ReviewList, '/reviews/<int:product_id>') #get all reviews of a specefic product