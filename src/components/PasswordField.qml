import QtQuick 2.15
import QtQuick.Controls 2.15

Column {
    property bool showPassword: false
	property alias text: passwordField.text

    width: parent.width

    Text {
        id: lblPassword
        text: qsTr("Password")
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
        border.color: passwordField.focus ? config.accentColor : config.borderColor

        TextField {
            id: passwordField
            anchors.left: parent.left
            anchors.leftMargin: 8
            anchors.top: parent.top
            anchors.bottom: parent.bottom
            anchors.right: eyeIcon.left
            anchors.rightMargin: 16
            font.pixelSize: 16
            color: config.secondaryTextColor
            echoMode: showPassword ? TextInput.Normal : TextInput.Password
            background: null

            Keys.onPressed: {
                if (event.key === Qt.Key_Return || event.key === Qt.Key_Enter) {
                    sddm.login(username, password, sessionIndex);
                    event.accepted = true;
                }
			}
        }

        Image {
            id: eyeIcon
            width: 24
            height: 24
            anchors.verticalCenter: parent.verticalCenter
            anchors.right: parent.right
            anchors.rightMargin: 8
            source: showPassword ? config.eyePath : config.eyeSlashPath
            fillMode: Image.PreserveAspectFit

            MouseArea {
                anchors.fill: parent
                cursorShape: Qt.PointingHandCursor
                onClicked: showPassword = !showPassword
            }
        }
    }
}
