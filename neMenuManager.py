from maya.app.general import nodeEditorMenus
import menuFactory as ne_factory
import logging
logging.basicConfig()
logger = logging.getLogger(__name__)
"""
usage:
import sys
path = "T://software//neMenuManager"
if path not in sys.path:
    sys.path.append(path)

import neMenuManager as neMM
nedMenuManager = neMM.NodeEditorMenuManager(autoLoadMenus=True, reload=False)
for id, e in nedMenuManager.iterMenuItems():
    print(id)
"""


class NodeEditorMenuManager(object):
    def __init__(self, autoLoadMenus=True, reload=False):
        self.menus = nodeEditorMenus.customInclusiveNodeItemMenuCallbacks
        self._ids = []
        if reload:
            logger.warning("Resetting ne_factory.MENUCACHE now!")
            ne_factory.MENUCACHE = {}

        if ne_factory.MENUCACHE:
            # We should REMOVE any previously appeded functions in maya or we end up with duplicates!
            self._ids = ne_factory.MENUCACHE.keys()
            self.removeAll()
        else:
            logger.warning("Creating ne_factory.MENUCACHE now!")
            ne_factory.createMenuCache()

        if autoLoadMenus:
            # Maya sucks at editing the menus, so we're going to iter twice. First for the mainMenu items
            # Then again for anything flagged as a subMenu of something else.
            # This means we only EVER go 1 level deep menu|subMenu NOT menu|menu|subMenu

            for id, menu in ne_factory.MENUCACHE.iteritems():
                self.addMenu(menu=menu)
                self._ids.append(id)

    def addMenu(self, menu):
        """
        :param menu: `MenuBase` instance
        """
        if menu.menufunction() is not None:
            self.menus.append(menu.menufunction())
            logger.info("Added: {} id:{} func: {}".format(menu.name(), menu.id(), menu.menufunction()))

    def iterMenuItems(self):
        """
        :return: `int` `MenuBase() Instance`
        """
        for id, data in ne_factory.MENUCACHE.iteritems():
            yield id, data

    def removeMenu(self, menuid):
        """
        :param menuid: `int`
        :return: `bool`
        """
        if menuid in ne_factory.MENUCACHE.keys():
            menu = ne_factory.MENUCACHE[menuid]
            try:
                self.menus.remove(menu.menufunction())
            except ValueError:
                logger.warning("Failed to remove {} from maya's internal callback list!".format(menu.name()))
                return False

            ne_factory.MENUCACHE.pop(menuid, None)
            self._ids.remove(menuid)

            logger.info("Successfully removed menu {}".format(menu.name()))
            return True

        return False

    def removeAll(self):
        """Remove all the menus before a reload!"""
        while self._ids:
            for eachID in self._ids:
                self.removeMenu(menuid=eachID)

    def currentCache(self):
        return ne_factory.MENUCACHE

    def __repr__(self):
        str = "menuItems:\n"
        for k, v in self.iterMenuItems():
            str += "\t id: {}".format(k)
            str += "\t name: {}".format(v.name())
            str += "\t nodeType: {}".format(v.nodeType())
            str += "\t isradial: {}".format(v.isRadial())
            str += "\t pos: {}".format(v.radialPos())
            str += "\t func: {}\n".format(v.menufunction())

        return str

