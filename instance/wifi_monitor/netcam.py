import time, network
import sensor, image
import socket
# 注意，wifi必须是2.4g频段，加密方式最好是wpa2
SERVER_ADDR = ('ip地址', 1437) # 改成接收端的IP地址
clock = time.clock()                # Create a clock object to track the FPS.

def connect_network():
    station = network.WLAN(network.STA_IF)
    station.active(True)

    station.connect("wifi名字", "密码")# 改成你自己的wifi名字与密码
    return station.isconnected()

def init():
    if not connect_network():
        print('connect failed')
        return
    print('connect success')

    print('init camera...')
    sensor.reset()                      # Reset and initialize the sensor.
    sensor.set_pixformat(sensor.JPEG) # Set pixel format to RGB565 (or GRAYSCALE)
    sensor.set_framesize(sensor.QVGA)   # Set frame size to QVGA (320x240)
    sensor.skip_frames(time = 2000)     # Wait for settings take effect.

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        frame = sensor.snapshot()
        cframe = frame.compressed(quality=35)

        client_socket.sendto(cframe, SERVER_ADDR)

        time.sleep_ms(100)



def main():
    init()

main()
