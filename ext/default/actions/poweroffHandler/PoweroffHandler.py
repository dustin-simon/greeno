from modules.action.ActionHandler import ActionHandler
from core.application.Application import Application
import sys
import json

class PoweroffHandler(ActionHandler):
    
    def handleAction(self, jsonData):

        jsonResponse = {
            "message": "Thank you!"
        }

        jsonString = json.dumps(jsonResponse)

        Application.getApplication().setSystemStatus(Application.STATUS_POWEROFF, True)

        return jsonString