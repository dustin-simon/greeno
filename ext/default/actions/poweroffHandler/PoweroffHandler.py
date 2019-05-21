from modules.action.ActionHandler import ActionHandler
import sys
import json

class PoweroffHandler(ActionHandler):
    
    def handleAction(self, jsonData):
        print("goodbye!")

        jsonResponse = {
            "message": "Thank you!"
        }

        jsonString = json.dumps(jsonResponse)

        print(jsonString)

        return jsonString