print("Hello!")

from core.application.GreenoApplication import GreenoApplication
import os

configFile = "../system.xml"
app = GreenoApplication(configFile)
app.config.print()

app.start()
app.getStatusObserver().join()