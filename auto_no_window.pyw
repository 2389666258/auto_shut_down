"""
 copyrigth: ICOVETOUS
 time: 2023-7-1
 auto_shut_down\auto.py
"""

from util import *
import time


def main():
    while True:
        # 检测电源状态 接通电源/拔掉电源
        power_status = check_power_status()

        # 如果拔掉电源 执行延迟关机操作 并 弹出提示框 power_status = False
        if not power_status:
            # 延迟关机
            delay_shutdown()

        # 如果接通电源 取消延迟关机操作
        else:
            # 取消关机
            cancel_shutdown()

        # 每隔 check_time 秒检测一次
        time.sleep(check_time)


if __name__ == "__main__":
    print('--> 程序开始')
    main()
    print('程序结束 <--')
