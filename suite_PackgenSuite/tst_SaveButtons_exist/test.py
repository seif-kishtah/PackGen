# -*- coding: utf-8 -*-

import names



def main():
    startApplication("PackGen")
    save_button = waitForObject(names.mainWindow_Save_QPushButton)
    test.verify(save_button.enabled, "Save button should be enabled")
    test.verify(save_button.visible, "Save button should be visible")
    test.verify(save_button.text == "Save", "Save button text should be 'Save'")