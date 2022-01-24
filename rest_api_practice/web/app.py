from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

def checkPOstedData(postedData, functionName):
    if functionName in (['add', 'substract', 'multiply']):
        if "x" not in postedData or "y" not in postedData:
             return 301
        else:
            return 200
    elif functionName in (['divide']):
        if "x" not in postedData or "y" not in postedData:
             return 301
        elif postedData["y"]==0:
            return 302
        else:
            return 200

class Add(Resource):
    def post(self):
        #read data
        postedData = request.get_json()
        #verify validity of data
        status_code = checkPOstedData(postedData, 'add')
        if (status_code!=200):
            retJson = {
                "Message": "An error happened",
                "Status Code":status_code
            }
            return jsonify(retJson)
        #do the calculation and return the json
        x= postedData['x']
        y= postedData['y']
        x = int(x)
        y = int(y)
        val = x+y
        retData = {
            'message': val,
            'status': 201 
        }
        return jsonify(retData)

class Substract(Resource):
    def post(self):
        #read data
        postedData = request.get_json()
        #verify validity of data
        status_code = checkPOstedData(postedData, 'substract')
        if (status_code!=200):
            retJson = {
                "Message": "An error happened",
                "Status Code":status_code
            }
            return jsonify(retJson)
        #do the calculation and return the json
        x = postedData['x']
        y = postedData['y']
        x = int(x)
        y = int(y)
        val = x-y
        retData = {
            'message': val,
            'status': 200 
        }
        return jsonify(retData)

class Multiply(Resource):
    def post(self):
        #read data
        postedData = request.get_json()
        #verify validity of data
        status_code = checkPOstedData(postedData, 'substract')
        if (status_code!=200):
            retJson = {
                "Message": "An error happened",
                "Status Code":status_code
            }
            return jsonify(retJson)
        #do the calculation and return the json
        x = postedData['x']
        y = postedData['y']
        x = int(x)
        y = int(y)
        val = x*y
        retData = {
            'message': val,
            'status': 200 
        }
        return jsonify(retData)

class Divide(Resource):
    def post(self):
        #read data
        postedData = request.get_json()
        #verify validity of data
        status_code = checkPOstedData(postedData, 'divide')
        if (status_code==302):
            retJson = {
                "Message": "DivisionbyZeroError: cannot divide by zero",
                "Status Code":status_code
            }
            return jsonify(retJson)

        elif (status_code==301):
            retJson = {
                "Message": "An error occured",
                "Status Code":status_code
            }
            return jsonify(retJson)
        #do the calculation and return the json
        x = postedData['x']
        y = postedData['y']
        x = int(x)
        y = int(y)
        val = x/y
        retData = {
            'message': val,
            'status': 200 
        }
        return jsonify(retData)

api.add_resource(Add,'/add')
api.add_resource(Substract,'/substract')
api.add_resource(Multiply,'/multiply')
api.add_resource(Divide,'/divide')


@app.route('/')
def hello_world():
    return "hello world"


if __name__ =='__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0')
    