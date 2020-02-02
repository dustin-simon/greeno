from lib.app.core.action.ActionHandler import ActionHandler

class DashboardHandler(ActionHandler):

    def request(self, request, response):

        data = [
            {
                'headline': 'Informationen',
                'endpoint': 'core/greenoinfo'
            }
        ]

        response.setData(data)

        return response