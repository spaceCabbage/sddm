import QtQuick 2.15
import QtQuick.Controls 2.15

Rectangle {
    id: loginButton
    width: parent.width
    height: 48
    color: config.accentColor
    radius: 24

    Text {
        id: lblLogin
        anchors.centerIn: parent
        text: qsTr("Login")
        color: config.onAccentColor
        font.pixelSize: 16
    }

    MouseArea {
        id: mouseArea
        hoverEnabled: true
        anchors.fill: parent
        cursorShape: Qt.PointingHandCursor
        onClicked: {
            sddm.login(username, password, sessionIndex);
        }
    }
}
