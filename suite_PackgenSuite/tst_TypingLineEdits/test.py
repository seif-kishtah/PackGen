# -*- coding: utf-8 -*-

import names

def main():
    startApplication("PackGen")
    
    test_data = {
        "Name": "TestPacket1",
        "Address": "192.168.1.1",
        "Port": "8080",
        "Type": "TCP",  
        "ASCII": "HelloWorld",
        "HEX": "48656C6C6F"
    }
    
    for field, value in test_data.items():
        test.log(f"Testing {field} field with value: {value}")
        if field == "Type":
            combobox = waitForObjectExists(getattr(names, f"mainWindow_{field}_QComboBox"))
            combobox.setCurrentText(value)            
            selected_text = combobox.currentText
            test.compare(selected_text, value, f"{field} combobox should display '{value}'")
            
        else:
            line_edit = waitForObjectExists(getattr(names, f"mainWindow_{field}Edit_QLineEdit"))
            type(line_edit, value)
            test.compare(line_edit.text, value, f"{field} field should display '{value}'")
            line_edit.clear()
