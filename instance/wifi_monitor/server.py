import socket
import cv2
import numpy as np
from PIL import Image

PORT = 1437
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
address = ('', PORT)  
server_socket.bind(address)  # 为服务器绑定一个固定的地址，ip和端口
# server_socket.settimeout(10)  #设置一个时间提示，如果10秒钟没接到数据进行提示

while True:
    receive_data, client = server_socket.recvfrom(1024 * 1024)
    # 二进制数据流转np.ndarray [np.uint8: 8位像素]
    img = cv2.imdecode(np.frombuffer(receive_data, np.uint8), cv2.IMREAD_COLOR)
    # # 将bgr转为rbg
    rgb_img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    # np.ndarray转IMAGE
    cv2.imshow('hello', rgb_img)
    # 显示图片
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break