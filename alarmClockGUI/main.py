import tkinter as tk
import datetime
import winsound
import time


class AlarmClock:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Alarm Clock")

        # create the time label
        self.time_label = tk.Label(text="", font=("Helvetica", 48))
        self.time_label.pack(pady=20)

        # create the entry field for the alarm time
        self.alarm_time_entry = tk.Entry(font=("Helvetica", 24))
        self.alarm_time_entry.pack(pady=10)

        # create the button to set the alarm
        self.set_alarm_button = tk.Button(text="Set Alarm", font=("Helvetica", 24), command=self.set_alarm)
        self.set_alarm_button.pack(pady=10)

        # start the GUI main loop
        self.update_clock()
        self.root.mainloop()

    def update_clock(self):
        # update the time label with the current time
        now = datetime.datetime.now()
        self.time_label.config(text=now.strftime("%H:%M:%S"))
        self.root.after(1000, self.update_clock)

    def set_alarm(self):
        # get the alarm time from the entry field
        while True:
            time.sleep(1)
            alarm_time_str = self.alarm_time_entry.get()
            alarm_time = datetime.datetime.strptime(alarm_time_str, "%H:%M")
            alarm_time_formatted = alarm_time.strftime("%H:%M:%S")

            # calculate the number of seconds until the alarm goes off
            current_time = datetime.datetime.now()
            now = current_time.strftime("%H:%M:%S")
            print(alarm_time_formatted)
            print(now)

            if now == alarm_time_formatted:
                self.alarm()
                break

    def alarm(self):
        # play a sound to alert the user that the alarm has gone off
        winsound.Beep(440, 1000)


alarm_clock = AlarmClock()
