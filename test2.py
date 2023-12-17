import screen_brightness_control as sbc
import time
import winsound
duration = 100  # milliseconds
freq = 440  # Hz


# get the brightness
brightness = sbc.get_brightness()
# get the brightness for the primary monitor
primary = sbc.get_brightness(display=0)

# set the brightness to 100%
for i in range(10):
    sbc.set_brightness(30)
    time.sleep(0.1)
    sbc.set_brightness(80)
    winsound.Beep(freq, duration)
# set the brightness to 100% for the primary monitor
#sbc.get_brightness(100, display=0)

# show the current brightness for each detected monitor
#for monitor in sbc.list_monitors():
#print(monitor, ':', sbc.get_brightness(display=monitor), '%')
print(f"Code is done:")