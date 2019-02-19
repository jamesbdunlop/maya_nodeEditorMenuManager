from maya import cmds
import logging
logging.basicConfig()
logger = logging.getLogger(__name__)


class MenuBase(object):
    ID = None
    MENUNAME = None
    NODENAME = None
    FUNCTION = None
    ISSUBMENU = False
    SUBMENUS = list()

    def __init__(self, isRadial=False, radialPos="", hasSubMenu=False, lastSubMenu=False):
        self.__isRadial = isRadial
        self.__radialPos = radialPos
        self.__func = None
        self.__hasSubMenu = hasSubMenu
        self.__lastSubMenu = lastSubMenu
        # Set the cmd instance on init we want to create only ONE instance of the menuCmd.
        # So well force that now and reuse it thereafter
        self.menufunction()

    def id(self):
        return self.ID

    def name(self):
        return self.MENUNAME

    def nodeType(self):
        return self.NODENAME

    def isRadial(self):
        return self.__isRadial

    def radialPos(self):
        return self.__radialPos

    def createMenuItem(self):
        if self.FUNCTION is None:
            return

        if self.isRadial():
            self._menuItem = cmds.menuItem(label=self.MENUNAME, c=self.FUNCTION,
                                           subMenu=self.hasSubMenu(),
                                           radialPosition=self.radialPos(),
                                           )
            if self.ISSUBMENU and self.__lastSubMenu:
                # Reset the maya internal parent so we don't end up
                # with all subsequent menus parented under this one!!
                cmds.setParent("..", menu=True)
        else:
            self._menuItem = cmds.menuItem(label=self.MENUNAME, c=self.FUNCTION,
                                           subMenu=self.hasSubMenu(),
                                           )
            if self.ISSUBMENU and self.__lastSubMenu:
                # Reset the maya internal parent so we don't end up
                # with all subsequent menus parented under this one!!
                cmds.setParent("..", menu=True)
        return self._menuItem

    def hasSubMenu(self):
        return self.__hasSubMenu

    def subMenus(self):
        return self.SUBMENUS

    def subMenus(self):
        return self.SUBMENUS

    def menufunction(self):
        if self.FUNCTION is None:
            return

        if self.__func is None:
            if self.NODENAME is not None:
                # Create the menu command for the node we have rightClicked over in Maya
                def menuCmd(ned, node):
                    if cmds.nodeType(node) == self.NODENAME:
                        self.createMenuItem()
                        return True
                    else:
                        return False
            else:
                # Add a general menu to all nodes. Take care with Radial positions here as you might clash with a node
                # based menu item!
                def menuCmd(ned, node):
                    self.createMenuItem()
                    return True

            self.__func = menuCmd
            return menuCmd
        else:
            return self.__func
