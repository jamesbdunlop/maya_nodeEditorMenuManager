#  Copyright (c) 2020.  James B Dunlop
# pylint: disable=import-error, invalid-name, missing-class-docstring, line-too-long, missing-module-docstring, invalid-name
import logging

from maya import cmds as cmds

logger = logging.getLogger(__name__)


class NEMenu:
    ID = ""                 # string name of the ID you want to assign. Keep these unique as they become keys in a dict.
    NODE_TYPE = ""          # string name of the nodetype in Maya eg: "transform"
    MENU_NAME = ""          # string name of the menu as it will appear in the rc
    IS_RADIAL = False       # bool for it we want this to appear in the radial menu or not.
    POSITION = ""           # string name of the radial position. Valid positions are:
                                # "NW", "N", "NE", "W", "SW", "S" , "SE", "E"
    MENU_KWARGS = {'enable': True,
                   'subMenu': False,
                   'enableCommandRepeat': False, # Note this will error if set to True.
                   'boldFont': True,
                   }
    _NODE = None

    @staticmethod
    def doIt(node):
        """ Your code goes here for when the menu is triggered.
        See menus.TransformExample

        Args:
            node (str): Name of the node that the menu was invoked over. This is passed along by Maya.

        Returns:
            None
        """
        pass

    def getfunction(self, ned, node, func=""):
        nodetype = cmds.nodeType(node)
        if nodetype != self.NODE_TYPE:
            return False

        if self.IS_RADIAL:
            cmds.menuItem(radialPosition=self.POSITION, label=self.MENU_NAME,
                          c=func, **self.MENU_KWARGS)
            return True

        cmds.menuItem(label=self.MENU_NAME, c=func, **self.MENU_KWARGS)

        return True
