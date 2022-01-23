#  Copyright (c) 2020.  James B Dunlop
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
        ["neMenus", ".example", "MenuExample01"],
        ["neMenus", ".example", "MenuExample02"],
        ["neMenus", ".example", "MenuExample03"],
        ]
    }