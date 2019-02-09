from maya.app.general import nodeEditorMenus
import logging
import NEdMenuManager.factory as neFactory
logging.basicConfig()
logger = logging.getLogger(__name__)


class NodeEditorMenuManager(object):
    def __init__(self, autoLoadMenus=True):
        self.menus = nodeEditorMenus.customInclusiveNodeItemMenuCallbacks

        if autoLoadMenus:
            print("AutoLoading nodeEditor menus now... {}".format(neFactory.MENUCACHE.keys()))
            for id, menu in neFactory.MENUCACHE.iteritems():
                self.addMenu(menu=menu)

    def addMenu(self, menu):
        """
        :param menu: `MenuBase` instance
        """
        self.menus.append(menu().menufunction())
        logger.info("{}|{} id:{}".format(menu.NODENAME, menu.MENUNAME, menu.ID))
        print("{}|{} id:{}".format(menu.NODENAME, menu.MENUNAME, menu.ID))

    def iterMenuItems(self):
        """
        :return: `int` `list`
        """
        for id, data in neFactory.MENUCACHE.iteritems():
            yield id, data

    def removeMenu(self, menuid):
        """
        :param menuid: `int`
        :return: `bool`
        """
        logger.info("Removing id {}".format(menuid))
        for id, menu in neFactory.MENUCACHE:
            if id == menuid:
                self.menus.remove(menu.menufunction())
                neFactory.MENUCACHE.pop(menuid, None)
                logger.info("Successfully removed menu!")
                return True

        logger.warning("Failed to remove menu!")
        return False

    def __repr__(self):
        str = "menuItems:\n"
        for k, v in self.iterMenuItems():
            str += "\tid: {} | node: {} name: {} \t| isradial: {} | pos: {}\n".format(
                k, v[0].NODENAME, v[0].MENUNAME, v[0].isRadial(), v[0].radialPos())
