print("Hello!")

from core.application.Application import Application

app = Application.getApplication()
app.getConfig().print()