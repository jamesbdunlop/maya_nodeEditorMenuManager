try:
    from maya import cmds
except ImportError:
    pass
from menus import typeIDs as nem_typeids
import logging
logging.basicConfig()
logger = logging.getLogger(__name__)


class MenuBase(object):
    ID = nem_typeids.BASEID
    MENUNAME = ""
    NODENAME = ""
    FUNCTION = None

    def __init__(self, isRadial=False, radialPos=""):
        self.__isRadial = isRadial
        self.__radialPos = radialPos
        self._func = None

    def menu(self):
        """

        :return: `function`
        """
        raise NotImplementedError("Not implemented")

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

    def menufunction(self):
        if self.FUNCTION is None:
            return

        if self._func is None:
            def menuCmd(ned, node):
                if cmds.nodeType(node) == self.NODENAME:
                    try:
                        cmds.menuItem(label=self.MENUNAME, radialPosition=self.radialPos(), c=self.FUNCTION)
                        return True
                    except RuntimeError:
                        logger.warning("Can not create a valid menu item for {}".format(self.MENUNAME))
                        return False
                else:
                    return False
            self._func = menuCmd
            return menuCmd
        else:
            return self._func
