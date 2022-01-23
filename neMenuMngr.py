#  Copyright (c) 2020.  James B Dunlop
# pylint: disable=import-error, invalid-name, missing-class-docstring, line-too-long, missing-module-docstring, invalid-name
import importlib
import inspect
import logging

import nemodulemapping as nemodulemapping
from neMenuManager.menuManager import MenuManager

logger = logging.getLogger(__name__)

MODULE_MAPPING = nemodulemapping.MODULE_MAPPING

def addNodeEditorMenusByNodeType(nodeType, manager=None):
    """

    Args:
        nodeType (str): Name of the nodeType in Maya. eg: "transform"

    Returns:
        neMenuManager.MenuManager()
    """
    if manager is None:
        manager = MenuManager()

    for package, moduleName, className in MODULE_MAPPING.get(nodeType, [[None] * 3]):
        if moduleName is None or package is None or className is None:
            raise Exception("MODULE_MAPPING MISSING: {}".format(nodeType))

        module = importlib.import_module(moduleName, package)

        try:
            inspect.isclass(getattr(module, className))
        except AttributeError:
            raise Exception(
                "Failed to find class for typeID: {} in module: {}".format(
                    nodeType, moduleName
                )
            )

        getClass = getattr(module, className)
        neMenu = getClass()

        manager.addMenu(neMenu)

    return manager

def addMenus(removeFirst=False):
    """ Iter through the entire MODULE_MAPPING dict and add all the nodeTypes to the menuManager.

    Returns:
        None
    """
    manager = MenuManager()
    if removeFirst:
        manager.removeAll()

    for nodeType in MODULE_MAPPING.keys():
        addNodeEditorMenusByNodeType(nodeType, manager)

    return manager

def removeMenus():
    """ Removes all the menus.

    Returns:
        None
    """
    manager = MenuManager()
    manager.removeAll()

    return manager