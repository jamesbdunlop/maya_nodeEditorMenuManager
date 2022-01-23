#  Copyright (c) 2020.  James B Dunlop
# pylint: disable=import-error, invalid-name, missing-class-docstring, line-too-long, missing-module-docstring, invalid-name

from neMenuManager.constants import nodeTypes as nemmc_nodeTypes
"""
This dict is used by the  importlib.import_module(moduleName, package) to source the menu classes from the files.

The expected format is
"nodeTypeName": [
                ["package", "moduleName", "className"],
                ["package", "moduleName", "className"],
                ],

Note if you add a new menu py be sure to update this file or it won't appear the next time you add the menus.
"""
MODULE_MAPPING = {
    nemmc_nodeTypes.TRANSFORM: [
        ["neMenus", ".menus.example", "MenuExample01"],
        ["neMenus", ".menus.example", "MenuExample02"],
        ["neMenus", ".menus.example", "MenuExample03"],
        ]
    }