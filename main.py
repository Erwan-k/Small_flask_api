from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from routes.exemple_route import exemple_route

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(exemple_route,"/exemple_route") 

if __name__ == "__main__":
	app.run(debug=True,port=5000,host='0.0.0.0')
