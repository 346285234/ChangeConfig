import QtCore
import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Dialogs
import QtQuick.Controls.Material
import QtQuick.Layouts

import io.qt.changeconfig

ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: qsTr("Change Config Tool")
    Material.theme: Material.Dark
    Material.accent: Material.Red

    Bridge {
        id: bridge
    }

    ColumnLayout {
        spacing: 2
        Layout.preferredWidth: 400
        anchors.centerIn: parent

        RowLayout {
            Layout.fillWidth: true

            FileDialog {
                id: fileDialog
                currentFolder: StandardPaths.standardLocations(StandardPaths.DownloadLocation)[0]
                onAccepted: {
                    bridge.setAppPath(transformUrlToStr(selectedFile))
                    updateUI()
                }

            }

            Label {
                text: "Path"
            }

            TextField {
                id: path
                Layout.preferredWidth: 300

            }

            Button {
                text: "Select"

                onClicked: {
                    fileDialog.open()
                }
            }
        }

        RowLayout {
            Label {
                text: "Environment"
            }

            RadioButton {
                id: release
                text: "Release"

                onClicked: bridge.setEnvironment(true)
            }

            RadioButton {
                id: debug
                text: "Debug"

                onClicked: bridge.setEnvironment(false)
            }
        }

        RowLayout {
            Label {
                text: "Read image"
            }

            RadioButton {
                id: openReadImage
                text: "Open"

                onClicked: bridge.setReadImage(true)
            }

            RadioButton {
                id: closeReadImage
                text: "Close"

                onClicked: bridge.setReadImage(false)
            }
        }


    }

    Component.onCompleted: {
        updateUI()
    }

    function updateUI() {
        path.text = bridge.getAppPath()
        if (bridge.getEnvironment()) {
            release.checked = true
        } else {
            debug.checked = true
        }
        if (bridge.getReadImage()) {
            openReadImage.checked = true
        } else {
            closeReadImage.checked = true
        }
    }

    function transformUrlToStr(url) {
        var urlString = url.toString();
        if (urlString.startsWith("file://")) {
            return urlString.substr(7);
        }
        return urlString;
    }
}
