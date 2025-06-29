import QtQuick 2.15
import QtQuick.Controls 2.15

Rectangle {
    width: 48
    height: 48
    color: config.buttonColor
    border.width: 2
    border.color: config.borderColor
    radius: 24

    Image {
        id: restartImage
        anchors.centerIn: parent
        source: "../assets/restart.png"
        width: 32
        height: 32
    }

    MouseArea {
        anchors.fill: parent
        cursorShape: Qt.PointingHandCursor
        onClicked: {
            sddm.reboot();
        }
    }
}
