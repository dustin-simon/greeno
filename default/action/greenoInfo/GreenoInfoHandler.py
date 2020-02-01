from lib.app.core.action.Action import Action
from lib.defaults.action.info.InfoHandler import InfoHandler

from datetime import datetime

class GreenoInfoHandler(InfoHandler):

    def request(self, jsonData):

        response = super().request(jsonData)

        info = response[Action.REQUEST_DATA_KEY]

        data = [
            {
                'name': 'name',
                'label': 'Name',
                'value': info["name"]
            }, {
                'name': 'version',
                'label': 'Version',
                'value': info["version"]
            }, {
                'name': 'time',
                'label': 'System-Zeit',
                'value': datetime.now().strftime("%d.%m.%Y %H:%M")
            }
        ]

        response[Action.REQUEST_DATA_KEY] = data

        return response