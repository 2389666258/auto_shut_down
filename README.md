# auto_shut_down

### Copyrigth: ICOVETOUS
### Time: 2023-7-1 23:43
### Version: 1.0.0
### Language: python3.9
### System: windows10
### Editor: PyCharm

### --- description ---
### ​A program that delays the shutdown of a laptop when it is powered down.
#### 此程序用于检测 当前电脑(laptop) 是否接通电源
#### 如果 拔掉电源 --> 执行 自动延迟关机 --> 并 弹出提示框(可选) 询问 是否取消延迟关机
#### 且可以 连接网络内台式机(desktop) 并执行相同操作

### --- warning ---
#### 1. 此程序需要管理员权限
#### 2. 此程序需要安装 psutil 包
#### 3. 此程序需要安装 tkinter 包
#### 4. 此程序需要安装 psexec.exe
#### 5. 若需要连接 网络内其他机器机(e.g. desktop) 需一系列配置 和 更改注册表
#### 6. 此程序可设置.bat文件的快捷方式至开机启动项中 以达到开机自启
