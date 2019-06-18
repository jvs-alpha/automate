from flask import Flask,request
from flask_restful import Api,Resource

app = Flask(__name__)
api = Api(app)

class wifidat(Resource):
    def get(self):
        ssid = request.args.get("ssid")
        passwd = request.args.get("passwd")
        f = open("txt","w+")
        f.write("ssid:"+ssid+"\n")
        f.write("passwd"+passwd+"\n")
        f.close()
        return "worked",200

api.add_resource(wifidat,"/")

if __name__ == "__main__":
    app.run("0.0.0.0","4000",debug=True)
