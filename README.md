# Maya NodeEditor Menu Manager

This is a small handler for adding and removing menus from the nodeEditor in Maya.

**Adding a menu:**
------------------

Comes in 2 parts.
1. An entry into the constants.modulemapping to allow the factory to automatically add your menu the 
next time you invoke the addAll
2. A menu class in the .menus; subClassing the menus.base class.

