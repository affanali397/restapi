from flask_restful import Api

from app import flaskAppInstance
from .task import Task

restServer = Api(flaskAppInstance)


restServer.add_resource(Task,"/api/v1.0/task")

