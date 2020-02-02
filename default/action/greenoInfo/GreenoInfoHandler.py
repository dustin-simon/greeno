from lib.defaults.action.info.InfoHandler import InfoHandler

from datetime import datetime

class GreenoInfoHandler(InfoHandler):

    def request(self, request, response):

        response = super().request(request, response)

        info = response.getData()

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

        response.setData(data)

        return response