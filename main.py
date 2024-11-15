# This Python file uses the following encoding: utf-8
import sys
import os
from pathlib import Path
from PySide6.QtCore import QObject, Slot
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine, QmlElement

from config import Config

# To be used on the @QmlElement decorator
# (QML_IMPORT_MINOR_VERSION is optional)
QML_IMPORT_NAME = "io.qt.changeconfig"
QML_IMPORT_MAJOR_VERSION = 1

@QmlElement
class Bridge(QObject):

    def __init__(self):
        super().__init__()
        current_folder = os.path.dirname(os.path.abspath(__file__))
        app_path = os.path.abspath(os.path.join(current_folder, '../../../../..'))
        self.config = Config(app_path)

    @Slot(result=str)
    def getAppPath(self):
        return self.config.app_path

    @Slot(str)
    def setAppPath(self, str):
        self.config = Config(str)

    @Slot(result=bool)
    def getEnvironment(self):
        if self.config.getEnvironment() == "release":
            return True
        else:
            return False

    @Slot(bool)
    def setEnvironment(self, isRelease):
        self.config.setEnvironment(isRelease)

    @Slot(result=bool)
    def getReadImage(self):
        return self.config.getReadImage()

    @Slot(bool)
    def setReadImage(self, isOn):
        self.config.setReadImage(isOn)


if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    qml_file = Path(__file__).resolve().parent / "main.qml"
    engine.load(qml_file)
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())
