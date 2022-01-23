#  Copyright (c) 2020.  James B Dunlop
# pylint: disable=import-error, invalid-name, missing-class-docstring, line-too-long, missing-module-docstring, invalid-name

"""
This dict is used by the  importlib.import_module(moduleName, package) to source the menu class from the files.

The expected format is
"nodeTypeName": [
                ["package", "moduleName", "className"],
                ["package", "moduleName", "className"],
                ],

"""
MODULE_MAPPING = {
    "transform": [
        ["nodeEditorMenuManger", ".menus.example", "MenuExample01"],
        ["nodeEditorMenuManger", ".menus.example", "MenuExample02"],
        ["nodeEditorMenuManger", ".menus.example", "MenuExample03"],
        ["nodeEditorMenuManger", ".menus.example", "MenuExample04"]
        ]
    }