# -*- coding: utf-8 -*-

import names

def main():
    # Start the application
    startApplication("PackGen")
    
    packets = [
        {"Name": "Packet1", "Address": "192.168.1.1", "Port": "8080", "Type": "TCP", "ASCII": "Hello1", "HEX": "48656C6C6F31"},
        {"Name": "Packet2", "Address": "192.168.1.2", "Port": "8081", "Type": "UDP", "ASCII": "Hello2", "HEX": "48656C6C6F32"},
        {"Name": "Packet3", "Address": "192.168.1.3", "Port": "8082", "Type": "SSL", "ASCII": "Hello3", "HEX": "48656C6C6F33"}
    ]
    
    for packet in packets:
        for field, value in packet.items():
            if field == "Type":
                combobox = waitForObjectExists(getattr(names, f"mainWindow_{field}_QComboBox"))
                combobox.setCurrentText(value)
            else:
        
                line_edit = waitForObjectExists(getattr(names, f"mainWindow_{field}Edit_QLineEdit"))
                type(line_edit, value)
        
        save_button = waitForObjectExists(names.mainWindow_Save_QPushButton)
        mouseClick(save_button)
        snooze(1)  
    
    saved_table = waitForObjectExists(names.mainWindow_SaveTable_QTableWidget)
    test.compare(saved_table.rowCount, len(packets), f"There should be {len(packets)} packets in the saved table")
    test.log(f"Row count before deletion: {saved_table.rowCount}")
    
    packet_to_delete = "Packet2"
    for row in range(saved_table.rowCount):
        cell_text = saved_table.item(row, 1).text()  
        if cell_text == packet_to_delete:
            saved_table.setCurrentCell(row, 0)  # Select the first cell in the row
            test.log(f"Selected row with packet: {packet_to_delete}")
            
            delete_button = waitForObjectExists(names.mainWindow_DeleteSaved_QPushButton)
            mouseClick(delete_button)
            test.log(f"Deleted packet: {packet_to_delete}")
            break
    
    test.compare(saved_table.rowCount, len(packets) - 1, f"There should be {len(packets) - 1} packets after deletion")
    test.log(f"Row count after deletion: {saved_table.rowCount}")
    
    remaining_packets = [packet["Name"] for packet in packets if packet["Name"] != packet_to_delete]
    for row in range(saved_table.rowCount):
        cell_text = saved_table.item(row, 1).text()  
        test.verify(cell_text in remaining_packets, f"Packet '{cell_text}' should remain in the table")
