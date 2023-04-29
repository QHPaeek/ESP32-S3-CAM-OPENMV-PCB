import sensor, image, time
#初始化摄像头
sensor.reset()
#除非在 JPEG 中使用 CIF 或更低分辨率时，否则驱动程序需要安装和激活 PSRAM。
#使用YUV或RGB会给芯片带来很大的压力，因为写入PSRAM不是特别快。结果是图像数据可能丢失。如果启用了 WiFi，则尤其如此。
#如果需要 RGB 数据，建议使用 or / 捕获 JPEG 并将其转换为 RGB。
#sensor.set_pixformat(sensor.JPEG)
sensor.set_pixformat(sensor.RGB565)# 暂时先使用RGB565
sensor.set_framesize(sensor.QVGA)# qvga提升帧率，需要清晰度可以使用vga
sensor.skip_frames(time = 2000)
def jpeg_to_rgb(img):
    buffer = bytearray(img.size() * 2)
    img.compress(buffer, quality=70) # 将JPEG图像压缩为字节数组
    return image.Image(320,240,image.RGB565,source=buffer)

# 配置颜色阈值
red_threshold = (12, 100, -2, 23, -4, 8) # 红色的颜色阈值
color_thresholds = [(12, 100, -2, 23, -4, 8)] # 阈值列表

# 查找红色颜色块
while(True):
    img = sensor.snapshot() # 拍摄一张图像
#   img = jpeg_to_rgb(img) # 将JPEG图像转换为RGB图像
    blobs = img.find_blobs(color_thresholds, pixels_threshold=100, area_threshold=100, merge=True) # 查找颜色块
    if blobs:
        # 如果找到颜色块，则绘制矩形框
        for blob in blobs:
            img.draw_rectangle(blob.rect())
            img.draw_cross(blob.cx(), blob.cy())
    else:
        # 如果未找到颜色块，则清空屏幕
        img.clear()