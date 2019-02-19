try:
    from maya import cmds
except ImportError:
    pass
from menus import typeIDs as nem_typeids, base as nem_base
import logging
logging.basicConfig()
logger = logging.getLogger(__name__)


def test(*args):
    print("Hello nodeEditor")


class COPYNODES(nem_base.MenuBase):
    ID = nem_typeids.COPYID
    MENUNAME = nem_typeids.COPY_MENUNAME
    NODENAME = nem_typeids.COMMONNODENAME
    FUNCTION = test
    ISSUBMENU = True

    def __init__(self, lastSubMenu=False):
        nem_base.MenuBase.__init__(self, lastSubMenu=lastSubMenu)


class PASTENODES(nem_base.MenuBase):
    ID = nem_typeids.PASTEID
    MENUNAME = nem_typeids.PASTE_MENUNAME
    NODENAME = nem_typeids.COMMONNODENAME
    FUNCTION = test
    ISSUBMENU = True

    def __init__(self, lastSubMenu=False):
        nem_base.MenuBase.__init__(self, lastSubMenu=lastSubMenu)


class UTILS(nem_base.MenuBase):
    ID = nem_typeids.UTILSID
    MENUNAME = nem_typeids.UTILS_MENUNAME
    NODENAME = nem_typeids.COMMONNODENAME
    FUNCTION = ""

    def __init__(self):
        nem_base.MenuBase.__init__(self,
                                   isRadial=nem_typeids.UTILS_ISRADIAL,
                                   radialPos=nem_typeids.UTILS_RADIALPOS,
                                   hasSubMenu=True)
        self.SUBMENUS.append(COPYNODES())
        self.SUBMENUS.append(PASTENODES(lastSubMenu=True))
