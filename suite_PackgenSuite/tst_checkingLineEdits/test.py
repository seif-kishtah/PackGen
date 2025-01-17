# -*- coding: utf-8 -*-

import names


def main():
    startApplication("PackGen")
    snooze(2)
    
    line_edits = [
        names.mainWindow_NameEdit_QLineEdit,
        names.mainWindow_ASCIIEdit_QLineEdit,
        names.mainWindow_HEXEdit_QLineEdit,
        names.mainWindow_AddressEdit_QLineEdit,
        names.mainWindow_PortEdit_QLineEdit
    ]
    
    for line_edit in line_edits:
        edit = waitForObjectExists(line_edit)
        test.compare(edit.text, "", f"{line_edit} should be empty initially")
