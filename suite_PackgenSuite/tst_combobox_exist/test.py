# -*- coding: utf-8 -*-

import names


def main():
    startApplication("PackGen")
    test.compare(waitForObjectExists(names.mainWindow_Type_QComboBox).count, 3)
    test.compare(waitForObjectExists(names.mainWindow_Type_QComboBox).enabled, True)
