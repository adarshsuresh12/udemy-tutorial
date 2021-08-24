from flask import Flask,jsonify, request
from flask_restful import Api, Resource

from pymongo import MongoClient

app= Flask(__name__)
api= Api(app)

client=MongoClient("mongodb://db:27017")
db=client.addDB
UserNum = db["UserNum"]

UserNum.insert({
    'num_of_users':0
})

class Visit(Resource):
    def get(self):
        prev_num = UserNum.find({})[0]['num_of_users']
        new_num = prev_num + 1
        UserNum.update({}, {"$set":{"num_of_users":new_num}})
        return str("Hello user " + str(new_num))

class Add(Resource):
    def post(self):
        #resource add requested using POST
        # step1: getting post data
        data=request.get_json()
        z=int(data["x"])+int(data["y"])
        ans={
            "z": z
        }
        return jsonify(ans)
    def get(self):
        #resource add reqested using GET
        pass
class Subtract(Resource):
    pass

api.add_resource(Add, "/add")
api.add_resource(Visit, "/hello")

@app.route('/')
def hello_world():
    samplejson={
        "hello":"world"
    }
    return jsonify(samplejson)
@app.route('/posttry', methods=["POST"])
def something():
    d=request.get_json()
    if "x" not in d:
        return "Error", 400
    print(d["x"])
    return jsonify(d),200
# return index.html
# return render_template("index.html")
if __name__ == "__main__":
        app.run(host='0.0.0.0',debug=True)