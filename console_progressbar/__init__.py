# -*- coding: utf-8 -*-
'''
Simple progress bar for console
'''
import sys
from console_progressbar.progressbar import ProgressBar


__author__ = 'Carlos Alexandre S. da Fonseca'
__version__ = '1.1.2'
__date__ = '2019-08-08'  # YYYY-MM-DD

_DEBUG_MODE = False

if _DEBUG_MODE: # pragma: no cover
    print("Python " + ".".join(map(str, sys.version_info[:3])))
