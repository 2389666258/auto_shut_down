"""
 copyrigth: ICOVETOUS
 time: 2023-7-1
 version: 1.0.0
 language: python3.9
 system: windows10
 editor: PyCharm
 --- description ---
 此程序用于检测 当前电脑(laptop) 是否接通电源
 如果 拔掉电源 --> 执行 自动延迟关机 --> 并 弹出提示框(可选) 询问 是否取消延迟关机
 且可以 连接网络内台式机(desktop) 并执行相同操作
 --- warning ---
 1. 此程序需要管理员权限
 2. 此程序需要安装 psutil 包
 3. 此程序需要安装 tkinter 包
 4. 此程序需要安装 psexec.exe
 5. 若需要连接 网络内其他机器机(e.g. desktop) 需一系列配置 和 更改注册表
 6. 此程序可设置.bat文件的快捷方式至开机启动项中 以达到开机自启
"""

import psutil
import tkinter as tk
from tkinter import messagebox
import subprocess

# 设置 台式机(desktop) IP
desktop_ip = "192.168.10.241"
# 设置 检测时间间隔 (s)
check_time = 5
# 设置 延迟关机时间 (s)
delay_time = 60
# 设置 取消关机后 到 再次进入延时关机 的时间 (s)
cancel_time = 600
# 是否已经执行 延迟关机 操作
already_delay_shutdown = False


# 运行 cmd 指令
def run_cmd(cmd):
    # 使用 subprocess 创建一个不可见窗口并执行 cmd 指令
    subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                     shell=True, creationflags=subprocess.CREATE_NO_WINDOW)


# 检测电源状态
def check_power_status():
    power_status = psutil.sensors_battery().power_plugged
    return power_status


# 关机提示对话框
def shutdown_prompt():
    # 创建主窗口
    window = tk.Tk()
    window.withdraw()
    window.attributes('-topmost', True)  # 设置窗口置顶
    result = messagebox.askyesno("取消", "取消关机？", default='yes', parent=window)
    # 关闭主窗口
    window.destroy()

    return result


# 延迟关机
def delay_shutdown():
    # 执行 延迟关机 操作
    command = "shutdown -s -t " + str(delay_time)
    run_cmd(command)
    print(" 执行 本机 延迟关机...")
    # 连接台式机: 并执行 延迟关机 操作
    command = "psexec \\\\" + desktop_ip + " shutdown -s -t " + str(delay_time)
    run_cmd(command)
    print(" 执行 台式机 延迟关机...")


# 取消关机
def cancel_shutdown():
    # 执行 取消关机 操作
    command = "shutdown -a"
    run_cmd(command)
    print(" 已取消 本机 延迟关机")
    # 连接台式机: 并执行 取消关机 操作
    command = "psexec \\\\" + desktop_ip + " shutdown -a"
    run_cmd(command)
    print(" 已取消 台式机 延迟关机")
