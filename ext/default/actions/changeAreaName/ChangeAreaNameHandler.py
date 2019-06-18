from modules.action.ActionHandler import ActionHandler
from core.application.Application import Application
from modules.area.Area import Area
import json

class ChangeAreaNameHandler(ActionHandler):
    
    def handleAction(self, jsonData):
        areaID = None

        try:
            areaID = jsonData["data"]["id"]
        except Exception as e:
            pass

        if areaID == None:
            print("areaID is not set")
            return json.dumps(self.createRequestErrorResponse())

        try:
            area = Area.getByID(areaID)
        except Exception as e:
            return json.dumps(self.createRequestErrorResponse())

        try:
            newName = jsonData["data"]["name"]
        except Exception as e:
            return json.dumps(self.createRequestErrorResponse())

        try:
            area.setName(newName)
        except Exception as e:
            return json.dumps(self.createRequestErrorResponse())

        Area.saveData()

        jsonResponse = {
            'status': 'OK',
            'requestAction': self.action
        }

        data = {
            'id': area.getID(),
            'name': area.getName()
        }

        jsonResponse["data"] = data
        
        return json.dumps(jsonResponse)