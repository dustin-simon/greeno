print("Hello!")

from core.application.GreenoApplication import GreenoApplication

configFile = "../system.xml"
app = GreenoApplication(configFile)
app.config.print()

app.start()
app.getStatusObserver().join()