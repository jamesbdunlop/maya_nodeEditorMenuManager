#  Copyright (c) 2020.  James B Dunlop
# pylint: disable=import-error, invalid-name, missing-class-docstring, line-too-long, missing-module-docstring, invalid-name
from maya import cmds as cmds
from neMenus import base as nedmm_base
from neMenuManager.constants import nodeTypes as nedmmc_nodetypes


# FlatMenu
class MenuExample01(nedmm_base.NEMenu):
    ID = "menuExample01"
    NODE_TYPE = nedmmc_nodetypes.TRANSFORM
    MENU_NAME = "ExampleMenu01"

    @staticmethod
    def doIt(node):
        print("#############################")
        print("node: %s", node)
        print("MenuExample01.MNODE: %s", MenuExample01.MNODE)

    def menuFunction(self, ned, node):
        MenuExample01.MNODE = node
        nedmm_base.NEMenu._menuFunction(self, ned, node, func=self.doIt)


# RadialMenu
class MenuExample02(nedmm_base.NEMenu):
    ID = "menuExample02"
    NODE_TYPE = nedmmc_nodetypes.TRANSFORM
    MENU_NAME = "ExampleMenu02"
    IS_RADIAL = True
    POSITION = "W"

    @staticmethod
    def doIt(node):
        print("#############################")
        print("node: %s", node)
        print("MenuExample02.MNODE: %s", MenuExample02.MNODE)

    def menuFunction(self, ned, node):
        MenuExample02.MNODE = node
        nedmm_base.NEMenu._menuFunction(self, ned, node, func=self.doIt)


# FlatMenu with subMenu items
class MenuExample03(nedmm_base.NEMenu):
    ID = "menuExample03"
    NODE_TYPE = nedmmc_nodetypes.TRANSFORM
    MENU_NAME = "ExampleMenu03"
    MENU_KWARGS = {'enable': True,
                   'subMenu': True,
                   'enableCommandRepeat': False,
                   'boldFont': True,
                   }

    @staticmethod
    def subMenu1_item1_DoIt(node):
        print("#############################")
        print("I am subMenu1_item1_DoIt")

    @staticmethod
    def subMenu1_item2_DoIt(node):
        print("#############################")
        print("I am subMenu1_item2_DoIt")

    @staticmethod
    def subMenu1_item3_DoIt(node):
        print("#############################")
        print("I am subMenu1_item3_DoIt")

    @staticmethod
    def subMenu2_item1_DoIt(node):
        print("#############################")
        print("I am subMenu2_item1_DoIt")

    def menuFunction(self, ned, node):
        # This constructs a more complex menu structure with xNum of subMenus.
        # Note the use of cmds.setParent here if incorrectly used your menus will not look correct!!!
        MenuExample03.MNODE = node
        # Because all the other examples don't care for appending menus etc we should check if we the _menuFunction
        # found the correct nodeType or not.
        status = nedmm_base.NEMenu._menuFunction(self, ned, node)
        if not status:
            return status

        # SubMenuItem01
        cmds.menuItem(label="example03SubMenu1Item1", c=self.subMenu1_item1_DoIt)
        # SubMenuItem02
        cmds.menuItem(label="example03SubMenu1Item2", c=self.subMenu1_item2_DoIt)
        cmds.menuItem(label="example03SubMenu2SubMenu", subMenu=True)
        cmds.menuItem(label="example03SubMenu2SubMenuItem1", c=self.subMenu2_item1_DoIt)
        cmds.setParent('..', menu=True)
        cmds.menuItem(label="example03SubMenu1Item3", c=self.subMenu1_item3_DoIt)
        cmds.setParent('..', menu=True)


# Common Menu
class MenuExample04(nedmm_base.NEMenu):
    ID = "menuExample04"
    NODE_TYPE = nedmmc_nodetypes.COMMONNODENAME
    MENU_NAME = "CommonExampleMenu04"

    @staticmethod
    def doIt(node):
        print("#############################")
        print("I am MenuExample04 doIt!")

    def menuFunction(self, ned, node):
        MenuExample04.MNODE = node
        nedmm_base.NEMenu._menuFunction(self, ned, node, func=self.doIt, skipNodeTypeCheck=True)
