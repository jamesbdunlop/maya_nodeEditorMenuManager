from maya.app.general import nodeEditorMenus
import logging
import menuFactory as ne_factory
logging.basicConfig()
logger = logging.getLogger(__name__)
"""
usage:
import sys
path = "T://software//neMenuManager"
if path not in sys.path:
    sys.path.append(path)

import neMenuManager as neMM
nedMenuManager = neMM.NodeEditorMenuManager()
for id, e in nedMenuManager.iterMenuItems():
    print(id)
"""


class NodeEditorMenuManager(object):
    def __init__(self, autoLoadMenus=True):
        self.menus = nodeEditorMenus.customInclusiveNodeItemMenuCallbacks
        self._ids = []
        if ne_factory.MENUCACHE:
            self._ids = ne_factory.keys()
            self.removeAll()
        else:
            logger.warning("Creating MENUCACHE now!")
            ne_factory.createMenuCache()

        if autoLoadMenus:
            logger.info("AutoLoading nodeEditor menus")
            for id, menu in ne_factory.MENUCACHE.iteritems():
                self.addMenu(menu=menu)
                self._ids.append(id)

    def addMenu(self, menu):
        """
        :param menu: `MenuBase` instance
        """
        if menu.menufunction() is not None:
            self.menus.append(menu.menufunction())
            logger.info("Added: {}|{} id:{} func: {}".format(menu.nodeType(), menu.name(), menu.id(), menu.menufunction()))

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
        logger.info("Removing id {}".format(menuid))
        if menuid in ne_factory.MENUCACHE.keys():
            try:
                self.menus.remove(ne_factory.MENUCACHE[menuid].menufunction())
            except ValueError:
                logger.warning("Failed to remove menuid: {} from maya's internal callback list!".format(menuid))
                return False

            ne_factory.MENUCACHE.pop(menuid, None)
            self._ids.remove(menuid)

            logger.info("Successfully removed menu!")
            return True

        logger.warning("Failed to remove menu!")
        return False

    def removeAll(self):
        """Remove all the menus before a reload!"""
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
            str += "\t pos: {}\n".format(v.radialPos())
            str += "\t func: {}\n".format(v.menufunction())

        return str
