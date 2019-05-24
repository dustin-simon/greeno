print("Hello!")

from core.application.Application import Application

app = Application.getApplication()
app.getConfig().print()

app.start()
app.getSystemStatusObserver().join()