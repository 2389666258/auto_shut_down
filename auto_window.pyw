"""
 copyrigth: ICOVETOUS
 time: 2023-7-1
 auto_shut_down\auto.py
"""

from util import *
import time


def main():
    global already_delay_shutdown
    while True:
        # 检测电源状态 接通电源/拔掉电源
        power_status = check_power_status()

        # 如果已经执行延迟关机操作 延长下次检测时间
        if already_delay_shutdown:
            time.sleep(cancel_time)

        # 如果拔掉电源 执行延迟关机操作 并 弹出提示框 power_status = False
        if not power_status:
            # 延迟关机
            delay_shutdown()

            # 是否取消关机
            result = shutdown_prompt()
            if result:
                # 取消关机
                cancel_shutdown()
                # 延迟关机操作 已执行
                already_delay_shutdown = True

        # 每隔 check_time 秒检测一次
        time.sleep(check_time)


if __name__ == "__main__":
    print('--> 程序开始')
    main()
    print('程序结束 <--')
