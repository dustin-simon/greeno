from modules.action.ActionHandler import ActionHandler
from core.application.Application import Application
from modules.area.Area import Area
import json

class GetRootAreaHandler(ActionHandler):
    
    def handleAction(self, jsonData):

        rootArea = Area.getRootArea()

        if rootArea == None:
            #TODO: return fail response
            pass

        response = {
            'requestAction': self.getAction(),
            'status': 'OK'
        }

        data = {
            'name': rootArea.getName(),
            'id': rootArea.getID()
        }

        subAreas = []

        for a in rootArea.getSubAreas():
            areaObject = {
                'name': a.getName(),
                'id': a.getID()
            }

            subAreas.append(areaObject)
        
        data["subAreas"] = subAreas
        response["data"] = data

        return json.dumps(response)