from picamera import PiCamera
import time
import sys


if __name__ == "__main__":
    camera = PiCamera()
    camera.start_preview()
    time.sleep(3)
    file_path = "/home/pi/pic.png" if len(sys.argv) > 2 else sys.argv[1]
    camera.capture(file_path)
    camera.stop_preview()


