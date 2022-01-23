#  Copyright (c) 2020.  James B Dunlop
# pylint: disable=import-error, invalid-name, missing-class-docstring, line-too-long, missing-module-docstring, invalid-name
from maya import cmds as cmds
from nodeEditorMenuManger.constants import nodeTypes as nedmmc_nodetypes
from nodeEditorMenuManger.menus import base as nedmm_base


# FlatMenu
class MenuExample01(nedmm_base.NEMenu):
    ID = "menuExample01"
    NODE_TYPE = nedmmc_nodetypes.TRANSFORM
    MENU_NAME = "ExampleMenu01"

    @staticmethod
    def doIt(node):
        print("#############################")
        print("node: %s", node)
        print("MenuExample01._NODE: %s", MenuExample01._NODE)
        print("#############################")

    def getfunction(self, ned, node):
        MenuExample01._NODE = node
        nedmm_base.NEMenu.getfunction(self, ned, node, func=self.doIt)


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
        print("MenuExample02._NODE: %s", MenuExample02._NODE)
        print("#############################")

    def getfunction(self, ned, node):
        MenuExample02._NODE = node
        nedmm_base.NEMenu.getfunction(self, ned, node, func=self.doIt)


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
    def subMenu1DoIt(node):
        print("#############################")
        print("I am a submenu called 1")
        print("#############################")

    @staticmethod
    def subMenu2DoIt(node):
        print("#############################")
        print("I am a submenu called 2")
        print("#############################")

    def getfunction(self, ned, node):
        MenuExample03._NODE = node
        nedmm_base.NEMenu.getfunction(self, ned, node)

        # SubMenuItem01
        cmds.menuItem(label="example03SubMenu1", c=self.subMenu1DoIt)
        # SubMenuItem02
        cmds.menuItem(label="example03SubMenu2", c=self.subMenu2DoIt)
        cmds.setParent('..', menu=True)


# RadialMenu with subMenu items
class MenuExample04(nedmm_base.NEMenu):
    ID = "menuExample04"
    NODE_TYPE = nedmmc_nodetypes.TRANSFORM
    MENU_NAME = "ExampleMenu04"
    IS_RADIAL = True
    POSITION = "S"
    MENU_KWARGS = {'enable': True,
                   'subMenu': True,
                   'enableCommandRepeat': False,
                   'boldFont': True,
                   }
    @staticmethod
    def subMenu1DoIt(node):
        print("#############################")
        print("I am a submenu called 1")
        print("#############################")

    @staticmethod
    def subMenu2DoIt(node):
        print("#############################")
        print("I am a submenu called 2")
        print("#############################")

    def getfunction(self, ned, node):
        MenuExample04._NODE = node
        nedmm_base.NEMenu.getfunction(self, ned, node)

        # SubMenuItem01
        cmds.menuItem(label="example03SubMenu1", c=self.subMenu1DoIt)

        # SubMenuItem02
        cmds.menuItem(label="example03SubMenu2", c=self.subMenu2DoIt)
        cmds.setParent('..', menu=True)