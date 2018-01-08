
import time
from PythonTimer import PythonTimer

# instanciate PythonTimer
my_timer = PythonTimer()

# monitor only one line
my_timer.start_timer('one')
time.sleep(0.2)
my_timer.stop_timer('one')

# if multiple lines, will cumulate the result
for loop in [0.1, 0.2, 0.3]:
    my_timer.start_timer('loop')
    print(loop)
    time.sleep(loop)
    my_timer.stop_timer('loop')


print(my_timer.get_cumulated_times())
print(my_timer.get_cumulated_count())
