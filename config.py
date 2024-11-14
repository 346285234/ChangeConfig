import json
import unittest


class Config:

    def __init__(self, app_path):
        self.app_path = app_path

    def getReadImage(self):
        filepath = self.app_path + '/Contents/Helpers/DentalScanAppLogic.app/Contents/Resources/config/DentalScanAppLogic/default/config/OpenCfg.json'
        with open(filepath, 'r') as file:
            data = json.load(file)

        return data['Default']['ReadImage']
    
    def setReadImage(self, isOn):
        filepath = self.app_path + '/Contents/Helpers/DentalScanAppLogic.app/Contents/Resources/config/DentalScanAppLogic/default/config/OpenCfg.json'
        with open(filepath, 'r') as file:
            data = json.load(file)

        data['Default']['ReadImage'] = isOn
        
        with open(filepath, 'w') as file:
            json.dump(data, file, indent=4)

    def getEnvironment(self):
        filepath = self.app_path + '/Contents/Resources/config/Launcher/LauncherCfg.json'
        with open(filepath, 'r') as file:
            data = json.load(file)

        return data['community']['env']

    def setEnvironment(self, isRelease):
        filepath = self.app_path + '/Contents/Resources/config/Launcher/LauncherCfg.json'
        with open(filepath, 'r') as file:
            data = json.load(file)

        if isRelease:
            data['community']['env'] = 'release'
        else:
            data['community']['env'] = 'beta'

        with open(filepath, 'w') as file:
            json.dump(data, file, indent=4)


class Test(unittest.TestCase):

    def setUp(self):
        app_path = "/Users/chenqian/Downloads/release_mac_17973_a84ed84d/IntraoralScan.app"
        self.config = Config(app_path)

    # def test_getReadImage(self):
    #     value = self.config.getReadImage()
    #     self.assertEqual(value , False)

    # def test_setReadImage(self):
    #     self.config.setReadImage(True)
    #     value = self.config.getReadImage()
    #     self.assertEqual(value , True)

    def test_getEnvironment(self):
        value = self.config.getEnvironment()
        self.assertEqual(value, 'beta')
    
    def test_setEnvironment(self):
        self.config.setEnvironment(True)
        value = self.config.getEnvironment()
        self.assertEqual(value, 'release')

if __name__ == '__main__':
    unittest.main()

