# -*- coding: utf-8 -*-
import names

@Given("I have started the PackGen application")
def step(context):
    startApplication("PackGen")


@When("I enter the first packet with the following details:")
def step(context):
    mouseClick(waitForObject(names.mainWindow_NameEdit_QLineEdit), 121, 5, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.mainWindow_NameEdit_QLineEdit), "<Ctrl+V>")
    mouseClick(waitForObject(names.mainWindow_ASCIIEdit_QLineEdit), 190, 8, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.mainWindow_ASCIIEdit_QLineEdit), "<Ctrl+V>")
    mouseClick(waitForObject(names.mainWindow_HEXEdit_QLineEdit), 102, 11, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.mainWindow_HEXEdit_QLineEdit), "<Ctrl+V>")
    mouseClick(waitForObject(names.mainWindow_AddressEdit_QLineEdit), 78, 3, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.mainWindow_AddressEdit_QLineEdit), "<Ctrl+V>")
    mouseClick(waitForObject(names.mainWindow_PortEdit_QLineEdit), 30, 5, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.mainWindow_PortEdit_QLineEdit), "<Ctrl+V>")
    mouseClick(waitForObject(names.mainWindow_Type_QComboBox), 67, 12, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.mainWindow_Type_QComboBox, "TCP"), 62, 11, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.mainWindow_Send_QPushButton))


@When("I enter the second packet with the following details:")
def step(context):
    doubleClick(waitForObject(names.mainWindow_NameEdit_QLineEdit), 111, 5, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.mainWindow_NameEdit_QLineEdit), "<Ctrl+V>")
    doubleClick(waitForObject(names.mainWindow_ASCIIEdit_QLineEdit), 80, 7, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.mainWindow_ASCIIEdit_QLineEdit), "<Ctrl+V>")
    doubleClick(waitForObject(names.mainWindow_HEXEdit_QLineEdit), 96, 4, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.mainWindow_HEXEdit_QLineEdit), "<Ctrl+V>")
    doubleClick(waitForObject(names.mainWindow_AddressEdit_QLineEdit), 89, 4, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_AddressEdit_QLineEdit), 89, 4, Qt.ControlModifier, Qt.LeftButton)
    type(waitForObject(names.mainWindow_AddressEdit_QLineEdit), "<Ctrl+V>")
    doubleClick(waitForObject(names.mainWindow_PortEdit_QLineEdit), 31, 11, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.mainWindow_PortEdit_QLineEdit), "<Ctrl+V>")
    mouseClick(waitForObject(names.mainWindow_Type_QComboBox), 60, 13, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.mainWindow_Type_QComboBox, "UDP"), 59, 5, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.mainWindow_Send_QPushButton))


@When("I send both packets")
def step(context):
    pass


@Then("the send table should contain 2 packets")
def step(context):
    pass


@When("I click the Clear Log button")
def step(context):
    clickButton(waitForObject(names.mainWindow_clearLog_QPushButton))


@Then("the send table should be empty")
def step(context):
    pass


