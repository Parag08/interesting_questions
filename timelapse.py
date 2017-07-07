'''
created by parag 07/07/07

you can start the program with python timelapse.py
and end it by pressing ctl-C final array will be printed at the end
for testing purpose please comment out last line
'''
import time
import signal
import sys

size = 100
'''
consider image_counter to be images that are taken per second and array to be array
of images that are stored so ideal cases are:
[1,2,...,99,100]
[2,4,....,98,100]
[4,8,....,96,100]
'''
array = [0 for x in range(size)]

def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    print(array)
    sys.exit(0)

class Photo(object):
    def __init__(self):
        self.string = 'photo taken'
    def takePhoto(self):
        print self.string

photo = Photo()

image_counter = 0
startTime = time.time()


i = 0
signal.signal(signal.SIGINT, signal_handler)

while True:
    if (time.time() - startTime > 1):
        print('array:',array,'i:',i,'image_counter:',image_counter)
        image_counter = image_counter + 1
        if i < size:
            array[i] = image_counter
            photo.takePhoto()
            i = i + 1
        else:
            place_found = False
            place = None
            array.sort()
            first_elem = array[0]
            for k in range(size):
                if array[k] % first_elem != 0:
                    place_found = True
                    if image_counter%first_elem == 0:
                        photo.takePhoto()
                        array[k] = image_counter
                    break
            if place_found == False:
                array.pop(0)
                array.append(image_counter)
            array.sort()
            i = i + 1
        startTime = time.time()
