import xml.etree.ElementTree as ET
from modules.area.Area import Area


class AreaLoader():

    def loadFromFile(self, saveFile):
        tree = ET.parse(saveFile)
        root = tree.getroot()

        rootAreaElement = root.find("area")

        self._createArea(rootAreaElement)

    def _createArea(self, xmlArea, parentArea=None):

        name = xmlArea.find("name").text
        areaID = xmlArea.find("id").text

        area = None

        if parentArea == None:
            rootAreaName = Area.getConfig().get("rootAreaName")
            area = Area(name=rootAreaName, areaID=areaID)
        else:
            area = Area(name=name, areaID=areaID, parent=parentArea)

        subAreasContainer = xmlArea.find("subAreas")
        subAreas = subAreasContainer.findall("area")

        for subArea in subAreas:
            self._createArea(subArea, area)
            