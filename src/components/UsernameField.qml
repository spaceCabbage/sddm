import QtQuick 2.15
import QtQuick.Controls 2.15

Column {
    width: parent.width
    property alias text: usernameField.text

    Text {
        id: lblUsername
        text: qsTr("Username")
        color: config.textColor
        font.pixelSize: 16
        font.weight: Font.Medium
    }

    Rectangle {
        width: parent.width
        height: 48
        radius: 8
        color: config.buttonColor
        border.width: 2
        border.color: usernameField.focus ? config.accentColor : config.borderColor

        TextField {
            id: usernameField
            text: userModel.lastUser
            anchors.fill: parent
            font.pixelSize: 16
            anchors.leftMargin: 8
            anchors.rightMargin: 8
            color: config.secondaryTextColor
			background: null
        }
    }
}
