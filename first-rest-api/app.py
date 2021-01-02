from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        "name": "Test 1",
        "items": [
            {
                "name": "Item 1",
                "price": 13.99
            }
        ]
    }
]


# POST /store {name:}
@app.route("/store", methods=["POST"])
def create_store():
    data = request.get_json()
    new_store = {
        "name": data["name"],
        "items": []
    }
    stores.append(new_store)

    return jsonify(new_store), 201


# GET /store/<string:name>
@app.route("/store/<string:name>")
def get_store(name: str):
    for store in stores:
        if name == store["name"]:
            return jsonify(store)

    return jsonify({"message": "Not Found"}), 404


# GET /store
@app.route("/store")
def get_stores():
    return jsonify({"stores": stores})


# POST /store/<string:name>/item {name:, price:}
@app.route("/store/<string:name>/item", methods=["POST"])
def create_item_in_store(name: str):
    for store in stores:
        if name == store["name"]:
            data = request.get_json()
            store["items"].append(data)

            return jsonify(store), 201

    return jsonify({"message": "Not Found"}), 404


# GET /store/<string:name>/item
@app.route("/store/<string:name>/item")
def get_items_in_store(name: str):
    for store in stores:
        if name == store["name"]:
            return jsonify({"items": store["items"]})

    return jsonify({"message": "Not Found"}), 404


if "__main__" == __name__:
    app.run(debug=True)