@Given("I have saved the following packets:")
def step(context):
    mouseClick(waitForObject(names.mainWindow_NameEdit_QLineEdit), 76, 8, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.mainWindow_NameEdit_QLineEdit), "<Ctrl+V>")
    type(waitForObject(names.mainWindow_NameEdit_QLineEdit), "<Backspace>")
    mouseClick(waitForObject(names.mainWindow_ASCIIEdit_QLineEdit), 113, 3, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.mainWindow_ASCIIEdit_QLineEdit), "<Ctrl+V>")
    type(waitForObject(names.mainWindow_ASCIIEdit_QLineEdit), "<Backspace>")
    mouseClick(waitForObject(names.mainWindow_HEXEdit_QLineEdit), 62, 0, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.mainWindow_HEXEdit_QLineEdit), "<Ctrl+V>")
    type(waitForObject(names.mainWindow_HEXEdit_QLineEdit), "<Backspace>")
    mouseClick(waitForObject(names.mainWindow_AddressEdit_QLineEdit), 78, 1, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.mainWindow_AddressEdit_QLineEdit), "<Ctrl+V>")
    type(waitForObject(names.mainWindow_AddressEdit_QLineEdit), "<Backspace>")
    mouseClick(waitForObject(names.mainWindow_PortEdit_QLineEdit), 30, 0, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.mainWindow_PortEdit_QLineEdit), "<Ctrl+V>")
    mouseClick(waitForObject(names.mainWindow_Type_QComboBox), 88, 10, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.mainWindow_Type_QComboBox, "TCP"), 74, 7, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.mainWindow_Save_QPushButton))
    doubleClick(waitForObject(names.mainWindow_NameEdit_QLineEdit), 69, 8, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.mainWindow_NameEdit_QLineEdit), "<Ctrl+V>")
    type(waitForObject(names.mainWindow_NameEdit_QLineEdit), "<Backspace>")
    doubleClick(waitForObject(names.mainWindow_ASCIIEdit_QLineEdit), 75, 6, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.mainWindow_ASCIIEdit_QLineEdit), "<Ctrl+V>")
    type(waitForObject(names.mainWindow_ASCIIEdit_QLineEdit), "<Backspace>")
    doubleClick(waitForObject(names.mainWindow_HEXEdit_QLineEdit), 103, 14, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.mainWindow_HEXEdit_QLineEdit), "<Ctrl+V>")
    type(waitForObject(names.mainWindow_HEXEdit_QLineEdit), "<Backspace>")
    doubleClick(waitForObject(names.mainWindow_AddressEdit_QLineEdit), 102, 3, Qt.NoModifier, Qt.LeftButton)
    doubleClick(waitForObject(names.mainWindow_AddressEdit_QLineEdit), 102, 3, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_AddressEdit_QLineEdit), 102, 3, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.mainWindow_AddressEdit_QLineEdit), "<Ctrl+V>")
    type(waitForObject(names.mainWindow_AddressEdit_QLineEdit), "<Backspace>")
    doubleClick(waitForObject(names.mainWindow_PortEdit_QLineEdit), 28, 10, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.mainWindow_PortEdit_QLineEdit), "<Ctrl+V>")
    type(waitForObject(names.mainWindow_PortEdit_QLineEdit), "<Backspace>")
    mouseClick(waitForObject(names.mainWindow_Type_QComboBox), 79, 19, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.mainWindow_Type_QComboBox, "UDP"), 54, 8, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.mainWindow_Save_QPushButton))
    doubleClick(waitForObject(names.mainWindow_NameEdit_QLineEdit), 113, 13, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.mainWindow_NameEdit_QLineEdit), "<Ctrl+V>")
    type(waitForObject(names.mainWindow_NameEdit_QLineEdit), "<Backspace>")
    doubleClick(waitForObject(names.mainWindow_ASCIIEdit_QLineEdit), 192, 12, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.mainWindow_ASCIIEdit_QLineEdit), "<Ctrl+V>")
    type(waitForObject(names.mainWindow_ASCIIEdit_QLineEdit), "<Backspace>")
    doubleClick(waitForObject(names.mainWindow_HEXEdit_QLineEdit), 149, 7, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.mainWindow_HEXEdit_QLineEdit), "<Ctrl+V>")
    type(waitForObject(names.mainWindow_HEXEdit_QLineEdit), "<Backspace>")
    doubleClick(waitForObject(names.mainWindow_AddressEdit_QLineEdit), 52, 8, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_AddressEdit_QLineEdit), 52, 8, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.mainWindow_AddressEdit_QLineEdit), "<Ctrl+V>")
    type(waitForObject(names.mainWindow_AddressEdit_QLineEdit), "<Backspace>")
    doubleClick(waitForObject(names.mainWindow_PortEdit_QLineEdit), 20, 12, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.mainWindow_PortEdit_QLineEdit), "<Ctrl+V>")
    type(waitForObject(names.mainWindow_PortEdit_QLineEdit), "<Backspace>")
    mouseClick(waitForObject(names.mainWindow_Type_QComboBox), 61, 22, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObjectItem(names.mainWindow_Type_QComboBox, "SSL"), 56, 4, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.mainWindow_Save_QPushButton))


@When("I type \"Packet\" in the search field")
def step(context):
    mouseClick(waitForObject(names.mainWindow_searchEdit_QLineEdit), 67, 13, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.mainWindow_searchEdit_QLineEdit), "Packet")


@Then("the saved table should show 3 packets")
def step(context):
    pass


@When("I type \"Packet1\" in the search field")
def step(context):
    mouseClick(waitForObject(names.mainWindow_searchEdit_QLineEdit), 114, 6, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.mainWindow_searchEdit_QLineEdit), "1")


@Then("the saved table should show 1 packet")
def step(context):
    pass


@When("I type \"Hello\" in the search field")
def step(context):
    doubleClick(waitForObject(names.mainWindow_searchEdit_QLineEdit), 26, 8, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.mainWindow_searchEdit_QLineEdit), "Hello")


@When("I clear the search field")
def step(context):
    doubleClick(waitForObject(names.mainWindow_searchEdit_QLineEdit), 71, 2, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.mainWindow_searchEdit_QLineEdit), "<Backspace>")
