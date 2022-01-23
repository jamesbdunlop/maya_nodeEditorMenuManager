#  Copyright (c) 2020.  James B Dunlop
# pylint: disable=import-error, invalid-name, missing-class-docstring, line-too-long, missing-module-docstring, invalid-name
from maya import cmds as cmds
from neMenus import base as nedmm_base
from neMenuManager.constants import nodeTypes as nedmmc_nodetypes


class ResetTransform(nedmm_base.NEMenu):
    ID = "ResetTransform"
    NODE_TYPE = nedmmc_nodetypes.TRANSFORM
    MENU_NAME = "Reset trs"

    @staticmethod
    def doIt(node):
        for attr in ("translateX", "translateY", "translateZ", "rotateX", "rotateY", "rotateZ"):
            cmds.setAttr("{}.{}".format(ResetTransform.MNODE, attr), 0)

        for attr in ("scaleX", "scaleY", "scaleZ"):
            cmds.setAttr("{}.{}".format(ResetTransform.MNODE, attr), 1)

    def menuFunction(self, ned, node):
        ResetTransform.MNODE = node
        nedmm_base.NEMenu._menuFunction(self, ned, node, func=self.doIt)
