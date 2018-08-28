import os
import sys
import cv2
import time
import picamera

rutaDeGuardado = './'

if __name__ == '__main__':
    camera = picamera.PiCamera()
    camera.resolution = (2592, 1944)
    camera.framerate = 2
    camera.exposure_mode = 'sports'
    camera.flash_mode = 'on'
    piCameraStream = camera.capture_continuous(format="bgra",
                                                use_video_port=True)
    camera.start_preview()
    contador = 0
    while True:
        lrs = piCameraStream.__next__()
        imageArray = lrs.array
        cv2.imshow('Imagen',v2.resize(imageArray,(320,240)))
        cv2.imwrite(rutaDeGuardado+'imagen_{}.jpg'.format(contador), imageArray)
        contador += 1
        ch = 0xFF & waitKey(1)
        if ch == ord('q'):
            break

    camera.stop_preview()
