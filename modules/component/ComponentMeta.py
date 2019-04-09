class ComponentMeta():

    def __init__(self, filePath):
        config = Config(filePath)
        config.load()

        self.model = config.get("model")
        self.supplier = config.get("supplier")
        self.type = config.get("type")
        self.name = config.get("name")
        self.friendlyName = config.get("friendlyName")

    