import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15
import "components"

// Dependencies:
// qt5-quickcontrols2

Rectangle {
    property var username: usernameField.text
    property var password: passwordField.text
    property var sessionIndex: sessionBox.currentIndex

    Rectangle {
        color: config.backgroundColor
        anchors.fill: parent
    }

    Image {
        anchors.fill: parent
        source: config.wallpaperPath
        fillMode: Image.PreserveAspectCrop
        visible: config.useWallpaper === "true"
    }

    Rectangle {
        anchors.centerIn: parent
        width: 600
        height: 324
        color: config.boxColor
        border.width: 2
        border.color: config.borderColor
        radius: 16

        Column {
            anchors.fill: parent
            anchors.margins: 24
            spacing: 16

            UsernameField {
                id: usernameField
            }

            PasswordField {
                id: passwordField
            }

            LoginButton {}

            Row {
                width: parent.width
                anchors.horizontalCenter: parent.horizontalCenter
                spacing: 8

                SessionComboBox {
                    id: sessionBox
                }

                RestartButton {}
                PowerButton {}
            }
        }
    }
}
