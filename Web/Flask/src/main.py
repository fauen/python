from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def page():
    return {"message": "Main page..."}

@app.route('/api/greet', methods=['GET'])
def greet():
    return jsonify(message="Hello there!")

if __name__ == "__main__":
    app.run(debug=True)