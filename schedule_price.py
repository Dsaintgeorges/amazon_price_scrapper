import threading
import time

import schedule

import price_logic


def run_continuously(interval=1):
    cease_continuous_run = threading.Event()

    class ScheduleThread(threading.Thread):
        @classmethod
        def run(cls):
            while not cease_continuous_run.is_set():
                schedule.run_pending()
                time.sleep(interval)

    continuous_thread = ScheduleThread()
    continuous_thread.start()
    return cease_continuous_run


schedule.every(12).hours.do(price_logic.update_price)

# Start the background thread
stop_run_continuously = run_continuously()

# Do some other things...
time.sleep(10)
stop_run_continuously.set()
