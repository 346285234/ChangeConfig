# This Python file uses the following encoding: utf-8

import json
import unittest
import ast

def read(filepath, keypath):
    data = load(filepath)
    return get(data, keypath)

def write(filepath, keypath, value):
    data = load(filepath)
    set(data, keypath, value)
    save(filepath, data)

def load(filepath):
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)

        return data
    except Exception as e:
        print(f"load failed: {filepath} {e}")


def save(filepath, data):
    try:
        with open(filepath, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"save failed: {filepath} {e}")


def get(data, keypath):
    if not keypath or not isinstance(keypath, list):
        raise ValueError("Key path must be a non-empty list.")

    key = keypath[0]

    if isinstance(data, dict):
        if key in data:
            if len(keypath) == 1:
                return data[key]
            else:
                return get(data[key], keypath[1:])
        
    elif isinstance(data, list):
        for item in data:
            if isSatisfyCondition(item, key):
                if len(keypath) == 1:
                    return item
                else:
                    return get(item, keypath[1:])

    return None
        

def set(data, keypath, value):
    if not keypath or not isinstance(keypath, list):
        raise ValueError("Key path must be a non-empty list.")

    key = keypath[0]

    if isinstance(data, dict):
        if key in data:
            if len(keypath) == 1:
                data[key] = value
            else:
                set(data[key], keypath[1:], value)
        else:
            if len(keypath) == 1:
                data[key] = value
            else:
                raise KeyError(f"{key} not found in the data.")
    elif isinstance(data, list):
        isKeyExist = False
        for index, item in enumerate(data):
            if isSatisfyCondition(item, key):
                isKeyExist = True
                if len(keypath) == 1 and value == '':
                    data.pop(index)
                else:
                    set(item, keypath[1:], value)
                        
        if not isKeyExist:
            data.append(value)
    
    else:
        pass
        
def isCondition(str):
    if '=' in str:
        return True
    
    if str == '*':
        return True

    return False

def isSatisfyCondition(data, str):
    if str == '*':
        return True

    condition_key, condition_values = parseEqualCondition(str)
    if isinstance(condition_values, list):
        if data[condition_key] in condition_values:
            return True
    else:
        if data[condition_key] == condition_values:
            return True
    
    return False

def parseEqualCondition(input_string):
    key, value = input_string.split('=')
    try:
        value = ast.literal_eval(value)
    except Exception:
        pass 

    return key, value


class Test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # def test_read_normal(self):
    #     apppath= "/Users/chenqian/Desktop/release_mac_17467_1d3a4355/IntraoralScan.app"
    #     filepath = apppath + '/Contents/Resources/config/Launcher/LauncherCfg.json'
    #     value = read(filepath, ['community', 'env'])
    #     self.assertEqual(value, "release")

    # def test_read_condition(self):
    #     apppath= "/Users/chenqian/Desktop/release_mac_17467_1d3a4355/IntraoralScan.app"
    #     filepath = apppath + '/Contents/Resources/config/Launcher/LauncherCfg.json'
    #     value = read(filepath, ['startmodulelists', "name=default", 'startmodules', 'name=IntraoralScan', 'loggingRules'])
    #     self.assertEqual(value, "")

    # def test_read_condition_item(self):
    #     apppath= "/Users/chenqian/Desktop/release_mac_17467_1d3a4355/IntraoralScan.app"
    #     filepath = apppath + '/Contents/Resources/config/Launcher/LauncherCfg.json'
    #     value = read(filepath, ['startmodulelists', 'name=default', 'startmodules', 'name=IntraoralScan'])
    #     self.assertIsNotNone(value)

    # def test_write_noraml(self):
    #     apppath= "/Users/chenqian/Desktop/release_mac_17467_1d3a4355/IntraoralScan.app"
    #     filepath = apppath + '/Contents/Resources/config/Launcher/LauncherCfg.json'
    #     write(filepath, ['community', 'env'], 'release')

    #     value = read(filepath, ['community', 'env'])
    #     self.assertEqual(value, "release")

    # def test_write_condition(self):
    #     apppath= "/Users/chenqian/Desktop/release_mac_17467_1d3a4355/IntraoralScan.app"
    #     filepath = apppath + '/Contents/Resources/config/Launcher/LauncherCfg.json'
    #     keypath = ['startmodulelists', "name=default", 'startmodules', '*', 'loggingRules']

    #     value = "" if True else '*.debug=false'
    #     write(filepath, keypath, value)

    #     value = read(filepath, keypath)
    #     self.assertEqual(value, '')

    # def test_write_multi_key(self):
    #     apppath= "/Users/chenqian/Desktop/release_mac_17467_1d3a4355/IntraoralScan.app"
    #     filepath = apppath + '/Contents/Helpers/IntraoralScan.app/Contents/Resources/config/IntraoralScan/DeviceCfg.json'
    #     keypath = ['supportDevices', f"name=['AOS', 'AOS3-LAB']", 'disabled']
    #     write(filepath, keypath, False)

    #     value = read(filepath, keypath)
    #     self.assertEqual(value, True)

    # def test_write_remove(self):
    #     apppath= "/Users/chenqian/Desktop/release_mac_17467_1d3a4355/IntraoralScan.app"
    #     filepath = apppath + '/Contents/Resources/config/Launcher/LauncherCfg.json'
    #     keypath = ['startmodulelists', 'name=default', 'startmodules', 'name=IntraoralScan']
    #     write(filepath, keypath, '')

    #     value = read(filepath, keypath)
    #     self.assertIsNone(value)

    # def test_write_add(self):
    #     apppath= "/Users/chenqian/Desktop/release_mac_17467_1d3a4355/IntraoralScan.app"
    #     filepath = apppath + '/Contents/Resources/config/Launcher/LauncherCfg.json'
    #     keypath = ['startmodulelists', 'name=default', 'startmodules', 'name=IntraoralScan']

    #     value = {'name': 'IntraoralScan', 'path': 'IntraoralScan.exe', 'log': True, 'logToFile': 1, 'loggingRules': '', 'logExpiredDateNum': 90, 'mustStart': True, 'isGUI': True, 'startLevel': 100, 'exitLevel': 100}
    #     write(filepath, keypath, value)

    #     value = read(filepath, keypath)
    #     self.assertIsNotNone(value)
    


if __name__ == "__main__":
    unittest.main()
