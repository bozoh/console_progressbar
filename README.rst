.. image:: https://api.travis-ci.org/bozoh/console_progressbar.svg?branch=master
    :target: https://travis-ci.org/bozoh/console_progressbar

====================
Console Progress Bar
====================

It's a very tiny lib to help devs to print a progress bar in console

Usage
=====

Here a very simple sample

    import time
    from console_progressbar import ProgressBar
    pb = ProgressBar(total=100,prefix='Here', suffix='Now', decimals=3, length=50, fill='X')
    pb.print_progress_bar(2)
    time.sleep(5)
    pb.print_progress_bar(25)
    time.sleep(5)
    pb.print_progress_bar(50)
    time.sleep(5)
    pb.print_progress_bar(95)
    time.sleep(5)
    pb.print_progress_bar(100)   

Parameters Description
======================

params: 
    total       - Required  : total iterations (Int) 
    prefix      - Optional  : prefix string (Str) 
    suffix      - Optional  : suffix string (Str) 
    decimals    - Optional  : positive number of decimals in percent complete (Int) 
    length      - Optional  : character length of bar (Int) 
    fill        - Optional  : bar fill character (Str) 
