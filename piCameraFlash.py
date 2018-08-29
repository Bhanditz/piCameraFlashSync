import os
import sys
import cv2
import time
import picamera
import picamera.array
import RPi.GPIO as GPIO
from libraries.picameraArray import PiRGBAArray

rutaDeGuardado = './'

if __name__ == '__main__':
    # We initialize some parameters within the initializer so It has better performance
    GPIO.setmode(GPIO.BCM)
    # Se introduce el número de pin
    pinInput = 12                               # En Modo board
    GPIO.setup(pinInput,GPIO.OUT)
    GPIO.output(pinInput,GPIO.LOW)
    #camera = picamera.PiCamera(resolution = (2592,1944),framerate = 2,sensor_mode=0,clock_mode='reset')
    #camera.exposure_mode = 'sports'
    #camera.flash_mode = 'on'
    #lowResCap = PiRGBAArray(camera)
    #piCameraStream = camera.capture_continuous(lowResCap,
                                                format="bgra",
                                                splitter_port=2,
                                                use_video_port=True)

    contador = 0
    #camera.start_preview()
    with picamera.PiCamera() as camera:
        with picamera.array.PiRGBArray(camera) as output:
            while True:
                #if contador == 1:
                #    print(camera.sensor_mode)
                #lrs = piCameraStream.__next__()
                #imageArray = lrs.array
                #lowResCap.truncate(0)

                camera.capture(output, 'rgb')
                print('Captured %dx%d image' % (output.array.shape[1], output.array.shape[0]))
                print(type(output.array))
                cv2.imshow('Imagen',cv2.resize(imageArray,(320,240)))
                #cv2.imwrite(rutaDeGuardado+'imagen_{}.jpg'.format(contador), imageArray)
                contador += 1
                ch = 0xFF & cv2.waitKey(1)
                if ch == ord('q'):
                    break
