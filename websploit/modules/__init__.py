import os
import pkgutil
from websploit.core.utils import CPrint
cp = CPrint()

__all__ = list(module for _, module, _ in pkgutil.iter_modules([os.path.dirname(__file__)]))


def all_modules():
    """print available modules in nice way"""
    cp.green(f"{'Modules':<20}\t{'Description':<20}")
    cp.green(f"{'--'*10}\t{'--'*13}")
    for module in __all__:
        try:
            current_module = globals()[module].Main()
            cp.yellow(f"{module:<20}\t{current_module.__doc__}")
        except AttributeError:
            print(f"*** Module `{module}` not has `Main` class!")
    print("\n")


def module_list():
    return __all__
