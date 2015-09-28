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


def get_test_object(testst, offline=False):
    if '.' in testst:
        modname, clsname = testst.rsplit('.', 1)
    elif ':' in testst:
        modname, clsname = testst.split(':')
        clsname = 'Test' + clsname
    else:
        modname = testst
        clsname = 'Test' + testst
    try:
        mod = import_(os.path.join(dirname, modname))
        cls = getattr(mod, clsname)
        instance = cls(offline=offline)
        return instance
    except ImportError:
        raise ValueError("Test Unrecognized :" + testst)
