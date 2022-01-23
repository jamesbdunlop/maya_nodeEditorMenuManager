#  Copyright (c) 2020.  James B Dunlop
# pylint: disable=import-error, invalid-name, missing-class-docstring, line-too-long, missing-module-docstring, invalid-name
import logging

from maya.app.general import nodeEditorMenus

logger = logging.getLogger(__name__)


class NEDMenuManager:
    """ Setup singleton for the NEDMenus to use"""
    instance = None

    class __NodeEditorMenus:
        def __init__(self):
            # Our handler dict for manging the list of functions maya has.
            self.activeMenus = dict()
            # The maya list that will just accept the funcs() to use for the menus.
            self.menus = nodeEditorMenus.customInclusiveNodeItemMenuCallbacks

        def addMenu(self, menu):
            """Adds a menu to the maya nodeEditorMenus list

            Args:
                menu (MenuBase): instance of the MenuBase class

            Returns:
                None
            """
            if menu.ID in self.activeMenus.keys():
                self.removeMenu(menu.ID)

            self.activeMenus[menu.ID] = [menu, menu.menuFunction]
            self.menus.append(self.activeMenus[menu.ID][1])
            logger.info("Added: \t{}|{} id:{}".format(menu.NODE_TYPE, menu.MENU_NAME, menu.ID))

        def iterMenuItems(self):
            """

            Returns:
                int, list[menu, function]
            """
            for idx, menuData in self.activeMenus.items():
                yield idx, menuData

        def removeMenu(self, menuid):
            """

            Args:
                menuid (string): the id of the menu to remove

            Returns:
                bool

            """
            logger.info("Removing id %s", menuid)
            for id, data in list(self.iterMenuItems()):
                if id == menuid:
                    self.menus.remove(data[1])
                    self.activeMenus.pop(menuid, None)
                    logger.info("SUCCESS: removed menu: %s", menuid)
                    return True

            logger.info("FAILED: to find menu: %s to remove!", menuid)
            return False

        def removeAll(self):
            for idx, _ in list(self.iterMenuItems()):
                self.removeMenu(idx)

        def __repr__(self):
            rprstr = "menuItems:\n"
            for k, v in self.iterMenuItems():
                rprstr += "\tid: {} | node: {} name: {} \t| isradial: {} | pos: {}\n".format(
                    k, v[0].NODE_TYPE, v[0].MENU_NAME, v[0].IS_RADIAL, v[0].POSITION
                )
            return rprstr

    def __new__(cls, *args, **kwargs):
        if NEDMenuManager.instance is None:
            NEDMenuManager.instance = NEDMenuManager.__NodeEditorMenus()
        return NEDMenuManager.instance

    def __getattr__(self, item):
        return getattr(self.instance, item)

    def __setattr__(self, key, value):
        return setattr(self.instance, key, value)


