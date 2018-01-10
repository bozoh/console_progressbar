import time
from console_progressbar import ProgressBar

pb = ProgressBar(100,'Aqui', 'Agora', 3, 50, 'X')
pb.print_progress_bar(2)
time.sleep(5)
pb.print_progress_bar(25)
time.sleep(5)
pb.print_progress_bar(50)
time.sleep(5)
pb.print_progress_bar(95)
time.sleep(5)
pb.print_progress_bar(100)