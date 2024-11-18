import unittest
from myjson import read, write


class Config:

    def __init__(self, app_path):
        self.app_path = app_path

    def getReadImage(self):
        filepath = self.app_path + '/Contents/Helpers/DentalScanAppLogic.app/Contents/Resources/config/DentalScanAppLogic/default/config/OpenCfg.json'
        return read(filepath, ['Default', 'ReadImage'])
    
    def setReadImage(self, isOn):
        filepath = self.app_path + '/Contents/Helpers/DentalScanAppLogic.app/Contents/Resources/config/DentalScanAppLogic/default/config/OpenCfg.json'
        write(filepath, ['Default', 'ReadImage'], isOn)


    def getEnvironment(self):
        filepath = self.app_path + '/Contents/Resources/config/Launcher/LauncherCfg.json'
        return read(filepath, ['community', 'env'])

    def setEnvironment(self, isRelease):
        filepath = self.app_path + '/Contents/Resources/config/Launcher/LauncherCfg.json'
        if isRelease:
            value = 'release'
        else:
            value = 'beta'
        write(filepath, ['community', 'env'], value)

    def getStartWithUI(self):
        filepath = self.app_path + '/Contents/Resources/config/Launcher/LauncherCfg.json'
        keypath = ['startmodulelists', 'name=default', 'startmodules', 'name=IntraoralScan']
        if read(filepath, keypath) != None:
            return True

        return False

    def setStartWithUI(self, isOn):
        filepath = self.app_path + '/Contents/Resources/config/Launcher/LauncherCfg.json'
        keypath = ['startmodulelists', 'name=default', 'startmodules', 'name=IntraoralScan']
        if isOn:
            value = {'name': 'IntraoralScan', 'path': 'IntraoralScan.exe', 'log': True, 'logToFile': 1, 'loggingRules': '', 'logExpiredDateNum': 90, 'mustStart': True, 'isGUI': True, 'startLevel': 100, 'exitLevel': 100}
        else:
            value = ''
        write(filepath, keypath, value)


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

