import importlib
import os
import sys


def auto_import(package_name: str, excluded: set[str] | None = None):
    """Auto-import all modules in the current package directory.

    Usage in __init__.py:
        from autoimport import auto_import
        auto_import("shell")  # imports all .py files in shell/ except __init__
        auto_import("shell", {"awscli"})  # exclude specific modules
    """
    if excluded is None:
        excluded = set()
    excluded.add("__init__")

    package_file = sys.modules[package_name].__file__
    if package_file is None:
        return
    package_dir = os.path.dirname(package_file)

    for module in os.listdir(package_dir):
        if module.endswith(".py") and module[:-3] not in excluded:
            importlib.import_module(f"{package_name}.{module[:-3]}")
