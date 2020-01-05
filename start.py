print("Hello!")

from core.application.GreenoApplication import GreenoApplication

configFile = "../system.xml"
app = GreenoApplication(configFile)

print(app.config.getProperties())

app.start()
app.getStatusObserver().join()