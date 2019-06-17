import xml.etree.ElementTree as ET

class AreaSaver():

    def __init__(self, rootArea):
        self.rootArea = rootArea

    def getXMLTree(self):
        root = ET.Element("areas")
        rootAreaElement = self._createAreaXmlElement(root, self.rootArea)

        return root

    @classmethod
    def _createAreaXmlElement(self, parentElement, area):
        areaElement = ET.SubElement(parentElement, "area")
        
        idElement = ET.SubElement(areaElement, "id")
        idElement.text = area.getID()

        nameElement = ET.SubElement(areaElement, "name")
        nameElement.text = area.getName()

        subAreasElement = ET.SubElement(areaElement, "subAreas")

        for subArea in area.getSubAreas():
            subAreaElement = self._createAreaXmlElement(subAreasElement, subArea)