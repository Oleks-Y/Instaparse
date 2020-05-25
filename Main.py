from flask import  Flask, jsonify,request
from ParseMain import getInfo
app = Flask(__name__)
@app.route('/instaparse/tasks', methods = ['GET'])
def getReq():
    name = request.args.get('name')
    return jsonify(getInfo(name))

if __name__ == "__main__":
    app.run(debug=True)