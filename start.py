print("Hello!")

from core.application.GreenoApplication import GreenoApplication

configFile = "../system.xml"
app = GreenoApplication(configFile)

app.start()
app.getStatusObserver().join()