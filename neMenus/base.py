#  Copyright (c) 2020.  James B Dunlop
# pylint: disable=import-error, invalid-name, missing-class-docstring, line-too-long, missing-module-docstring, invalid-name
import logging

from maya import cmds as cmds
import maya.api.OpenMaya as om2

logger = logging.getLogger(__name__)


class NEMenu:
    ID = ""                 # string name of the ID you want to assign. Keep these unique as they become keys in a dict.
    NODE_TYPE = ""          # string name of the nodetype in Maya eg: "transform" from the constants.nodeTypes module
    MENU_NAME = ""          # string name of the menu as it will appear in the rc
    IS_RADIAL = False       # bool for it we want this to appear in the radial menu or not.
    POSITION = ""           # string name of the radial position. Valid positions are:
                                # "NW", "N", "NE", "W", "SW", "S" , "SE", "E"
    MENU_KWARGS = {'enable': True,
                   'subMenu': False,
                   'enableCommandRepeat': False, # Note this will error if set to True.
                   'boldFont': True,
                   }
    MNODE = None

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

    def _menuFunction(self, ned, node, func="", skipNodeTypeCheck=False):
        """ Please see the example.py menu for the use of this method with the menuFunction() method.

        This is here to mainly just remove some boiler plate from the menuFunction, and should be added after you have
        set the node as a class attr in your menuFunction method for your menu.

        Args:
            ned (str): For Internal Maya Use
            node (str): For Internal Maya Use
            func (function): The function the command will be associated with via the cmds.menuItem
            skipNodeTypeCheck (bool):

        Returns:
            Bool
        """
        # Note sticking to cmds here as om2 can return a kPluginDependNode which is non descript if you want to add to
        # something like the inverseMatrix node etc..
        nodetype = cmds.nodeType(node)
        if nodetype != self.NODE_TYPE and not skipNodeTypeCheck:
            return False

        if self.IS_RADIAL:
            cmds.menuItem(radialPosition=self.POSITION,
                          label=self.MENU_NAME,
                          c=func,
                          **self.MENU_KWARGS)
            return True

        cmds.menuItem(label=self.MENU_NAME,
                      c=func,
                      **self.MENU_KWARGS)
        return True

    def menuFunction(self):
        """Intended to be over loaded per menu. Check example.py for uses"""
        pass