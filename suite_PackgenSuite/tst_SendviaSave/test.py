# -*- coding: utf-8 -*-

import names

import time

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
    test.compare(saved_table.rowCount, 1, "There should be 1 packet in the saved table")
    
    send_button = waitForObjectExists("{container=':mainWindow_SaveTable_QTableWidget' type='QPushButton' text='Send'}")
    mouseClick(send_button)
    
    send_table = waitForObjectExists(names.mainWindow_SendTable_QTableWidget)
    test.compare(send_table.rowCount, 1, "There should be 1 packet in the send table")
    
    expected_columns = ["Time", "To Address", "To Port", "Method", "ASCII", "Hex"]
    for col, field in enumerate(expected_columns):
        cell_item = send_table.item(0, col)
        cell_text = cell_item.text()  # Extract the text from the QTableWidgetItem
        test.log(f"Checking {field} in send table: {cell_text}")
        
        # if field == "Time":
        #     # Verify the Time column contains a valid date and time
        #     try:
        #         time.strptime(cell_text, "%Y-%m-%d %H:%M:%S")  # Adjust the format as needed
        #         test.passes("Time format is valid")
        #     except ValueError:
        #         test.fail(f"Invalid Time format: {cell_text}")
        if field == "To Address":
            test.compare(cell_text, packet_details["Address"], f"{field} should match '{packet_details['Address']}'")
        elif field == "To Port":
            test.compare(cell_text, packet_details["Port"], f"{field} should match '{packet_details['Port']}'")
        elif field == "Method":
            test.compare(cell_text, packet_details["Type"], f"{field} should match '{packet_details['Type']}'")
        elif field == "ASCII":
            test.compare(cell_text, packet_details["ASCII"], f"{field} should match '{packet_details['ASCII']}'")
        elif field == "HEX":
            test.compare(cell_text, packet_details["HEX"], f"{field} should match '{packet_details['HEX']}'")