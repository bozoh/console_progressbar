'''
Simple progress bar for console
'''

__version__ = '1.0.0'

"""
Create terminal progress bar
@params:
    total       - Required  : total iterations (Int)
    prefix      - Optional  : prefix string (Str)
    suffix      - Optional  : suffix string (Str)
    decimals    - Optional  : positive number of decimals in percent complete (Int)
    length      - Optional  : character length of bar (Int)
    fill        - Optional  : bar fill character (Str)
"""
class ProgressBar(object):
    def __init__(self, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
        self.__prefix = prefix
        self.__suffix = suffix
        self.__decimals = decimals
        self.__length = length
        self.__fill = fill
        self.__total = total
    
    #         iteration   - Required  : current iteration (Int)
    def generate_pbar(self, iteration):
        """
        Create and return the progress bar string
        @params:
            iteration   - Required  : current iteration (Int)
        """
        percent = ("{0:." + str(self.__decimals) + "f}").format(100 * (iteration / float(self.__total)))
        filledLength = int(self.__length * iteration // self.__total)
        bar = self.__fill * filledLength + '-' * (self.__length - filledLength)
        return '{0} |{1}| {2}% {3}'.format(self.__prefix, bar, percent, self.__suffix)

    
    #         iteration   - Required  : current iteration (Int)
    def print_progress_bar (self, iteration):
        """
        Prints the progress bar
        @params:
        iteration   - Required  : current iteration (Int)
        """
        print('\r%s' % (self.generate_pbar(iteration)), end = '\r')
        # Print New Line on Complete
        if iteration == self.__total: 
            print()
