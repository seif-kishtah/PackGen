# -*- coding: utf-8 -*-

import names
#checking empty send table using property rowcount

def main():
    startApplication("PackGen")    
    send_table = waitForObjectExists(names.mainWindow_SendTable_QTableWidget)
    test.compare(send_table.rowCount, 0, "Send table should be empty initially")