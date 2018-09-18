# -*- coding: utf-8 -*-
'''
    Simple progress bar for console
'''
from __future__ import print_function
import sys


class ProgressBar(object):
    """
    Create terminal progress bar
    @params:
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        zfill       - Optional  : bar zero fill character (Str)
    """
    def __init__(self, total, prefix='', suffix='', decimals=1, length=100, fill='█', zfill='-'):
        self.__prefix = prefix
        self.__suffix = suffix
        self.__decimals = decimals
        self.__length = length
        self.__fill = fill
        self.__zfill = zfill
        self.__total = total

    def generate_pbar(self, iteration):
        """
        Create and return the progress bar string
        @params:
            iteration   - Required  : current iteration (Int)
        """
        percent = ("{0:." + str(self.__decimals) + "f}")
        percent = percent.format(100 * (iteration / float(self.__total)))
        filled_length = int(self.__length * iteration // self.__total)
        pbar = self.__fill * filled_length + self.__zfill * (self.__length - filled_length)
        return '{0} |{1}| {2}% {3}'.format(self.__prefix, pbar, percent, self.__suffix)

    def print_progress_bar(self, iteration):
        """
        Prints the progress bar
        @params:
        iteration   - Required  : current iteration (Int)
        """
        print('\r%s' % (self.generate_pbar(iteration)), end='')
        sys.stdout.flush()
        # Print New Line on Complete
        if iteration == self.__total:
            print()
