from modules.action.ActionHandler import ActionHandler
import json
from core.application.Application import Application

class InfoHandler(ActionHandler):
    
    def handleAction(self, jsonData):

        jsonResponse = {
            'requestAction': self.getAction(),
            'status': 'OK',
            'data': {
                'version': Application.getApplication().getConfig().get("version")
            }
        }

        return json.dumps(jsonResponse)