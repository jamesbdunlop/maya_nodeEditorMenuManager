# Maya NodeEditor Menu Manager

This is a small handler for adding and removing menus from the nodeEditor in Maya.

![exampleGif](/nemm_example.gif)

![resetXFexampleGif](/resetTransformExample.gif)

**Important:**
==============
To add a menu, it is defined in 2 parts.
1. A new menu class in the neMenus, subClassing the menus.base class.
2. An entry into the modulemapping to allow the factory to automatically add your menu the 
next time you invoke the addMenus()

Adding a menu:
==============
Step 1:
-------
To create a new menu you should inherit from the base class.
Go ahead and create a new .py file or add a class to an existing in the neMenus folder.

Step 2:
-------
Be sure to over load the menuFunction() and doIt() methods. 
It's important to set the class attr for MNODE if you want to use this data passed along by Maya that you invoked the menu
from, and then to avoid typing the same boilerPlate over and over call the protected _menuFunction eg:
```
    def menuFunction(self, ned, node):
        MenuExample01.MNODE = node
        nedmm_base.NEMenu._menuFunction(self, ned, node, func=self.doIt)
```

The doIt() is all the code you need to run when the menu is triggered. Be sure to have the node arg as that is 
required by Maya, though this is usually a bool.

For more complex menus with subMenus etc refer to MenuExample03 in the example.py

Step 3:
------
Add the correct data to the nemodulemapping.py file into the MODULE_MAPPING dict. This is for the factory to find and import the menu classes.
Check the doc string in the file for more info.

______
Usage:
------
Once you're done with that you should be good to run the usage below.

Inside Maya in a python script editor;
```
import sys
paths = ["PATHTOREPO/maya_nodeEditorMenuManager"]
for path in paths:
    sys.path.append(path)

import neMenuMngr as neMenuMngr
neMenuMngr.addMenus(removeFirst=True)
```