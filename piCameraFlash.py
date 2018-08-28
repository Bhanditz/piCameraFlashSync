import os
import sys

import picamera

if __name__ == '__main__':
    camera = picamera.PiCamera()
    camera.framerate = 2
    camera.exposure_mode = 'sports'
    camera.flash_mode = 'on'

    camera.start_preview()
    for i in range(5):
        sleep(5)
        camera.capture('/home/pi/Desktop/image%s.jpg' % i)
    camera.stop_preview()
