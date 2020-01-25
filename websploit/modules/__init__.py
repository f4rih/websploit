import os
import pkgutil

__all__ = list(module for _, module, _ in pkgutil.iter_modules([os.path.dirname(__file__)]))


def all_modules():
    """print available modules in nice way"""
    print(f"{'Modules':30}\t{'Description'}")
    print(f"{'='*30}\t{'='*30}")
    for module in __all__:
        try:
            current_module = globals()[module].Main()
            print(f"{module:30}\t{current_module.__doc__}")
        except AttributeError:
            print(f"*** Module `{module}` not has `Main` class!")
    print("\n")


def module_list():
    return __all__
