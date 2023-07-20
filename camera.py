

import sensor, image, time

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA)
sensor.skip_frames(time = 2000)

clock = time.clock()
w = sensor.width()
h = sensor.height()
upWallROI = (int(w/3), int(h/2.7), int(w/3) ,int(h/3))
wallTreshold = [(0, 8, -128, 127, -12, 127)]
drive(20)
while(True):
    img = sensor.snapshot()
    blobs = img.find_blobs(wallTreshold , pixel_treshold=100, area_threshold=100, roi=upWallROI, merge=True)
    size = 0
    if len(blobs) > 0:
        blo[(0, 8, -128, 127, -12, 127)]b = blobs[0]
        img.draw_rectangle(blob.rect())
        size = blob.pixels()
        print(size)
    if size > 1000:
        drive(0)
        time.sleep(1)
