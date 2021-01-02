from flask_restful import Resource, Api, reqparse
from flask import Flask
from flask_jwt import JWT, jwt_required
from security import authenticate, identity

app = Flask(__name__)
app.config["SECRET_KEY"] = b'\xff\xc4;\xad,\x1e\x9cW\xb4\x8a\x90!.\xbfK\xed'

api = Api(app)

# JWT creates endpoint /auth
jwt = JWT(app, authentication_handler=authenticate, identity_handler=identity)

items = []


def parse_item_payload():
    parser = reqparse.RequestParser()
    parser.add_argument("price", type=float,
                        help="Price of item as floating-point number.",
                        required=True)
    return parser.parse_args()


class Item(Resource):
    @jwt_required()
    def get(self, name: str):
        for item in items:
            if name == item["name"]:
                return item

        return {"item": None}, 404

    def post(self, name: str):
        data = parse_item_payload()
        item = {"name": name, "price": data["price"]}
        items.append(item)

        return item, 201

    def put(self, name: str):
        data = parse_item_payload()

        for item in items:
            if name == item["name"]:
                item.update(data)

                return {"item": item}

        item = {"name": name, "price": data["price"]}
        items.append(item)

        return {"item": item}, 201

    def delete(self, name: str):
        for item in items:
            if name == item["name"]:
                items.remove(item)

                return {"message": "Successfully deleted"}

        return {"item": None}, 404


class ItemList(Resource):
    def get(self):
        return {"items": items}


api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")

if "__main__" == __name__:
    app.run(debug=True)
