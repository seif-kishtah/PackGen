# -*- coding: utf-8 -*-

import names


def main():
    # Iterate over each record in the dataset
    for record in testData.dataset("Test_data.tsv"):
        # Extract fields from the dataset
        name = testData.field(record, "Name")
        ascii = testData.field(record, "ASCII")
        hex = testData.field(record, "HEX")
        address = testData.field(record, "Address")
        port = testData.field(record, "Port")
        packet_type = testData.field(record, "Type")  # Renamed from 'type' to 'packet_type'
        
        test.log(f"Processing record: Name={name}, ASCII={ascii}, HEX={hex}, Address={address}, Port={port}, Type={packet_type}")
        startApplication("PackGen")
        
        packet_details = {
            "Name": name,
            "Address": address,
            "Port": port,
            "Type": packet_type,  # Use the renamed variable
            "ASCII": ascii,
            "HEX": hex
        }
        
        for field, value in packet_details.items():
            if field == "Type":
                combobox = waitForObjectExists(getattr(names, f"mainWindow_{field}_QComboBox"))
                combobox.setCurrentText(value)
            else:
                line_edit = waitForObjectExists(getattr(names, f"mainWindow_{field}Edit_QLineEdit"))
                type(line_edit, value)  # Now 'type()' refers to the built-in function
        
        save_button = waitForObjectExists(names.mainWindow_Save_QPushButton)
        mouseClick(save_button)
        
        saved_table = waitForObjectExists(names.mainWindow_SaveTable_QTableWidget)
        row_count = saved_table.rowCount
        test.compare(row_count, 1, "There should be 1 packet in the saved table")
        
        for col, (field, value) in enumerate(packet_details.items(), start=1):
            cell_text = saved_table.item(0, col).text()
            test.compare(cell_text, value, f"Column '{field}' should display '{value}'")
        
        