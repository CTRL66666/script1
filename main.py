#version=1.45
import tkinter as tk
from tkinter import messagebox
import subprocess
import time
import random
import winshell
import sys
import json
# 显式导入所有 requests 子模块
from requests import get, post, exceptions  # 必须添加
from requests.exceptions import RequestException
from requests.adapters import HTTPAdapter
import requests
from urllib3.util.retry import Retry
import certifi  # 证书依赖
import os
import pystray  # 最小化托盘
import io  # 提供了用于处理流（stream）的接口。io 模块支持多种类型的流，包括文件流、内存流、网络流等，并提供了统一的接口来操作这些流。
import base64
from PIL import Image
from PIL import ImageTk
from icon import icon_data  # 自定义任务栏图标
import threading
import pyautogui
import win32gui
import win32con
from threading import Thread  # 提供了用于处理流（stream）的接口。io 模块支持多种类型的流，包括文件流、内存流、网络流等，并提供了统一的接口来操作这些流。


##校园网无响应时应暂停脚本或尝试连接wifi！，电脑睡眠后暂停工作现象,需要重启线程，cycle——login函数需要检测脚本启动状态！
# 调用 tk.Tk() 时，它会初始化 Tkinter 运行环境，并创建一个主窗口。返回值是实例
# 这个主窗口是所有其他 GUI 组件（如按钮、标签、文本框等）的容器。

# 还写一个检测ip地址是否属于校园网的方法，提醒用户是否连接了校园网,或者自动连接校园网wifi

# 配置文件隐藏,debug显示时间,防休眠,load配置提示框优化，开机自启动脚本并运行 ，代码瘦身,版本详情，使用说明,启动ui,音效添加?


#global app #全局变量
def main():

    from gui import app
    from gui import root
    from pump_thread import register_wake_notify
    # 再设置窗口图标
    # app.root.wm_iconbitmap(app.tk_icon)

    app.root.wm_iconphoto(True, app.tk_icon)
    try:
        os.remove(app.temp_icon)
    except:
        pass
    # 删除临时图标文件

    x_position = (app.screen_width - app.main_window_width) // 2
    y_position = (app.screen_height - app.main_window_height) // 2 - 100
    app.root.geometry(f"{app.main_window_width}x{app.main_window_height}+{x_position}+{y_position}")

    # root.after()  #设置定时任务，检查线程存活
    register_wake_notify()  # 休眠自唤醒,修改后的注册方法
    root.mainloop()
    print(app.config)
    print(app.log)
    print("Program end")

if __name__ == "__main__":
    main()


'''
self.temp_icon = "temp_icon.ico"

with open(self.temp_icon, "wb") as f:
    f.write(base64.b64decode(icon_data))
self.icon_data_coded=base64.b64decode(icon_data) #编码后的图像数据
self.icon_image = Image.open(self.temp_icon) # Image.open 方法期望的是一个文件路径或一个类似文件的对象，而不是直接的图像数据。
'''

"""
class App: #可插入休眠恢复运行代码
    def __init__(self, root):
        # ...原有初始化代码...
        self.register_wake_notify()  # 新增注册唤醒通知,设置系统唤醒事件的监听。

    def register_wake_notify(self):
        message_map = {
            win32con.WM_POWERBROADCAST: self.on_power_event #定义了要监听的消息类型及其对应的处理函数。这里是WM_POWERBROADCAST消息，该消息在电源状态发生变化时发送。
        }
        win32gui.PumpMessages(message_map)  #用于处理消息队列中的消息，并将匹配的消息分派给相应的处理函数。

    def on_power_event(self, hwnd, msg, wparam, lparam): #接收到WM_POWERBROADCAST消息时被调用。
        if wparam == win32con.PBT_APMRESUMEAUTOMATIC: #检查wparam参数是否等于PBT_APMRESUMEAUTOMATIC（表示系统自动从休眠状态恢复），来判断系统是否刚刚唤醒。
            print("检测到系统唤醒")
            if self.start_sign and (not self.script_thread.is_alive()):
                print("重启守护线程")
                self.script_thread = Thread(target=self.cycle_login, daemon=True)
                self.script_thread.start()
                self.status_label.config(text="已恢复运行")
                return True #返回True表示消息已被处理，阻止进一步传播。
"""

"""
最后修改：优化了访问代码的逻辑，有网状态时不会发送校园网登录请求;
        电脑休眠结束后恢复script_thread线程

"""