# Hello World Example
#
# Welcome to the OpenMV IDE! Click on the green run arrow button below to run the script!

import sensor, image, time

sensor.reset()                      # Reset and initialize the sensor.
sensor.set_pixformat(sensor.JPEG)   #JPEG压缩格式，帧率较高，推荐使用。
#sensor.set_pixformat(sensor.GRAYSCALE)  #灰度
#sensor.set_pixformat(sensor.RGB565)  #彩色，每个像素16bit，可以直接使用画图
sensor.set_framesize(sensor.VGA)    # 设置图像分辨率，VGA分辨率为640*480
#VGA可以替换为以下的分辨率格式：
#sensor.QQQQVGA: 40x30
#sensor.QQQVGA: 80x60
#sensor.QQVGA: 160x120
#sensor.QVGA: 320x240
#sensor.VGA: 640x480
#当帧数过低时可以通过降低分辨率的方式来提高帧数。
sensor.skip_frames(time = 2000)     # Wait for settings take effect.
clock = time.clock()                # Create a clock object to track the FPS.
#sensor.set_hmirror(True) #水平翻转
#sensor.set_vflip(True)   #垂直方向翻转
#有些OV2640模块的方向是倒着的，可以取消这两行的注释来将图像翻转为正确方向
while(True):
    clock.tick()                    # Update the FPS clock.
    img = sensor.snapshot()         # Take a picture and return the image.
    print(clock.fps())              # Note: OpenMV Cam runs about half as fast when connected
                                    # to the IDE. The FPS should increase once disconnected.
