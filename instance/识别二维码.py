import sensor, image, time

# 初始化摄像头
sensor.reset()
sensor.set_pixformat(sensor.GRAYSCALE)
# 二维码识别必须使用灰度格式
sensor.set_framesize(sensor.VGA)
sensor.skip_frames(time = 2000)

while True:
    img=sensor.snapshot()
    e=img.find_qrcodes()
    if e:
        print(e)
	# 如果识别到二维码，则打印二维码的信息