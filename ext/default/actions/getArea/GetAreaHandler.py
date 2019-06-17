from modules.action.ActionHandler import ActionHandler
from core.application.Application import Application
from modules.area.Area import Area
import json

class GetAreaHandler(ActionHandler):
    
    def handleAction(self, jsonData):
        areaID = None

        try:
            areaID = jsonData["data"]["id"]
        except Exception as e:
            print(e)
            pass

        if areaID == None:
            print("areaID is not set")
            return json.dumps(self.createRequestErrorResponse())

        try:
            area = Area.getByID(areaID)
        except Exception as e:
            print(e)
            return json.dumps(self.createRequestErrorResponse())


        jsonResponse = {
            'status': 'OK',
            'requestAction': self.action
        }

        data = {
            'id': area.getID(),
            'name': area.getName()
        }

        subAreas = []

        for a in area.getSubAreas():
            subAreas.append({
                'id': a.getID(),
                'name': a.getName()
            })

        data["subAreas"] = subAreas

        jsonResponse["data"] = data
        
        return json.dumps(jsonResponse)