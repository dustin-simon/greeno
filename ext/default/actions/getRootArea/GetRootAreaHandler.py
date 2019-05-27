from modules.action.ActionHandler import ActionHandler
from core.application.Application import Application
from modules.area.Area import Area
import json

class GetRootAreaHandler(ActionHandler):
    
    def handleAction(self, jsonData):

        rootArea = Area.getByName(Area.getConfig().get("rootAreaName"))

        if rootArea != None:
            jsonResponse = {
                'requestAction': self.getAction(),
                'status': 'OK',
                'data': {
                    'name': rootArea.getName()
                }
            }
        else:
            jsonResponse = {
                'requestAction': self.getAction,
                'status': 'SERVER_ERROR'
            }
        

        return json.dumps(jsonResponse)