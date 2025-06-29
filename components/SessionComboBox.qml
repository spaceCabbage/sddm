import QtQuick 2.15
import QtQuick.Controls 2.15

Column {
    property alias currentIndex: session.currentIndex

    width: 600 - 24 * 2 - 8 * 2 - 48 * 2
    spacing: 4
    anchors.bottom: parent.bottom

    ComboBox {
        id: session
        width: parent.width
        height: 48
        font.pixelSize: 14

        indicator: Image {
            anchors.verticalCenter: parent.verticalCenter
            anchors.right: parent.right
            anchors.rightMargin: 8
            width: 24
            height: 24
            source: "../assets/chevron-down.png"
        }
        model: sessionModel
        textRole: "name"
        currentIndex: sessionModel.lastIndex

        KeyNavigation.backtab: password
        KeyNavigation.tab: layoutBox

        background: Rectangle {
            radius: 24
            border.width: 2
            border.color: config.borderColor
            color: config.buttonColor
        }

        contentItem: Text {
            text: session.displayText
            color: config.textColor
            font.pixelSize: 16
            verticalAlignment: Text.AlignVCenter
            elide: Text.ElideRight
            anchors.fill: parent
            anchors.leftMargin: 16
        }

        popup: Popup {
            y: session.height
            width: session.width
            implicitHeight: contentItem.implicitHeight
            padding: 0

            contentItem: ListView {
                implicitHeight: contentHeight
                model: session.popup.visible ? session.delegateModel : null
                delegate: session.delegate
                currentIndex: session.highlightedIndex
            }

            background: Rectangle {
                radius: 8
                border.width: 2
                border.color: config.borderColor
                color: config.buttonColor
            }
        }

        delegate: ItemDelegate {
            width: session.width
            highlighted: session.highlightedIndex === index
            contentItem: Text {
                text: model.name
                color: config.textColor
                font.pixelSize: 16
                elide: Text.ElideRight
                verticalAlignment: Text.AlignVCenter
            }
            background: Rectangle {
                color: highlighted ? config.borderColor : "transparent"
                radius: 8
            }
        }
    }
}
