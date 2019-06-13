from flask import Flask
from flask_restful import request,Resource,Api
import json
from controls import *
app = Flask(__name__)   # Here we are creating the object for the app
api = Api(app)          # Here we are sending the object to the Api of the flask_restful
key = "R0dTYWZlSG91c2UK"

class base(Resource):   # This is the class we are goin to use for the base
    def get(self):      # This method will be called if we get a "GET" request
        return {"name":"GGSafeHouse"},200

    def post(self):
        dat = request.get_json()
        try:
            if(dat["val"] == "True"):
                on()
                print("True")
                return "on success", 201
            elif(dat["val"] == "False"):
                off()
                print("False")
                return "off success",201
            else:
                return "query problem",422
        except KeyError:
            return "query problem",422

        #if(val[9:13] == "True"):    # This will get the slice from the sting to check
        #    return make(),201       # If true this will return

# curl -d '{"key":"True"}' -H "Content-Type: application/json" -X POST http://localhost:5000



api.add_resource(base,"/")  # This is for adding the class to the api diretory

if(__name__ == "__main__"):
    app.run("127.0.0.1","5000",debug=True)
