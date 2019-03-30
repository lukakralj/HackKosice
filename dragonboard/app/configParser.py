import json
import Configs


class ConfigParser:
    def __init__(self):
        self.loader = None
        self.loadConfig()

    def loadConfig(self):
        with open(Configs.configs['path']+"config.json") as file:
            jsonString = file.read()
            self.loader = json.loads(jsonString)

    def fetchFace(self, name):
        if self.loader:
            for face in self.loader:
                if face["filename"] == name:
                    return (face["filename"], face["personName"], face["address"])
        return None

    def fetchFaceAttribute(self, attribute=None):
        attributes = []
        if self.loader:
            for face in self.loader:
                if attribute:
                    attributes.append(face[attribute])
                else:
                    attributes.append(face)
        return attributes


print(ConfigParser().fetchFaceAttribute("personName"))
