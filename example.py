
import time
from PythonTimer import PythonTimer

# instanciate PythonTimer
my_timer = PythonTimer()

# monitor only one line
my_timer.start('one')
time.sleep(0.2)
my_timer.stop('one')

# if multiple lines, will cumulate the result
for loop in [0.1, 0.2, 0.3]:
    my_timer.start('loop')
    print(loop)
    time.sleep(loop)
    my_timer.stop('loop')

# if multiple lines, will cumulate the result
for num in range(50000):
    my_timer.start('range')
    print(num)
    my_timer.stop('range')


print(my_timer.get_perf_counter_ms())
print(my_timer.get_process_time_ms())
print(my_timer.get_count())
