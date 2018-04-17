import datetime
from flask import Flask
from flask_restful import Api, Resource, reqparse
app = Flask(__name__)
api = Api(app)
users = [
    {
        "id": "1234",
        "order_id": "123421",
        "product_id": "891343",
        "user_id": "auie",
        "rating": 5,
        "review": "ajsjd",
        "created_at": "2012-12-15 10:14:51.898000"
    },
    {
        "id": "9382",
        "order_id": "20311",
        "product_id": "29393",
        "user_id": "diisa",
        "rating": 5,
        "review": "ajsjd",
        "created_at": "2012-12-15 10:14:51.898000"

    },
    {
        "id": "92",
        "order_id": "2342",
        "product_id": "9302",
        "user_id": "fjiks",
        "rating": 5,
        "review": "ajsjd",
        "created_at": "2012-12-15 10:14:51.898000"
    }
]

class User(Resource):
    
    def get(self, name):
        for user in users:
            if(name == user["id"]):
                return user, 200
        return "User not found", 404
    
    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("order_id")
        parser.add_argument("product_id")
        parser.add_argument("user_id")
        parser.add_argument("rating")
        parser.add_argument("review")
        args = parser.parse_args()
        for user in users:
            if(name == user["id"]):
                return "User with name {} already exists".format(name), 400
        user = {
            "id": name,
            "order_id": args["order_id"],
            "product_id": args["product_id"],
            "user_id": args["user_id"],
            "rating": args["rating"],
            "review": args["review"],
            "created_at": str(datetime.datetime.utcnow())
        }
        users.append(user)
        return user, 201
    
    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("order_id")
        parser.add_argument("product_id")
        parser.add_argument("user_id")
        parser.add_argument("rating")
        parser.add_argument("review")
        args = parser.parse_args()
        for user in users:
            if(name == user["id"]):
                user["order_id"] = args["order_id"]
                user["product_id"] = args["product_id"]
                user["user_id"] = args["user_id"]
                user["rating"]: args["rating"]
                user["review"]: args["review"]
                user["updated_at"] = str(datetime.datetime.utcnow())
                return user, 200
        user = {
            "id": name,
            "order_id": args["order_id"],
            "product_id": args["product_id"],
            "user_id": args["user_id"],
            "rating": args["rating"],
            "review": args["review"],
            "created_at": str(datetime.datetime.utcnow())
        }
        users.append(user)
        return user, 201

    def delete(self, name):
        global users
        users = [user for user in users if user["id"] != name]
        return "{} is deleted.".format(name), 200

api.add_resource(User, "/user/<string:name>")
app.run(debug=True)

