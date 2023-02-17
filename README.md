# ESP32-S3-CAM-OPENMV-PCB
一个基于ESP32-S3-WROOM-1模组的机器视觉模块，可以刷OPENMV
有24P的FPC排线座，可以插OV2640模块。板型类似openmv，可以刷Openmv的固件。
固件参考https://github.com/1847123212/esp32_mpy和https://github.com/Kevincoooool/esp32s3_openmv_lvgl
目前参考了ksdiy的开发板引脚定义，之后可能会改。
编译好的固件已经上传，bootloader从0x00开始，partition-table从0x8000开始，micropython从0x10000开始。
对比一般的esp32-cam加入了TYPE-C接口，可以使用Openmv_ide进行开发。
使用立创EDA设计，双层板，可以在嘉立创免费打样
