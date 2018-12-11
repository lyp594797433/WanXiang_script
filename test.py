# -*- coding=utf-8 -*-
import os
import sys
import json
import re
import subprocess
from PIL import Image
import matplotlib.pyplot as plt
def get_screen_size():
    '获取手机屏幕大小'
    size_str = os.popen('adb shell wm size').read()
    if not size_str:
        print('请安装 ADB 及驱动并配置环境变量')
        sys.exit()
    m = re.search(r'(\d+)x(\d+)', size_str)
    if m:
        return "{height}x{width}".format(height=m.group(2), width=m.group(1))
    return "1920x1080"

class Screenshot():  # 截取手机屏幕并保存到电脑
	def __init__(self):
		# 查看连接的手机
		connect = subprocess.Popen("adb devices", stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
		stdout, stderr = connect.communicate()  # 获取返回命令
		# 输出执行命令结果结果
		stdout = stdout.decode("utf-8")
		stderr = stderr.decode("utf-8")
		print(stdout)
		print(stderr)

	def delFilePhone(self,cmd):
		screenExecute = subprocess.Popen(str(cmd), stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
		stdout, stderr = screenExecute.communicate()

	# def delFilePc(self,cmd):
	# 	screenExecute = subprocess.Popen(str(cmd), stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
	# 	stdout, stderr = screenExecute.communicate()

	def screen(self, cmd):  # 在手机上截图
		screenExecute = subprocess.Popen(str(cmd), stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
		stdout, stderr = screenExecute.communicate()
		# 输出执行命令结果结果
		stdout = stdout.decode("utf-8")
		stderr = stderr.decode("utf-8")
		print(stdout)
		print(stderr)

	def saveComputer(self, cmd):  # 将截图保存到电脑
		screenExecute = subprocess.Popen(str(cmd), stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
		stdout, stderr = screenExecute.communicate()
		stdout = stdout.decode("utf-8")
		stderr = stderr.decode("utf-8")
		snap_obj = Image.open(r'd:/3.png')
		plt.imshow(snap_obj)
		plt.show()
		# image_obj = snap_obj.crop((200, 200, 100, 100))
		# plt.imshow(image_obj)
		# plt.show()
		# image_obj.save('d:/2.png')
		# 输出执行命令结果结果
		# stdout = stdout.decode("utf-8")
		# stderr = stderr.decode("utf-8")
		# print(stdout)
		# print(stderr)
cmd1 = r"adb shell /system/bin/screencap -p /sdcard/3.png"  # 命令1：在手机上截图3.png为图片名
cmd2 = r"adb pull /sdcard/3.png d:/3.png"  # 命令2：将图片保存到电脑 d:/3.png为要保存到电脑的路径
cmd3 = r"adb shell rm /sdcard/3.png"  # 命令3：删除手机图片
screen = Screenshot()
screen.screen(cmd1)
screen.saveComputer(cmd2)

# print(get_screen_size())