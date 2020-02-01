print("Hello!")

from core.application.GreenoApplication import GreenoApplication

configFile = "../system.xml"
appFile = "./app.xml"

app = GreenoApplication(configFile, appFile)

app.start()
app.getStatusObserver().join()