import os, pprint
import importlib, inspect
import logging
logging.basicConfig()
logger = logging.getLogger(__name__)

BASE = os.path.dirname(__file__)
MENUSPATH = "{}/menus".format(BASE)


MENUCACHE = {}
def createMenuCache(path=MENUSPATH, pkg="menus"):
    """
    Recurisvely fetch all the .py modules in the menus folder and any classes defined as a menu and add these to the
    cache
    :param path: `str` path to the root menus folder
    :param pkg: `str` .separated path for the importlib.import_module to use
    """
    for module in os.listdir(path):
        if module == '__init__.py' or module.endswith(".pyc"):
            continue

        if module.endswith(".py"):
            mod = importlib.import_module(name=".{}".format(module[:-3]), package=pkg)
            for eachMenu in inspect.getmembers(mod, inspect.isclass):
                MENUCACHE[eachMenu[1].ID] = eachMenu[1]
        else:
            createMenuCache(path="{}/{}".format(path, module), pkg="{}.{}".format(pkg, module))

    logger.info("MenuCache:")
    pprint.pprint(MENUCACHE)

if __name__ == "__main__":
    createMenuCache(MENUSPATH)
