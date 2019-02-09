try:
    from maya import cmds
except ImportError:
    pass
from NEdMenuManager.menus import typeIDs as nem_typeids
from NEdMenuManager import base as nem_base
import logging
logging.basicConfig()
logger = logging.getLogger(__name__)

def createOutputJnts(*args):
    ## Create outputs for the selected hermite nodes
    exitB = "Exit"
    doitB = "doIt"
    if not cmds.ls(sl=True):
        logger.warning("You must have a {} selected!".format(nem_typeids.HA_NODENAME))
        return
    confirm = cmds.confirmDialog(title="Create?", message="Ok?", button=doitB, db=doitB, b=exitB, cb=exitB)
    if confirm == doitB:
        for e in cmds.ls(sl=True):
            outCount = cmds.getAttr("{}.outputCount".format(e))
            for x in range(outCount):
                loc = cmds.joint(n='{}_out{}'.format(e, x))
                cmds.select(clear=True)
                cmds.connectAttr("{}.outputs[{}].translate".format(e, x), "{}.translate".format(loc), f=True)
                cmds.connectAttr("{}.outputs[{}].rotate".format(e, x), "{}.rotate".format(loc), f=True)
                cmds.connectAttr("{}.outputs[{}].scale".format(e, x), "{}.scale".format(loc), f=True)


class HermiteArraySOUTH(nem_base.MenuBase):
    ID = nem_typeids.HASOUTH
    MENUNAME = nem_typeids.HASOUTH_MENUNAME
    NODENAME = nem_typeids.HA_NODENAME
    FUNCTION = createOutputJnts

    def __init__(self):
        nem_base.MenuBase.__init__(self, isRadial=True, radialPos="S")


class HermiteArrayNORTH(nem_base.MenuBase):
    ID = nem_typeids.HANORTH
    MENUNAME = nem_typeids.HANORTH_MENUNAME
    NODENAME = nem_typeids.HA_NODENAME
    FUNCTION = ""

    def __init__(self):
        nem_base.MenuBase.__init__(self, isRadial=True, radialPos="N")
