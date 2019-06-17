from modules.action.ActionHandler import ActionHandler
from core.application.Application import Application
from modules.area.Area import Area
import json

class CreateAreaHandler(ActionHandler):
    
    def handleAction(self, jsonData):

        parentID = None

        if "parentID" in jsonData["data"]:
            parentID = jsonData["data"]["parentID"]
        
        name = jsonData["data"]["name"]

        if parentID != None:
            parentArea = Area.getByID(parentID)
        else:
            parentArea = Area.getRootArea()

        newArea = Area(name, None, parentArea)

        jsonResponse = {
            'status': 'OK',
            'requestAction': self.getAction(),
            'data': {
                'id' : newArea.getID(),
                'name': newArea.getName()
            }
        }

        Area.saveData()
        
        return json.dumps(jsonResponse)