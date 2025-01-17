# -*- coding: utf-8 -*-

import names


def main():
    startApplication("PackGen")
    
    line_edits = [
        "Name",
        "Address",
        "Port",
        "ASCII",
        "HEX"
    ]
    
    test.log("Starting positive test case: Clear non-empty fields")
    for field in line_edits:
        line_edit = waitForObjectExists(getattr(names, f"mainWindow_{field}Edit_QLineEdit"))
        type(line_edit, "TestData")  #
    
    clear_button = waitForObjectExists(names.mainWindow_ClearContent_QPushButton)
    mouseClick(clear_button)
    
    for field in line_edits:
        line_edit = waitForObjectExists(getattr(names, f"mainWindow_{field}Edit_QLineEdit"))
        test.compare(line_edit.text, "", f"{field} field should be cleared")
    
    test.log("Starting negative test case: Clear already empty fields")
    for field in line_edits:
        line_edit = waitForObjectExists(getattr(names, f"mainWindow_{field}Edit_QLineEdit"))
        test.compare(line_edit.text, "", f"{field} field should already be empty")
    
    mouseClick(clear_button)
    
    for field in line_edits:
        line_edit = waitForObjectExists(getattr(names, f"mainWindow_{field}Edit_QLineEdit"))
        test.compare(line_edit.text, "", f"{field} field should remain empty")