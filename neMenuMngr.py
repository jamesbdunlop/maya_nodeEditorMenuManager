#  Copyright (c) 2020.  James B Dunlop
import neMenuManager.neMenuManagerFactory as mm_factory


def addMenus(removeFirst=True):
    """

    Args:
        removeFirst (bool): If you want to remove all the previously loaded menus before adding all the menus again.

    Returns:
        None
    """
    mm_factory.addAllMenus(removeFirst=removeFirst)
