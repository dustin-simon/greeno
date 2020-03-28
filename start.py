print("Hello!")

from core.application.GreenoApplication import GreenoApplication

app = GreenoApplication(
    systemFile="../system.xml",
)

app.start()
app.getStatusObserver().join()