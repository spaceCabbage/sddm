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
        anchors.centerIn: parent
        source: config.shutdownPath
        width: 32
        height: 32
    }

	MouseArea {
		id: powerButton
        anchors.fill: parent
        cursorShape: Qt.PointingHandCursor
        onClicked: {
            sddm.poweroff();
        }
    }
}
