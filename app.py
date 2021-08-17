from flask import Flask,jsonify
app= Flask(__name__)
@app.route('/')
def hello_world():
    samplejson={
        "hello":"world"
    }
    return jsonify(samplejson)
# return index.html
# return render_template("index.html")
if __name__ == "__main__":
        app.run(debug=True)