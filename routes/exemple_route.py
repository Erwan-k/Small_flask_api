
from flask_restful import Resource, reqparse

class exemple_route(Resource):
	def get(self):
		return "retour route 1"
