# -*- coding: utf-8 -*-

import names

def main():
    startApplication("PackGen")
    packet_details = {
        "Name": "TestPacket1",
        "Address": "192.168.1.1",
        "Port": "8080",
        "Type": "TCP",  
        "ASCII": "HelloWorld",
        "HEX": "48656C6C6F"
    }
    
    for field, value in packet_details.items():
        if field == "Type":
            combobox = waitForObjectExists(getattr(names, f"mainWindow_{field}_QComboBox"))
            combobox.setCurrentText(value)
        else:
            line_edit = waitForObjectExists(getattr(names, f"mainWindow_{field}Edit_QLineEdit"))
            type(line_edit, value)
    
    save_button = waitForObjectExists(names.mainWindow_Save_QPushButton)
    mouseClick(save_button)
    saved_table = waitForObjectExists(names.mainWindow_SaveTable_QTableWidget)
    row_count = saved_table.rowCount
    test.compare(row_count, 1, "There should be 1 packet in the saved table")
    
    for col, (field, value) in enumerate(packet_details.items(), start=1):
        cell_text = saved_table.item(0, col).text()
        test.compare(cell_text, value, f"Column '{field}' should display '{value}'")