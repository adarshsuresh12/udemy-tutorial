from flask import Flask,jsonify, request
app= Flask(__name__)
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