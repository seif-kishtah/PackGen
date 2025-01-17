# -*- coding: utf-8 -*-

import names

def main():
    startApplication("PackGen")
    
    packet_details = {
        "Name": "TestPacket1",
        "Address": "",  
        "Port": "8080",
        "Type": "TCP",  
        "ASCII": "HelloWorld",
        "HEX": "48656C6C6F"
    }
    
    for field, value in packet_details.items():
        if value:  
            if field == "Type":
             
                combobox = waitForObjectExists(getattr(names, f"mainWindow_{field}_QComboBox"))
                combobox.setCurrentText(value)
            else:
                line_edit = waitForObjectExists(getattr(names, f"mainWindow_{field}Edit_QLineEdit"))
                type(line_edit, value)
    
    save_button = waitForObjectExists(names.mainWindow_Save_QPushButton)
    mouseClick(save_button)
    
    try:
        warning_message = waitForObjectExists(names.o_QMessageBox)
        test.compare(warning_message.text, "All fields must be filled out.", "Warning message should be displayed")
    except:
        test.fail("Warning message was not displayed")
    
    ok_button = waitForObjectExists("{type='QPushButton' text='OK'}")
    mouseClick(ok_button)