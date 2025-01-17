# -*- coding: utf-8 -*-

import names


def main():
    startApplication("PackGen")
    test.compare(waitForObjectExists(names.mainWindow_ClearContent_QPushButton).enabled, True)
    test.compare(str(waitForObjectExists(names.mainWindow_ClearContent_QPushButton).text), "Clear Contents")
