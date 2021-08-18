from flask import Flask,jsonify, request
from flask_restful import Api, Resource
app= Flask(__name__)
api= Api(app)

class Add(Resource):
    def post(self):
        #resource add requested using POST
        # step1: getting post data
        data=request.get_json()
    def get(self):
        #resource add reqested using GET
class Subtract(Resource):
    pass

api.add_resource(Add, "/add")

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
        app.run(debug=True)