from lib.app.core.action.ActionHandler import ActionHandler
from lib.app.core.action.Action import Action

class DashboardHandler(ActionHandler):

    def request(self, jsonData):

        response = self.createResponse()

        data = [
            {
                'headline': 'Informationen',
                'endpoint': 'core/greenoinfo'
            }
        ]

        response[Action.REQUEST_DATA_KEY] = data

        return response