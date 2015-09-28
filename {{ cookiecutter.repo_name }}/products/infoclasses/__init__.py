"""
This file is part of tendril
See the COPYING, README, and INSTALL files for more information
"""

import os
import imp


dirname, fname = os.path.split(os.path.abspath(__file__))


def import_(filename):
    (path, name) = os.path.split(filename)
    (name, ext) = os.path.splitext(name)
    (f, filename, data) = imp.find_module(name, [path])
    return imp.load_module(name, f, filename, data)


def get_product_info_class(line, infodict):
    modname = line
    try:
        mod = import_(os.path.join(dirname, modname))
        func = getattr(mod, 'get_info_class')
        instance = func(infodict)
        return instance
    except ImportError:
        raise ImportError("Product Line Unrecognized :" + line)

