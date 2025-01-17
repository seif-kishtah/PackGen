# -*- coding: utf-8 -*-

import names

def main():
    startApplication("PackGen")
    saved_table = waitForObjectExists(names.mainWindow_SendTable_QTableWidget)
    expected_columns = ["Time","To Address", "To Port", "Method", "ASCII", "Hex"]
    column_count = saved_table.columnCount
    test.compare(column_count, len(expected_columns), "Column count should match")
    for index, expected_column in enumerate(expected_columns):
        column_header = saved_table.horizontalHeaderItem(index).text()        
        test.compare(column_header, expected_column, f"Column {index + 1} should be '{expected_column}'")
