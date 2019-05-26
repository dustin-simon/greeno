from modules.action.ActionHandler import ActionHandler
import json

class PingHandler(ActionHandler):
    
    def handleAction(self, jsonData):

        jsonResponse = {
            'requestAction': self.getAction(),
            'status': 'OK',
            "message": "Pong!"
        }

        return json.dumps(jsonResponse)